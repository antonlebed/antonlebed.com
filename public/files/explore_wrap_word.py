"""
explore_wrap_word.py -- THE WRAP WORD: is the sublinear-supply rider's
landing sequence automatic? (Sibling of explore_pending_fires.py, which
measured this word and left its arithmetic as the named residual; and of
explore_decidable_side.py, explore_sqrt_supply.py.)

THE SETTING. A sound decider exists for the growing-window machine on a
sublinear modulus supply, with one hole: a fire branch that consults
another signal's PHASE has its question EXTRACTED rather than answered.
On the canonical supply m_g = ceil(sqrt g) the extracted questions all
have one shape -- "is t_k congruent to a mod L for some k?", where t_k is
the k-th time a frontier-riding counter wraps. Completeness of the
decider on that supply is exactly the arithmetic of that sequence. The
sibling measured the sequence and named a neighborhood for it: the word
looked quasi-Beatty (gaps non-decreasing, bounded multiplicity), which is
where Sturmian and Ostrowski-automatic decision procedures live, and the
logic leg there is already a theorem -- the first-order theory of
Presburger arithmetic plus a Sturmian word is decidable at every
quadratic irrational. So the residual narrowed to DEFINABILITY: is this
word automatic in a numeration system that carries such a theory?

THIS SCRIPT ANSWERS THE DEFINABILITY QUESTION, and it starts by asking
whether the question has a referent.

THE OBJECT (this record's own vocabulary; the machine is not under test).
  THE RIDER      the supply-only recurrence v := (v + 1) mod m(g), one
                 pass per tick, g the frontier, m_g = max(2, ceil sqrt g).
  A LANDING      a pass at which v returns to 0. t_k = the k-th landing.
  THE GAP WORD   d_k = t_k - t_(k-1). Its letters are the moduli that
                 wrapped, and they GROW without bound.
  THE RESIDUE WORD  w_k = t_k mod L, for a fixed modulus L. This is the
                 finite-alphabet object, and the extracted questions are
                 questions about it.
  A SINGLETON    a gap value used exactly once. (Most are used twice.)

THE HAND ATTACK (derived on paper before any engine code; the run
adjudicates).

(1) THE CLOSED FORM. After a landing at t the stored value climbs 1 per
pass, so the next landing is the first pass whose elapsed count j equals
the current modulus: j = ceil sqrt(t + j + 2) with the frontier offset
the sibling's rig uses. Since d >= ceil sqrt X is equivalent to
d*d >= X, the gap is
                  d = min{ d >= 2 : d*d - d - 2 >= t },
and the whole word is generated with no simulation at all -- one
non-decreasing pointer, O(1) amortized per landing. The rider itself is
the CONTROL this must reproduce, tick for tick.

(2) MULTIPLICITY IS AT MOST 2, PROVED. Write f(d) = d*d - d - 2. The gap
takes the value d exactly on the landings t in (f(d-1), f(d)], a window
of length f(d) - f(d-1) = 2d - 2, walked in steps of d. Since
2d - 2 < 2d, at most two landings fall in it. So the sibling's measured
"multiplicity <= 2" is not a horizon artifact; it is forced, and its
assertion band of 3 is slack.

(3) THE DRIFT IS LOGARITHMIC, AND ITS RATIO IS TRANSCENDENTAL. The same
window gives the average count 2 - 2/d, so a value is a SINGLETON with
density 2/d, and the singleton count up to gap D is
                  S(D) ~ 2 ln D.
Equivalently the n-th singleton sits at D_n ~ exp(n/2): the singletons
are spaced GEOMETRICALLY with ratio sqrt(e). This is the whole content of
the definability question. A word built from a purely quadratic rule
would be ultimately periodic in k modulo any L -- and the residue word is
NOT, because each singleton shifts the phase by one. The shifts arrive at
positions growing like a geometric sequence, which is exactly the shape
an automatic sequence CAN have (the ruler sequence is 2-automatic, its
marks at the powers of 2). So automaticity turns on the RATIO: base-b
automaticity needs the marks at powers of an integer, Ostrowski
automaticity over a quadratic irrational needs them at the denominators
of its convergents, which grow like powers of a quadratic unit. sqrt(e)
is transcendental (Hermite), so it is neither.
SUPERSEDED BY (5), AND WRONG WHERE IT IS SHARPEST: the ratio is 2, an
integer, so the last two sentences invert the real answer. The step that
fails is the density -- see finding 2. The reasoning ABOUT the ratio
stands and is what made the measured 2 legible on sight.

(4) THE PHRASE HAS NO REFERENT AS WRITTEN. "Ostrowski-automatic over the
expansion of sqrt g" names a continued fraction of a VARIABLE -- g is the
running frontier, not a number, and there is no fixed quadratic
irrational anywhere in this supply. The gap word's own letters are
unbounded, so it is not a word over a finite alphabet at all and no
automaticity predicate applies to it. The vocabulary was inherited from
the neighborhood the sibling reached for, and it named a different
object. The only automaticity question that TYPES is the residue word's,
which is what this script tests.

THE KILL, AS OBSERVABLES THE RIG PRINTS (fixed before the engine).
  LIVES  the residue word's b-kernel COUNT saturates -- stops rising with
         depth -- for some b in {2, 3, 6}. Then a candidate automaton
         exists and the next question is how far it holds.
  DIES   the kernel counts keep rising at every depth through 6 for every
         b, AND the measured singleton slope S(D)/ln D sits in [1.8, 2.2].
         Then the drift is logarithmic with a transcendental ratio and the
         word is automatic in no such system.
Either way the residue questions themselves are separately observable:
whether a class is permanently empty is printed as a first-hit index or
as NONE at the horizon.
  ADJUDICATED (post-run): NEITHER BRANCH FIRED. No kernel saturated, so
  LIVES missed; the slope came in at 1.43 against a band of [1.8, 2.2],
  so DIES missed too. The two branches were written to look exhaustive
  and were not -- DIES welded a kernel observable to a slope observable
  with an AND, so a right kernel reading was voided by a wrong slope
  prediction. The lesson is the weld, not the band: a kill naming two
  independent observables needs them adjudicated separately, or a
  surprise in either one silently disarms the whole criterion. What
  actually decided the question was the singleton VALUES, which no
  branch named because the first slate did not expect them to be
  exactly anything.

SECTIONS.

S1  THE CLOSED FORM, CONTROLLED. Run the concrete rider tick by tick
    over the sibling's horizon and the closed form over the same range;
    the landing sequences must agree exactly. Then reproduce the
    sibling's recorded mod-6 census on its own prefix. This control runs
    FIRST and everything downstream is read only if it passes.

S2  THE ALPHABET. Over landings out to k = 10 million: the largest gap,
    the largest multiplicity, and whether the gaps stay non-decreasing.
    Reads on the derivation of (2), and settles whether the gap word is
    over a finite alphabet at all.

S3  THE DRIFT, AND THE OFFSET RECURRENCE UNDER IT. Collect the singleton
    gap values out to the horizon; print S(D)/ln D at each decade, the
    successive ratios, and the values themselves -- the first slate reads
    the slope, the second reads the list. Then run the offset recurrence
    beside the generator and check the closed forms for t_last and
    t_first against it, landing for landing.

S4  THE RESIDUE WORD. Class censuses mod 6 and mod 60 at k = 10^4, 10^5,
    10^6, 10^7, plus the FIRST index hitting each class, or NONE, and the
    class weights against the derived 2:2:1:2:5. This is where a
    permanently empty class shows -- and whether it is an arithmetic
    obstruction or a small-horizon accident is settled by (6), not by
    the census.

S5  AUTOMATICITY. The b-kernel test: a word is b-automatic if and only if
    its b-kernel -- the set of subsequences w(b^e * k + r) -- is finite.
    Count distinct kernel elements at increasing depth for b in {2, 3, 6}.
    Two rig conditions the test has to meet or it reports nothing. Kernel
    elements are compared on a COMMON PREFIX, so a subsequence shorter
    than that prefix cannot be compared and would drop out silently --
    which reads as saturation for a purely mechanical reason. So the
    depth is capped PER BASE at the point where b^depth still leaves
    every subsequence longer than the comparison prefix, and the cap is
    printed with the counts. And prefix comparison can only MERGE two
    distinct kernel elements, never split one, so the count is a LOWER
    bound -- which is the conservative direction for a prediction of
    non-saturation. Positive controls run first: the routine must return
    2 on the Thue-Morse word, which is 2-automatic, and a small constant
    on a periodic word.

S6  THE DECISION PROCEDURE. The extracted question class, answered: given
    L, compute the reachable residues from the closed form alone -- v*v
    and v*v - v over v mod L, against the eventual cycle of 6 * 2^n mod L
    -- and check the answer against brute enumeration of the landings,
    for every L from 2 to 60.

PREDICTIONS (fixed before the run; adjudication added post-run).
  PR1  The closed form reproduces the concrete rider's landings exactly
       over the sibling's horizon, and the mod-6 census on the sibling's
       own prefix is its recorded one: class 4 empty, class 5 carrying
       roughly triple weight.
  PR2  Gaps non-decreasing to k = 10^7; maximum multiplicity exactly 2,
       never 3 -- the sibling's band is slack by one.
  PR3  S(D)/ln D lands in [1.8, 2.2] at the horizon, and the late
       singleton ratios D_(n+1)/D_n cluster near sqrt(e) = 1.6487.
  PR4  Class 4 mod 6 is hit at some finite k -- the phase drift is
       unbounded, so no class is permanently forbidden -- and the first
       such index is printed. Falsifier: still empty at k = 10^7.
  PR5  The mod-60 hit count rises strictly with the horizon and reaches
       at least 50 of 60 classes by k = 10^7.
  PR6  Controls pass (Thue-Morse kernel 2, periodic word small). The
       mod-6 residue word's kernel count RISES at every depth, to the
       per-base cap, for b = 2, 3 and 6 -- no saturation, hence no
       automaton in any of these bases.

THE SECOND SLATE (frozen after the first run, before its engine code).
The first run refuted PR3 head-on and handed back a sharper object. The
singleton count was LOGARITHMIC as predicted, but the coefficient came
in at 1.47, not 2 -- and the singleton gap values printed as
2, 3, 6, 12, 24, ..., that is EXACTLY 3 * 2^n. The spacing ratio is 2,
an integer, not the transcendental sqrt(e) the density argument
predicted; so the density argument was wrong about which landings are
rare, and the rigidity it missed is the whole answer.

(5) THE OFFSET RECURRENCE (hand-derived from the printed singletons,
before the second engine). Write f(v) = v*v - v - 2, so value v takes
its sources in (f(v-1), f(v)], and track the TOP OFFSET
                  a_v = f(v) - t_last(v),
the distance from the window's top to the last source in it. The next
window's first source is t_last(v) + v, so the second source there
exists exactly when a_v >= 1, and the two branches close:
      a_v >= 1  (two sources)  =>  a_(v+1) = a_v - 1
      a_v == 0  (one source)   =>  a_(v+1) = v.
The offset COUNTS DOWN and RESETS TO v on reaching zero. So a singleton
at v + 1 puts the next zero exactly v steps later, hence the next
singleton at 2v + 2: the singletons DOUBLE, which is what the run
printed. Solving the recurrence gives, with s(v) the largest 3 * 2^n that is at
most v,
      a_v = 2 s(v) - 1 - v,
so a_v = 0 exactly at v = 2 s(v) - 1, and the singleton is the value
ABOVE it, v + 1 = 2 s(v), which is the next 3 * 2^n. The landing set is
then closed-form and recurrence-free:
      t_last(v)  = v*v - 2 s(v) - 1
      t_first(v) = v*v - v - 2 s(v-1) - 1.
The two indices differ -- t_first is fed by the PREVIOUS window's
offset -- and s(v) = s(v-1) at every v except v = 3 * 2^n, where the two
formulas COINCIDE at v*v - 2v - 1. That coincidence IS the singleton:
the window's only landing is both its first and its last.

(6) THE MOD-6 EXCLUSION IS A THEOREM, NOT A HORIZON ARTIFACT. Since
s = 3 * 2^n, the term 2s = 6 * 2^n vanishes mod 6, and the landings mod 6
are exactly v*v - 1 and v*v - v - 1. Over v mod 6 those are
{5, 0, 3, 2, 3, 0} and {5, 5, 1, 5, 5, 1}: the union is {0, 1, 2, 3, 5}
and CLASS 4 IS NEVER HIT, for every k. The same count gives the weights
0:2, 1:2, 2:1, 3:2, 5:5 per six values of v -- the triple weight on
class 5 the first run reproduced. So PR4 is refuted, and refuted by a
proof rather than by a longer horizon: a program halting on a landing
congruent to 4 mod 6 loops forever, and that is now a rule.

(7) SO THE DEFINABILITY QUESTION HAS AN ANSWER, IN THE WRONG
NUMERATION. The word is not Sturmian and not Ostrowski over any
quadratic irrational -- there is none in sight. It is indexed by the
GAP VALUE v, and the only non-polynomial ingredient is s(v), the largest
3 * 2^n below v, which is read off v's leading BINARY digits. Mod L the
whole landing set is therefore a finite union of arithmetic data:
v*v and v*v - v are periodic in v mod L, and 6 * 2^n mod L is eventually
periodic in n. Hence the extracted question class is DECIDABLE by a
finite check, with no automaticity theorem needed.

SECOND-SLATE PREDICTIONS (fixed before its engine code).
  PR7  The offset recurrence's two branches reproduce the generator's
       gap word exactly out to the horizon, and the singleton set is
       exactly {2} union {3 * 2^n} -- the 2 being the initialization
       edge, everything above it the doubling.
  PR8  The closed forms t_last(v) = v*v - 2 s(v) - 1 and
       t_first(v) = v*v - v - 2 s(v-1) - 1 reproduce the landing
       sequence exactly and in order, coinciding exactly at the
       singletons.
  PR9  Class 4 mod 6 is empty at every horizon (superseding PR4, which
       predicted the opposite), and the class weights converge to
       2:2:1:2:5 on classes 0, 1, 2, 3, 5.
  PR10 The decision procedure -- reachable classes mod L computed from
       v mod L and the cycle of 6 * 2^n mod L -- agrees with brute
       enumeration of the landings for every L from 2 to 60.

RESOURCE ENVELOPE (named before the run). Streaming counters only at the
10^7 horizon -- no landing list is retained; the kernel test holds one
bytearray of 10^6 letters. Well inside the 512MB analysis ceiling.
Estimated wall clock under two minutes, dominated by the 10^7 pointer
walk.

PREDICTIONS ADJUDICATED (post-run). PR1, PR2, PR7, PR8, PR9 and PR10
CONFIRMED. PR3, PR4 and PR5 REFUTED, and all three by the same
discovery -- the word is far more rigid than the first slate's density
heuristic allowed. PR6 confirmed in the letter (no kernel saturates)
but SUPERSEDED in its meaning: the answer was never going to come from
the k-indexed word, and the finite kernel test is evidence, not proof.
Four rig errors preceded the clean run, each caught by the script's own
asserts before any finding was written: the kernel depth was uncapped
(short subsequences dropping out would have read as saturation), the
offset was transcribed with a spurious + v, t_first was written over
s(v) where the derivation gives s(v-1), and the decision procedure
dropped the pre-period of 6 * 2^n mod L -- which silently lost classes
at every L divisible by 4, and was caught only because the procedure was
checked against brute enumeration rather than trusted.

FINDINGS (entered after the run; every number below is printed output;
run record at the end).

1. THE WRAP WORD IS CLOSED-FORM, AND THE SUPPLY'S ARITHMETIC IS SOLVED
   (rule, proved by the offset recurrence and mechanized; S3b). With
   f(v) = v*v - v - 2 and s(v) the largest 3 * 2^n at most v, every
   landing is
        t_last(v)  = v*v - 2 s(v) - 1,
        t_first(v) = v*v - v - 2 s(v-1) - 1,
   and the two coincide exactly at v = 3 * 2^n. The proof is the offset
   a_v = f(v) - t_last(v): it counts DOWN by one per gap value and
   RESETS to v on reaching zero, because the window (f(v-1), f(v)] has
   length 2v - 2 and is walked in steps of v. Checked against the
   generator for every gap value 4..100009 and on all 199999 landings
   from t = 5 to t = 10001803491, in order and with no extras. So the
   sequence needs no simulation at all, and the "residue problem" was
   never a problem about a word -- it is a problem about one quadratic
   and one power of two.

2. THE SINGLETONS ARE EXACTLY THE POWERS-OF-TWO MULTIPLES OF 3 (rule;
   S3). The gap values used once rather than twice are 2 (the
   initialization edge) and 3 * 2^n -- all 22 of them out to gap
   5000012, ratios printing as 2.000 with no exception. This is the
   whole of the word's non-polynomial content, and it is what makes the
   count logarithmic: S(D) = 2 + floor(log2(D/3)) exactly, so
   S(D)/ln D = 1.426 at the horizon gap 5000012, converging to
   1/ln 2 = 1.443 from below and nowhere near the 2 the density
   heuristic gave -- the shortfall at any finite horizon being the
   2 - log2(3) = +0.415 offset of the two edge singletons, divided by
   ln D. THE
   HEURISTIC NAMED THE WRONG RARE EVENT: it computed the AVERAGE count
   per gap value (2 - 2/v) and read the deficit as a density, when the
   deficit is not spread at all -- it is one event per doubling. An
   average is not a density unless the deviations are independent, and
   here they are perfectly correlated by the reset.

3. CLASS 4 MOD 6 IS EMPTY FOR EVERY k AT THIS FRONTIER OFFSET -- a
   genuine arithmetic obstruction, not a horizon artifact, and not a
   fact about the supply either (rule; S4, scoped by S7 and finding 6).
   Since s(v) = 3 * 2^n,
   the term 2 s(v) = 6 * 2^n vanishes mod 6, so the landings mod 6 are
   exactly v*v - 1 and v*v - v - 1; over v mod 6 those take the values
   {5, 0, 3, 2, 3, 0} and {5, 5, 1, 5, 5, 1}. Four is in neither list.
   The same count fixes the weights at 0:2, 1:2, 2:1, 3:2, 5:5, which
   the census meets to three decimals at 10^7 landings
   ({0: 1666670, 1: 1666670, 2: 833335, 3: 1666670, 5: 4166655}) and
   which explains the sibling's recorded triple weight on class 5: it
   is v*v - v - 1 landing on 5 at four of the six classes of v. So a
   growing-window program that halts on a landing congruent to 4 mod 6
   LOOPS FOREVER, and that is now decided rather than extracted.

4. THE EXTRACTED QUESTION CLASS IS DECIDABLE, BY A FINITE CHECK (rule
   by construction, verified; S6). Given L, the reachable residues are
   computed from the closed form alone: v*v and v*v - v over v mod L,
   against the tail set of 6 * 2^n mod L, with the narrow blocks
   enumerated outright below the point where a block first spans L
   consecutive values of v. Verified equal to brute enumeration of the
   landings for every L from 2 to 60. The exclusions are large and
   structural, not incidental -- L = 60 excludes 22 of its 60 classes,
   L = 56 excludes 19, L = 48 excludes 18 -- and they are FIXED: the
   mod-60 census reads 38 of 60 classes at k = 10^4 and the same 38 at
   k = 10^7, refuting the prediction that the reachable set grows.
   Completeness of the sound decider on this supply is therefore no
   longer conditional on a conjecture.

5. THE CONJECTURE'S OWN VOCABULARY NAMED THE WRONG OBJECT (finding
   about the question, not the answer; S2 and the hand attack). Three
   layers, each fatal on its own. The GAP word's letters grow without
   bound -- the largest is 5000012 at the horizon -- so it is not a word
   over a finite alphabet and carries no automaticity predicate at all.
   "Ostrowski-automatic over the expansion of sqrt g" names the
   continued fraction of a VARIABLE: g is the running frontier, and
   there is no fixed quadratic irrational anywhere in the supply. And
   the finite-alphabet object that does exist, the residue word, is
   indexed by the landing count k, in which its structure is invisible:
   the b-kernel count rises at every depth to the cap for b = 2
   (3, 7, 15, 31, 63, 109, 155, 180, 191, 200, 206), for b = 3 and for
   b = 6, against controls that return 2 on Thue-Morse and plateau at 21
   on a periodic word. The structure lives in the GAP index v, where it
   is a quadratic plus a leading-binary-digit read. The Sturmian
   neighborhood was inherited from the row the question was asked in,
   and it cost the question its referent: the decidable-logic theorem
   the conjecture leaned on was never needed, because the object was
   never in its scope.

6. THE SUPPLY OWNS THE DOUBLING; THE FRONTIER OFFSET OWNS THE RESIDUES
   (rule; S7, asked by the audit and not by either slate above).
   Everything in findings 1-4 was derived at ONE offset, the sibling
   rig's pregrow = 2, and the two halves separate cleanly. The DOUBLING
   is structural: across offsets 0, 1, 2, 3, 5, 10, 17 and 40 the
   singletons are always a seed followed by exact ratio-2 steps -- seed
   3 at offset 0, 2 at offset 1, 5 at offset 5, 7 at offset 40 -- which
   is forced, since the offset recurrence never reads the offset, it
   only counts down and resets. The RESIDUE answers are not: shifting
   the start shifts every landing, and only pregrow = 2 excludes class 4
   mod 6, every other offset tested hitting all six classes. So the
   mod-6 exclusion of finding 3 is a fact about the sibling rig's
   initialization and never about the sqrt supply, and the decidability
   of finding 4 is what survives generally -- the same derivation runs
   at any fixed offset, with the seed read off the run rather than
   assumed to be 3.

SCOPE + HONESTY. Findings 1, 2 and 3 are proved by the offset
recurrence and hold for every v >= 4, which is where the offset's closed
form is checked and below which s(v-1) has no value: the singletons at
gaps 2 and 3 are initialization edges, verified computationally and not
argued, and every singleton from 6 up is derived. Finding 4's procedure is proved by
construction and checked against enumeration only for L <= 60 and
landings to k = 2000000; larger L is a wider check, not a different
argument. That enumeration runs off the closed-form GENERATOR rather
than the concrete rider, so what pins it to the machine is S1, which
runs the rider tick by tick and finds the two identical -- the chain is
two links and both are checked, but it is a chain and not one check. Finding 5's automaticity leg is the one OBSERVATION here: a
finite kernel test at a capped depth is evidence of non-automaticity in
those three bases, never proof, and prefix comparison makes the counts a
lower bound. Nothing here touches the machine class, the landing lemma
or the supply oracle, all of which are the sibling's and stand. And
findings 1 through 4 are stated AT THE SIBLING RIG'S FRONTIER OFFSET,
which finding 6 is the measurement of: the doubling survives any offset,
the residue answers do not, and no claim here is a claim about every
sublinear supply.

RUN RECORD (python prime/code/memwatch.py prime/code/explore_wrap_word.py;
13.3 s wall clock, 54.1 MB peak working set against the 512 MB ceiling,
16 checks, all sections assert). S1 2437 landings to t = 1500000,
census {0: 408, 1: 407, 2: 204, 3: 407, 5: 1011} reproduced exactly.
S2 10^7 landings, non-decreasing, max multiplicity 2, largest gap
5000012. S3 22 singletons, S(D)/ln D = 1.426 at D = 5000012, values
2 and 3 * 2^n,
late ratios 2.000. S3b recurrence exact for v = 4..100009; closed forms
exact on 199999 landings, t = 5 to 10001803491; 15 coincidences, all at
3 * 2^n. S4 class 4 empty at every horizon, weights 2.000/2.000/1.000/
2.000/5.000, mod-60 38 of 60 at both 10^4 and 10^7. S5 controls 2 and
21-plateau; no base saturates. S6 procedure == brute for all L in 2..60.
S7 eight frontier offsets, every one a seed then exact doubling; only
pregrow = 2 excludes class 4 mod 6.
Verdict: the residue problem is CLOSED -- the wrap word has a closed
form, the extracted question class is decided by a finite check, the
mod-6 exclusion is a proved obstruction at the rig's own offset rather
than an artifact of the horizon (and not a property of the supply,
which is what S7 is for), and the Sturmian framing the question arrived
in had no referent.
"""

