"""IS THE SHORT FAMILY THE 2-TORSION, OR DOES SHORTNESS FALL OFF WITH THE
ORDER? -- the same per-class shares cut by a class's ORDER in the narrow
class group, against one rival dial from the level below the group.

THE QUESTION. explore_class_share.py found the principal deficit at small
p to be the extreme member of a family effect: the AMBIGUOUS classes --
those equal to their own inverse -- run short of their own field's
non-ambiguous classes at small p, at BOTH signs, closing with p at both.
Ambiguity was the finest cut available there because it is computable
without Gauss composition: C = C^-1 is a symmetry of the reduced form.
But "equal to its own inverse" is "order at most 2", and a grading by the
2-rank is consistent with two different laws -- that order 2 is special,
and that shortness falls off with the order and order 2 is merely its
extreme. Composition separates them, and nothing else does. The cut also
lives in the GROUP, which is the same object at both signs, so it is the
first dial tried that could EXPLAIN the sign-independence rather than
re-measure it: every mechanism on the table so far -- the class minimum,
the conductor model the |D| cut ran against -- separates a definite form
from an indefinite one, and the effect does not.

WHOSE VOCABULARY THE SUSPICION IS WRITTEN IN. Probe 1 wrote its suspicion
in the FORM's vocabulary (a class has a minimum) and the minimum graded
nothing. This one is written in the GROUP's: a class has an order, an
inverse, a subgroup it generates. The two vocabularies name the same
classes and have different variables, and the corpus has now failed once
with the geometric one. The rival dial below is deliberately from a THIRD
vocabulary -- REPRESENTATION, what a class can reach at all -- so that
the group is tested against something that is not a weaker copy of it.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) COMPOSITION, AND WHY THE COPRIME ROUTE. Dirichlet composition of
      (a1,b1,c1) and (a2,b2,c2) of the same discriminant is stated in
      general with a gcd(a1, a2, (b1+b2)/2) and is easy to get subtly
      wrong. It is elementary when gcd(a1, a2) = 1: the composite is
      (a1 a2, B, (B^2 - D)/(4 a1 a2)) with B the CRT solution of
      B = b1 mod 2a1 and B = b2 mod 2a2, which is consistent because
      b1 = b2 = D mod 2 and gcd(2a1, 2a2) = 2. So the whole of the
      composition is one CRT, PROVIDED a coprime representative exists
      and can be found. It always can: for gcd(x, z) = 1 the value
      f(x, z) is the leading coefficient of a form equivalent to f, since
      (x, z) completes to a determinant-1 matrix, and the values f(x, z)
      over coprime (x, z) are not all divisible by a fixed prime (a
      primitive form represents integers coprime to any given modulus).
      The transformed form under M = [[x, y], [z, w]] with xw - yz = 1 is
      a' = f(x, z), b' = 2(a x y + c z w) + b(x w + y z),
      c' = f(y, w), and w, y come from the extended gcd of x and z.

  (2) THE ORDER, AND THE COST OF GETTING IT. The order of C is the least
      n with C^n trivial, which is a walk along the cyclic subgroup <C>.
      Walking every class separately costs sum-of-orders compositions per
      field, which is quadratic in h+ and is the reason to do it once:
      the walk of <g> hands back the order of EVERY element it passes,
      since g^j has order n/gcd(j, n). So the classes are processed with
      the orders already learned skipped, and a field with a cyclic group
      costs ONE walk. This is an identity about cyclic groups and not an
      approximation.

  (3) AMBIGUOUS IS ORDER AT MOST 2, WHICH MAKES C2 A REAL CONTROL. Probe
      1's ambiguity test is a symmetry of the reduced form -- reducing
      (a, -b, c) and asking whether it lands in the same class. The order
      computed here comes from composition, which shares no code with
      that test. So "the classes of order at most 2 are exactly the
      classes the form test called ambiguous" is an agreement between two
      independent computations of one subgroup, and it pins the
      composition at every field rather than at a spot check. Probe 1
      already pinned that count to 2^(t-1) at every field of both signs,
      so a third quantity is in the agreement for free.

  (4) THE RIVAL DIAL IS THE SMALLEST REPRESENTED PRIME, AND IT IS THE
      REPAIR OF THE ONE DIAL THAT DIED. Probe 1 killed the class MINIMUM
      m(C) -- the least value a class represents -- as a grading, and the
      minimum is also exactly what produced the trivial class's hard zero
      (no prime below |D|/4 is principal at D < 0, verified there at zero
      violations). Both facts are true because the trivial class's
      minimum is 1 and 1 IS NOT PRIME: the derivation that worked was
      never about the smallest VALUE, it was about the smallest value
      that is a prime the count can see. That is a different dial,
      untried, computable from the sweep, and it makes the question one
      about what a class can reach rather than about group structure. Call
      it q(C), the least split prime the class holds below the cap.

  (5) AND q(C) IS CIRCULAR IF READ NAIVELY, WHICH DECIDES THE DESIGN. A
      class whose first split prime is late has, by definition, fewer
      primes in a bottom bin: "q grades the bottom-bin share" is not a
      finding, it is the same number twice. Two readings answer it and
      both are printed. THE LIVE WINDOW: per field take Q = max over its
      classes of q(C) and read every class's share over the primes above
      Q, where every class of the field is known to be live and no class
      is under its own floor. THE MATCHED-q PAIRING: compare an ambiguous
      class against a non-ambiguous one OF THE SAME FIELD whose q sits in
      the SAME band, which removes the floor without removing any primes.
      The two fail differently and neither is the other's control -- see
      WHAT IS NOT CONTROLLED at the foot.

  (6) THE POPULATION IS PROBE 1'S, UNCHANGED. Fundamental discriminants
      of both signs to |D| <= 4000 over the odd split p <= 10^4, bins and
      MIN_SPLIT identical, so that C2 below compares against a printed
      number rather than a re-derived one.

THE SLATE -- PREDICTIONS, FROZEN BEFORE THE ENGINE, AT BOTH SIGNS. Probe
1's own first reading called its effect one sign's and was wrong, so
every prediction here is stated for both sides or not at all.

  P1. ORDER 2 IS SPECIAL AND SHORTNESS DOES NOT FALL OFF WITH THE ORDER.
      Within fields holding both, the paired bottom-bin gap of the
      NON-TRIVIAL order-2 classes against the classes of order above 2 is
      at most -0.10 at both signs; and among the classes of order above 2
      the means at orders 3, 4 and 5-or-more agree within 0.05 at both
      signs. The reason to expect it: a class of order 2 has a reduced
      form with a symmetry (b = 0, a = b, or a = c) and a class of order
      4 has none, so there is a structural fact at order 2 that has no
      analogue at higher order, while "further from the identity" is a
      distance the group does not otherwise measure.

  P2. THE REPRESENTATION FLOOR IS REAL AND SIGN-INDEPENDENT. Within a
      field, the median q of the ambiguous classes exceeds the median q
      of the non-ambiguous ones at a majority of fields at BOTH signs.
      This is the dial the class minimum failed to be, and unlike the
      minimum it has no reason to separate the signs.

  P3. AND THE FLOOR IS MOST OF THE FAMILY EFFECT. In the live window the
      paired ambiguous deficit is at most half its bottom-bin size at
      both signs. If it holds, the 2-torsion deficit is the trivial
      class's hard zero generalized to the whole subgroup, and the front
      probe 1 left -- a sign-independent effect with no sign-independent
      mechanism -- closes on a mechanism that is about representation and
      not about the class group at all.

  P4. AND THE MATCHED-q PAIRING AGREES WITH THE WINDOW. At matched q the
      paired ambiguous gap is also at most half the unmatched one, at
      both signs. P3 and P4 disagreeing is informative and is why both
      are frozen: they remove the floor by opposite operations.

THE KILLS, AS OBSERVABLES -- what the rig PRINTS, read after the controls
and weighed for meaning only afterward.

  K1 kills P1: the printed within-field paired mean gap, non-trivial
     order-2 against order-above-2, bin 0. A gap shallower than -0.10 at
     either sign kills the first half. And the printed order column over
     3, 4, 5+ over non-ambiguous classes: a spread above 0.05 at either
     sign kills the second, and a MONOTONE such column is the rival law
     rather than noise.

  K2 kills P2: the printed count of fields where the ambiguous median q
     exceeds the non-ambiguous median q, against the count of fields
     holding both. At or below half at either sign is the kill.

  K3 kills P3: the printed live-window paired gap beside the bin-0 paired
     gap, both signs. More than half surviving at either sign is the
     kill.

  K4 kills P4: the printed matched-q paired gap beside the same bin-0
     gap. More than half surviving at either sign is the kill.

THE POSITIVE CONTROLS, run and read FIRST.

  C1. COMPOSITION IS A GROUP LAW, printed as four violation counts. Every
      composed form has discriminant D and integral third coefficient;
      every composed class key is one the field's inventory already holds
      (a key that is not raises rather than mis-counts, which is the pin
      on the reduction as well); the trivial class is a two-sided
      identity; and every class's order divides h+. Any nonzero count
      voids every order in this rig.

  C2. THE 2-TORSION, TWICE. The count of classes of order at most 2 must
      equal the count of classes probe 1's form-symmetry test calls
      ambiguous, at every field of both signs -- two independent
      computations of one subgroup, per derivation (3). Printed as
      disagreements; anything but zero and the composition is wrong or
      the ambiguity test is.

  C3. THE INCUMBENT'S OWN NUMBER. Restricted to the same population and
      bins, the within-field paired ambiguous-vs-non-ambiguous bottom-bin
      gap must reproduce explore_class_share.py's K6: -0.1507 on the real
      side over 189 fields and -0.2160 imaginary over 880. A rig that
      disagrees with the incumbent on the incumbent's own statistic is
      wrong until shown otherwise, and this one shares no code with it
      above the class inventories.

  C4. THE HARD ZERO, RE-READ AS A FLOOR. At D < 0 the trivial class's q
      must be at least |D|/4 at every field, which is probe 1's C4 stated
      in the new dial's own terms rather than re-run in the old one.
      Printed as a violation count.

THE FINDINGS.

  THE CONTROLS. C1 prints zero at all five counts over 1217 imaginary and
  1216 real fields: every composed form has discriminant D and an
  integral third coefficient, every composed key is one the inventory
  already holds, no cyclic walk overran, every order divides h+, and the
  trivial class is a two-sided identity at every field. C6 prints zero
  non-commuting pairs and zero non-associative triples over every field's
  first three classes -- the law itself, which the identity and the order
  checks constrain without pinning, since a rule computing C1 * C2^-1
  would pass an order check and fail a two-sided identity while a rule
  wrong in some third way could pass both. C2 prints zero
  disagreements -- the classes of order at most 2 are exactly the classes
  the form-symmetry test calls ambiguous, at every field of both signs,
  which pins the composition against a computation sharing no code with
  it. C3 reproduces explore_class_share.py's K6 EXACTLY: -0.1507 on 189
  real fields with the ambiguous mean lower at 0.841, and -0.2160 on 880
  imaginary at 0.777. C4 prints zero. C5's size-matched placebo runs
  0.492 real and 0.465 imaginary -- chance, so K2 below is not the
  small-set artifact it would otherwise be. C7 prints ZERO (field, class)
  pairs with no q, on 3879 real and 23593 imaginary: every class of every
  kept field holds a split prime below 10^4, so the q-conditioned
  readings drop nothing and the bias that control was built for does not
  exist here. IT ALSO RE-ATTRIBUTES THE WINDOW'S POPULATION LOSS: the
  window keeps 222 of 880 imaginary fields and none of the loss is a
  class without a q, so all of it is the density requirement of four
  primes per class above the cut -- which selects SMALL h+, and h+ is
  itself a grading of this deficit. That is a second reason the window
  needs its own baseline and not the full population's.

  **THE DEFICIT IS GRADED BY THE CLASS'S ORDER, MONOTONICALLY AND AT BOTH
  SIGNS -- SO THE SHORT FAMILY IS NOT THE 2-TORSION** (observation; K1's
  first half survives and its second half FIRES, P1 half dead, and the
  half that died is the one that matters). Order 2 is short exactly as
  probe 1 measured it, -0.1507 real and -0.2160 imaginary. But it is not
  special: paired WITHIN a field against the other classes of order above
  2, the classes of order 3 run -0.1126 real on 62 fields and -0.0557
  imaginary on 372, those of order 4 run -0.0957 on 26 and -0.0130 on
  326, and those of order 5 or more run **+0.1118 on 84 and +0.0395 on
  604** -- lower at only 0.214 and 0.344 of fields where order 3 is lower
  at 0.710 and 0.634. So the classes of large order run LONG and the
  small ones short, at both signs, and probe 1's family finding is the
  top of it: "the 2-torsion is short" is true only because 2 is a small
  order. WHAT THE LADDER IDENTIFIES IS ITS SHAPE AND NOT ITS LEVEL, for
  the constraint probe 1 filed: a field's h+ ratios average to 1 by
  construction, so if the small orders are short the large ones MUST be
  long, and no rung's sign is independent of the others.

  **AND THE LADDER IS A LADDER RUNG BY RUNG AT D < 0, AND AT ITS BOTTOM
  RUNG ONLY AT D > 0** (K1d, added at audit, and K1c does not license the
  ladder claim without it). K1c's three readings carry three DIFFERENT
  reference groups on three different field sets -- order 3 is read
  against {4, 5+} and order 4 against {3, 5+} -- so they can be read as
  three comparisons and not as an ordering. Paired within a field against
  the NEXT order up, with nothing else in the field entering either arm,
  every adjacent rung carries the ladder's SIGN, though not every one
  carries a size or a population: -0.1867 real on 946
  fields and -0.4226 imaginary on 935 at order 1 against 2, then -0.0074
  on 60 and -0.1471 on 290 at 2 against 3, -0.1714 on FOUR and -0.0327 on
  94 at 3 against 4, and -0.1005 on 26 and -0.0160 on 326 at 4 against
  5-or-more. THE BOTTOM RUNG IS THE CONFOUNDED ONE AND IT IS THE LARGEST,
  which has to be said before the shape is read: order 1 is the trivial
  class, and at D < 0 the trivial class carries the DERIVED hard zero C4
  verifies -- no split prime below |D|/4 lies in it at all -- so -0.4226
  is an order step plus a mechanism already explained, and the same rung
  at D > 0 (-0.1867) has no such contaminant and is less than half the
  size. Every other rung of this rig excludes the trivial class, so the
  contaminant is confined to this one. THE TWO SIGNS ARE THEN NOT EQUALLY
  SERVED, and the populations say why. At D < 0 all four rungs are
  negative on 94 fields or more, and the STEPS SHRINK MONOTONICALLY as
  the order rises -- 0.423, 0.147, 0.033, 0.016 -- and they still shrink
  monotonically over the three UNCONTAMINATED rungs alone, 0.147, 0.033,
  0.016, which is where the shape actually rests. At D > 0 only the bottom
  rung has both a usable population and a real size; the 2-against-3 step
  is null there (-0.0074, and the lower arm wins at 0.450 of fields,
  below half), and the 3-against-4 step sits on four fields and is worth
  nothing. So the LADDER is an imaginary-side result and what is
  established at both signs is SMALL ORDER against LARGE, which is what
  K1c and K5 measure. The real side's indefinite forms are the same
  population probe 1 found thin for every fine cut.

  **AND THE POOLED ORDER COLUMN IS UNREADABLE, BY THE SAME CONSTRAINT
  THAT FORCED THE PAIRING ABOVE** (K1b, superseded by K1c). Pooled
  the column runs 1.0019, 1.0830, 1.0848 over orders 3, 4, 5+ on the real
  side and 1.0108, 1.0516, 1.0438 imaginary -- which reads as the same
  ladder and cannot be quoted for it, the order-3 pairs coming from
  fields with 3 | h+ and the order->=5 pairs from fields with large h+
  while the within-field ratios sum to a constant. The kill K1 was frozen
  as (a spread above 0.05) would have fired on the real side and not the
  imaginary one off that column; the paired reading fires at both. So a
  kill frozen on a pooled statistic is not a kill criterion, and this
  slate froze one after explore_class_share.py had already paid for it.

  **THE REPRESENTATION FLOOR IS REAL, SIGN-INDEPENDENT, AND NOT THE
  MECHANISM** (P2 survives on K2; P3 and P4 both DIE, on K3 and K4). The
  ambiguous classes' median first split prime exceeds the non-ambiguous
  classes' at 0.873 of real fields and 0.982 of imaginary ones, against a
  size-matched placebo at 0.492 and 0.465 -- so a class of small order
  does start later, at both signs, which is the dial the class MINIMUM
  failed to be. It does not explain the deficit. At matched q the gap
  survives at 0.80 of its size on the real side (-0.1210 against -0.1507)
  and 0.59 imaginary, and over the FINE q bands at 0.75 real (-0.1125)
  and 0.38 imaginary (-0.0828). So the floor carries most of the
  imaginary deficit -- about three fifths of it -- and a quarter of the
real one, which is what a
  floor should do, the derived hard zero being a definite-form fact with
  no indefinite counterpart -- while what is left is the sign-independent
  part. Two mechanisms, and the sign-dependent one is the smaller.

  **AND THE LIVE WINDOW'S APPARENT VERDICT WAS ITS POPULATION** (K3, read
  only after the like-for-like figure was added). Against the bin-0 gap
  over ALL fields the window looks decisive -- -0.0562 against -0.1507
  real and -0.0619 against -0.2160 imaginary, both inside the half P3
  asked for. But the window keeps 159 of 189 real fields and only 222 of
  880 imaginary ones, and on ITS OWN fields the bin-0 gap is -0.1362 and
  -0.0869: the window survives at 0.41 and 0.71, and P3 dies at the
  imaginary sign. The whole of the imaginary side's apparent collapse was
  the 658 fields the window dropped. A window that selects its population
  must be read against that population's own baseline, and the first
  framing of K3 did not print one.

  **THE LADDER IS NOT THE FLOOR IN DISGUISE, AT THE ENDS** (K5, added at
  audit; it is the question K1c and K2 jointly raise). Re-run at matched
  q over the fine bands, the order comparison keeps its two ends at both
  signs -- order 5 or more still runs long at +0.1005 real on 50 fields
  and +0.0306 imaginary on 568, and orders 3 and 4 still run short at
  -0.0331 and -0.1656 real, -0.0340 and -0.0255 imaginary. WHAT THIS
  READING CANNOT SAY IS ANYTHING ABOUT THE RUNG ORDER, and the reason is
  K1c's: these three numbers carry three different reference groups on
  three different field sets, so 3 against 4 is not a comparison here
  however the two happen to sit. The rung-by-rung instrument is K1d, and
  its 3-against-4 cell is already four fields wide on the real side
  before any q condition, so matching q cannot recover it. What matched q
  therefore establishes is SMALL ORDER against LARGE, at both signs, on
  cells of 33 to 568 fields -- and the real side's are thin enough that
  only the imaginary side's columns carry weight on their own.

WHAT IS NOT CONTROLLED, stated rather than left for a reader to find. The
live window and the matched-q pairing remove the floor by opposite
operations and each keeps a bias the other does not. The window drops
every prime below Q, which is MORE of a low-q class's primes than of a
high-q class's -- and the ambiguous classes are the high-q ones under P2,
so the window flatters them: a deficit that SURVIVES the window is strong
evidence and a deficit that VANISHES there is consistent both with the
floor explaining it and with the window's own bias. The matched-q pairing
has no such bias but conditions on a quantity measured from the same
primes it then counts, so its cells are not independent draws. Neither is
the other's control; what they jointly rule out is a floor effect that
survives both removals, and what they cannot separate is a floor effect
from a q-graded one. AND THE ORDER LADDER'S LEVEL IS NOT IDENTIFIED at
all, for the constant-sum reason K1c states: the rungs are measured
against each other and a common baseline would have to come from outside
the field, which is exactly the pooling this rig refuses.

RUN RECORD: wall 4.4 s, 1217 imaginary and 1216 real fundamental
discriminants to |D| <= 4000 over the odd split p <= 10^4, fields with
fewer than 20 split primes dropped -- probe 1's population unchanged, per
derivation (6). Pure Python, well inside the analysis ceiling. The
composition is the new cost and it is small: derivation (2)'s cyclic walk
hands back the order of every element it passes, so a field with a cyclic
group costs one walk, and the wall is within 0.3 s of probe 1's on the
same population. K1c, K3's like-for-like baseline, K4's fine bands, C5
and K5 were all added during the audit and none costs a second sweep.
"""

