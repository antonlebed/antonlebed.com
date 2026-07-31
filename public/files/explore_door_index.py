r"""explore_door_index.py -- is the door a unit-group index? The ladder
column of (matrix, ladder) read as one filtration rather than three
ingredients.

THE QUESTION. The abstract walker prices a state through a supply MATRIX
n(d, c) over the class group plus a per-item LADDER, and the ladder is a
COLUMN the matrix cannot supply (explore_element_schedule_nf.py; a count of
items per colour carries no per-place ladder). What has never been asked is
whether the ladder is PRIMITIVE. A seated place's door is the least r with
lam(P^(e+r)) not dividing the state's invariant L, and lam(P^a) is the
EXPONENT of a finite unit group -- so read structurally the walk may be
choosing minimal-cost open subgroups in an inverse limit of unit groups,
with the price an INDEX, and the ladder, the gap and the head would be
shadows of ONE filtration rather than three ingredients.

THE MOVE IS A TEST, NOT A REFRAME. Every door below is recomputed from the
residue ring ITSELF -- units enumerated from an HNF basis, orders taken in
the actual group -- and never through any engine's lam_P, then checked
against the door the engine charges. Four rings: the three quadratic
engines (Z[sqrt-5], Z[w] with w^2 = w - 6, Z[i]) and the cubic
Z[x]/(x^3 - x - 1). The brute-forcer and the walker are both IMPORTED
(explore_cubic_ring.py, explore_populated_door.py) rather than rewritten,
so a disagreement is between two things the corpus already trusts.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. The suspicion is
written in the LOCAL UNIT GROUP's terms -- U_j = 1 + m^j, the L-torsion
subgroup, an index -- and deliberately not in the schedule family's, whose
words (colour, gap, ladder, door) are exactly what is under test. A rig
written in the family's vocabulary could only confirm the family.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 From the closed form to all four rings. explore_cubic_ring.py F1's
    (N-1)*p^ceil((a-1)/e) is EXACT at the cubic ring and MISSES at three
    columns of the quadratic engines, all at p = 2 with f = 1. Nothing here
    uses it. Each engine's own hand-derived lam_P is the thing being
    checked, and the brute-forcer is the checker.
 T2 From the ideal world to the element world. Every reading here is
    IDEAL-world: one place, one exponent, no riders. The class layer is
    trivial at the cubic ring (h = 1) and unread at the others. Whether
    the rider's cost is an index too is NOT touched.
 T3 From "index" as a size to "index" as a subgroup index. The price a
    move pays is a NUMBER, N(P)^r; calling it an index is a claim about
    WHICH subgroup pair it counts, and there are two candidates (the
    additive filtration m^e/m^(e+r) and the multiplicative U_e/U_(e+r)).
    They are not equal, and S3 is where they are made to part.

THE HAND-ATTACK, on paper before any engine code.

  (a) THE DOOR IS AN L-TORSION INDEX, and this half is a group-theoretic
  identity rather than a finding. For a finite abelian G, exp(G) divides L
  iff every element is killed by L iff G[L] = G iff [G : G[L]] = 1. So

      door(P, e, L) = least r >= 1 with [G(e+r) : G(e+r)[L]] > 1,
      G(a) = (O/X^a)^*,

  which mentions no lambda and no ladder. Agreement with the engines is
  therefore a CONTROL on their lam_P tables, and the finding would be a
  disagreement. It bites hardest where it is cheapest: all three columns
  the closed form misses are at q = 2, where depth 13 is 8192 residues.

  (b) WHAT THE INDEX AT THE DOOR IS -- and this half is not an identity.
  |G(a)| = q^(a-1)*(q-1), and G(a) = k^* x U_1/U_a with k^* cyclic of order
  q - 1. Suppose (q-1) | L, so the whole of k^* is L-torsion and the door
  is decided by the p-part. Write t = v_p(L). For a Z_p-module
  M = sum Z/p^(c_i), |M[p^t]| = prod p^min(c_i, t), so

      [M : M[p^t]] = prod p^max(c_i - t, 0).

  At a tame place U_1/U_a = m/m^a = O_P/m^(a-1), which as a Z_p-module is
  (Z/p^(k+1))^(s*f) x (Z/p^k)^((e-s)*f) for a - 1 = k*e + s, 0 <= s < e.
  The door is the LEAST a with exp > p^t, i.e. ceil((a-1)/e) = t+1, i.e.
  a - 1 = t*e + 1: so s = 1 and exactly f elementary divisors reach p^(t+1)
  while the rest sit at p^t. [That step is the e > 1 branch written as if it
  were universal, and e = 1 is the commonest case: there a - 1 = t + 1 and
  s = 0, so the count is e*f rather than s*f. It is f either way, so the
  conclusion below is unaffected and F3 states the step correctly. Left
  standing because the design is the record of what was frozen.] Hence

      [G(door) : G(door)[L]] = p^f = q -- EXACTLY ONE RESIDUE LAYER,

  while the PRICE is q^r. So the walk pays r layers to buy one layer's
  worth of escape, and the premium is q^(r-1). [The clause this paragraph
  froze next -- "r > 1 at a seated place is exactly a ladder that has not
  moved yet" -- is FALSE, and F3 carries the correction: a head is one source
  of a premium and a populated invariant is another. Left standing because
  the design is the record of what was frozen.]
  CHECKED BY HAND AT A HEAD TOO, where the tame derivation does not apply:
  Z[i] at the ramified place over 2 has U_1 = mu_4 x U_3 with U_3 free of
  rank 2, so G(8) = Z/4 x Z/8 x Z/4; from e = 3, L = 4 the engine charges
  r = 5 and a = 8, and the index there is 2^max(2-2,0) * 2^max(3-2,0) *
  2^max(2-2,0) = 2 = q. The one-layer reading survives a plateau.

  (c) WHERE THE INDEX READING BREAKS, found by hand-attacking (b) and
  worth more than (b) confirmed. If (q-1) does NOT divide L the door is
  forced by the PRIME-TO-p part and there is no reason for the index to be
  a power of q at all. The void is precisely that state: L = 1, so at a
  split place of norm 5 the door is r = 1, the price is 5, and the index is
  |F_5^*| = 4, which does not even DIVIDE the price. So "the price is the
  index" is false as stated, and the first prediction this rig would have
  frozen -- index divides price, equality iff r = 1 -- is refuted on paper.
  What survives is a conditional, and the condition is the state having
  already absorbed the residue field's own cyclic part.

  (d) SO WHICH FILTRATION IS THE PRICE? |U(a)| = q^(a-1)*(q-1) gives, for a
  SEATED place (e >= 1), [U_e : U_(e+r)] = q^(e+r-1)/q^(e-1) = q^r = the
  price exactly. At an UNSEATED place (e = 0) the price is still q^r while
  the whole unit group has only q^(r-1)*(q-1) elements -- short by q/(q-1),
  because U_0/U_1 = k^* has order q - 1 and not q. The price is therefore
  uniformly the ADDITIVE index [m^e : m^(e+r)] = q^r, and coincides with
  the multiplicative one precisely on seated places. That is a SEAM at the
  OPENING MOVE, which is where the greedy image's opening count lives.

  (e) AND THE THREE INGREDIENTS ARE ONE SEQUENCE AND TWO OF ITS FEATURES.
  The ladder is a |-> exp(G(a)); the GAP is the eventual constant number of
  rungs per factor of p in that sequence; the HEAD is its transient. Both
  are read OFF the one sequence, so the ladder is not three columns. It is
  still not derivable from the MATRIX: the filtration is fixed by (p, e, f)
  and a colour carries only q = p^f -- 23 = P*Q^2 at the cubic ring being
  two places of one colour whose columns part (explore_cubic_ring.py F4).

DISTRUST THE MARGIN. The derived half is (b), twice -- from the module
structure at a tame place and by hand at Z[i]'s plateau. The VIBES half was
"the price is an index", and hand-attacking it is what produced (c) and (d);
both are frozen as predictions the engine decides, not as results.

PREDICTIONS, fixed before the engine ran, each naming what the rig PRINTS.
  P1 The imported brute-forcer reproduces every engine's OWN filed lam_P at
     every (place, depth) fitting the cap, at all four rings, including
     Z[i]'s hand-derived plateau. 0 disagreements.
  P2 The door recomputed from the residue ring alone -- least r whose
     brute-forced group exponent fails to divide L -- equals the engine's
     door_r at every reading. 0 disagreements. (The PREDICATE is lam_P-free
     at every reading; L is the walk's and therefore is not, so F2 reports
     separately how many readings have L recomputed from the rings too.)
  P3 At every reading where (q-1) | L, the L-torsion index at the door is
     EXACTLY q. One residue layer, at a head as much as at a tame place.
  P4 At readings where (q-1) does NOT divide L, that fails, and the void's
     own openings are the witness: an index that need not divide the price.
  P5 The price q^r equals the multiplicative congruence index
     |U(e+r)|/|U(e)| at every SEATED place, and exceeds it by exactly
     q/(q-1) at every UNSEATED one -- unit counts taken from the enumerated
     residue rings, not from the formula.
  P6 Re-pricing OPENINGS by the multiplicative index changes at least one
     trajectory in at least one of the four rings. The discount is
     q/(q-1), largest at q = 2, so an opening at a norm-2 place is the
     candidate to undercut. (The prediction hit and its stated MECHANISM
     did not, which is why the rig prints undercut-or-tie per divergence
     rather than inferring it: every one is a tie.)
  P7 The gap read off the brute-forced exponent sequence is the
     ramification index e at every place, and the head is 0 at every place
     of the cubic ring and nonzero at exactly the columns the corpus files
     as headed.

KILL-SHAPES, as observables.
  K1 the forcer disagrees with a filed table: the instrument is wrong and
     nothing below is readable.
  K2 a directly computed door differs from the engine's: the walker's doors
     are not this filtration's, and the whole reading is wrong.
  K3 an index at a door with (q-1) | L that is not q: the one-layer reading
     is wrong and the premium has no meaning.
  K4 no walk changes under the multiplicative price: P6 is false and the
     opening seam is inert -- a weaker finding, not a dead one.

THE SECTIONS.
  S1  positive control: the brute-forcer against all four engines' lam_P.
  S2  the door recomputed as an L-torsion index, over walked states.
  S3  the price ledger: which filtration's index the price is.
  S4  the counterfactual walk under the multiplicative price.
  S5  the ladder as one sequence: gap and excess read off brute exponents.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 PRIMITIVE AND ELIMINABLE ARE TWO QUESTIONS, AND "A FURTHER COLUMN" WAS
   HOLDING THEM AS ONE -- THE LADDER IS NOT THE FIRST AND IS NOT THE SECOND
   EITHER (property for the reduction, which is the definition of exp;
   property GIVEN ONE WITNESS for the non-eliminability, the witness being a
   measured pair of places sharing a colour with different columns and
   therefore a rule in range).
   The ladder is a |-> exp((O/X^a)^*), so its GAP and its HEAD are that one
   sequence's asymptotic step and its transient rather than ingredients
   beside it -- NOT PRIMITIVE as a triple. But the sequence is fixed by
   (p, e, f) while a colour carries only q = p^f, so a supply matrix still
   cannot supply it -- NOT ELIMINABLE as a column, with 23 = P*Q^2 at the
   cubic ring the witness (explore_cubic_ring.py F4). That distinction is
   the answer to the question asked, and it is the whole of what is new
   here.
   THE REDUCTION ITSELF IS NOT NEW, AND IT IS NOT EVEN A MEASUREMENT --
   WHICH IS STRONGER AGAINST THIS FILE THAN BEING SCOOPED WOULD BE.
   explore_tick_pump.py F1 states the tick ladder as lambda's jump set with a
   number ring's tail gap its ramification index at 90 of 90 places of norm
   <= 200 to depth 24 -- and that gap is not an observation at all: it is the
   second branch of the level recursion psi(i) = min(p*i, i + e), hence a
   THEOREM for every complete DVR with finite residue field, derived in that
   file's own hand-attack. (explore_head_width.py F2 corrects the HEAD's
   criterion, which is the transient and a different object -- not this gap.)
   So there is nothing here for 12 sequences to add, at any scale or by any
   path.
   WHAT THE SEQUENCES ARE, THEN, IS A CONTROL (rule in range; 12 sequences
   brute-forced from the residue rings at every place of norm <= 12 whose
   column reaches depth 5). A theorem's re-measurement tests the INSTRUMENT:
   gap = e at all 8 places of excess 0, read off enumerated unit-group
   exponents with no lambda consulted, is evidence that the excess measure
   and the enumeration are sound -- which is what F3's readings then rest on.
   Two of the four rings are outside tick_pump's, and the cubic's place sits
   at a ring with no head at ANY place (explore_cubic_ring.py F3, that ring's
   claim and not this sequence's). The 4 sequences
   carrying an excess are Z[sqrt-5] over 2 (2), Z[w]'s TWO split places over
   2 (1 each) and Z[i] over 2 (3) -- four readings of the three distinct
   COLUMNS explore_cubic_ring.py F1 reports the closed form missing, and the
   first three are tick_pump's own three headed places, reproduced by a
   different instrument.
   THE MEASURES ARE NOT THE SAME NUMBER AND MUST NOT BE COMPARED AS ONE:
   tick_pump reports a head as a COUNT OF DEPTHS (4 at Z[sqrt-5] over 2),
   this file as an EXCESS IN RUNGS above the settled gap (2 there). Both are
   features of one sequence; only their zero/nonzero split is shared. The
   excess is summed per step and clipped at 0, a leading step NARROWER than
   the gap not being a head -- the signed sum read Z[i]'s plateau as 2 by
   letting its own first step cancel a rung.

F2 THE DOOR IS AN L-TORSION INDEX, AND THAT HALF IS AN IDENTITY -- SO WHAT
   THE MEASUREMENT IS WORTH IS THE ONE THING IT ADDS TO A CONTROL THAT
   ALREADY EXISTS (property;
   175 doors over walked states of 4 rings, each recomputed as the least r
   with [G(e+r) : G(e+r)[L]] > 1 from enumerated residue rings by a predicate
   consulting no lam_P, 90 of them with the invariant L recomputed there as
   well, 0 disagreements; on 185 filed lambda readings likewise reproduced).
   exp(G) | L iff G[L] = G iff the index is 1, so
   agreement was never going to be news and is not filed as such. NOR IS
   THE INDEPENDENT RECOMPUTATION ITSELF NEW: explore_populated_door.py F1
   already recomputes the seated door as a VALUATION predicate independent
   of the engine's divisibility test and reproduces door_r at 717 readings,
   with the k^* x U_1/U_a splitting that makes it work stated there as a
   property of every Dedekind domain with finite residue fields. WHAT IS
   ADDED IS THE PATH: that control still reads a filed lam_P, so it checks
   the engines' PREDICATE and not their COLUMNS. These 175 read no filed
   column, so every door the four engines charge -- Z[i]'s hand-derived
   plateau included -- now stands on enumerated residue rings. The instrument
   is explore_cubic_ring.py's monic-order forcer at a fourth job.
   AND THE PATH IS NOT LAMBDA-FREE AT ALL 175, WHICH THE FIRST DRAFT OF THIS
   FINDING CLAIMED. The door PREDICATE consults no lam_P anywhere, but the
   invariant L it is tested against is the WALK's, and the walk computes L
   from lam_P. So L is recomputed from the residue rings too wherever every
   seated place fits the enumeration cap -- lcm of brute-forced exponents --
   and asserted against the engine's, with the door re-derived off the brute
   L: 90 of the 175, 0 off. Those 90 are the readings with no lambda anywhere
   in the path; the other 85 check a lambda-free predicate against a
   lambda-derived L, which is a weaker and still useful thing.

F3 AT A SEATED PLACE THE DOOR BUYS ONE RESIDUE LAYER WHILE THE WALK PAYS FOR
   r OF THEM, SO THE MOVE CARRIES A PREMIUM OF q^(r-1) -- AND A HEAD IS ONE
   OF ITS TWO SOURCES, NOT THE DEFINITION OF IT. SEATED IS THE WHOLE SCOPE:
   at an opening the index is not one layer and there is no premium to read,
   which is the second half of this finding and not a caveat on it (rule in
   range;
   170 L-torsion indices counted element by element inside a 4096-residue
   cap, every one with (q-1) | L equal to q). Where the state has already
   absorbed the residue field's cyclic part, the index at the door is
   EXACTLY q at every reading -- one layer -- while the price is q^r. The
   derivation is the module structure: at the least a with
   ceil((a-1)/e) = t+1 exactly f elementary divisors of O_P/m^(a-1) reach
   p^(t+1) -- s*f of them where e > 1 and e*f where e = 1, f in both cases --
   so the index is p^f = q, and it survives a plateau where that
   derivation does not apply (checked by hand at Z[i], measured here). The
   sharpest specimen printed is Z[sqrt-5] at the ramified place over 2 from
   e = 3: r = 4, price 16, index 2 -- fifteen sixteenths of that price buys
   no new layer.
   THE PREMIUM HAS TWO SOURCES AND THE CRISP FORM OF THIS FINDING KEPT ONLY
   ONE. r > 1 needs v_p(L) to run ahead of what this place's own column has
   reached, and a HEAD is one way -- the ladder has not moved yet. The other
   is a POPULATED invariant: v_p(L) is a max over ALL seated places, so
   another place over the same p pushes r up at a perfectly headless one.
   That is explore_populated_door.py's whole subject and its F4 has the
   witness this file's own walks do not reach -- Z[sqrt-5]'s split place over
   41 at exponent 1, a place of gap 1 with no head at all, whose door is
   widened from 1 to 6 by its conjugate seated at 6. So "a head IS a premium"
   is false in the direction that reads best, and what is true is q^(r-1)
   with r read off the STATE. What the premium IS, either way, is the ratio
   between what a move costs and what it opens -- a quantity the ladder and
   the state jointly set and neither owns.
   AND THE CONDITION IS THE SEATED/UNSEATED SEAM, WHICH IS NOT NEW AND IS
   WHAT MAKES THE ONE-LAYER LAW SCOPED RATHER THAN GENERAL.
   explore_populated_door.py F1 already establishes that a SEATED place has
   q - 1 dividing L so the door's prime-to-p clause drops, and that file's
   own transplant flag calls the e = 0 column a different object; what
   hand-attacking the prediction added was that the difference is visible in
   the INDEX. Where (q-1) does not divide L the door is forced by the
   prime-to-p part and the index need not even DIVIDE the price: all 8 such
   readings break the law, and they are openings -- Z[i] opening its inert
   place over 3 at price 9 for an index of 2, the cubic ring opening a
   rational place at price 5 for an index of 4.

F4 THE PRICE IS THE ADDITIVE FILTRATION'S INDEX, AND ITS MULTIPLICATIVE
   READING PARTS FROM IT AT THE OPENING MOVE BY EXACTLY q/(q-1) (rule in
   range; 204 seated and 143 opening readings over the 14 least-norm places
   of each of the 4 rings at e = 0..3 and r = 1..3, every unit count
   ENUMERATED from the residue ring rather than taken from the formula the
   check is testing). At a SEATED place the price N(P)^r is
   the congruence index |U(e+r)|/|U(e)| exactly; at an UNSEATED one the
   same price exceeds that index by q/(q-1), because U_0/U_1 is the residue
   field's k^* of order q-1 and not q. So the price is uniformly
   [m^e : m^(e+r)] and the two filtrations agree precisely on seated
   places. THAT SEAM IS NOT INERT, AND ITS MECHANISM IS DEGENERACY RATHER
   THAN DISCOUNT -- which measuring the divergence instead of naming it is
   what found. Re-pricing openings by the multiplicative index changes 4 of 9
   trajectories, and all 4 divergences are TIES the norm ordering breaks
   rather than undercuts: priced under the SAME rule, the move the additive
   price chose costs exactly what the multiplicative winner costs. Both
   witnesses are arithmetic coincidences of q^(r-1)*(q-1) -- 2^1*1 = 3^0*2 =
   2 sends both void walks to their norm-2 place at r = 2 over a norm-3
   opening at r = 1, and 3^1*2 = 7^0*6 = 6 sends both planted seeds of
   Z[sqrt-5] to a norm-3 opening at r = 2 over a norm-7 one at r = 1. So the
   multiplicative price is strictly LESS SEPARATING on openings than the
   additive one, and it moved no walk by being cheaper anywhere. Which bears
   on a COUNT rather than on a trajectory -- a tie is what an orbit count
   multiplies, and the opening count is where the greedy image's last
   unabstracted factor sits (explore_greedy_image_nf.py). Which of the two
   prices the corpus means has never been asked.

RUN RECORD. `python explore_door_index.py`, under memwatch.py. One process,
CPython, no BLAS. 1057 checks, 6.0 s wall, peak working set 43.0 MB against
the 512 MB ceiling. Four engines imported, never reimplemented: the walker
and its seeds from explore_populated_door.py, the monic-order brute-forcer
from explore_cubic_ring.py. S1 185 readings, S2 175 doors -- 90 of them with L
recomputed from the rings as well -- and 170 index
counts of which 8 are unabsorbed and all 8 break the one-layer law, S3 347
price readings, S4 9 walks of which 4 diverge with all 4 divergences ties,
S5 12 sequences with 4 carrying an excess. All seven FROZEN predictions hit
and no kill-shape fired, with one qualification: P6 hit while the mechanism
it named did not, which is why S4 prints tie-or-undercut per divergence
instead of letting the summary infer it. An eighth prediction never reached
the freeze at all -- index divides price, equality iff r = 1 -- killed on
paper at the void during the hand-attack, and P3 is its corrected
conditional form.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from math import gcd

import explore_cubic_ring as CR
import explore_populated_door as PD

CHECKS = 0

BRUTE_CAP = 15000     # residues allowed in one enumerated quotient
IDX_CAP = 4096        # residues allowed when COUNTING an L-torsion index
NORM_CAP = 30         # places entering the S1 control, by norm
WALK_MOVES = 20       # moves from each seed in S2/S4
LADDER_DEPTH = 12     # depths the S5 sequences are read to


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def lcm(a, b):
    return a * b // gcd(a, b)


# ------------------------------------------------------------- the engines
# One record per ring: the module the walker reads, the monic reduction rule
# for the brute-forcer, the map from a place to (p, h(t)), and the ramified
# places the planted seeds use. Nothing about lambda is recorded here.
def _engines():
    quads = CR._load_quadratics()
    out = []
    for name, M in quads:
        T, N0 = CR.QUAD_RULE[M.__name__]
        out.append(dict(name=name, mod=M, R=(N0, T),
                        gen=lambda M, pl: CR.quadratic_ideal(M, pl),
                        rams=[pl for pl in M.UNIVERSE
                              if pl[0] == 'ram' and M.place_norm(pl) <= 30]))
    cub_rams = [pl for pl in CR.UNIVERSE if pl[1] == 2]
    out.append(dict(name="Z[theta] (-23)", mod=CR, R=CR.CUBIC_REDUCE,
                    gen=lambda M, pl: (pl[0], CR.cubic_gen_poly(pl)),
                    rams=cub_rams))
    return out


def brute_ok(eng, pl):
    """Can this place's ideal be handed to the brute-forcer at all?"""
    if eng['mod'] is CR:
        return pl[0] <= CR.ROOT_CAP
    return True