import math
from collections import Counter

CHECKS = 0
def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1
    print(f"  [ok] {msg}")


# ---------------------------------------------------------------- #
# the two generators: the concrete rider, and the closed form       #
# ---------------------------------------------------------------- #

def ceil_sqrt(g):
    r = math.isqrt(g)
    return r if r * r == g else r + 1

def rider_landings(horizon, pregrow=2):
    """THE CONTROL. The concrete recurrence, tick by tick: per pass the
    frontier grows by one and v := (v + 1) mod max(2, ceil sqrt g).
    Returns the pass indices at which v returns to 0."""
    g = pregrow
    v = 0
    out = []
    for t in range(1, horizon + 1):
        g += 1
        v = (v + 1) % max(2, ceil_sqrt(max(1, g)))
        if v == 0:
            out.append(t)
    return out

def wrap_gaps(count):
    """THE CLOSED FORM. Yields the gap word d_1, d_2, ... : from a
    landing at t the next gap is the least d >= 2 with d*d - d - 2 >= t.
    The pointer d is non-decreasing, so this is O(1) amortized."""
    t = 0
    d = 2
    for _ in range(count):
        while d * d - d - 2 < t:
            d += 1
        t += d
        yield d

def wrap_times(count):
    """The landing sequence itself, streamed."""
    t = 0
    for d in wrap_gaps(count):
        t += d
        yield t


