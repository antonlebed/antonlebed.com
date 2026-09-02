"""explore_the_twelve.py -- reading the undercut census's last residual off
the rig, and asking whether its absence is the absence the corpus files.

THE QUESTION. explore_undercut.py's census leaves 1866 tie pairs with no
certificate. 1822 are refused because a core lies inside the RIDER'S REACH
and 32 because a core can still be seated FRESH -- both HYPOTHESIS failures,
which the corpus reads as ring-design questions. The remaining **12** are
filed differently: "a branch with no cheaper witness at all -- a genuine
absence rather than a hypothesis this lemma cannot meet", and the reading
that follows is that a ring will not help them and an argument might. That
reading is load-bearing -- it is what makes the twelve a WANTED ARGUMENT and
the other 1854 a wanted ring -- and it has never been read off the pairs
themselves, only off a roll-up that counts the reason string "no-undercut".
So: WHAT ARE THE TWELVE, and is the absence they carry the absence the
corpus files?

THE MACHINERY, re-derived from the parent rig rather than remembered. A
place is priced deg * sigma with sigma = T + 1 - e for a place whose degree
lambda_odd already covers and sigma = 1 for a FRESH-ELIGIBLE one (its
degree's factor 2^d - 1 missing from lambda). The undercut certificate
refuses on three tags:

  "eligible"      the TARGET is fresh-eligible, so a fresh move can seat it;
  "ridable"       the TARGET is inside the rider set (element world);
  "no-undercut"   no place of degree <= the target's is strictly cheaper by
                  more than the slack.

and the residual roll-up sorts the 1866 by which tags a pair's two branches
carry. THE HINGE THIS RIG TURNS ON: the witness list that decides
"no-undercut" DISQUALIFIES a fresh-eligible place, and it must -- an
eligible witness is priced at its bare degree d, and the move that seats it
leaves it at exponent 1 under an unmoved tick, so its price jumps from d to
d*T in one step and the gap the certificate opened closes behind it. The
parent rig carries the filter and controls it (a state whose only cheaper
neighbour is fresh-eligible must REFUSE, and must FIRE with the filter
lifted). So the tag "no-undercut" means "no cheaper INELIGIBLE witness", and
the corpus's "no cheaper witness at all" is a strictly stronger sentence.
Whether the two coincide on these twelve is a question about the twelve and
nobody has asked it.

THE HAND-ATTACK, on paper before any engine code.

 A. WHAT AN ODD-EVEN RESIDUAL IS. The species is a tie between a FRESH core
    P_f (kind "fresh", price its bare degree d_f, since sigma = 1) and a
    non-fresh core P_c seated at e_c > 0 (price d_c * (T + 1 - e_c)), at
    d_f != d_c. `judge` tries both orders, so the pair's reason string is the
    SET of the two branches' tags. F5 reports all 12 as ODD-EVEN with a fresh
    member on the other side, which reads as the tag pair
    {eligible, no-undercut}: taking P_c leaves P_f still fresh-eligible
    (never frozen, tag "eligible"), and taking P_f leaves P_c with no cheaper
    ineligible witness (tag "no-undercut").
 B. WHY A CHEAPER ELIGIBLE WITNESS IS THE THING TO LOOK FOR, and why it is
    not a long shot. At the tie state the menu minimum is the tie cost c, and
    an unseated eligible place of degree d offers a vehicle at d, so
    c <= every eligible degree present. The branch that certifies takes the
    FRESH move at P_f, which raises lambda_odd by 2^(d_f) - 1 and so kills
    eligibility exactly at the degrees DIVIDING d_f -- every other eligible
    degree survives the move untouched, at a price still equal to its bare
    degree. The target P_c is priced d_c * sigma_c with sigma_c >= 1. So a
    surviving eligible degree d <= d_c with d < d_c * sigma_c is a strictly
    cheaper witness, and it is disqualified for its eligibility ALONE. The
    prediction below is that this is what the twelve are.
 C. WHAT THAT WOULD MEAN, weighed after the run and not before: if the
    twelve carry a cheaper eligible witness, their refusal is the ELIGIBILITY
    hypothesis biting, which is the same KIND of refusal as the other 1854 --
    a hypothesis this lemma cannot meet at this state, not an absence. If
    they carry none, the corpus's reading stands as written and the argument
    hunt is the right one.
 D. THE ONE THING B DOES NOT SETTLE. An eligible witness cannot be
    substituted into lemma A -- the induction breaks exactly there, which is
    why the filter exists. So a cheaper eligible witness does NOT certify the
    twelve; it relocates them, from "no witness exists" to "the only witness
    is one this induction cannot use". Those are different open problems and
    the rig must not print the first as the second.

TRANSPLANT FLAGS, fixed at the freeze.
 1. Nothing is carried from the number rings; this rig runs the parent's own
    ladder over flag 2 and inherits its scope.
 2. The parent's classification is RE-RUN here rather than trusted: S1
    reproduces the residual roll-up in full, so a drift between the two rigs
    shows as a count mismatch and not as a silent re-reading.
 3. "The branches do not meet" is the parent's rejoin detectors' verdict and
    is not re-derived; this rig only reads what the twelve ARE.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 THE CENSUS REPRODUCES. What the rig PRINTS: the residual roll-up by
    species and reason over both regions, both worlds, six rings, against the
    parent's own three-way split.
    KILL: any total other than 1866 residual pairs, 1822 ridable, 32
    fresh-seatable, 12 no-undercut. A miss here means the two rigs disagree
    about which pairs are in question and nothing below can be read.
PR2 THE TWELVE ARE ONE SHAPE. What the rig PRINTS: for each of the twelve,
    its ring, world, region, the two cores with degree / exponent / kind, the
    tie cost, the tick, and the tag each branch carries.
    KILL: one of the twelve whose tag pair is not {eligible, no-undercut}, or
    whose no-undercut target is the FRESH member -- either would mean the
    corpus's sentence describes a different set than the count does.
PR3 THE ABSENCE IS THE ELIGIBILITY FILTER. What the rig PRINTS: for each of
    the twelve, the cheapest witness at degree <= the target's with the
    eligibility filter LIFTED -- its degree, its price and its eligibility --
    beside the target's own price and the best INELIGIBLE price.
    KILL: zero of the twelve carry a strictly cheaper eligible witness. Then
    the absence is genuine as filed and the wanted argument is the right
    read.
PR4 WHAT THE TWO BRANCHES DO, printed and not predicted: the canonical
    continuation of each branch for FORWARD_T moves, the coordinates at which
    the two exponent vectors differ at each step, and whether the fresh
    member is ever seated in the branch that declined it.

THE DESIGN, in four sections after the control.

 S1 THE POSITIVE CONTROL, run before any residual is read.
    (a) THE CENSUS REPRODUCED (PR1): the parent's own judge path re-run over
        both regions, rolled up by species and reason.
    (b) THE WITNESS SEARCH, planted. A state where the only cheaper place at
        or below the target's degree is fresh-eligible must report ABSENT
        under the filter and PRESENT with it lifted -- otherwise S3 measures
        nothing. And a state with a cheaper INELIGIBLE place must report
        present under both, or the lifted search is not a superset.
 S2 THE TWELVE, dumped whole (PR2).
 S3 THE ABSENCE, SPLIT (PR3): the lifted witness search on each of the
    twelve, and the split of the twelve by whether the absence survives it.
 S4 THE TWO BRANCHES (PR4), followed along the canonical continuation.
 S5 IS THE TIE ONE MOVE OLD -- the section the run added, its own slate and
    its two observables frozen in its docstring before its engine ran.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 THE TWELVE ARE NOT AN ABSENCE, AND THE CORPUS'S READING OF THEM IS
   BACKWARDS (rule in range; 12 of 12 read off the pairs, the enumeration
   exhaustive over the parent's own scanned region, S3). Nothing here is
   derived -- the witnesses are READ, which is the whole point, the reading
   this replaces having been taken off a reason string instead. Not one of
   the twelve lacks a cheaper
   witness. Eight are refused because the cheapest witness -- a degree-1
   place seated at exponent 1, priced 4 -- is TIED EXACTLY with the target
   (a degree-2 place at exponent 3, also priced 4), and four because the
   witness is cheaper by 1 against a genus SLACK of 1. The tag the roll-up
   counts is "no cheaper witness clearing the slack", and the corpus reads
   it as "no cheaper witness at all", which is a strictly stronger sentence
   the pairs do not support. ALL TWELVE ARE ELEMENT-WORLD, which is the same
   fact from the other side: the slack IS the genus, so the ideal world
   contributes none, and the refusal is a hypothesis this lemma cannot meet
   at this state -- the same KIND of refusal as the other 1854, not a
   different one. AND THE OBJECT IS SMALLER THAN ITS COUNT: the twelve are
   twelve (state, pair) RECORDS off 7 distinct tie states in 2 ring-world
   slices, a tie state with several members of one type contributing several
   pairs. Nobody had counted the states, and "twelve" reads as twelve
   independent obstructions.

F2 AND THE ABSENCE IS ONE MOVE OLD, WHICH CLOSES THEM (rule in range, 12 of
   12 over the scanned region, S5; the tie-break itself a derivation, and
   the freeze it hands to is the undercut lemma in its ELEMENT-world form,
   whose two extra hypotheses the rig checks rather than assumes). At the
   state the
   certificate refuses on, the menu has exactly ONE minimal move, and it is
   the tied witness's own. A tie is not symmetric when the witness's degree
   is lower: a clock move at a degree-1 witness Q against a degree-2 target
   P sends price(Q) to T' - T and price(P) to 2(sigma_P + T' - T), and the
   run reads the successor at 4 against 12 -- clear of the slack at every
   one of the twelve. So the target is FROZEN one move into the branch that
   declined it, along every minimal-move continuation there is, the minimal
   move being unique. The other branch seats that same target at its own
   door, T + 1 = 5 against the frozen 3, and exponents never fall. THE TWO
   LIMITS DIFFER AT THAT PLACE, at all twelve. The undercut lemma needs no
   companion argument and no new ring: it needs one move.

F3 SO THE CENSUS'S RESIDUAL HAS NO HARD CORE, and the line it divides at is
   the one it always drew. Every uncovered pair the parent rig files is
   refused by a HYPOTHESIS -- the rider's reach at 1822, a fresh-seatable
   core at 32, and the genus slack at the last 12, which separate anyway one
   move later. What still WANTS a certificate is the rider's reach at 1822
   and the fresh-seatable core at 32 -- and the second is already accounted
   for, sitting at a fallen minimum and out-competed rather than dominated
   (the parent's F6), which is why the parent's own F7 names the rider's
   reach as what stands between this lemma and every species here. The
   reading this replaces -- that a dozen pairs want an argument rather than
   a ring -- was never read off the pairs; it was read off a reason string.

F4 WHAT THIS DOES NOT SAY, and one thing it does not need. The separation
   above does NOT rest on the parent's delayed-rejoin search, which is
   capped and reports its own truncation: two branches holding different
   exponents at one place forever cannot meet, whatever a bounded search
   found. That also fixes the direction of the cap's error -- truncation can
   only ADD pairs to this residual, never remove one, and each of the twelve
   is closed on its own. The twelve are separated at a place, not at a
   limit CARDINALITY, and the enumeration is the parent's scanned region
   (the exhaustive states at h3 and h4, both genus 1) rather than every
   state of every ring -- transplant flag 3's line, inherited. And S5's
   uniqueness of the minimal move is a fact about these twelve states, not a
   lemma: a tie whose refusing successor offered SEVERAL minimal moves would
   need every one of them checked, which is why the column is printed per
   pair rather than summed.

Run: `python explore_the_twelve.py`. RUN RECORD (83 checks, ~2.5 s, peak
28.8 MB under memwatch). S1(a): the parent's residual roll-up reproduced
exactly -- 1866 pairs, 1822 rider's reach, 32 fresh-seatable, 12
no-undercut, and by species class/ridable 1303, depth/ridable 295,
even-even/ridable 162, odd-even/eligible+ridable 62, odd-odd/eligible 32,
odd-even/eligible+no-undercut 12. S1(b): the lifted witness search asserted
a superset at every plant, ABSENT under the filter and cheaper with it
lifted at the deep plant on 3 rings, cheaper under both at the shallow plant
on 3 -- so the filter is separated from the state. S2: 12 records off 7 distinct tie states in 2 ring-world slices; all 12
odd-even,
element world, exhaustive region, tags eligible+no-undercut with the
no-undercut branch targeting the non-fresh member at every one; 4 at h3 (tie
cost 4, tick 4, d3 fresh against d2 e3) and 8 at h4 (cost 5, tick 4, d2 e3
against d4 fresh). S3: target price 4 at all twelve; best witness d1 e2 @ 3
(gap 1, slack 1) at the four h3 pairs and d1 e1 @ 4 (gap 0) at the eight h4
ones; 0 carry a cheaper witness once the eligibility filter is lifted, which
KILLED PR3 as it was framed. S5: the witness's move minimal at 12 of 12 and
the certificate firing at the successor at 12 of 12 (a degree-1 place at
4 + 1 < 12); every minimal move at the refusing state enumerated -- 1 move,
0 of them the target's own core, 1 of 1 certifying, at all twelve. S4: the
separation read at step 7 of the canonical continuation, the certified
target at 5 against 3 (9 against 3 at one pair, the seating branch having
moved it again), asserted distinct at all twelve.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_greedy_image_ec as EC
import explore_coarse_type as CT
import explore_reordering as RO
import explore_undercut as UC

FORWARD_T = 8        # moves each branch is followed for in S4
CHECKS = 0


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def best_witness(L, world, st, lam, pl, allow_eligible):
    """The cheapest candidate undercutter for `pl`, as
    (place, degree, price, eligible) or None -- the parent's own witness list
    under either setting of its eligibility filter, minimised by price."""
    best = None
    for q in UC.witnesses(L, world, st, lam, pl,
                          allow_eligible=allow_eligible):
        p = UC.price(L, st, q, lam)
        if best is None or p < best[2]:
            best = (q, L.R.deg[q], p, UC.eligible(L.R, q, lam))
    return best


def judge_dump(L, world, region_tag, st, lam, cost, a, b, sp, out):
    """The parent rig's `judge`, re-run for its TAGS rather than its
    verdict, and recording the pair whole when neither branch certifies.

    The order is the parent's own -- the lower degree first, at equal degrees
    the deeper -- because the reported branch must be the one the corpus's
    roll-up counted, not a re-derivation that happens to agree in aggregate.
    """
    R = L.R
    (v1, (p1, e1, r1, k1), _), (v2, (p2, e2, r2, k2), _) = a, b
    if R.deg[p1] != R.deg[p2]:
        order = [(a, b)] if R.deg[p1] < R.deg[p2] else [(b, a)]
    else:
        order = [(a, b)] if e1 > e2 else [(b, a)]
    order.append((order[0][1], order[0][0]))
    tags, branches = [], []
    fired = False
    for first, other in order:
        po = other[1][0]
        st2 = EC.apply_veh(st, first[0])
        lam2 = R.lam_state(st2)
        v, tag, detail = UC.undercut(L, world, st2, lam2, po)
        tags.append(tag)
        branches.append((first, other, st2, lam2, tag, detail))
        if v:
            fired = True
            break
    if fired:
        return
    rj = RO.rejoins(L, world, st, v1, v2)
    if rj in ("rejoin", "unreadable"):
        return
    if RO.meets(L, world, st, v1, v2, RO.BFS_BUDGET, RO.BFS_CAP):
        return
    why = "+".join(sorted(set(tags)))
    out.append(dict(ring=L.name, world=world, region=region_tag, sp=sp,
                    why=why, st=st, lam=lam, cost=cost, L=L,
                    reads=(a[1], b[1]), branches=branches))


def collect(ladder):
    """Every UNCOVERED residual pair over both regions, recorded whole."""
    out = []
    for L in ladder:
        for world in ("ideal", "element"):
            for region_tag, region in (("exhaustive", UC.exhaustive),
                                       ("trajectory", UC.trajectory)):
                for st, lam in region(L, world):
                    try:
                        _, cost, ties = RO.menu_of(L, world, st)
                    except AssertionError:
                        continue
                    if len(ties) < 2:
                        continue
                    for a, b, sp in UC.cross_pairs(L, world, st, lam, ties):
                        judge_dump(L, world, region_tag, st, lam, cost,
                                   a, b, sp, out)
    return out


# ------------------------------------------------------- S1 the control
def s1a_census(res):
    """PR1: the roll-up, against the parent rig's own printed three-way
    split."""
    why = {}
    for r in res:
        why[(r["sp"], r["why"])] = why.get((r["sp"], r["why"]), 0) + 1
    print("  species    reason                       pairs")
    for k, v in sorted(why.items()):
        print("    %-10s %-26s %d" % (k[0], k[1], v))
    hard = sum(v for k, v in why.items() if "no-undercut" in k[1])
    ride = sum(v for k, v in why.items()
               if "ridable" in k[1] and "no-undercut" not in k[1])
    el = sum(v for k, v in why.items()
             if "ridable" not in k[1] and "no-undercut" not in k[1])
    print("  TOTAL %d residual pairs: %d rider's reach, %d fresh-seatable, "
          "%d no-undercut" % (len(res), ride, el, hard))
    ok(len(res) == 1866, "the residual is %d pairs, not the parent's 1866"
       % len(res))
    ok((ride, el, hard) == (1822, 32, 12),
       "the three-way split reads (%d, %d, %d), not the parent's "
       "(1822, 32, 12)" % (ride, el, hard))
    return [r for r in res if "no-undercut" in r["why"]]


def s1b_witness(ladder):
    """The lifted witness search must be a strict superset, and must change
    the verdict exactly where the only cheaper place is fresh-eligible."""
    print("  ring     planted state                     own  filtered  "
          "lifted")
    fired_eligible = fired_both = 0
    for L in ladder:
        R = L.R
        d3 = R.by_deg.get(3, [])
        if not d3 or not R.by_deg.get(2, []):
            continue
        tgt = d3[0]
        # TWO plants, and the DEEP one is the whole control. Degree 1 is
        # never fresh-eligible (2^1 - 1 = 1 divides everything), so an
        # unseated degree-1 place is always an ineligible witness at price
        # T + 1 -- which means the filter can only bite where the TARGET is
        # cheaper than that. Seating the degree-3 target at exponent 7 sets
        # kappa = 3, T = 8: the target costs 3*(9 - 7) = 6, every unseated
        # degree-1 place costs 9, and a degree-2 place is fresh-eligible
        # while 3 does not divide lambda -- cheaper at its bare 2, and
        # visible to the lifted search alone.
        for label, st in (("deg-3 at e=7, T=8 (deep)", {tgt: 7}),
                          ("deg-3 at e=1, T=1 (shallow)", {tgt: 1})):
            lam = R.lam_state(st)
            if not any(UC.eligible(R, q, lam) for q in R.by_deg[2]):
                continue
            bf = best_witness(L, "ideal", st, lam, tgt, False)
            bl = best_witness(L, "ideal", st, lam, tgt, True)
            own = UC.price(L, st, tgt, lam)
            fl = bf is not None and bf[2] < own
            ll = bl is not None and bl[2] < own
            ok(bl is not None and (bf is None or bl[2] <= bf[2]),
               "%s: the lifted search is not a superset of the filtered one"
               % L.name)
            print("  %-8s %-33s %-4d %-9s %s"
                  % (L.name, label, own,
                     "cheaper" if fl else "ABSENT",
                     "cheaper" if ll else "ABSENT"))
            if ll and not fl:
                fired_eligible += 1
            if ll and fl:
                fired_both += 1
    ok(fired_eligible,
       "no planted state separates the filtered search from the lifted one, "
       "so S3 would measure nothing")
    ok(fired_both,
       "no planted state has a cheaper INELIGIBLE witness, so the lifted "
       "search is never checked against a case the filter should pass")
    print("  planted states where the filter alone hides a cheaper witness: "
          "%d; where both find one: %d" % (fired_eligible, fired_both))


# ---------------------------------------------------------- S2 the twelve
def s2_dump(twelve):
    """PR2: the twelve, whole."""
    print("  #  ring     world    region      species   tags")
    print("     cost tick  core A (deg,exp,kind)   core B (deg,exp,kind)")
    for i, r in enumerate(twelve):
        (pa, ea, ra, ka), (pb, eb, rb, kb) = r["reads"]
        R = r["L"].R
        print("  %-2d %-8s %-8s %-11s %-9s %s"
              % (i + 1, r["ring"], r["world"], r["region"], r["sp"],
                 r["why"]))
        print("     %-4d %-5d %-22s %s"
              % (r["cost"], UC.tick(r["lam"]),
                 "d%d e%d %s" % (R.deg[pa], ea, ka),
                 "d%d e%d %s" % (R.deg[pb], eb, kb)))
        ok(r["sp"] == "odd-even",
           "a no-undercut residual of species %s, not odd-even" % r["sp"])
        ok(r["why"] == "eligible+no-undercut",
           "a no-undercut residual whose tags read %s" % r["why"])
        tgt = [br for br in r["branches"] if br[4] == "no-undercut"][0][1]
        ok(tgt[1][3] != "fresh",
           "%s: the no-undercut branch targets the FRESH member" % r["ring"])
    # HOW MANY OBJECTS ARE THESE REALLY. "Twelve pairs" is a count of
    # (state, pair) records, and a tie state with several members of one
    # type contributes several pairs off ONE state -- so the honest size of
    # the residual is its distinct STATES, which is what a reader takes
    # "twelve" to mean and what nobody has counted.
    states = set(RO.vkey(r["st"]) for r in twelve)
    rings = set((r["ring"], r["world"]) for r in twelve)
    print("  the twelve are %d DISTINCT tie states over %d ring-world "
          "slices" % (len(states), len(rings)))


# ------------------------------------------------------ S3 the absence
def s3_absence(twelve):
    """PR3: is the absence the eligibility filter, or is it absence?"""
    print("  #  target    own  best witness      gap  slack  why it refuses")
    split = {}
    for i, r in enumerate(twelve):
        L, world = r["L"], r["world"]
        br = [b for b in r["branches"] if b[4] == "no-undercut"][0]
        _, other, st2, lam2, _, _ = br
        po = other[1][0]
        own = UC.price(L, st2, po, lam2)
        bf = best_witness(L, world, st2, lam2, po, False)
        bl = best_witness(L, world, st2, lam2, po, True)
        slack = 0 if world == "ideal" else L.g
        ok(bf is None or bf[2] + slack >= own,
           "#%d: the FILTERED search finds a cheaper witness where the "
           "parent rig reported none" % (i + 1))
        ok(bl is None or bl[2] + slack >= own,
           "#%d: the LIFTED search finds a cheaper witness, which PR3 "
           "predicted and the run must then report" % (i + 1))
        # the three ways a refusal can arrive, which the one tag conflates
        if bf is None:
            why = "no witness at all"
        elif bf[2] == own:
            why = "TIED exactly"
        elif bf[2] < own:
            why = "cheaper, INSIDE the slack"
        else:
            why = "dearer"
        split[why] = split.get(why, 0) + 1
        print("  %-2d d%-2d e%-4d %-4d %-17s %-4s %-6d %s"
              % (i + 1, L.R.deg[po], st2.get(po, 0), own,
                 "-" if bf is None else "d%d e%d @ %d"
                 % (bf[1], st2.get(bf[0], 0), bf[2]),
                 "-" if bf is None else str(own - bf[2]), slack, why))
    print("  the twelve by WHY the certificate refuses: %s"
          % dict(sorted(split.items())))
    print("  worlds: %s" % dict(sorted(
        (w, sum(1 for r in twelve if r["world"] == w))
        for w in set(r["world"] for r in twelve))))
    return split


# --------------------------------------------- S5 is the tie one move old?
def s5_tiebreak(twelve):
    """THE SECTION THE RUN ADDED, its slate frozen before its engine.

    S3 shows the twelve refused not for want of a witness but because the
    cheapest one is TIED with the target or cheaper only inside the genus
    slack. A tie between a witness Q and a target P is not symmetric when
    deg Q < deg P: a CLOCK move at Q sends price(Q) to deg Q * (T' - T) and
    price(P) to deg P * (sigma_P + T' - T), and with deg Q < deg P and
    sigma_P >= 1 the second is strictly larger -- by (deg P - deg Q)(T' - T)
    plus deg P * sigma_P, which at T' = 2T is a margin the tick doubles
    thereafter. So the ABSENCE should be TRANSIENT: one move at the tied
    witness and the certificate fires.

    PR5, frozen before this engine ran. What the rig PRINTS: for each of the
    twelve, the degrees of witness and target, whether the witness's own door
    vehicle is a MINIMAL move at the state the certificate refused on, and
    the undercut verdict on the target at the successor of that move.
    KILL: one of the twelve where the certificate still refuses after a clock
    move at the tied witness. That would mean the tie is not one move from a
    certificate and the transience reading is wrong.
    WHAT IT DOES NOT SETTLE, fixed here so the run cannot be read past it: a
    certificate at a LATER state freezes the target from there on, which is a
    statement about that state's continuations and not about the branch pair
    at the tie -- unless the move is minimal, in which case it is on the
    greedy path itself. The minimality column is what separates the two and
    it is printed either way."""
    print("  #  witness  target  witness move minimal?  undercut at the "
          "successor")
    fires = minimal = 0
    for i, r in enumerate(twelve):
        L, world = r["L"], r["world"]
        br = [b for b in r["branches"] if b[4] == "no-undercut"][0]
        _, other, st2, lam2, _, _ = br
        po = other[1][0]
        bw = best_witness(L, world, st2, lam2, po, False)
        if bw is None:
            print("  %-2d %-8s %-7s %-22s %s" % (i + 1, "-", "-", "-", "-"))
            continue
        q = bw[0]
        rq = UC.sigma(L.R, st2, q, lam2)
        veh = {q: rq} if world == "ideal" else L.complete(q, rq)
        try:
            _, _, ties = RO.menu_of(L, world, st2)
            mins = [RO.vkey(v) for v in ties]
        except AssertionError:
            mins = []
        is_min = RO.vkey(veh) in mins
        st3 = EC.apply_veh(st2, veh)
        lam3 = L.R.lam_state(st3)
        v, tag, detail = UC.undercut(L, world, st3, lam3, po)
        fires += bool(v)
        minimal += bool(is_min)
        print("  %-2d d%-7d d%-6d %-22s %s"
              % (i + 1, bw[1], L.R.deg[po], "YES" if is_min else "no",
                 "FIRES -- %s" % detail if v else "refuses (%s)" % tag))
    print("  the certificate fires at the successor in %d of %d, and the "
          "witness's" % (fires, len(twelve)))
    print("  move is itself minimal in %d of %d" % (minimal, len(twelve)))
    ok(fires == len(twelve),
       "the tie is not one move from a certificate: %d of %d still refuse"
       % (len(twelve) - fires, len(twelve)))

    # PR6, frozen before this loop ran. ONE minimal move certifying says the
    # target freezes along THAT continuation; the branch pair is a claim
    # about the whole minimal-move class, which is what the parent rig's
    # rejoin search quantifies over. So every minimal move at the refusing
    # state is applied and the target re-tested. What the rig PRINTS: per
    # pair, the number of minimal moves, how many are the target's OWN core
    # (where it deepens instead of freezing), and how many of the rest
    # certify it. KILL: nothing -- this is printed, not predicted; a mixed
    # column means the freeze is policy-dependent and the twelve stay open
    # for the reason this column names rather than the one the corpus files.
    print("\n  EVERY minimal move at the refusing state, not only the "
          "witness's")
    print("  #  minimal moves  target's own  others certifying  verdict")
    closed = 0
    for i, r in enumerate(twelve):
        L, world = r["L"], r["world"]
        br = [b for b in r["branches"] if b[4] == "no-undercut"][0]
        _, other, st2, lam2, _, _ = br
        po = other[1][0]
        try:
            _, _, ties = RO.menu_of(L, world, st2)
        except AssertionError:
            ties = []
        own_core = certs = 0
        for veh in ties:
            core = RO.core_of(L, world, st2, veh, lam2)[0]
            if core == po:
                own_core += 1
                continue
            st3 = EC.apply_veh(st2, veh)
            if UC.undercut(L, world, st3, L.R.lam_state(st3), po)[0]:
                certs += 1
        rest = len(ties) - own_core
        verdict = ("FROZEN after one move, every policy"
                   if rest and certs == rest and not own_core
                   else "the target can still move" if own_core
                   else "policy-dependent")
        closed += verdict.startswith("FROZEN")
        print("  %-2d %-14d %-13d %-18s %s"
              % (i + 1, len(ties), own_core, "%d of %d" % (certs, rest),
                 verdict))
    print("  of the twelve, %d freeze the target after one move under EVERY "
          "minimal" % closed)
    print("  move -- the rest are named by their own column above")


# ------------------------------------------------------ S4 the branches
def s4_branches(twelve):
    """PR4: where the two branches stand, move by move."""
    print("  #  step  differing coordinates (place: exp_A / exp_B)")
    for i, r in enumerate(twelve):
        L, world = r["L"], r["world"]
        (va, _, _), (vb, _, _) = r["branches"][0][0], r["branches"][0][1]
        sa = EC.apply_veh(r["st"], va)
        sb = EC.apply_veh(r["st"], vb)
        fresh = [c for c in r["reads"] if c[3] == "fresh"][0][0]
        seated_at = None
        rows = []
        for step in range(FORWARD_T):
            diff = sorted(set(sa) | set(sb))
            d = [(p, sa.get(p, 0), sb.get(p, 0)) for p in diff
                 if sa.get(p, 0) != sb.get(p, 0)]
            rows.append((step, d))
            if seated_at is None and sb.get(fresh, 0) and sa.get(fresh, 0):
                seated_at = step
            for which in ("a", "b"):
                s = sa if which == "a" else sb
                try:
                    _, _, ties = RO.menu_of(L, world, s)
                except AssertionError:
                    ties = None
                if not ties:
                    continue
                if which == "a":
                    sa = EC.apply_veh(s, ties[0])
                else:
                    sb = EC.apply_veh(s, ties[0])
        # THE SEPARATION ITSELF, which is what the whole pair was asking:
        # the target the certificate freezes, read in both branches at the
        # horizon. S5 shows it frozen one move into the branch that declined
        # it; the other branch seats it at its own door, and exponents never
        # fall, so a persistent difference here IS the two limits differing.
        br = [b for b in r["branches"] if b[4] == "no-undercut"][0]
        po = br[1][1][0]
        ea, eb = sa.get(po, 0), sb.get(po, 0)
        ok(ea != eb,
           "#%d: the two branches agree at the frozen target (%d vs %d)"
           % (i + 1, ea, eb))
        first, last = rows[0], rows[-1]
        print("  %-2d %-5d %s" % (i + 1, first[0],
                                  ", ".join("d%d: %d/%d" % (L.R.deg[p], x, y)
                                            for p, x, y in first[1]) or "-"))
        print("     %-5d %s" % (last[0],
                                ", ".join("d%d: %d/%d" % (L.R.deg[p], x, y)
                                          for p, x, y in last[1]) or "-"))
        print("     the declined fresh member (d%d) is seated in BOTH by "
              "step %s" % (L.R.deg[fresh],
                           "-" if seated_at is None else seated_at))
        print("     THE SEPARATION: the certified target (d%d) reads %d "
              "against %d at step %d" % (L.R.deg[po], ea, eb, FORWARD_T - 1))


def main():
    ladder = CT.build_ladder()

    section("S1  THE POSITIVE CONTROL")
    print("(a) THE CENSUS REPRODUCED -- the parent rig's residual roll-up")
    res = collect(ladder)
    twelve = s1a_census(res)
    print("\n(b) THE WITNESS SEARCH WITH THE ELIGIBILITY FILTER LIFTED")
    s1b_witness(ladder)

    section("S2  THE TWELVE")
    s2_dump(twelve)

    section("S3  THE ABSENCE, SPLIT")
    s3_absence(twelve)

    section("S5  IS THE TIE ONE MOVE OLD?")
    s5_tiebreak(twelve)

    section("S4  THE TWO BRANCHES")
    s4_branches(twelve)

    print("\n%d checks passed." % CHECKS)


if __name__ == "__main__":
    main()