# ------------------------------------- the residue ring, enumerated for real
_UNITS = {}


def units_at(eng, pl, a):
    """(units, one, q) at O/X^a, enumerated from an HNF basis of the ideal.
    The units are the residues NOT lying in X. Cached per (ring, place, a).
    Nothing in this path consults any lam_P."""
    key = (eng['name'], pl, a)
    if key in _UNITS:
        return _UNITS[key]
    M, R = eng['mod'], eng['R']
    n = len(R)
    q = M.place_norm(pl)
    p, hpoly = eng['gen'](M, pl)
    gens = CR.ideal_gens_generic(p, hpoly, R)
    basis = CR.ideal_pow(gens, a, R, n)
    one_basis = CR.hnf(gens, n)
    dims = [basis[i][i] for i in range(n)]
    total = 1
    for d in dims:
        total *= d
    assert total == q ** a, ("residue count %d is not %d^%d at %s"
                            % (total, q, a, pl))
    one = CR.reduce_mod(tuple(1 if k == 0 else 0 for k in range(n)), basis, n)
    zero = tuple([0] * n)
    units = []

    def walk(idx, acc):
        if idx == n:
            u = tuple(acc)
            if CR.reduce_mod(u, one_basis, n) != zero:
                units.append(u)
            return
        for x in range(dims[idx]):
            acc.append(x)
            walk(idx + 1, acc)
            acc.pop()

    walk(0, [])
    val = (units, one, q, basis, R, n)
    _UNITS[key] = val
    return val