# ================================================================ #
# S1 -- the closed form, controlled                                 #
# ================================================================ #

SIBLING_HORIZON = 1500000
SIBLING_MOD6 = {0: 408, 1: 407, 2: 204, 3: 407, 5: 1011}

def s1_closed_form_control():
    print("== S1  the closed form against the concrete rider ==")
    concrete = rider_landings(SIBLING_HORIZON)
    n = len(concrete)
    derived = []
    for t in wrap_times(n + 8):
        if t > SIBLING_HORIZON:
            break
        derived.append(t)
    ok(derived == concrete,
       f"closed form == concrete rider on all {n} landings out to "
       f"t = {SIBLING_HORIZON} (no simulation needed)")
    census = Counter(t % 6 for t in concrete)
    ok(dict(sorted(census.items())) == SIBLING_MOD6,
       f"the recorded mod-6 census reproduced exactly on this prefix: "
       f"{dict(sorted(census.items()))} -- class 4 empty, class 5 at "
       f"triple weight")
    return n


# ================================================================ #
# S2 -- the alphabet                                                #
# ================================================================ #

HORIZON_K = 10000000

def s2_alphabet():
    print("== S2  the gap word's alphabet (is it finite?) ==")
    prev = 0
    nondec = True
    mult = 0
    run = 0
    largest = 0
    for d in wrap_gaps(HORIZON_K):
        if d < prev:
            nondec = False
        run = run + 1 if d == prev else 1
        if run > mult:
            mult = run
        prev = d
        largest = d
    ok(nondec, f"gaps non-decreasing over all {HORIZON_K} landings")
    ok(mult == 2,
       f"maximum multiplicity is exactly {mult} -- the window "
       f"(f(d-1), f(d)] has length 2d - 2 < 2d, so two landings is the "
       f"ceiling and three is unreachable")
    ok(largest > 1000,
       f"the largest gap is {largest}: the letters GROW, so the gap word "
       f"is not a word over a finite alphabet and carries no "
       f"automaticity predicate")
    return largest