import os
import sys
import time
from collections import defaultdict
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_principal_share import (          # noqa: E402
    primes_upto, kronecker, fundamental_discriminants,
    reduce_form, class_data_real, reduce_definite, class_number_imag,
    form_at,
)
from explore_class_share import (              # noqa: E402
    classes_imag, classes_real, mean,
)

DBOUND = 4000
PCAP = 10 ** 4
BIN0 = 1000               # the bottom bin, where the deficit lives
MIN_SPLIT = 20            # a field with fewer split primes carries no share
Q_BANDS = ((2, 10), (11, 50), (51, 200), (201, PCAP))
Q_LABELS = ("q<=10", "q 11-50", "q 51-200", "q>200")
FINE_BANDS = ((2, 5), (6, 10), (11, 20), (21, 40), (41, 80), (81, 160),
              (161, 320), (321, 640), (641, PCAP))
ORDER_LABELS = ((3, "ord 3"), (4, "ord 4"), (5, "ord >=5"))
WINDOW_MIN = 4            # primes per class the live window must hold


def band_of_q(q, bands=Q_BANDS):
    for i, (lo, hi) in enumerate(bands):
        if lo <= q <= hi:
            return i
    return None


# ----------------------------------------------------------- composition

def xgcd(a, b):
    old_r, r, old_s, s, old_t, t = a, b, 1, 0, 0, 1
    while r:
        k = old_r // r
        old_r, r = r, old_r - k * r
        old_s, s = s, old_s - k * s
        old_t, t = t, old_t - k * t
    return old_r, old_s, old_t