def _powmod(u, k, one, basis, R, n):
    res, b = one, u
    while k:
        if k & 1:
            res = CR.reduce_mod(CR.omul(res, b, R), basis, n)
        b = CR.reduce_mod(CR.omul(b, b, R), basis, n)
        k >>= 1
    return res


_EXP = {}


def brute_exp(eng, pl, a):
    """Exponent of (O/X^a)^*, taken in the group itself."""
    key = (eng['name'], pl, a)
    if key in _EXP:
        return _EXP[key]
    units, one, q, basis, R, n = units_at(eng, pl, a)
    order = q ** (a - 1) * (q - 1)
    fac, m, d = [], order, 2
    while d * d <= m:
        while m % d == 0:
            fac.append(d)
            m //= d
        d += 1
    if m > 1:
        fac.append(m)
    fac = sorted(set(fac))
    exp = 1
    for u in units:
        if _powmod(u, exp, one, basis, R, n) == one:
            continue
        o = order
        for r in fac:
            while o % r == 0 and _powmod(u, o // r, one, basis, R, n) == one:
                o //= r
        exp = lcm(exp, o)
    _EXP[key] = exp
    return exp


def torsion_index(eng, pl, a, L):
    """[G(a) : G(a)[L]], counted element by element in the actual group."""
    units, one, q, basis, R, n = units_at(eng, pl, a)
    killed = 0
    for u in units:
        if _powmod(u, L, one, basis, R, n) == one:
            killed += 1
    assert len(units) % killed == 0, "L-torsion is not a subgroup"
    return len(units) // killed


def unit_count(eng, pl, a):
    return len(units_at(eng, pl, a)[0]) if a >= 1 else 1


def brute_state_L(eng, M, st):
    """The state invariant recomputed from the residue rings: lcm of the
    brute-forced exponents over the seated places. Returns None if any
    seated place is outside the enumeration cap -- which is why the door
    readings report how many of them got here, rather than claiming the
    whole path is lambda-free when only the PREDICATE is."""
    out = 1
    for pl, e in st.items():
        if e < 1:
            continue
        if not brute_ok(eng, pl) or M.place_norm(pl) ** e > BRUTE_CAP:
            return None
        out = lcm(out, brute_exp(eng, pl, e))
    return out


def direct_door(eng, pl, e, L):
    """The door computed from the residue rings alone: the least r whose
    brute-forced group exponent fails to divide L. No lam_P in this path.
    Returns None if the search leaves the enumeration cap first."""
    q = eng['mod'].place_norm(pl)
    r = 1
    while q ** (e + r) <= BRUTE_CAP:
        if L % brute_exp(eng, pl, e + r):
            return r
        r += 1
    return None


# ------------------------------------------------- S1 the positive control
def s1_control():
    section("S1  POSITIVE CONTROL -- the brute-forcer against all four "
            "engines' own filed lambda")
    print("  Every door below is recomputed from these residue rings, so the")
    print("  rings have to reproduce the tables the engines charge from")
    print("  FIRST. Z[i]'s ramified column is hand-derived and is the one")
    print("  that matters most: a forcer that reproduces a plateau it did")
    print("  not write is the instrument.")
    print()
    print("  %-15s %-14s %-4s %-11s %-11s %s"
          % ("ring", "place", "a", "brute", "filed", ""))
    n = 0
    for eng in ENGINES:
        M = eng['mod']
        for pl in M.UNIVERSE:
            if M.place_norm(pl) > NORM_CAP:
                if M is not CR:
                    break
                continue
            if not brute_ok(eng, pl):
                continue
            q = M.place_norm(pl)
            for a in range(1, 16):
                if q ** a > BRUTE_CAP:
                    break
                got, want = brute_exp(eng, pl, a), M.lam_P(pl, a)
                flag = "" if got == want else "  <-- DISAGREE"
                if a <= 3 or got != want:
                    print("  %-15s %-14s %-4d %-11d %-11d %s"
                          % (eng['name'], str(pl), a, got, want, flag))
                ok(got == want, "%s: brute %d at %s^%d against filed %d"
                                % (eng['name'], got, pl, a, want))
                n += 1
    print("  ... (depths 4 and up asserted, printed only on disagreement)")
    print("  %d filed readings reproduced, 0 off. The instrument stands." % n)
    return n


# ---------------------------------------------- S2 the door as an index
def s2_doors():
    section("S2  THE DOOR RECOMPUTED AS AN L-TORSION INDEX -- least r with "
            "[G(e+r) : G(e+r)[L]] > 1")
    print("  Left of the bar: what the engine charges. Right: what the")
    print("  residue rings say, with no lambda anywhere in the path. The")
    print("  index column is the one non-tautological number here -- P3 says")
    print("  it is exactly q wherever (q-1) | L, and P4 says the void's own")
    print("  openings break that.")
    print()
    print("  %-15s %-10s %-3s %-14s %-3s %-3s %-8s %-6s %-6s %s"
          % ("ring", "seed", "st", "place", "e", "r", "price", "direct",
             "index", "q-1|L"))
    rows, n_cmp, n_idx, n_break, n_unabs, n_freeL = [], 0, 0, 0, 0, 0
    for eng in ENGINES:
        M = eng['mod']
        for seedname, seed in PD.seeds_for(M, eng['rams']):
            for step, st, L in PD.walk(M, seed, moves=WALK_MOVES):
                _, ties = M.ideal_menu(st, L)
                targets = set(st.keys()) | {ties[0][0]}
                for pl in sorted(targets, key=M.place_key):
                    if not brute_ok(eng, pl):
                        continue
                    e = st.get(pl, 0)
                    q = M.place_norm(pl)
                    eng_r = M.door_r(pl, e, L)
                    dir_r = direct_door(eng, pl, e, L)
                    if dir_r is None:
                        continue
                    # The predicate is lambda-free either way; L is not,
                    # unless the seated places themselves fit the cap.
                    Lb = brute_state_L(eng, M, st)
                    if Lb is not None:
                        ok(Lb == L, "%s state %s: brute L %d against %d"
                                    % (eng['name'], st, Lb, L))
                        n_freeL += 1
                        ok(direct_door(eng, pl, e, Lb) == eng_r,
                           "%s %s^%d: door off a brute L disagrees"
                           % (eng['name'], pl, e))
                    ok(dir_r == eng_r,
                       "%s %s^%d against L=%d: engine door %d, rings %d"
                       % (eng['name'], pl, e, L, eng_r, dir_r))
                    n_cmp += 1
                    a = e + eng_r
                    idx, absorbed = None, (L % (q - 1) == 0) if q > 1 else True
                    if q ** a <= IDX_CAP:
                        idx = torsion_index(eng, pl, a, L)
                        n_idx += 1
                        if absorbed:
                            ok(idx == q,
                               "%s %s at a=%d, L=%d: index %d, not q=%d"
                               % (eng['name'], pl, a, L, idx, q))
                        else:
                            n_unabs += 1
                            if idx != q:
                                n_break += 1
                    key = (eng['name'], seedname, pl, e, L)
                    rows.append((key, eng_r, idx, absorbed))
                    if len(rows) <= 26 or (idx is not None and not absorbed):
                        print("  %-15s %-10s %-3d %-14s %-3d %-3d %-8d "
                              "%-6d %-6s %s"
                              % (eng['name'], seedname[:10], step, str(pl), e,
                                 eng_r, q ** eng_r, dir_r,
                                 "-" if idx is None else idx,
                                 "yes" if absorbed else "NO"))
    print("  ...")
    print("  %d doors recomputed from the rings, 0 off (K2 silent), of which"
          % n_cmp)
    print("  %d had the state invariant L recomputed from the rings TOO and"
          % n_freeL)
    print("  agreed -- the only readings with no lambda anywhere in the path,")
    print("  the predicate being lambda-free at all of them either way.")
    print("  %d of them carried an index count inside the %d-residue cap;"
          % (n_idx, IDX_CAP))
    print("  every one of the %d with (q-1) | L came out at exactly q, and"
          % (n_idx - n_unabs))
    print("  %d of the %d UNABSORBED ones came out at something else --"
          % (n_break, n_unabs))
    print("  P4's witnesses, and the denominator is printed because the two")
    print("  sets are not the same size.")
    return n_cmp, n_idx, n_break, n_unabs, n_freeL, rows


# ----------------------------------------------------- S3 the price ledger
def s3_price():
    section("S3  THE PRICE LEDGER -- which filtration's index the price is")
    print("  price = N(P)^r, from the engines' own ideal_menu. Against it:")
    print("  the MULTIPLICATIVE congruence index |U(e+r)|/|U(e)|, with both")
    print("  unit counts ENUMERATED rather than formula'd. P5 says they agree")
    print("  on seated places and part by exactly q/(q-1) at an opening.")
    print()
    print("  %-15s %-14s %-3s %-3s %-8s %-8s %s"
          % ("ring", "place", "e", "r", "price", "mult idx", "ratio"))
    n_seat, n_open = 0, 0
    for eng in ENGINES:
        M = eng['mod']
        for pl in M.UNIVERSE[:14]:
            if not brute_ok(eng, pl):
                continue
            q = M.place_norm(pl)
            for e in (0, 1, 2, 3):
                for r in (1, 2, 3):
                    if q ** (e + r) > BRUTE_CAP:
                        continue
                    price = q ** r
                    mult = unit_count(eng, pl, e + r) // unit_count(eng, pl, e)
                    if e >= 1:
                        ok(price == mult,
                           "%s %s: seated price %d against mult index %d"
                           % (eng['name'], pl, price, mult))
                        n_seat += 1
                    else:
                        ok(price * (q - 1) == mult * q,
                           "%s %s: opening price %d, mult %d, not q/(q-1)"
                           % (eng['name'], pl, price, mult))
                        n_open += 1
                    if e <= 1 and r <= 2 and q <= 5:
                        print("  %-15s %-14s %-3d %-3d %-8d %-8d %s"
                              % (eng['name'], str(pl), e, r, price, mult,
                                 "1" if price == mult
                                 else "%d/%d" % (q, q - 1)))
    print("  ...")
    print("  %d seated readings: price = |U(e+r)|/|U(e)| exactly."
          % n_seat)
    print("  %d opening readings: price = that index times q/(q-1). The")
    print("  price is uniformly the ADDITIVE index [m^e : m^(e+r)] = q^r,")
    print("  and the multiplicative reading is short at the opening because")
    print("  U_0/U_1 is the residue field's k^*, of order q-1 and not q.")
    return n_seat, n_open


# ------------------------------------------------ S4 the counterfactual walk
def mult_price(M, pl, e, r):
    """What the move would cost if the price were the MULTIPLICATIVE index."""
    q = M.place_norm(pl)
    return q ** r if e >= 1 else q ** (r - 1) * (q - 1)


def mult_menu(M, st, L):
    """The same menu under the multiplicative price. The break threshold is
    NOT the ideal menu's: an opening at norm q can cost as little as q - 1,
    so a place of norm above `best` may still undercut and the scan may only
    stop once nrm - 1 exceeds best. It must also stop by BREAKING -- a scan
    that runs out of universe has not proved its minimum, which is what the
    engines' own `best <= MAXP` guard says and what a truncated trajectory
    would hide."""
    best, ties, broke = None, [], False
    for pl in M.UNIVERSE:
        nrm = M.place_norm(pl)
        if best is not None and nrm - 1 > best:
            broke = True
            break
        e = st.get(pl, 0)
        r = M.door_r(pl, e, L)
        cost = mult_price(M, pl, e, r)
        if best is None or cost < best:
            best, ties = cost, [(pl, r)]
        elif cost == best:
            ties.append((pl, r))
    assert broke, "universe guard: the multiplicative menu was truncated"
    ties.sort(key=lambda t: M.place_key(t[0]))
    return best, ties


def s4_counterfactual():
    section("S4  THE COUNTERFACTUAL WALK -- the same walker with openings "
            "priced by the multiplicative index")
    print("  The seam of S3 is at the OPENING move, which is where the greedy")
    print("  image's opening count lives. If the discount q/(q-1) never")
    print("  changes a choice the seam is inert (K4). Trajectories compared")
    print("  move for move; the first divergence is printed.")
    print()
    n_walks, n_div, n_tie = 0, 0, 0
    for eng in ENGINES:
        M = eng['mod']
        for seedname, seed in PD.seeds_for(M, eng['rams']):
            st_a, st_b = dict(seed), dict(seed)
            L_a, L_b = M.lam_state(st_a), M.lam_state(st_b)
            n_walks += 1
            first = None
            for step in range(1, WALK_MOVES + 1):
                _, ta = M.ideal_menu(st_a, L_a)
                _, tb = mult_menu(M, st_b, L_b)
                if first is None and ta[0] != tb[0]:
                    # Is the winner a strict UNDERCUT, or a TIE the norm
                    # ordering breaks? Priced under the SAME rule, which is
                    # the only comparison that answers it: what the
                    # multiplicative price charges for the move the ideal
                    # price chose.
                    pi, ri = ta[0]
                    rival = mult_price(M, pi, st_b.get(pi, 0), ri)
                    won = mult_price(M, tb[0][0], st_b.get(tb[0][0], 0),
                                     tb[0][1])
                    first = (step, ta[0], tb[0],
                             M.place_norm(pi) ** ri, won,
                             "undercut" if won < rival else "tie at %d" % won)
                pa, ra = ta[0]
                st_a[pa] = st_a.get(pa, 0) + ra
                L_a = M.lam_state(st_a)
                pb, rb = tb[0]
                st_b[pb] = st_b.get(pb, 0) + rb
                L_b = M.lam_state(st_b)
            if first is not None:
                n_div += 1
                if first[5].startswith("tie"):
                    n_tie += 1
                print("  %-15s %-12s move %d: ideal picks %s r=%d at %d, "
                      "mult picks %s r=%d at %d -- %s"
                      % (eng['name'], seedname[:12], first[0],
                         first[1][0], first[1][1], first[3],
                         first[2][0], first[2][1], first[4], first[5]))
            else:
                print("  %-15s %-12s identical for %d moves"
                      % (eng['name'], seedname[:12], WALK_MOVES))
    print()
    print("  %d of %d walks diverge under the multiplicative price, and %d"
          % (n_div, n_walks, n_tie))
    print("  of those divergences are TIES the norm ordering breaks rather")
    print("  than undercuts -- the multiplicative price collapsing options the")
    print("  additive one separates, which is a different fact from a swap.")
    return n_walks, n_div, n_tie


# ------------------------------------------------- S5 the ladder as one seq
def s5_one_sequence():
    section("S5  THE LADDER AS ONE SEQUENCE -- gap and head read off the "
            "brute-forced exponents")
    print("  The sequence is a |-> exp((O/X^a)^*), taken in the group. The")
    print("  GAP is the eventual constant number of rungs per factor of p;")
    print("  the HEAD is the leading stretch of wider gaps. Both are")
    print("  FEATURES of the one sequence rather than columns beside it.")
    print()
    print("  %-15s %-14s %-3s %-3s %-4s %-5s %s"
          % ("ring", "place", "e", "f", "gap", "exc", "exponents"))
    n, n_head = 0, 0
    for eng in ENGINES:
        M = eng['mod']
        for pl in M.UNIVERSE:
            if M.place_norm(pl) > 12:
                if M is not CR:
                    break
                continue
            if not brute_ok(eng, pl):
                continue
            q, p = M.place_norm(pl), M.place_char(pl)
            depth = 1
            while depth < LADDER_DEPTH and q ** (depth + 1) <= BRUTE_CAP:
                depth += 1
            if depth < 5:
                continue
            seq = [brute_exp(eng, pl, a) for a in range(1, depth + 1)]
            vs = [CR.v_p(x, p) if x % p == 0 else 0 for x in seq]
            jumps = [a for a in range(1, depth) if vs[a] > vs[a - 1]]
            if len(jumps) < 2:
                continue
            steps = [jumps[i + 1] - jumps[i] for i in range(len(jumps) - 1)]
            gap = steps[-1]
            tail = len(steps)
            while tail > 0 and steps[tail - 1] == gap:
                tail -= 1
            # The EXCESS: rungs the leading steps carry ABOVE the settled
            # gap. Clipped at 0 per step, because a leading step NARROWER
            # than the gap is not a head and must not cancel one -- the
            # signed sum read Z[i]'s plateau as 2 by subtracting its own
            # first step.
            excess = sum(max(s - gap, 0) for s in steps[:tail])
            e_pl = 2 if (eng['mod'] is not CR and pl[0] == 'ram') else (
                pl[1] if eng['mod'] is CR else 1)
            f_pl = (pl[2] if eng['mod'] is CR
                    else (2 if pl[0] == 'inert' else 1))
            print("  %-15s %-14s %-3d %-3d %-4d %-5d %s"
                  % (eng['name'], str(pl), e_pl, f_pl, gap, excess,
                     ",".join(str(x) for x in seq[:8])))
            if excess == 0:
                ok(gap == e_pl,
                   "%s %s: headless gap %d against e=%d"
                   % (eng['name'], pl, gap, e_pl))
            else:
                n_head += 1
            n += 1
    print("  %d sequences read, %d of them carrying an excess. A place with" % (n, n_head))
    print("  excess 0 has gap = e; an excess IS the same sequence's transient,")
    print("  not a second column beside it.")
    return n, n_head


ENGINES = _engines()


def main():
    print(__doc__.split("THE QUESTION.")[0].strip())
    n1 = s1_control()
    n2, n_idx, n_break, n_unabs, n_freeL, _ = s2_doors()
    n_seat, n_open = s3_price()
    n_walks, n_div, n_tie = s4_counterfactual()
    n5, n5_head = s5_one_sequence()
    section("SUMMARY")
    print("  S1 %d filed lambda readings reproduced from the residue rings"
          % n1)
    print("  S2 %d doors recomputed as L-torsion indices (%d of them with L"
          % (n2, n_freeL))
    print("     recomputed from the rings too), %d indices counted," % n_idx)
    print("     %d of %d unabsorbed readings breaking the one-layer law"
          % (n_break, n_unabs))
    print("  S3 %d seated + %d opening price readings" % (n_seat, n_open))
    print("  S4 %d of %d walks diverge under the multiplicative price, %d of"
          % (n_div, n_walks, n_tie))
    print("     the divergences being ties the norm ordering breaks")
    print("  S5 %d exponent sequences read, %d carrying an excess"
          % (n5, n5_head))
    print("  %d checks." % CHECKS)


if __name__ == "__main__":
    main()