# ================================================================ #
# S3 -- the drift                                                   #
# ================================================================ #

def s3_drift():
    print("== S3  the singleton drift (slope and ratio) ==")
    singles = []
    prev = 0
    run = 0
    for d in wrap_gaps(HORIZON_K):
        if d == prev:
            run += 1
        else:
            if run == 1 and prev:
                singles.append(prev)
            run = 1
        prev = d
    if run == 1 and prev:
        singles.append(prev)
    print(f"  {len(singles)} singleton gap values up to gap {prev}")
    print("  decade   S(D)   S(D)/ln D")
    for e in range(2, 8):
        D = 10 ** e
        s = sum(1 for x in singles if x <= D)
        if s:
            print(f"  10^{e:<5} {s:<6} {s / math.log(D):.3f}")
    # D is the HORIZON GAP, the same D the decade table uses -- dividing
    # by the last singleton instead would report a different number for
    # the same count.
    slope = len(singles) / math.log(prev) if singles else 0.0
    print(f"  S(D)/ln D = {slope:.3f} at D = {prev} (the horizon gap); "
          f"the first slate predicted 2.0, band [1.8, 2.2]")
    print(f"  asymptote 1/ln 2 = {1 / math.log(2):.3f}, approached from "
          f"below by the {2 - math.log2(3):+.3f} offset of the two edge "
          f"singletons")
    tail = singles[-12:]
    ratios = [b / a for a, b in zip(tail, tail[1:])]
    print(f"  singleton values: {singles[:14]} ...")
    print(f"  late ratios: {', '.join(f'{r:.3f}' for r in ratios)}")
    ok(not (1.8 <= slope <= 2.2),
       f"PR3 REFUTED: the slope is {slope:.3f}, outside its own band -- "
       f"the density argument named the wrong rare event")
    predicted = [2] + [3 * 2 ** n for n in range(30)]
    predicted = [x for x in predicted if x <= singles[-1]]
    ok(singles == predicted,
       f"the singletons are EXACTLY 2 and the powers-of-two multiples of "
       f"3, all {len(singles)} of them -- the spacing ratio is 2, an "
       f"integer, and 1/log(2) = {1 / math.log(2):.3f} is the slope")
    return singles, slope