def coprime_lead(f, n, D, tries=16):
    """A form equivalent to f whose leading coefficient is coprime to n.

    f(x, z) at coprime (x, z) is the leading coefficient of an equivalent
    form -- derivation (1). The pairs are tried cheapest-first, so a form
    already coprime to n costs nothing.
    """
    a, b, c = f
    if gcd(abs(a), abs(n)) == 1:
        return f
    for s in range(1, tries):
        for x in range(-s, s + 1):
            for z in {s - abs(x), abs(x) - s}:
                if (x, z) == (0, 0) or gcd(abs(x), abs(z)) != 1:
                    continue
                a2 = a * x * x + b * x * z + c * z * z
                if a2 == 0 or gcd(abs(a2), abs(n)) != 1:
                    continue
                g, u, v = xgcd(x, z)
                if g != 1:
                    continue
                y, w = -v, u
                b2 = 2 * (a * x * y + c * z * w) + b * (x * w + y * z)
                return (a2, b2, (b2 * b2 - D) // (4 * a2))
    raise RuntimeError("no coprime representative found")


def compose_forms(f1, f2, D, bad):
    """Dirichlet composition through a coprime representative."""
    a1, b1, c1 = f1
    a2, b2, c2 = coprime_lead(f2, f1[0], D)
    m = abs(a2)
    if m == 1:
        k = 0
    else:
        g, inv, _ = xgcd(a1 % m, m)
        k = (inv * ((b2 - b1) // 2)) % m
    A = a1 * a2
    B = b1 + 2 * a1 * k
    if (B * B - D) % (4 * A):
        bad[0] += 1
        return None
    C = (B * B - D) // (4 * A)
    if B * B - 4 * A * C != D:
        bad[0] += 1
        return None
    return (A, B, C)


def make_composer(D, sign, recs, member, rt, bad):
    """key x key -> key, for one field."""
    def comp(k1, k2):
        f = compose_forms(k1, k2, D, bad)
        if f is None:
            return None
        if sign < 0:
            key = reduce_definite(f, D)
        else:
            key = member.get(reduce_form(f, D, rt))
        if key not in recs:
            bad[1] += 1
            return None
        return key
    return comp


def class_orders(recs, triv, comp, hplus, bad):
    """The order of every class, one cyclic walk per unlearned class."""
    orders = {triv: 1}
    for key in recs:
        if key in orders:
            continue
        seq, cur = [triv], key
        while cur != triv:
            seq.append(cur)
            cur = comp(cur, key)
            if cur is None or len(seq) > hplus + 1:
                bad[2] += 1
                return None
        n = len(seq)
        if hplus % n:
            bad[3] += 1
            return None
        for j, el in enumerate(seq):
            if j:
                orders.setdefault(el, n // gcd(j, n))
    return orders


# ------------------------------------------------------------- the sweep

def sweep(sign, plist):
    """Per field: class records, orders, per-class bin-0 and window counts."""
    rows, bad, law_bad = [], [0, 0, 0, 0], [0, 0]
    id_bad = c2_bad = c4_bad = 0
    for D in fundamental_discriminants(1, DBOUND, sign):
        if sign < 0:
            recs, triv = classes_imag(D)
            member, rt = None, None
            hplus = class_number_imag(D)
        else:
            recs, member, triv, rt = classes_real(D)
            _, hplus, _ = class_data_real(D, rt)
        if len(recs) != hplus:
            continue
        hits = []
        for p in plist:
            if p == 2 or D % p == 0 or kronecker(D, p) != 1:
                continue
            b = form_at(D, p)
            num = b * b - D
            if sign < 0:
                key = reduce_definite((p, b, num // (4 * p)), D)
            else:
                key = member[reduce_form((p, b, num // (4 * p)), D, rt)]
            hits.append((p, key))
        if len(hits) < MIN_SPLIT:
            continue
        comp = make_composer(D, sign, recs, member, rt, bad)
        ok = comp(triv, triv) == triv
        for key in recs:
            if comp(triv, key) != key or comp(key, triv) != key:
                ok = False
                break
        if not ok:
            id_bad += 1
            continue
        probe = sorted(recs)[:3]
        for u in probe:
            for v in probe:
                if comp(u, v) != comp(v, u):
                    law_bad[0] += 1
                for x in probe:
                    if comp(comp(u, v), x) != comp(u, comp(v, x)):
                        law_bad[1] += 1
        orders = class_orders(recs, triv, comp, hplus, bad)
        if orders is None:
            continue
        if (sum(1 for k in recs if orders[k] <= 2)
                != sum(1 for r in recs.values() if r[2])):
            c2_bad += 1
            continue
        q = {}
        n0 = defaultdict(int)
        tot0 = 0
        for p, key in hits:
            if key not in q:
                q[key] = p
            if p < BIN0:
                n0[key] += 1
                tot0 += 1
        if sign < 0 and q.get(triv, PCAP + 1) * 4 < -D:
            c4_bad += 1
        rows.append((D, hplus, recs, orders, dict(n0), tot0, q, hits))
    return rows, bad, id_bad, c2_bad, c4_bad, law_bad


def ratio(cnt, total, hplus):
    return cnt * hplus / total if total else float("nan")


# ---------------------------------------------------------- the readings

def paired(rows, group_a, group_b, window=False, matched=False,
           qbands=None, window_pop=False):
    """Mean within-field gap between two class groups, bin 0 or window.

    group_a/group_b take (key, rec, order) and return a bool. A field
    contributes one number: the mean ratio over group A minus the mean
    over group B, both measured on the same primes of that field.
    """
    diffs = []
    for D, hplus, recs, orders, n0, tot0, q, hits in rows:
        if hplus == 1:
            continue
        if window or window_pop:
            if len(q) != hplus:
                continue
            lo = max(q.values())
            wcnt = defaultdict(int)
            wtot = 0
            for p, key in hits:
                if lo < p < BIN0:
                    wcnt[key] += 1
                    wtot += 1
            if wtot < WINDOW_MIN * hplus:
                continue
        if window:
            cnt, tot = wcnt, wtot
        else:
            cnt, tot = n0, tot0
            if tot == 0:
                continue
        ga, gb = [], []
        for key, rec in recs.items():
            o = orders[key]
            r = ratio(cnt.get(key, 0), tot, hplus)
            if group_a(key, rec, o):
                ga.append((key, r))
            elif group_b(key, rec, o):
                gb.append((key, r))
        if not ga or not gb:
            continue
        if matched:
            ba = defaultdict(list)
            bb = defaultdict(list)
            bands = qbands or Q_BANDS
            for key, r in ga:
                if key in q:
                    ba[band_of_q(q[key], bands)].append(r)
            for key, r in gb:
                if key in q:
                    bb[band_of_q(q[key], bands)].append(r)
            per = [mean(ba[b]) - mean(bb[b]) for b in ba if b in bb]
            if not per:
                continue
            diffs.append(mean(per))
        else:
            diffs.append(mean([r for _, r in ga]) - mean([r for _, r in gb]))
    below = sum(1 for d in diffs if d < 0)
    return mean(diffs), len(diffs), (below / len(diffs) if diffs else 0.0)


def order_column(rows):
    """K1 second half: bin-0 ratio by class order, NON-ambiguous classes."""
    acc = defaultdict(list)
    for D, hplus, recs, orders, n0, tot0, q, hits in rows:
        if hplus == 1 or tot0 == 0:
            continue
        for key, rec in recs.items():
            o = orders[key]
            if o <= 2:
                continue
            tag = o if o < 5 else 5
            acc[tag].append(ratio(n0.get(key, 0), tot0, hplus))
    return {t: (mean(v), len(v)) for t, v in sorted(acc.items())}


def _med(xs):
    xs = sorted(xs)
    n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


def q_medians(rows, placebo=False):
    """K2: fields where the ambiguous median q exceeds the non-ambiguous.

    C5, the SIZE-MATCHED NULL (added after the smoke run and flagged for
    it). The ambiguous classes are FEW -- 2^(t-1) - 1 of them non-trivial
    -- and the non-ambiguous many, so the reading compares a small set's
    median against a large set's. Under `placebo` the small set is drawn
    from the NON-ambiguous classes instead, size-matched and compared
    against the median of all of them, which is the same comparison with
    ambiguity removed and nothing else changed. The draw is by a fixed
    rule (the classes sorted by key, taken at a stride set by the field's
    own D) rather than by a generator, so the control reproduces.
    """
    fields = higher = 0
    for D, hplus, recs, orders, n0, tot0, q, hits in rows:
        if hplus == 1:
            continue
        amb = [q[k] for k, r in recs.items()
               if orders[k] <= 2 and not r[0] and k in q]
        non = [q[k] for k, r in recs.items() if orders[k] > 2 and k in q]
        if not amb or not non:
            continue
        if placebo:
            if len(non) <= len(amb):
                continue
            pool = [q[k] for k in sorted(k for k, r in recs.items()
                                         if orders[k] > 2 and k in q)]
            start = abs(D) % len(pool)
            amb = [pool[(start + i) % len(pool)] for i in range(len(amb))]
        fields += 1
        if _med(amb) > _med(non):
            higher += 1
    return fields, higher


def main():
    t0 = time.time()
    plist = primes_upto(PCAP)
    print("population: |D| <= %d both signs, odd split p <= %d, bottom bin"
          " p < %d, min split %d" % (DBOUND, PCAP, BIN0, MIN_SPLIT))
    out = {}
    for sign, name in ((-1, "imaginary"), (+1, "real")):
        rows, bad, idb, c2b, c4b, lawb = sweep(sign, plist)
        out[sign] = rows
        print("\n%s: %d fields kept" % (name, len(rows)))
        print("  C1 composition: disc/integrality %d | key not in inventory"
              " %d | walk overran %d | order does not divide h+ %d |"
              " identity %d" % (bad[0], bad[1], bad[2], bad[3], idb))
        print("  C6 the law itself, over every field's first three"
              " classes: non-commuting pairs %d | non-associative"
              " triples %d" % (lawb[0], lawb[1]))
        print("  C2 order<=2 against the form-symmetry ambiguity test:"
              " disagreements %d" % c2b)
        print("  C4 trivial q below |D|/4: %s"
              % (c4b if sign < 0 else "n/a"))

    print("\n--- C3: the incumbent's own statistic. Within-field paired"
          "\n    ambiguous vs non-ambiguous, bin 0, non-trivial classes."
          "\n    explore_class_share.py K6 printed -0.1507 on 189 real"
          "\n    fields and -0.2160 on 880 imaginary.")
    famb = lambda k, r, o: r[2] and not r[0]           # noqa: E731
    fnon = lambda k, r, o: not r[2]                    # noqa: E731
    for sign, name in ((+1, "real"), (-1, "imag")):
        g, n, frac = paired(out[sign], famb, fnon)
        print("  %-5s %+.4f on %d fields, ambiguous lower at %.3f"
              % (name, g, n, frac))

    print("\n--- K1a: is order 2 special? Within-field paired, bin 0,"
          "\n    NON-TRIVIAL order-2 classes against order > 2 -- the same"
          "\n    split as C3 but cut by the COMPOSED order, which C2 says"
          "\n    is the same partition and this prints as the same number.")
    amb = lambda k, r, o: o == 2 and not r[0]          # noqa: E731
    non = lambda k, r, o: o > 2                        # noqa: E731
    for sign, name in ((+1, "real"), (-1, "imag")):
        g, n, frac = paired(out[sign], amb, non)
        print("  %-5s %+.4f on %d fields, order-2 lower at %.3f"
              % (name, g, n, frac))

    print("\n--- K1b: does shortness fall off with the order? Bin-0 ratio"
          "\n    by order over classes of order above 2, pooled.")
    print("%-9s | %-22s | %-22s" % ("order", "real (pairs)", "imag (pairs)"))
    cr, ci = order_column(out[+1]), order_column(out[-1])
    for tag, lab in ORDER_LABELS:
        rv = "%.4f (%d)" % cr[tag] if tag in cr else "--"
        iv = "%.4f (%d)" % ci[tag] if tag in ci else "--"
        print("%-9s | %-22s | %-22s" % (lab, rv, iv))

    print("\n--- K1c (added at audit; it SUPERSEDES K1b, which is the"
          "\n    pooled reading probe 1 already filed as unreadable). The"
          "\n    order-3 pairs above come from fields with 3 | h+ and the"
          "\n    order->=5 pairs from fields with large h+, and within any"
          "\n    field the h+ ratios sum to a constant -- so the column is"
          "\n    a comparison across DIFFERENT fields. Paired WITHIN a"
          "\n    field, each order against the other classes of order"
          "\n    above 2 of that same field:")
    for lo, hi, lab in ((3, 3, "ord 3"), (4, 4, "ord 4"), (5, 10 ** 9,
                                                           "ord >=5")):
        for sign, name in ((+1, "real"), (-1, "imag")):
            ga = (lambda k, r, o, lo=lo, hi=hi: lo <= o <= hi)
            gb = (lambda k, r, o, lo=lo, hi=hi: o > 2 and not lo <= o <= hi)
            g, n, frac = paired(out[sign], ga, gb)
            print("  %-8s %-5s %+.4f on %4d fields, lower at %.3f"
                  % (lab, name, g, n, frac))

    print("\n--- K1d (added at audit; the ladder claim needs it and K1c"
          "\n    does not license it). K1c's three readings have three"
          "\n    DIFFERENT reference groups -- order 3 is read against"
          "\n    {4, 5+} and order 4 against {3, 5+} -- on different"
          "\n    field sets, so they cannot be ordered against each"
          "\n    other. A ladder is a claim about ADJACENT rungs and this"
          "\n    is the only reading that measures one: each order paired"
          "\n    within a field against the NEXT order up, and nothing"
          "\n    else in the field entering either arm.")
    for a, b, lab in ((1, 2, "1 vs 2"), (2, 3, "2 vs 3"), (3, 4, "3 vs 4"),
                      (4, 5, "4 vs 5+")):
        for sign, name in ((+1, "real"), (-1, "imag")):
            ga = (lambda k, r, o, a=a: o == a)
            gb = (lambda k, r, o, b=b: o == b if b < 5 else o >= 5)
            g, n, frac = paired(out[sign], ga, gb)
            print("  ord %-7s %-5s %+.4f on %4d fields, lower at %.3f"
                  % (lab, name, g, n, frac))

    print("\n--- C7 (added at audit): the classes with NO split prime"
          "\n    below the cap have no q, and every q-conditioned reading"
          "\n    below drops them from both arms. They are the shortest"
          "\n    classes there are and the likeliest to be small-order,"
          "\n    so the drop flatters the arm under test and every gap"
          "\n    below is a floor on the true one. Printed as the share"
          "\n    of (field, class) pairs lost, over fields with h+ > 1.")
    for sign, name in ((+1, "real"), (-1, "imag")):
        tot = miss = ambmiss = ambtot = 0
        for D, hplus, recs, orders, n0, tot0, q, hits in out[sign]:
            if hplus == 1:
                continue
            for key in recs:
                tot += 1
                if orders[key] <= 2:
                    ambtot += 1
                if key not in q:
                    miss += 1
                    if orders[key] <= 2:
                        ambmiss += 1
        print("  %-5s %d of %d pairs have no q (%.3f); of the order<=2"
              " pairs, %d of %d (%.3f)"
              % (name, miss, tot, miss / tot if tot else 0,
                 ambmiss, ambtot, ambmiss / ambtot if ambtot else 0))

    print("\n--- K2: the representation floor. Fields where the ambiguous"
          "\n    classes' median q exceeds the non-ambiguous classes'.")
    for sign, name in ((+1, "real"), (-1, "imag")):
        f, h = q_medians(out[sign])
        fp, hp = q_medians(out[sign], placebo=True)
        print("  %-5s %4d of %4d fields (%.3f)  |  C5 size-matched"
              " placebo, non-ambiguous only: %4d of %4d (%.3f)"
              % (name, h, f, h / f if f else 0,
                 hp, fp, hp / fp if fp else 0))

    print("\n--- K3: the LIVE WINDOW. Same paired comparison over the"
          "\n    primes above the field's largest q, where every class is"
          "\n    live and none sits under its own floor.")
    print("    Printed beside the BIN-0 gap over the same fields (added"
          "\n    at audit): the window drops most of the population, so"
          "\n    the bin-0 figure the kill is read against must be the"
          "\n    one on THIS population and not the one on all fields.")
    for sign, name in ((+1, "real"), (-1, "imag")):
        g, n, frac = paired(out[sign], amb, non, window=True)
        g0, n0_, f0 = paired(out[sign], amb, non, window_pop=True)
        print("  %-5s window %+.4f on %d fields, ambiguous lower at %.3f"
              "\n        bin 0, same fields %+.4f on %d, lower at %.3f"
              % (name, g, n, frac, g0, n0_, f0))

    print("\n--- K4: the MATCHED-q pairing. Same comparison, ambiguous"
          "\n    against non-ambiguous of the same field AND the same q"
          "\n    band, which removes the floor without removing a prime.")
    print("    A wide band leaves residual q inside it, and the ambiguous"
          "\n    classes sit at the top of a band under K2 -- so the FINE"
          "\n    bands are printed beside the coarse ones (added at audit)"
          "\n    and a gap that shrinks across them is a residual floor.")
    for sign, name in ((+1, "real"), (-1, "imag")):
        g, n, frac = paired(out[sign], amb, non, matched=True)
        gf, nf, ff = paired(out[sign], amb, non, matched=True,
                            qbands=FINE_BANDS)
        print("  %-5s coarse %+.4f on %d fields, ambiguous lower at %.3f"
              "\n        fine   %+.4f on %d fields, ambiguous lower at %.3f"
              % (name, g, n, frac, gf, nf, ff))
    print("  q bands, coarse: %s" % ", ".join(Q_LABELS))
    print("  q bands, fine:   %s"
          % ", ".join("%d-%d" % b for b in FINE_BANDS))

    print("\n--- K5 (added at audit, and it is the question K1c and K4"
          "\n    jointly raise rather than one either answers): K1c grades"
          "\n    by order and K2 says order 2 carries a later first prime,"
          "\n    so the ORDER LADDER may be the FLOOR ladder wearing the"
          "\n    group's name. The same within-field order comparison, at"
          "\n    matched q over the fine bands.")
    for lo, hi, lab in ((3, 3, "ord 3"), (4, 4, "ord 4"), (5, 10 ** 9,
                                                           "ord >=5")):
        for sign, name in ((+1, "real"), (-1, "imag")):
            ga = (lambda k, r, o, lo=lo, hi=hi: lo <= o <= hi)
            gb = (lambda k, r, o, lo=lo, hi=hi: o > 2 and not lo <= o <= hi)
            g, n, frac = paired(out[sign], ga, gb, matched=True,
                                qbands=FINE_BANDS)
            print("  %-8s %-5s %+.4f on %4d fields, lower at %.3f"
                  % (lab, name, g, n, frac))

    print("\nwall %.1f s" % (time.time() - t0))
    return out


if __name__ == "__main__":
    main()