def s3b_offset_recurrence():
    """The mechanism under the doubling, and the closed form it gives."""
    print("== S3b the offset recurrence and the closed forms ==")
    f = lambda v: v * v - v - 2

    def s_of(v):
        s = 3
        while 2 * s <= v:
            s *= 2
        return s

    # the recurrence run beside the generator's own gap word
    landings = []
    t = 0
    d = 2
    for _ in range(200000):
        while d * d - d - 2 < t:
            d += 1
        t += d
        landings.append(t)
    by_value = {}
    prev = 0
    for a, b in zip([0] + landings, landings):
        by_value.setdefault(b - a, []).append(a)
    # a_v from the recurrence, checked against the generator's windows
    rec_ok = True
    bad = None
    a = None
    vmax = max(by_value)
    for v in range(4, vmax):
        srcs = by_value.get(v)
        if not srcs:
            rec_ok, bad = False, (v, "value skipped")
            break
        a_v = f(v) - srcs[-1]
        if a is not None:
            expect = a - 1 if a >= 1 else v - 1
            if a_v != expect:
                rec_ok, bad = False, (v, f"{a_v} != {expect}")
                break
        a = a_v
        if a_v != 2 * s_of(v) - 1 - v:
            rec_ok, bad = False, (v, f"{a_v} != closed form")
            break
    ok(rec_ok,
       f"the offset recurrence holds for every gap value 4..{vmax - 1}: "
       f"a counts down by 1 and RESETS to v at zero, and its closed form "
       f"a_v = 2s(v) - 1 - v is exact{'' if rec_ok else f' -- FAILED {bad}'}")
    # the closed forms, as the landing set
    derived = []
    for v in range(4, vmax + 1):
        first = v * v - v - 2 * s_of(v - 1) - 1
        last = v * v - 2 * s_of(v) - 1
        if first != last:
            derived.append(first)
        derived.append(last)
    lo, hi = derived[0], derived[-1]
    cut = [t for t in landings if lo <= t <= hi]
    ok(derived == cut,
       f"the closed forms reproduce all {len(derived)} landings from "
       f"t = {lo} to t = {hi}, in order and with no extras -- the "
       f"recurrence is gone")
    coincide = [v for v in range(4, vmax + 1)
                if v * v - v - 2 * s_of(v - 1) - 1 == v * v - 2 * s_of(v) - 1]
    ok(coincide == [3 * 2 ** n for n in range(30)
                    if 4 <= 3 * 2 ** n <= vmax],
       f"the two formulas coincide at exactly the {len(coincide)} "
       f"singletons {coincide[:6]}... -- one landing that is both the "
       f"window's first and its last")
    return vmax


# ================================================================ #
# S4 -- the residue word                                            #
# ================================================================ #

def s4_residues():
    print("== S4  the residue word: which classes are reachable ==")
    marks = {10 ** 4: None, 10 ** 5: None, 10 ** 6: None, 10 ** 7: None}
    c6 = Counter()
    c60 = Counter()
    first6 = {}
    first60 = {}
    snap = {}
    for k, t in enumerate(wrap_times(HORIZON_K), start=1):
        r6 = t % 6
        r60 = t % 60
        c6[r6] += 1
        c60[r60] += 1
        if r6 not in first6:
            first6[r6] = k
        if r60 not in first60:
            first60[r60] = k
        if k in marks:
            snap[k] = (dict(sorted(c6.items())), len(c60))
    print("  horizon      mod-6 census                              mod-60 hit")
    for k in sorted(snap):
        cen, hit = snap[k]
        print(f"  {k:<12} {str(cen):<42} {hit}/60")
    print("  first index hitting each class mod 6: " +
          ", ".join(f"{a}:{first6.get(a, 'NONE')}" for a in range(6)))
    hit60 = len(c60)
    ok(4 not in first6,
       f"PR4 REFUTED: class 4 mod 6 is EMPTY at every horizon out to "
       f"k = {HORIZON_K} -- and by (6) it is empty for every k, since "
       f"2s vanishes mod 6 and neither v*v - 1 nor v*v - v - 1 is ever 4")
    weights = [c6[a] / c6[2] for a in (0, 1, 2, 3, 5)]
    print("  class weights against class 2 (derived 2:2:1:2:5): " +
          ", ".join(f"{w:.3f}" for w in weights))
    ok(all(abs(w - e) < 0.06 for w, e in zip(weights, (2, 2, 1, 2, 5))),
       f"the derived weights 2:2:1:2:5 are met -- the triple weight on "
       f"class 5 is v*v - v - 1 hitting 5 at four of the six v-classes")
    print(f"  mod 60: {hit60} of 60 classes hit at the horizon, "
          f"{snap[10 ** 4][1]} at k = 10^4")
    return first6, hit60, snap


# ================================================================ #
# S5 -- automaticity: the kernel test                               #
# ================================================================ #

KERNEL_LEN = 10000000
KERNEL_CMP = 4000

def max_depth(b, n=KERNEL_LEN, cmp_len=KERNEL_CMP):
    """The deepest e with every subsequence w(b^e * k + r) still longer
    than the comparison prefix -- past it the test stops measuring the
    word and starts measuring the truncation."""
    e = 0
    while n // (b ** (e + 1)) >= cmp_len:
        e += 1
    return e

def kernel_count(word, b, depth, cmp_len=KERNEL_CMP):
    """The b-kernel at a given depth: the distinct subsequences
    w(b^e * k + r) for e <= depth, 0 <= r < b^e, each compared on a
    common prefix. A word is b-automatic iff its full kernel is FINITE,
    so a count that keeps rising with depth is the obstruction. Prefix
    comparison can only merge, so this is a LOWER bound on the count."""
    seen = set()
    for e in range(depth + 1):
        step = b ** e
        for r in range(step):
            seen.add(bytes(word[r::step][:cmp_len]))
    return len(seen)

def thue_morse(n):
    return bytearray(bin(i).count("1") & 1 for i in range(n))

def periodic_word(n, period=7):
    return bytearray(i % period % 2 for i in range(n))

def s5_automaticity():
    print("== S5  the b-kernel test (controls first) ==")
    tm = thue_morse(KERNEL_LEN)
    ok(kernel_count(tm, 2, max_depth(2)) == 2,
       f"control: the Thue-Morse word's 2-kernel is 2 at depth "
       f"{max_depth(2)} -- the routine detects a genuine automatic "
       f"sequence")
    per = periodic_word(KERNEL_LEN)
    pcounts = [kernel_count(per, 2, dep) for dep in range(1, max_depth(2) + 1)]
    ok(pcounts[-1] == pcounts[-2] == pcounts[-3],
       f"control: a periodic word's 2-kernel PLATEAUS -- {pcounts} -- so "
       "the routine detects saturation, which is the observable the kill "
       "is written on (a magnitude bound is not)")
    word = bytearray(t % 6 for _, t in
                     zip(range(KERNEL_LEN), wrap_times(KERNEL_LEN)))
    print("  the residue word mod 6 (depth capped per base):")
    rising = {}
    for b in (2, 3, 6):
        cap = max_depth(b)
        counts = [kernel_count(word, b, dep) for dep in range(1, cap + 1)]
        print(f"  b = {b}, cap {cap}: " +
              "  ".join(f"{c}" for c in counts))
        rising[b] = all(y > x for x, y in zip(counts, counts[1:]))
    ok(all(rising.values()),
       "no b in {2, 3, 6} saturates: the kernel count RISES at every "
       "depth to the cap, so the residue word is automatic in none of "
       "these bases")
    return rising


# ================================================================ #
# S6 -- the decision procedure                                      #
# ================================================================ #

def reachable_mod(L):
    """The extracted question, ANSWERED: which residues mod L does some
    landing take? From the closed form alone -- v*v and v*v - v run over
    v mod L, and 6 * 2^n mod L is eventually periodic in n, so the whole
    reachable set is a finite union.

    The one thing that cannot be waved through: v runs freely over Z/L
    only once a BLOCK is at least L wide, since block n covers exactly
    the v in [3*2^n, 3*2^(n+1)). So the procedure splits at
    N = the least n with 3*2^n >= L. Below N the blocks are narrow and
    the landings are enumerated OUTRIGHT (there are O(L) of them); at and
    above N every residue of v occurs in every block, and what remains is
    the tail set of 6 * 2^n mod L, walked from n = N. Dropping the
    pre-period instead is exactly the error this guards: it silently
    loses classes whenever 4 divides L."""
    N = 0
    while 3 * (2 ** N) < L:
        N += 1
    boundary = 3 * (2 ** N)
    out = set()
    for t in wrap_times(6 * boundary + 8):     # the narrow blocks, outright
        if t > boundary * boundary:
            break
        out.add(t % L)
    tail = set()
    c = (6 * (2 ** N)) % L
    while c not in tail:
        tail.add(c)
        c = (c * 2) % L
    for c in tail:
        for r in range(L):
            out.add((r * r - c - 1) % L)
            out.add((r * r - r - c - 1) % L)
    return out

def s6_decision_procedure():
    print("== S6  the decision procedure against brute enumeration ==")
    brute = {L: set() for L in range(2, 61)}
    for t in wrap_times(2000000):
        for L in brute:
            brute[L].add(t % L)
    mismatches = []
    for L in range(2, 61):
        if reachable_mod(L) != brute[L]:
            mismatches.append(L)
    ok(not mismatches,
       f"the procedure's reachable set matches brute enumeration for "
       f"every L in 2..60 (no mismatch) -- the extracted question class "
       f"is decided by a finite check on the closed form")
    excl = {L: L - len(reachable_mod(L)) for L in range(2, 61)}
    hard = sorted((v, L) for L, v in excl.items() if v)[-6:]
    print("  moduli with the most excluded classes: " +
          ", ".join(f"L={L}: {v} excluded" for v, L in reversed(hard)))
    return excl


# ================================================================ #
# S7 -- what the initialization owns                                #
# ================================================================ #

PREGROWS = (0, 1, 2, 3, 5, 10, 17, 40)

def s7_initialization():
    """THE THIRD SLATE, frozen before this section's code and asked by
    the audit rather than by the first two: everything above was derived
    at ONE frontier offset, the sibling rig's pregrow = 2. Which of it
    belongs to the SUPPLY and which to that choice?

    Predicted (hand): the DOUBLING is structural -- the offset recurrence
    never mentions the offset, it only counts down and resets -- so every
    initialization gives a seed followed by exact doublings, with only
    the seed moving. The RESIDUE answers are not structural: shifting the
    start shifts every landing, so the mod-6 exclusion is a fact about
    pregrow = 2 and not about the supply. Kill: a pregrow whose singleton
    ratios are not 2 would refute the first half; every pregrow excluding
    class 4 mod 6 would refute the second."""
    print("== S7  which of this belongs to the supply, and which to the "
          "offset ==")
    print("  pregrow  singleton seed + ratios          classes hit mod 6")
    all_doubling = True
    excluders = []
    for pg in PREGROWS:
        fires = rider_landings(400000, pregrow=pg)
        gaps = [b - a for a, b in zip([0] + fires, fires)]
        mult = Counter(gaps)
        top = max(mult)
        singles = sorted(d for d, n in mult.items() if n == 1 and d < top)
        ratios = [b / a for a, b in zip(singles[1:], singles[2:])]
        if not all(r == 2.0 for r in ratios):
            all_doubling = False
        hit = sorted(set(t % 6 for t in fires))
        if 4 not in hit:
            excluders.append(pg)
        print(f"  {pg:<8} seed {singles[:2]}, then "
              f"{'x2 exactly' if all(r == 2.0 for r in ratios) else 'NOT x2'}"
              f"        {hit}")
    ok(all_doubling,
       f"the DOUBLING is structural: every offset in {PREGROWS} gives a "
       f"seed then exact x2 -- the offset recurrence never reads the "
       f"frontier offset, it only counts down and resets")
    ok(excluders == [2],
       f"the mod-6 EXCLUSION is not: only pregrow {excluders} excludes "
       f"class 4, and the others hit all six -- so that exclusion is a "
       f"fact about the sibling rig's initialization, never about the "
       f"sqrt supply, and every residue claim here inherits that scope")
    return excluders


if __name__ == "__main__":
    s1_closed_form_control()
    s2_alphabet()
    s3_drift()
    s3b_offset_recurrence()
    s4_residues()
    s5_automaticity()
    s6_decision_procedure()
    s7_initialization()
    print(f"\nALL SECTIONS PASS ({CHECKS} checks)")
