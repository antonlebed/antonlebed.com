"""explore_fate_image_ff.py -- THE FATE IMAGE OFF Z: the same five demand
laws over F_2[x] (sibling of explore_fate_image.py, which draws the image
over Z, and of explore_function_field_lock.py, which runs cold greedy
dynamics over this same ring).

THE QUESTION. A demand law's FATE IMAGE Im(L, s) is the set of limits its
whole FREE policy class can reach from a seed -- the object the three fates
(breadth, depth, mortality) turned out to be the corners of. That image has
only ever been drawn over Z. This file draws it over F_2[x] and asks what
changed. Two answers were possible at the freeze and both were worth
having: the polynomial image is BIGGER (the ring buys reachable limits Z
forbids), or the image is the same body and what moves is where the GREEDY
policy sits inside it. The second is the more interesting, because the
corners are what the three fates are a slice of, and a greedy that changes
corners changes which fates a bare growth rule realises.

THE SETTING. A state is a monic polynomial N in F_2[x], the void is N = 1,
and a move multiplies: N -> N*m with m monic of degree >= 1 -- the transfer
of Z's "m >= 2", since |m| = 2^deg m >= 2. lambda(N) is the exponent of
(F_2[x]/N)^x; for a prime power with deg g = d,

    lambda(g^a) = (2^d - 1) * 2^ceil(log2 a)

(the equal-characteristic half of the local module law: the residue field
contributes the cyclic 2^d - 1 and Frobenius flattens the 1-units, so the
depth clock is LOGARITHMIC where Z's is linear). omega counts distinct
irreducible factors. W(L) is the largest monic polynomial whose lambda
divides L, and V(N) = W(lambda(N))/N is the transparency headroom. A LIMIT
is a supernatural polynomial: an exponent function on the monic
irreducibles, with values in {0, 1, 2, ...} u {oo}.

THE FIVE DEMAND LAWS transfer verbatim -- each is a condition on the ring
F_2[x]/N and none mentions the integers:
  INDEPENDENCE    -- m admissible iff gcd(m, N) = 1 (the extension splits).
  SEMISIMPLICITY  -- m admissible iff N*m is squarefree.
  NEW-IDEMPOTENTS -- m admissible iff omega(N*m) > omega(N).
  TRANSPARENCY    -- m admissible iff lambda(N*m) = lambda(N).
  DYNAMICS        -- m admissible iff lambda(N*m) > lambda(N).

TRANSPLANT FLAGS, fixed at the freeze. Every intuition below is imported
from a neighbouring parameter value -- the ring -- and each is marked
rather than trusted:
 1. "LEAST m" is a TOTAL order over Z and a DEGREE order here. Minimal-degree
    admissible moves are generically SEVERAL (2^d monic polynomials share
    each degree), so greed over Z is a FUNCTION of the state and greed here
    is a policy CLASS. Every filed sentence about "the greedy trajectory"
    over F_2[x] is an import carrying Z's determinacy with it.
 2. Over Z a re-push of a seated odd prime ALWAYS raises lambda, by the
    factor p. Here a re-push raises lambda only at the ceil(log2)
    FRONTIERS, so a depth construction must JUMP frontiers, never step.
 3. Over Z the wall W(L) is a Bernoulli denominator (an image-of-J order).
    Nothing about its value or its finiteness may be carried across; W is
    recomputed here from its definition and checked against brute search.
 4. BREADTH means EVERY prime seated (explore_growth_laws.py), not
    "infinitely many". Infinite support is NOT breadth. The filed reading
    that depth and breadth CO-OCCUR along this ring's greedy trajectory
    (explore_function_field_lock.py finding 5) is an import to be TESTED
    here, not assumed.

THE PREDICTIONS, fixed before any engine code was written, each naming what
the rig PRINTS. What they mean is weighed after the run.

Q1 THE WALL'S FORM. lambda(g^a) | L iff (2^d - 1) | L and a <= 2^v2(L), so
   with D(L) = {d : (2^d - 1) | L} (finite, and divisor-closed since
   e | d implies (2^e - 1) | (2^d - 1)) and A = 2^v2(L):

       W(L) = prod_{d in D(L)} (prod_{deg P = d} P)^A

   and every N with lambda(N) | L divides W(L). Predict brute search agrees
   at every L in the battery whose wall fits under the search cap.
   KILL: one disagreement, or one N with lambda(N) | L not dividing W(L).

Q2 THE SPECIAL FORM. At L = (2^n - 1)*2^v the divisor-closed set D(L) is
   exactly the divisors of n, and the product of all irreducibles of degree
   dividing n is x^(2^n) + x. Predict W((2^n - 1)*2^v) = (x^(2^n) + x)^(2^v)
   -- the wall ring is the product of every finite field whose degree
   divides n, one copy per irreducible.
   KILL: the two polynomials differ at any n, v in the battery.

Q3 TRANSPARENCY'S IMAGE is the single finite point { W(lambda(s)) }.
   KILL: a maximal transparent run ending anywhere else.

Q4 THE OTHER FOUR IMAGES have the SAME SHAPE as over Z, seed s written
   multiplicatively over the irreducibles:
     semisimplicity   s * prod_{P in S} P, S infinite and disjoint from
                      supp(s), from a SQUAREFREE seed; from any other seed
                      nothing is admissible and the image is { s }
     independence     s * prod_{P in S} P^{e_P}, S infinite and disjoint,
                      1 <= e_P < oo, the seed's own exponents FROZEN
     new-idempotents  every X with s | X and supp(X) infinite
     dynamics         every X with s | X and X infinite -- MAXIMAL
   and the last four nest strictly in that order with the transparency
   point outside the chain.
   KILL: a reachable limit violating a clause, a described member the
   construction cannot reach, or a chain inclusion that fails.

Q5 THE TWO COORDINATES. Read DEPTH-AVAILABLE (some member has an infinite
   exponent) and FINITE-SUPPORT-AVAILABLE (some member has finite support)
   off the images and predict they sit exactly where they sit over Z, at
   all five laws.
   KILL: any mismatch against the filed table.

Q6 THE GREEDY IMAGE, the object flag 1 forces into existence: Im_greedy(L, s)
   = the set of limits over the MINIMAL-DEGREE policy class. Over Z it is a
   singleton at every law, because the least admissible m is unique. Predict
   that over F_2[x] greedy DYNAMICS from the void has a plural minimal-degree
   set at its very first move (x^2, (x+1)^2 and x^2+x+1 all cost 2 there) and
   that distinct tie-break rules reach distinct limits, while greedy
   INDEPENDENCE stays a singleton -- every tie-break seats every irreducible.
   KILL: the void's minimal set is a singleton at dynamics, or two
   independence rules seat different sets.

Q7 WHERE THE GREEDY POINT SITS. Predict the greedy dynamics limit holds
   DEPTH and NOT BREADTH: at most one irreducible per degree is ever seated,
   so the support misses infinitely many irreducibles and the point is
   INTERIOR in the support coordinate rather than at its corner.
   KILL: a trajectory seating two irreducibles of one degree.

THE DESIGN, in seven sections after the control.

S1 POSITIVE CONTROL, run before any verdict is read; the run aborts if it
   fails. Seven things this file leans on and did not derive here must come
   back: the lambda law against the exponent of the unit group by direct
   enumeration; lambda's MONOTONICITY under divisibility, which is the
   hypothesis of the wall's lattice argument; the frontier INDEX CONVENTION
   v2(lambda(g^a)) = ceil(log2 a) read off the engine rather than trusted,
   since an off-by-one there corrupts every depth construction below; the
   irreducible counts against the Moebius formula, which the density
   verdict of S7 leans on; the door-menu claim that a minimal admissible
   dynamics move is a PRIME POWER, brute-checked against a full scan over
   every monic move at every state of a battery; the FRESH-DEGREE
   INVARIANT the menu rests on when it takes the least member of the
   frontier class without checking whether it is seated (a seated member
   would have put that degree's odd factor into lambda and the degree
   would not be fresh); and the filed greedy runs this file contrasts free
   policies against.

S2 THE WALL, Q1 and Q2: the closed form against brute search over every
   monic polynomial under the cap, the lattice claim checked directly, and
   the special form as a polynomial identity.

S3 THE ADMISSIBILITY ATLAS -- the mechanical basis of the two coordinates,
   measured before either is claimed. Over a battery of states and every
   monic move up to a degree cap, classify each admissible move by two
   bits: does it SEAT an irreducible the state lacked, does it RAISE the
   exponent of one it had. Where a demand makes a column tautological the
   print says so, so a structural zero is never read as evidence.

S4 THE REACH HALF -- run each law's construction against a battery of
   targets, in-image and out. For an in-image target every move must be
   admissible, the state must divide the target at every step, and the
   least unseated support irreducible must strictly RISE, so that a
   construction silently skipping a member fails instead of printing a
   clean prefix of the wrong limit. For an out-of-image target the rig
   scans every move under a cap and prints the mechanical reason.

S5 THE CLOSURE HALF -- for each law the invariant that bounds its image,
   checked over a state x move battery: frozen seed exponents and
   frozen-once-seated (independence), squarefreeness (semisimplicity),
   seats-a-new-irreducible (new-idempotents), never-empty (the three live
   laws, so no finite limit), and the finite reachable set (transparency,
   by exhaustion from several seeds).

S6 THE COORDINATE TABLE AND THE CHAIN -- the two coordinates as S3-S5
   measured them against the filed Z table, then the four inclusions and
   their strictness witnesses.

S7 THE GREEDY IMAGE, Q6 and Q7. The minimal-degree admissible SET at each
   state, its multiplicity, four tie-break rules run from several seeds,
   the seated support by degree against the irreducible count of that
   degree, and the domination test that decides Q7: whenever a degree class
   is already occupied, is the sibling's opening door ever minimal.

THE FINDINGS.

F1 THE FIVE IMAGES ARE THE SAME FIVE SHAPES, AND THE SAME CHAIN UNDER THE
   SAME SCOPE (rule; closure halves exhaustive over the battery, reach
   halves constructed and argued). The scope is one the filed Z statement
   leaves implicit and S6 makes explicit here: the bottom link holds at a
   SQUAREFREE seed only, because from any other seed semisimplicity admits
   nothing at all and its image is the single finite point {s}, which no
   infinite-support image contains -- so the law leaves the chain rather
   than sitting at its bottom. Every clause of the Z shapes survives the move to F_2[x], and
   the two coordinates sit exactly where the filed Z table puts them --
   0 mismatches over the five laws, each bit read off an S3-S5 witness. The
   mechanisms transfer because none of them was ever about the integers: a
   coprime move cannot carry a seated irreducible (0 violations over 2540
   state x move pairs), a squarefree state admits no second copy, a raised
   omega needs an unseated irreducible, and no live law's run halts. THE
   IMAGE BODY IS A PROPERTY OF THE DEMAND, NOT OF THE RING -- the answer to
   the question this file opened with, and the one that makes the fates'
   corner reading portable rather than a fact about Z. That last sentence is
   a SYNTHESIS over two rings and not a rule: what is at rule tier is the
   five shapes here, one ring at a time.

F2 THE MORTALITY CORNER IS GENERIC AND ITS VALUE IS NOT (rule, proved;
   brute-verified at 44 values of L, exhaustive over every monic polynomial
   of degree <= 10, with every state whose lambda divides L confirmed to
   divide W(L) at all 44). The wall has a closed form here:

       W(L) = prod_{d in D(L)} (prod_{deg P = d} P)^(2^v2(L)),
       D(L) = { d : (2^d - 1) | L }, divisor-closed, finite

   and at L = (2^n - 1)*2^v it collapses to W = (x^(2^n) + x)^(2^v). At
   v = 0 -- L = 2^n - 1, the clock a single field's unit group carries --
   the wall RING is then the product of every finite field whose degree
   divides n, one factor per irreducible; at v > 0 it is that polynomial's
   2^v-th power and the quotient is no longer a product of fields, since
   the exponent is exactly what the 2-part of the clock buys. Over Z the
   same corner sits at
   denominator(B_L / 2L) -- the image-of-J orders 24, 240, 504. So the
   DEPTH of the Z wall is a fact about Z and not about mortality: the
   corner is generic, elementary here and Bernoulli there, and the wall is
   the only one of the five images whose value moves at all.

F3 GREED STOPS NAMING A POINT (rule; the tie exhibited, the divergence's
   permanence proved). Over Z "least m" is a total order, so a greedy
   policy is a FUNCTION of the state and the greedy image -- the set of
   limits over the minimal-move policy class -- is a single point at every
   law, by definition and not by measurement. Here "least" orders by DEGREE
   and the minimal set is generically plural: the void's own first dynamics
   move is a 3-way tie at cost 2 (x^2 and (x+1)^2 clocked, x^2+x+1 fresh).
   Four tie-break rules reach 2 distinct limits from the void and 3 from
   two of the seeded starts. The divergence is PERMANENT rather than a
   prefix artifact: 'lex' and 'sib' first part at degree 3, one seating
   x^3+x+1 and the other x^3+x^2+1, and F4 forbids either from ever seating
   the other's. But plurality belongs to the (law, ring) PAIR and not to the
   ring: greedy INDEPENDENCE under the same tie-breaks seats exactly the
   same 8 irreducibles of degree <= 4 under every rule -- ties reorder the
   picks and the limit is the polynomial primorial regardless. Determinism
   was already filed as archimedean for the RULE (a tie-break is required
   here and not over Q); it is archimedean for the LIMIT too, at one law
   and not at the other.

F3b AND THE GREEDY DYNAMICS IMAGE IS A CONTINUUM (rule, proved; the
   lockstep half
   measured over 26 moves; the law scope is the point of F3 and stays
   attached here -- greedy INDEPENDENCE is still one limit). One lemma
   sizes it: every irreducible of a
   degree contributes the SAME factor 2^d - 1 to lambda, so a trajectory's
   whole cost structure depends on the DEGREES it opens and not on WHICH
   member of each degree it opens -- two policies differing only in that
   choice run in LOCKSTEP, identical in (cost, kind, degree) at all 26
   moves while picking different irreducibles at 19 of them. Every fresh
   opening is therefore a free choice among all N_2(d) members of its
   class, and the starvation makes each choice permanent, so the image
   holds one limit per CHOICE FUNCTION: the 20 openings in 26 moves
   already give a 49-digit number of distinct prefixes, the frontier
   degrees keep rising, and N_2(d) >= 2 from degree 3 on. THE GREEDY IMAGE
   HAS THE CARDINALITY OF THE CONTINUUM, where over Z the greedy image is
   a single point at every law.
   It is NOT an automorphism orbit, which is the natural guess and is
   refuted by the same data: Aut(F_2[x]) = {x, x+1} has order 2 while the
   image is uncountable, and concretely the 'sib' limit is neither the
   'lex' limit nor its automorphic image. Ties here are COST COLLAPSE --
   many places sharing a norm -- and only part of that collapse is
   symmetry, which is what makes the number-field side, where every filed
   tie IS a Galois orbit, the sharp comparison.

F4 THE SIBLING STARVATION (rule, proved; tie-break- and seed-independent,
   exercised 190-259 times per run over the census). Once one irreducible
   of degree d is seated, every sibling of that degree can enter only
   through the CLOCKED door at cost d*(2^c + 1), while the seated one's own
   DEEPENING door costs d*(2^c + 1 - e) with e >= 1 -- strictly cheaper at
   every clock, so a sibling is never in the minimal-cost set. Greedy
   dynamics therefore seats AT MOST ONE irreducible per degree from any
   polynomial seed under any tie-break: the void run at 26 moves has seated
   1 of the 2 irreducibles of degree 1 and 1 of the 99858 of degree 21. The
   support has density ZERO among the irreducibles and infinitely many are
   never seated. This closes the route the filed sibling shadow left open,
   which blocked a sibling's FRESH door and not its clocked one.

F5 SO THE GREEDY POINT IS INTERIOR, AND THE FILED CO-OCCURRENCE IS AN
   OVERCLAIM -- the correction is this file's headline. The melt is filed as
   a trajectory where "depth and breadth CO-OCCUR"
   (explore_function_field_lock.py finding 5), carried into the doc as what
   the ring adds to the fate picture: off Z even the GREEDY trajectory
   reaches the co-occurring class that over Z takes a free policy. But
   BREADTH means EVERY prime seated, and F4 says the greedy support misses
   all but one irreducible per degree -- including x+1, which that same
   finding 5 separately records as never opening. What co-occurs with depth
   here is INFINITE SUPPORT, which is an interior value of the support
   coordinate and not its extreme. Stated in the coordinates rather than in
   the fate names, which is where the difference actually lives: over Z
   greedy dynamics is EXTREMAL IN BOTH -- support minimal (one prime's
   column), exponent maximal -- while over F_2[x] it stays exponent-maximal
   and its support goes INTERIOR, infinite and missing all but one
   irreducible per degree. Both trajectories hold exactly the depth fate, so
   what the ring moves is not which fate greed holds but WHERE IN THE BODY
   it holds it, and it is the corpus's first greedy trajectory extremal in
   one coordinate and interior in the other. (The fate names cannot carry
   this: "depth" is a condition on ONE coordinate, an exponent maximal, and
   both trajectories meet it. Only the second coordinate separates them.)

F6 THE TRANSPLANT FLAGS PAID, both of them at the rig rather than in the
   prose. Flag 2 (a re-push lifts lambda over Z, only a frontier crossing
   does here) fired first: the dynamics construction seated an infinite
   exponent at exponent 1, Z's habit, and stalled at 2 of 4 targets --
   seating it at the frontier 2^c + 1 is the operative move. The pad then
   stalled a second way, searching the target's support inside a FIXED
   universe until the odd part had swallowed every degree in it; the fix is
   to search at the degree the existence argument itself names,
   bit_length(lambda_odd) + 1, where 2^d - 1 > lambda_odd cannot divide it
   -- so the rig now checks the argument's hypothesis rather than a finite
   substitute for it.

ADDED AFTER THE FREEZE, recorded rather than folded into the design above,
which stands as written. Three additions the slate did not name. The
PERMANENCE step in S7, which upgrades "the four rules reach different
prefixes" to "they reach different limits" by exhibiting the first degree
at which two runs part and appealing to F4's domination -- without it the
greedy-image verdict would have rested on prefixes, which are not limits.
The SEED SCOPE in S6, which found the filed chain to be a squarefree-seed
statement. And the whole of S8 -- HOW BIG THE GREEDY IMAGE IS: the
lockstep lemma measured on two runs, the free choice at each fresh opening
counted against N_2(d), and the automorphism reading tested rather than
assumed. The slate asked only whether the greedy image is plural; once it
was, its SIZE was a question the same rig could answer rather than hand
on, and the handover that would have asked it is what this file's own
output had already refuted.

SCOPE, fixed here rather than after the fact. The images are claims about
LIMITS and the rig walks PREFIXES: every reach verdict is a finite
construction plus a stated argument that it continues, and the argument's
hypothesis -- a suitable support member exists at the named degree -- is
what the rig checks. Closure verdicts are exhaustive over the battery's
move range only, with the general reason printed beside each count. The
wall is brute-verified only where its degree fits under the search cap.
The greedy census runs 26 moves from four seeds under four tie-break rules;
what carries it past the horizon is F4, which is proved rather than
sampled. Irreducibility is Rabin's test.

THE NEIGHBOURS, named so nothing here reads as newer than it is. The
lambda law over F_q[x] (Frobenius flattens the 1-units, so the depth clock
is logarithmic) is the equal-characteristic half of the local module law,
proved in a neighbouring file and classical before that; x^(2^n) + x as the
product of all irreducibles of degree dividing n is textbook; supernatural
numbers and their divisibility order are classical; the reachability set of
a nondeterministic rewriting system is the standard object. What is not
inherited: the wall read as the mortality corner of a fate image, the
greedy image as an object at all, and the reading that a ring changes where
greed sits in a body it does not change.

RUN RECORD. Pure Python, no third-party imports; single process, 1.4 s wall
clock, well under the memory ceiling. 151 checks, all clean -- distinct
verifications, not call counts: the door menu's internal scan-bound guard
raises rather than asserting, because counting it once per call put 1063
repetitions of one guard into the headline.

Run: `python explore_fate_image_ff.py`.
"""

import sys
from math import gcd, inf

INF = inf
FAIL = []
CHECKS = 0


def check(cond, msg):
    global CHECKS
    if not cond:
        FAIL.append(msg)
        print("  FAIL: " + msg)
    else:
        CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ------------------------------------------------- F_2[x] on int encodings
# bit i of the encoding is the coefficient of x^i, so the encoding order is
# degree-then-lex and 2 = x, 3 = x+1, 7 = x^2+x+1.

def pdeg(a):
    return a.bit_length() - 1


def pmul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r


def pdivmod(a, b):
    q = 0
    db = pdeg(b)
    while a and pdeg(a) >= db:
        s = pdeg(a) - db
        q ^= 1 << s
        a ^= b << s
    return q, a


def pmod(a, b):
    return pdivmod(a, b)[1]


def pmulmod(a, b, m):
    return pmod(pmul(a, b), m)


def ppow(a, n):
    r = 1
    while n:
        if n & 1:
            r = pmul(r, a)
        a = pmul(a, a)
        n >>= 1
    return r


def pgcd(a, b):
    while b:
        a, b = b, pmod(a, b)
    return a


def prime_divisors(n):
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


def is_irr(f):
    """Rabin irreducibility test on the int encoding."""
    d = pdeg(f)
    if d < 1:
        return False
    if d == 1:
        return True
    if f & 1 == 0:
        return False                       # divisible by x
    if bin(f).count("1") % 2 == 0:
        return False                       # f(1) = 0
    x = 2
    t = x
    for _ in range(d):
        t = pmulmod(t, t, f)
    if t != x:
        return False
    for p in prime_divisors(d):
        t = x
        for _ in range(d // p):
            t = pmulmod(t, t, f)
        if pgcd(t ^ x, f) != 1:
            return False
    return True


_IRR_CLASS = {}


def irr_class(d):
    """Every irreducible of degree d, in encoding order (small d only)."""
    if d not in _IRR_CLASS:
        _IRR_CLASS[d] = [f for f in range(1 << d, 2 << d) if is_irr(f)]
    return _IRR_CLASS[d]


def irr_count(d):
    """N_2(d) by the Moebius formula -- no enumeration."""
    tot = 0
    for e in range(1, d + 1):
        if d % e == 0:
            tot += mobius(e) * (1 << (d // e))
    return tot // d


def mobius(n):
    if n == 1:
        return 1
    r, m = 1, n
    for p in prime_divisors(n):
        if m % (p * p) == 0:
            return 0
        r = -r
    return r


def irr_nth(d, k):
    """The k-th irreducible of degree d in encoding order, lazily.

    The scan STOPS at the end of the degree class: without the bound an
    over-large k walks silently into degree d+1 and returns a polynomial
    of the wrong degree, which every cost above would then misprice.
    """
    f, seen = 1 << d, 0
    while f < (2 << d):
        if is_irr(f):
            if seen == k:
                return f
            seen += 1
        f += 1
    raise ValueError("degree %d has no irreducible number %d" % (d, k))


def irrs_upto(D):
    """Every irreducible of degree <= D, in (degree, encoding) order."""
    out = []
    for d in range(1, D + 1):
        out.extend(irr_class(d))
    return out


def factor_poly(m):
    """Full factorisation by trial division -- small m only."""
    fac = {}
    while pdeg(m) >= 1:
        if is_irr(m):
            fac[m] = fac.get(m, 0) + 1
            break
        hit = False
        for dd in range(1, pdeg(m) // 2 + 1):
            for g in irr_class(dd):
                if pmod(m, g) == 0:
                    fac[g] = fac.get(g, 0) + 1
                    m = pdivmod(m, g)[0]
                    hit = True
                    break
            if hit:
                break
        if not hit:                        # unreachable: a reducible poly
            fac[m] = fac.get(m, 0) + 1     # has a factor of degree <= deg/2
            break
    return fac


# ---------------------------------------------------------------- lambda law

def ceil_log2(a):
    return (a - 1).bit_length()            # a >= 1


def lcm(a, b):
    return a // gcd(a, b) * b


def lam_pp(d, a):
    """lambda(g^a) for deg g = d -- the char-2 law, re-bruted in S1."""
    return ((1 << d) - 1) << ceil_log2(a)


def lam_f(f):
    """lambda of a state carried as a factorisation {irreducible: exponent}."""
    L = 1
    for g, e in f.items():
        if e:
            L = lcm(L, lam_pp(pdeg(g), e))
    return L


def v2(n):
    return (n & -n).bit_length() - 1


def mul_f(f, m):
    """State times a move given by its int encoding."""
    out = dict(f)
    for g, e in factor_poly(m).items():
        out[g] = out.get(g, 0) + e
    return out


def mul_ff(f, g):
    """State times a state, both factorisations."""
    out = dict(f)
    for k, e in g.items():
        out[k] = out.get(k, 0) + e
    return out


def enc_f(f):
    """Int encoding of a state -- small states only."""
    r = 1
    for g, e in f.items():
        r = pmul(r, ppow(g, e))
    return r


def omega_f(f):
    return sum(1 for e in f.values() if e)


def deg_f(f):
    return sum(pdeg(g) * e for g, e in f.items())


# ------------------------------------------------------------ the wall W(L)

def wall_degrees(L):
    """D(L) = { d : (2^d - 1) | L }, finite because 2^d - 1 outgrows L."""
    out, d = [], 1
    while (1 << d) - 1 <= L:
        if L % ((1 << d) - 1) == 0:
            out.append(d)
        d += 1
    return out


def wall_f(L):
    """W(L) as a factorisation: every irreducible of an admissible degree,
    each at the exponent the 2-part of L allows."""
    A = 1 << v2(L)
    out = {}
    for d in wall_degrees(L):
        for g in irr_class(d):
            out[g] = A
    return out


def headroom_f(f):
    """V(N) = W(lambda(N)) / N, as a factorisation."""
    W = wall_f(lam_f(f))
    out = {}
    for g, e in W.items():
        r = e - f.get(g, 0)
        if r > 0:
            out[g] = r
    return out


# ------------------------------------------------------------- the five laws

def adm_independence(f, m):
    return all(not f.get(g) for g in factor_poly(m))


def adm_semisimplicity(f, m):
    fm = mul_f(f, m)
    return all(e <= 1 for e in fm.values())


def adm_newidem(f, m):
    return omega_f(mul_f(f, m)) > omega_f(f)


def adm_transparency(f, m):
    return lam_f(mul_f(f, m)) == lam_f(f)


def adm_dynamics(f, m):
    return lam_f(mul_f(f, m)) > lam_f(f)


LAWS = [
    ("independence", adm_independence),
    ("semisimplicity", adm_semisimplicity),
    ("new-idempotents", adm_newidem),
    ("transparency", adm_transparency),
    ("dynamics", adm_dynamics),
]
LAW_ADM = dict(LAWS)

# The filed Z table (explore_fate_image.py F2): depth-available and
# finite-support-available, per law. Carried as the comparison, never as
# the source -- both bits are re-measured here off this ring's witnesses.
Z_COORDS = {
    "independence": (False, False),
    "semisimplicity": (False, False),
    "new-idempotents": (True, False),
    "transparency": (False, True),
    "dynamics": (True, True),
}


# ------------------------------------------------------------------ targets

class Sup(object):
    """A supernatural polynomial: an exponent function on the irreducibles."""

    def __init__(self, name, expfn, finite_support=None):
        self.name = name
        self._e = expfn
        self.finite_support = finite_support     # None means infinite

    def e(self, g):
        return self._e(g)

    def support(self, univ):
        if self.finite_support is not None:
            return [g for g in self.finite_support]
        return [g for g in univ if self.e(g)]

    def divides_state(self, f):
        return all(e <= self.e(g) for g, e in f.items() if e)


def sup_from_dict(name, d):
    return Sup(name, lambda g: d.get(g, 0), sorted(d, key=lambda g: (pdeg(g), g)))


# ================================================================== S1

def s1_control():
    section("S1  POSITIVE CONTROL (run before any image verdict is read)")

    # (a) the lambda law against the exponent of the unit group
    bad, agree = [], 0
    for d in range(1, 5):
        for g in irr_class(d):
            for a in range(1, 6):
                N = ppow(g, a)
                if pdeg(N) > 9:
                    continue
                best = 1
                for u in range(1, 1 << pdeg(N)):
                    if pgcd(u, N) != 1:
                        continue
                    o, y = 1, u
                    while y != 1:
                        y = pmulmod(y, u, N)
                        o += 1
                    best = lcm(best, o)
                if best == lam_pp(d, a):
                    agree += 1
                else:
                    bad.append((g, a, best, lam_pp(d, a)))
    check(not bad, "lambda law disagrees with the unit group at %s" % bad[:3])
    print("  lambda(g^a) = exponent of the unit group: %d prime powers "
          "(deg <= 9) agree, %d fail" % (agree, len(bad)))

    # (b) monotonicity under divisibility -- the hypothesis the wall's
    # lattice argument needs. Tested at EVERY divisor of every battery
    # state, not just the one-step-down ones, so a law monotone only under
    # unit steps would fail here.
    univ = irrs_upto(3)
    states = [{g: 2, h: 1} for g in univ for h in univ if g != h]
    states += [{g: 3} for g in univ] + [{univ[0]: 1, univ[1]: 2, univ[2]: 1}]
    bad, pairs = [], 0
    for f in states:
        keys = sorted(f)
        ranges = [range(f[k] + 1) for k in keys]
        stack = [{}]
        for k, rng in zip(keys, ranges):
            stack = [{**d, k: e} for d in stack for e in rng]
        for sub in stack:
            pairs += 1
            if lam_f(f) % lam_f(sub):
                bad.append((f, sub))
    check(not bad, "lambda is not monotone under divisibility at %s" % bad[:2])
    print("  lambda monotone under divisibility, every divisor of every "
          "battery state: %d (state, divisor) pairs, %d failures"
          % (pairs, len(bad)))

    # (c) the index convention the depth constructions dereference
    bad = [(d, a) for d in (1, 2, 3) for a in range(1, 18)
           if v2(lam_pp(d, a)) != ceil_log2(a)]
    check(not bad, "v2(lambda(g^a)) != ceil(log2 a) at %s" % bad[:3])
    print("  index convention off the engine: v2(lambda(g^a)) = ceil(log2 a) "
          "(deg g = 1..3, a = 1..17)")

    # (d) irreducible counts against Moebius
    bad = [d for d in range(1, 9) if len(irr_class(d)) != irr_count(d)]
    check(not bad, "irreducible count disagrees with Moebius at %s" % bad)
    print("  irreducible counts d = 1..8: %s (Moebius, enumerated)"
          % [irr_count(d) for d in range(1, 9)])

    # (e) a minimal admissible dynamics move is a PRIME POWER, brute-checked
    states = [{}, {2: 1}, {2: 2}, {3: 1}, {7: 1}, {2: 1, 3: 1}, {2: 3},
              {7: 2}, {2: 1, 7: 1}, {11: 1}, {2: 2, 3: 1}]
    pp, scanned = 0, 0
    for f in states:
        best = None
        for m in range(2, 1 << 9):
            if adm_dynamics(f, m):
                if best is None or pdeg(m) < pdeg(best):
                    best = m
        scanned += 1
        fac = factor_poly(best)
        check(len(fac) == 1, "minimal dynamics move %d is not a prime power" % best)
        pp += 1
        # and the door formula reproduces its COST
        cands = dyn_doors(f)
        check(cands and cands[0][0] == pdeg(best),
              "door menu cost %s != brute minimal degree %d"
              % (cands[0][0] if cands else None, pdeg(best)))
    print("  minimal dynamics move is a prime power and matches the door "
          "menu: %d/%d states (full scan, moves of degree <= 8)" % (pp, scanned))

    # the fresh door's invariant, which lets the menu take the least of the
    # class without checking whether it is seated
    bad = []
    for f in states + [{2: 3, 7: 1}, {11: 1, 13: 2}, {2: 1, 3: 1, 7: 1}]:
        lam = lam_f(f)
        lam_odd = lam >> v2(lam)
        d = 1
        while lam_odd % ((1 << d) - 1) == 0:
            d += 1
        if any(e and pdeg(g) == d for g, e in f.items()):
            bad.append((f, d))
    check(not bad, "a seated irreducible sits at the fresh degree: %s" % bad[:3])
    print("  no seated irreducible ever sits at the FRESH degree: %d states, "
          "%d violations" % (len(states) + 3, len(bad)))

    # (f) the filed greedy runs, reproduced
    f, picks = {}, []
    for _ in range(11):
        cands = dyn_doors(f)
        m = cands[0][1]
        picks.append(m)
        f = mul_ff(f, {cands[0][2]: cands[0][3]})
    check(picks == [4, 2, 4, 7, 11, 16, 19, 37, 67, 131, 256],
          "the filed void run is not reproduced: %s" % picks)
    print("  dynamics greedy from the void (encoding order): %s" % picks)

    f, picks = {}, []
    for _ in range(6):
        m = 2
        while not adm_independence(f, m):
            m += 1
        picks.append(m)
        f = mul_f(f, m)
    check(picks == [2, 3, 7, 11, 13, 19],
          "independence greedy is not the polynomial primorial: %s" % picks)
    print("  independence greedy from the void:                %s" % picks)


# ================================================================== doors

def dyn_doors(f):
    """Every minimal-cost dynamics door, as (cost, m_enc, g, r, kind).

    The minimal admissible move is a prime power g^r (S1 (e) re-brutes
    this against a full scan). With c = v2(lambda) and lambda_odd the odd
    part, the three classes are DEEPEN (g seated at exponent e: the 2-part
    must cross its frontier, r = 2^c + 1 - e), FRESH (g unseated and
    (2^d - 1) not dividing lambda_odd: r = 1 lifts the odd part) and
    CLOCKED (g unseated but its degree's odd factor already sits in
    lambda_odd: only the frontier is left, r = 2^c + 1).

    Returned sorted by (cost, encoding); every entry of minimal cost is the
    tie set the greedy policy CLASS chooses from.
    """
    lam = lam_f(f)
    c = v2(lam)
    lam_odd = lam >> c
    seated = set(g for g, e in f.items() if e)
    cands = []

    for g, e in f.items():                                   # DEEPEN
        if not e:
            continue
        r = (1 << c) + 1 - e
        cands.append((pdeg(g) * r, ppow(g, r), g, r, "deepen"))

    d_fresh = 1                                              # FRESH
    while lam_odd % ((1 << d_fresh) - 1) == 0:
        d_fresh += 1
    # No irreducible of that degree can be SEATED -- a seated one would have
    # put 2^d_fresh - 1 into lambda_odd and the degree would not be fresh --
    # so the least of the class is always available (checked in S1).
    g = irr_nth(d_fresh, 0)
    cands.append((d_fresh, g, g, 1, "fresh"))

    # CLOCKED. Only degrees below d_fresh have their odd factor already in
    # lambda_odd, and a clocked door costs d*(2^c + 1), so one can be
    # minimal only under the bound below -- which is what keeps the scan
    # off the exponentially many irreducibles of a large degree.
    r = (1 << c) + 1
    bound = min(t[0] for t in cands) // r
    if bound > 12:                      # an engine invariant, not a finding:
        raise ValueError(               # counting it per call would inflate
            "the clocked scan bound blew up to %d" % bound)
    for d in range(1, min(bound, d_fresh - 1) + 1):
        for g in irr_class(d):
            if g in seated:
                continue
            cands.append((d * r, ppow(g, r), g, r, "clocked"))

    cands.sort(key=lambda t: (t[0], t[1]))
    return cands


def min_doors(f):
    """The minimal-cost tie set."""
    cs = dyn_doors(f)
    return [t for t in cs if t[0] == cs[0][0]]


def door_families(f):
    """Minimal-cost doors grouped into families a tie-break may choose from.

    A FRESH family stands for every unseated irreducible of its degree, all
    at the same cost, so its members are listed lazily; deepen and clocked
    doors are single candidates.
    """
    cs = min_doors(f)
    seated = set(g for g, e in f.items() if e)
    fams = []
    for cost, enc, g, r, kind in cs:
        if kind == "fresh":
            members = []
            j = 0
            while len(members) < 4 and j < irr_count(pdeg(g)):
                h = irr_nth(pdeg(g), j)
                if h not in seated:
                    members.append((h, h))          # (irreducible, move)
                j += 1
            fams.append((cost, kind, members, r))
        else:
            fams.append((cost, kind, [(g, enc)], r))
    return fams


TIE_RULES = ("lex", "sib", "fresh-first", "deepen-first")


def tie_pick(f, rule):
    """One minimal-cost move under a named tie-break rule."""
    fams = door_families(f)
    key = lambda t: t[2][0][1]                       # least move encoding
    if rule == "lex":
        fams.sort(key=key)
        fam, idx = fams[0], 0
    elif rule == "sib":
        fams.sort(key=key)
        fam = fams[0]
        idx = 1 if len(fam[2]) > 1 else 0
    elif rule == "fresh-first":
        fams.sort(key=lambda t: (0 if t[1] == "fresh" else 1, key(t)))
        fam, idx = fams[0], 0
    else:
        fams.sort(key=lambda t: (0 if t[1] == "deepen" else 1, key(t)))
        fam, idx = fams[0], 0
    g, r = fam[2][idx][0], fam[3]
    return g, r, fam[1], fam[0]


# ================================================================== S2

BRUTE_DEG_CAP = 10


def s2_wall():
    section("S2  THE WALL W(L) -- the closed form against brute search")
    print("  W(L) = the largest monic N with lambda(N) | L. The form under")
    print("  test: every irreducible whose degree d has (2^d - 1) | L, each")
    print("  at exponent 2^v2(L). Brute search runs over every monic")
    print("  polynomial of degree <= %d.\n" % BRUTE_DEG_CAP)

    lam_of = {}
    for n in range(2, 1 << (BRUTE_DEG_CAP + 1)):
        lam_of[n] = lam_f(factor_poly(n))
    lam_of[1] = 1

    tested, bad, lattice_bad, pairs = 0, [], [], 0
    rows = []
    for L in range(1, 65):
        W = wall_f(L)
        dW = deg_f(W)
        if dW > BRUTE_DEG_CAP:
            continue
        members = [n for n, l in lam_of.items() if L % l == 0]
        biggest = max(members, key=lambda n: (pdeg(n), n))
        wenc = enc_f(W)
        tested += 1
        if wenc != biggest:
            bad.append((L, wenc, biggest))
        for n in members:                     # the lattice claim
            pairs += 1
            if pmod(wenc, n) != 0:
                lattice_bad.append((L, n))
        if L in (1, 2, 3, 4, 6, 7, 21):
            rows.append((L, wall_degrees(L), 1 << v2(L), dW, wenc))
    check(not bad, "W formula disagrees with brute search: %s" % bad[:3])
    check(not lattice_bad,
          "a state with lambda | L does not divide W(L): %s" % lattice_bad[:3])
    print("  %-4s %-12s %-4s %-6s %s" % ("L", "D(L)", "A", "deg W", "W encoding"))
    for L, D, A, dW, w in rows:
        print("  %-4d %-12s %-4d %-6d %d" % (L, D, A, dW, w))
    print("\n  %d values of L with deg W(L) <= %d: %d disagreements with brute"
          % (tested, BRUTE_DEG_CAP, len(bad)))
    print("  every state with lambda | L divides W(L): %d (L, state) pairs "
          "checked, %d failures" % (pairs, len(lattice_bad)))

    # D(L) is divisor-closed
    bad = []
    for L in range(1, 200):
        D = set(wall_degrees(L))
        for d in D:
            for e in range(1, d + 1):
                if d % e == 0 and e not in D:
                    bad.append((L, d, e))
    check(not bad, "D(L) is not divisor-closed at %s" % bad[:3])
    print("  D(L) divisor-closed, L = 1..199: %d failures" % len(bad))

    # the special form
    print("\n  THE SPECIAL FORM at L = (2^n - 1)*2^v:")
    bad = []
    for n in range(1, 5):
        for v in range(0, 3):
            L = ((1 << n) - 1) << v
            if deg_f(wall_f(L)) > 24:
                continue
            lhs = enc_f(wall_f(L))
            rhs = ppow((1 << (1 << n)) | 2, 1 << v)   # (x^(2^n) + x)^(2^v)
            if lhs != rhs:
                bad.append((n, v))
            if v == 0:
                print("    n = %d, v = %d: L = %-4d W = x^(2^%d) + x, "
                      "deg %d, D = %s" % (n, v, L, n, pdeg(lhs), wall_degrees(L)))
    check(not bad, "the special form fails at (n, v) = %s" % bad[:3])
    print("    every (n, v) with n <= 4, v <= 2 under the degree cap: "
          "%d failures" % len(bad))
    print("  At v = 0 the wall RING is therefore the product of every finite")
    print("  field whose degree divides n, one factor per irreducible. At")
    print("  v > 0 the polynomial is that one's 2^v-th power and the quotient")
    print("  is no longer a product of fields -- the exponent is what the")
    print("  2-part of the clock buys, and only the rows above are fields.")


# ================================================================== S3

ATLAS_DEG_CAP = 6


def s3_atlas():
    section("S3  THE ADMISSIBILITY ATLAS -- what an admissible move DOES")
    print("  Every monic move of degree 1..%d over a battery of states,"
          % ATLAS_DEG_CAP)
    print("  classified by two bits: SEATS an irreducible the state lacked,")
    print("  RAISES one it already had. SEATLESS = admissible and seating")
    print("  nothing is the column the finite-support coordinate reads.\n")

    states = [{}, {2: 1}, {2: 2}, {3: 1}, {2: 1, 3: 1}, {7: 1}, {2: 1, 7: 1},
              {2: 3}, {2: 2, 3: 1}, {2: 1, 3: 1, 7: 1}, {11: 1}]
    moves = list(range(2, 1 << (ATLAS_DEG_CAP + 1)))
    out = {}
    print("  %-16s %8s %8s %8s %9s" % ("law", "adm", "seats", "raises", "seatless"))
    for name, adm in LAWS:
        tot = seats = raises = 0
        for f in states:
            for m in moves:
                if not adm(f, m):
                    continue
                tot += 1
                fm = factor_poly(m)
                seats += any(not f.get(g) for g in fm)
                raises += any(f.get(g) for g in fm)
        out[name] = (tot, seats, raises, tot - seats)
        print("  %-16s %8d %8d %8d %9d" % (name, tot, seats, raises, tot - seats))

    check(out["independence"][2] == 0, "an independence move raised a seated prime")
    check(out["semisimplicity"][2] == 0,
          "a semisimplicity move raised a seated prime")
    check(out["new-idempotents"][1] == out["new-idempotents"][0],
          "a new-idempotents move seated nothing")
    for nm in ("transparency", "dynamics"):
        check(out[nm][2] > 0, "%s never raises a seated irreducible" % nm)
        check(out[nm][0] - out[nm][1] > 0,
              "%s has no admissible move that seats nothing" % nm)
    print("\n  The three blind ROWS print structural zeros -- two in RAISES,")
    print("  one in SEATLESS -- and each is a TAUTOLOGY given its demand, so")
    print("  they are engine consistency and not evidence: a coprime move")
    print("  cannot carry a seated irreducible, a squarefree state admits no")
    print("  second copy, and a move raising omega must carry an unseated one.")
    print("  What is MEASURED is the sighted rows: both admit moves that seat")
    print("  nothing, which is what lets a run stop widening its support.")
    return out


# ================================================================== S4

REACH_STEPS = 7


def build_independence(target, f, univ):
    for g in target.support(univ):
        if not f.get(g):
            e = target.e(g)
            if e is INF:
                return None
            return {g: e}
    return None


def build_semisimplicity(target, f, univ):
    for g in target.support(univ):
        if not f.get(g):
            return {g: 1} if target.e(g) == 1 else None
    return None


def build_newidem(target, f, univ):
    """One fresh support irreducible, plus progress on every infinite
    exponent already seated."""
    m = {}
    for g, e in f.items():
        if e and target.e(g) is INF:
            m[g] = e                      # double the depth each step
    for g in target.support(univ):
        if not f.get(g):
            e = target.e(g)
            m[g] = m.get(g, 0) + (1 if e is INF else e)
            return m
    return None


def build_dynamics(target, f, univ):
    """Frontier-jumping depth plus the next unseated support member.

    TRANSPLANT FLAG 2 lives here: over Z one more copy of a seated prime
    always lifts lambda, and here it lifts lambda only past the ceil(log2)
    frontier, so every depth factor jumps to 2^c + 1.
    """
    lam = lam_f(f)
    c = v2(lam)
    lam_odd = lam >> c
    m = {}
    for g, e in f.items():
        if e and target.e(g) is INF:
            m[g] = (1 << c) + 1 - e       # cross the frontier
    for g in target.support(univ):
        if not f.get(g):
            e = target.e(g)
            # an infinite exponent is SEATED at the frontier, never at 1:
            # over Z one copy always lifts lambda and here only a frontier
            # crossing does (TRANSPLANT FLAG 2).
            m[g] = m.get(g, 0) + ((1 << c) + 1 if e is INF else e)
            break
    if not m:
        return None
    if lam_f(mul_ff(f, m)) > lam:
        return m
    # THE PAD, and its existence argument: a support member of degree
    # d = bit_length(lambda_odd) + 1 has 2^d - 1 > lambda_odd, so it cannot
    # divide lambda_odd and the odd part MUST rise. The rig searches at
    # exactly that degree, so it checks the argument's hypothesis (such a
    # member is in the target's support) rather than its conclusion.
    d = lam_odd.bit_length() + 1
    for k in range(4):
        g = irr_nth(d, k)
        if target.e(g) and not f.get(g) and g not in m:
            m[g] = 1
            return m
    return None


BUILDERS = {
    "independence": build_independence,
    "semisimplicity": build_semisimplicity,
    "new-idempotents": build_newidem,
    "dynamics": build_dynamics,
}


def reach(lawname, seed, target, univ, steps=REACH_STEPS):
    """Walk the construction; return (ok, steps_taken, note)."""
    adm = LAW_ADM[lawname]
    build = BUILDERS[lawname]
    f = dict(seed)
    last_idx = -1
    for i in range(steps):
        m = build(target, f, univ)
        if m is None:
            return False, i, "construction stalled"
        enc = enc_f(m)
        if pdeg(enc) < 1:
            return False, i, "empty move"
        if not adm(f, enc):
            return False, i, "move %d inadmissible" % enc
        f2 = mul_ff(f, m)
        if not target.divides_state(f2):
            return False, i, "state left the target"
        f = f2
        if target.finite_support is None:
            idx = next((j for j, g in enumerate(univ) if not f.get(g)), len(univ))
            if idx <= last_idx:
                return False, i, "the least unseated support member did not rise"
            last_idx = idx
    return True, steps, "ok"


def s4_reach(univ, wit):
    section("S4  THE REACH HALF -- constructions against a target battery")

    T_ALL1 = Sup("every irreducible at exponent 1", lambda g: 1)
    T_MIX = Sup("exponents 1, 2, 3 by degree", lambda g: 1 + (pdeg(g) % 3))
    T_DEEPX = Sup("x^oo times every other irreducible at 1",
                  lambda g: INF if g == 2 else 1)
    T_XINF = sup_from_dict("x^oo alone", {2: INF})
    T_XINF.finite_support = [2]
    T_SEEDED = Sup("(x^2+x+1) * x^oo", lambda g: INF if g == 2 else
                   (1 if g == 7 else 0), finite_support=[2, 7])

    print("  IN-IMAGE targets -- every move admissible, the state divides the")
    print("  target at every step, and the least unseated support member")
    print("  strictly rises.\n")
    print("  %-16s %-34s %6s %s" % ("law", "target", "steps", "verdict"))
    plan = [
        ("independence", {}, T_ALL1),
        ("independence", {}, T_MIX),
        ("independence", {7: 2}, T_MIX),
        ("semisimplicity", {}, T_ALL1),
        ("new-idempotents", {}, T_DEEPX),
        ("new-idempotents", {}, T_ALL1),
        ("dynamics", {}, T_DEEPX),
        ("dynamics", {}, T_ALL1),
        ("dynamics", {}, T_XINF),
        ("dynamics", {7: 1}, T_SEEDED),
    ]
    for lawname, seed, tgt in plan:
        seed2 = dict(seed)
        if lawname == "independence" and seed:
            tgt = Sup(tgt.name, lambda g, t=tgt, s=seed2:
                      max(t.e(g), s.get(g, 0)) if g not in s else s[g])
        okk, n, note = reach(lawname, seed2, tgt, univ)
        check(okk, "%s cannot reach %s: %s" % (lawname, tgt.name, note))
        print("  %-16s %-34s %6d %s" % (lawname, tgt.name, n, note))
        if not okk:
            continue
        # the POSITIVE witnesses S6 reads its YES bits off
        if any(tgt.e(g) is INF for g in tgt.support(univ)[:20]):
            wit["depth_pos"][lawname] = "reached %s (S4)" % tgt.name
        if tgt.finite_support is not None:
            wit["supp_pos"][lawname] = "reached %s (S4)" % tgt.name

    print("\n  OUT-OF-IMAGE targets -- the reason, by exhaustive scan over")
    print("  every monic move of degree <= 8.\n")

    f = {2: 1}
    hits = [m for m in range(2, 1 << 9)
            if adm_independence(f, m) and pmod(m, 2) == 0]
    check(not hits, "an independence move carried the seed's own irreducible")
    print("  independence from x, target wanting e_x = 2: %d of %d moves are"
          % (len(hits), (1 << 9) - 2))
    print("    admissible AND divisible by x -- the seed's exponents are frozen.")

    f = {2: 1, 3: 1}
    hits = [m for m in range(2, 1 << 9)
            if adm_semisimplicity(f, m) and pmod(m, 2) == 0]
    check(not hits, "a semisimplicity move raised a seated exponent")
    print("  semisimplicity from x(x+1), target wanting e_x = 2: %d admissible"
          % len(hits))
    print("    moves divisible by x -- every exponent is pinned to 1.")

    stall = [m for m in range(2, 1 << 9) if adm_semisimplicity({2: 2}, m)]
    check(not stall, "a non-squarefree state had an admissible move")
    print("  semisimplicity from x^2: %d admissible moves at all -- from a"
          % len(stall))
    print("    non-squarefree seed the image is the seed itself.")
    print("  Those three zeros are TAUTOLOGIES given their demands, exactly as")
    print("  the atlas's blind rows are: a coprime move cannot carry a seated")
    print("  irreducible, and a non-squarefree state has no squarefree")
    print("  multiple. What the scans test is the ENGINE, and the reason each")
    print("  target is out of image is the structural line beside it -- not a")
    print("  count. The dynamics row below is the one that could have gone")
    print("  either way.")

    dead = []
    for f in [{}, {2: 1}, {7: 3}, {2: 2, 3: 1}, {11: 1, 2: 5}]:
        if not any(adm_dynamics(f, m) for m in range(2, 1 << 9)):
            dead.append(f)
    check(not dead, "a dynamics state had no admissible move: %s" % dead[:2])
    print("  dynamics: every battery state has an admissible move, so no run")
    print("    halts and no limit is finite -- the closure half is vacuous.")


# ================================================================== S5

def s5_closure(univ, wit):
    section("S5  THE CLOSURE HALF -- the invariant that bounds each image")

    states = [{}, {2: 1}, {2: 2}, {3: 1}, {2: 1, 3: 1}, {7: 1}, {2: 1, 7: 1},
              {2: 3}, {2: 2, 3: 1}, {11: 1}]
    moves = list(range(2, 1 << 8))

    bad = 0
    for f in states:
        for m in moves:
            if adm_independence(f, m):
                fm = mul_f(f, m)
                for g, e in f.items():
                    if e and fm[g] != e:
                        bad += 1
    check(bad == 0, "independence changed a seated exponent")
    print("  independence: a seated exponent NEVER moves -- %d violations over"
          % bad)
    print("    %d state x move pairs. Seed exponents frozen, each seated"
          % (len(states) * len(moves)))
    print("    exponent final, so every image exponent is finite.")

    bad = sum(1 for f in states for m in moves
              if adm_semisimplicity(f, m)
              and any(e > 1 for e in mul_f(f, m).values()))
    check(bad == 0, "semisimplicity left a squarefree state")
    print("  semisimplicity: %d admissible moves leaving squarefreeness." % bad)

    bad = sum(1 for f in states for m in moves
              if adm_newidem(f, m)
              and not any(not f.get(g) for g in factor_poly(m)))
    check(bad == 0, "a new-idempotents move seated nothing")
    print("  new-idempotents: %d admissible moves seating nothing -- the"
          % bad)
    print("    support of any limit is infinite.")

    live = []
    for name in ("independence", "semisimplicity", "new-idempotents", "dynamics"):
        adm = LAW_ADM[name]
        n = sum(1 for f in states if any(adm(f, m) for m in moves))
        live.append((name, n))
    print("  liveness over the battery (states with an admissible move):")
    for name, n in live:
        print("    %-16s %d/%d" % (name, n, len(states)))
    check(dict(live)["semisimplicity"] < len(states),
          "semisimplicity never dies, so liveness is not a (law, seed) property")
    print("    semisimplicity dies from a non-squarefree seed and lives from")
    print("    the void: liveness belongs to the (law, seed) PAIR.")

    print("\n  transparency: the reachable set by exhaustion, from several")
    print("  seeds -- every maximal run ends at W(lambda(s)).")
    print("  %-14s %-8s %-10s %-10s %s"
          % ("seed", "lambda", "reached", "W(lambda)", "steps"))
    for seed in ({}, {2: 1}, {3: 1}, {2: 1, 3: 1}, {7: 1}, {2: 2}):
        f = dict(seed)
        steps = 0
        while True:
            V = headroom_f(f)
            if deg_f(V) < 1:
                break
            g = min(V, key=lambda h: (pdeg(h), h))
            f = mul_ff(f, {g: 1})
            steps += 1
        W = wall_f(lam_f(seed))
        check(enc_f(f) == enc_f(W),
              "transparency from %s halts at %d, not W = %d"
              % (seed, enc_f(f), enc_f(W)))
        print("  %-14s %-8d %-10d %-10d %d"
              % (enc_f(seed), lam_f(seed), enc_f(f), enc_f(W), steps))
    # the two witnesses S6 reads off this exhaustion
    wit["finite_reach"]["transparency"] = "the reachable set is finite (S5)"
    wit["supp_pos"]["transparency"] = "the image point IS finite (S5)"
    print("  The reachable set is FINITE and has a top, so the image is one")
    print("  finite point and the law is mortal -- as over Z, and for the")
    print("  same reason, which is the headroom fact and not the square.")


# ================================================================== S6

def s6_table(atlas, wit):
    section("S6  THE TWO COORDINATES, AND THE CHAIN")
    print("  Neither bit is typed in. A YES comes from a POSITIVE witness --")
    print("  S4 reached a target with that property under this law. A NO comes")
    print("  from a CLOSURE reason measured in S3/S5. A law with neither, or")
    print("  with both, FAILS rather than printing a verdict.\n")

    # closure reasons, read off the measured counts rather than asserted
    depth_neg, supp_neg = {}, {}
    for name, _ in LAWS:
        tot, seats, raises, seatless = atlas[name]
        if raises == 0:
            depth_neg[name] = "no admissible move raises a seated exponent (S3)"
        elif name in wit["finite_reach"]:
            depth_neg[name] = "the reachable set is finite by exhaustion (S5)"
        if seatless == 0:
            supp_neg[name] = "no admissible move seats nothing (S3)"

    print("  %-16s %-8s %-8s %-8s %s"
          % ("law", "depth", "fin-supp", "Z", "match"))
    mism, coords, reasons = 0, {}, {}
    for name, _ in LAWS:
        bits = []
        for coord, pos, neg in (("depth", wit["depth_pos"], depth_neg),
                                ("supp", wit["supp_pos"], supp_neg)):
            yes, no = name in pos, name in neg
            check(yes != no,
                  "%s/%s has %s witness" % (name, coord,
                                            "both a positive and a closure"
                                            if yes else "neither a positive nor a closure"))
            bits.append(yes)
            reasons[(name, coord)] = (pos[name] if yes else
                                      neg.get(name, "NO WITNESS"))
        d, s = bits
        coords[name] = (d, s)
        zd, zs = Z_COORDS[name]
        m = (d, s) == (zd, zs)
        mism += 0 if m else 1
        print("  %-16s %-8s %-8s %-8s %s"
              % (name, "yes" if d else "no", "yes" if s else "no",
                 ("yes" if zd else "no") + "/" + ("yes" if zs else "no"),
                 "=" if m else "MISMATCH"))
    check(mism == 0, "%d coordinate mismatches against the Z table" % mism)
    print("\n  %d mismatches against the filed Z table. The witness behind"
          % mism)
    print("  every bit:")
    for name, _ in LAWS:
        print("    %-16s depth: %s" % (name, reasons[(name, "depth")]))
        print("    %-16s supp:  %s" % ("", reasons[(name, "supp")]))

    print("\n  THE CHAIN. Membership predicates on a described limit, from")
    print("  the shapes S4 and S5 established, checked over a battery.")

    # a described limit: (support infinite?, exponents all 1?, some oo?)
    def in_semis(t):
        return t["supp_inf"] and t["all_one"]

    def in_indep(t):
        return t["supp_inf"] and not t["has_inf"]

    def in_newid(t):
        return t["supp_inf"]

    def in_dyn(t):
        return t["supp_inf"] or t["has_inf"]

    battery = [
        dict(name="every irreducible at 1", supp_inf=True, all_one=True,
             has_inf=False),
        dict(name="infinite support, exponents 1..3", supp_inf=True,
             all_one=False, has_inf=False),
        dict(name="infinite support with x^oo", supp_inf=True, all_one=False,
             has_inf=True),
        dict(name="x^oo alone", supp_inf=False, all_one=False, has_inf=True),
        dict(name="a finite polynomial", supp_inf=False, all_one=False,
             has_inf=False),
    ]
    print("  %-34s %-7s %-7s %-7s %s"
          % ("described limit", "semis", "indep", "newid", "dyn"))
    bad = 0
    for t in battery:
        a, b, c, d = in_semis(t), in_indep(t), in_newid(t), in_dyn(t)
        if (a and not b) or (b and not c) or (c and not d):
            bad += 1
        print("  %-34s %-7s %-7s %-7s %s"
              % (t["name"], "in" if a else "-", "in" if b else "-",
                 "in" if c else "-", "in" if d else "-"))
    check(bad == 0, "the chain inclusion fails at %d described limits" % bad)
    print("  %d inclusion failures. Strictness witnesses, one per link:" % bad)
    print("    semis  < indep : infinite support, exponents 1..3")
    print("    indep  < newid : infinite support with x^oo")
    print("    newid  < dyn   : x^oo alone")
    print("  The transparency point (a finite polynomial) is in NONE of the")
    print("  four, which is why it sits outside the chain.")

    # THE SEED SCOPE, which the chain needs and the filed statement of it
    # over Z leaves implicit. The bottom link holds at a SQUAREFREE seed
    # only: from a non-squarefree seed semisimplicity admits nothing (S4),
    # so its image is the single finite point {s} -- and the battery row
    # above shows a finite polynomial lies in NO image of the four. So the
    # law leaves the chain entirely rather than sitting at its bottom.
    dead = [m for m in range(2, 1 << 9) if adm_semisimplicity({2: 2}, m)]
    check(not dead, "a non-squarefree state had an admissible move")
    fin = battery[-1]
    check(fin["name"] == "a finite polynomial" and not in_indep(fin),
          "the finite-limit row is not the witness this scope needs")
    print("\n  SEED SCOPE. The bottom link is a SQUAREFREE-seed statement: from")
    print("  a non-squarefree seed semisimplicity admits %d moves, so its image"
          % len(dead))
    print("  is {s}, a finite point -- and the last row above shows no image of")
    print("  the four contains one. Semisimplicity then leaves the chain by the")
    print("  same door transparency never entered, and 'four form a chain' is")
    print("  false at those seeds. Same over Z, where the scope is implicit.")


# ================================================================== S7

GREEDY_STEPS = 26


def greedy_run(seed, rule, steps=GREEDY_STEPS):
    """Greedy dynamics under one tie-break rule. Returns the state, the
    move log, and the count of times a sibling door was dominated."""
    f = dict(seed)
    log, dominated = [], 0
    for _ in range(steps):
        # THE SIBLING DOMINATION, checked arithmetically at every state: for
        # each seated irreducible whose degree class still has an unseated
        # member, that member's only route in is the CLOCKED door at
        # d*(2^c + 1), and the seated one's own deepening door costs
        # d*(2^c + 1 - e) with e >= 1 -- strictly less, so the sibling is
        # never in the minimal set.
        c = v2(lam_f(f))
        for g, e in f.items():
            if not e:
                continue
            d = pdeg(g)
            if irr_count(d) <= sum(1 for h, ee in f.items()
                                   if ee and pdeg(h) == d):
                continue
            if d * ((1 << c) + 1) <= d * ((1 << c) + 1 - e):
                return None, None, "a sibling door was not dominated"
            dominated += 1
        g, r, kind, cost = tie_pick(f, rule)
        f = mul_ff(f, {g: r})
        log.append((g, r, kind, cost))
    return f, log, dominated


def s7_greedy(univ):
    section("S7  THE GREEDY IMAGE -- what greed reaches when 'least' ties")

    print("  Over Z the least admissible move is UNIQUE by definition -- a")
    print("  set of integers has one least element -- so the greedy image is")
    print("  a point there, unmeasured and unmeasurable. Here 'least' orders")
    print("  by DEGREE and the minimal set is")
    print("  generically plural. The void's own first move:\n")
    cs = min_doors({})
    print("  %-8s %-10s %-10s %s" % ("cost", "move", "kind", "reading"))
    for cost, enc, g, r, kind in cs:
        print("  %-8d %-10d %-10s g = %d, r = %d" % (cost, enc, kind, g, r))
    check(len(cs) >= 2, "the void's minimal-degree set is a singleton")
    print("\n  %d minimal-cost moves at the void: the greedy RULE does not"
          % len(cs))
    print("  name a move, and the tie-break is a choice outside the law.")

    print("\n  Four tie-break rules, %d moves each, from the void and three"
          % GREEDY_STEPS)
    print("  seeds. SEATED = irreducibles in the support; MAXDEG = the")
    print("  deepest degree seated; DEPTH = the largest exponent.\n")
    seeds = [({}, "void"), ({7: 1}, "x^2+x+1"), ({2: 1, 3: 1}, "x(x+1)"),
             ({11: 2}, "(x^3+x+1)^2")]
    print("  %-14s %-13s %6s %7s %7s %s"
          % ("seed", "rule", "seated", "maxdeg", "depth", "support (encodings)"))
    limits = {}
    per_degree_bad = []
    for seed, sname in seeds:
        for rule in TIE_RULES:
            f, log, dom = greedy_run(seed, rule)
            check(f is not None, "greedy run failed: %s" % dom)
            if f is None:
                continue
            supp = sorted((g for g, e in f.items() if e),
                          key=lambda h: (pdeg(h), h))
            counts = {}
            for g in supp:
                counts[pdeg(g)] = counts.get(pdeg(g), 0) + 1
            extra = {d: n for d, n in counts.items() if n > 1}
            seeded_extra = {d: n for d, n in extra.items()
                            if n > sum(1 for g in seed if pdeg(g) == d)}
            if seeded_extra:
                per_degree_bad.append((sname, rule, seeded_extra))
            limits.setdefault(sname, set()).add(
                tuple(sorted((g, e) for g, e in f.items() if e)))
            print("  %-14s %-13s %6d %7d %7d %s"
                  % (sname, rule, len(supp), max(pdeg(g) for g in supp),
                     max(f.values()), supp[:8]))
    check(not per_degree_bad,
          "a run seated two irreducibles of one degree: %s" % per_degree_bad[:2])

    print("\n  DISTINCT PREFIXES reached from each seed, over the four rules:")
    for sname, ls in limits.items():
        print("    %-14s %d" % (sname, len(ls)))
    check(len(limits["void"]) >= 2,
          "every tie-break rule reached the same prefix from the void")

    # A prefix is not a limit. What makes the divergence PERMANENT is the
    # domination below: at the first degree where two runs seat different
    # irreducibles, both classes are occupied from then on, so neither run
    # can ever seat the other's member and the supports differ forever.
    fa = greedy_run({}, "lex")[0]
    fb = greedy_run({}, "sib")[0]
    sa = {pdeg(g): g for g, e in fa.items() if e}
    sb = {pdeg(g): g for g, e in fb.items() if e}
    dsplit = min((d for d in sa if d in sb and sa[d] != sb[d]), default=None)
    check(dsplit is not None,
          "the two void runs never seat different irreducibles")
    print("\n  The first degree at which 'lex' and 'sib' part: %d -- one seats"
          % dsplit)
    print("  %d, the other %d. Both classes are occupied from that move on, so"
          % (sa[dsplit], sb[dsplit]))
    print("  by the domination below neither run can ever seat the other's")
    print("  member: the divergence is PERMANENT and the LIMITS differ, not")
    print("  merely the prefixes.")

    print("\n  Greedy INDEPENDENCE under the same kind of tie-break -- least")
    print("  degree first, then the 1st / 2nd / last unseated irreducible of")
    print("  that degree:\n")
    print("  %-10s %s" % ("rule", "seated after 8 moves"))
    sets = []
    for rname, pick in (("first", 0), ("second", 1), ("last", -1)):
        f = {}
        for _ in range(8):
            d = 1
            while True:
                free = [g for g in irr_class(d) if not f.get(g)]
                if free:
                    break
                d += 1
            g = free[pick] if pick < len(free) else free[-1]
            check(adm_independence(f, g), "an independence pick was inadmissible")
            f = mul_ff(f, {g: 1})
        s = frozenset(g for g, e in f.items() if e)
        sets.append(s)
        print("  %-10s %s" % (rname, sorted(s, key=lambda h: (pdeg(h), h))))
    check(len(set(sets)) == 1,
          "independence tie-breaks reached different sets: %d" % len(set(sets)))
    check(sets[0] == frozenset(irrs_upto(4)),
          "independence greed did not seat every irreducible of degree <= 4")
    print("  Every rule has seated exactly the %d irreducibles of degree <= 4:"
          % len(irrs_upto(4)))
    print("  ties reorder the picks and change nothing about the LIMIT, which")
    print("  is the polynomial primorial under every tie-break. So plurality")
    print("  of the greedy image is a property of the (law, ring) pair, not of")
    print("  the ring alone.")

    print("\n  THE SIBLING DOMINATION, which is why the support is thin. A")
    print("  sibling of a SEATED irreducible of degree d can only open")
    print("  CLOCKED, at cost d*(2^c + 1); the seated one's own deepening")
    print("  door costs d*(2^c + 1 - e) with e >= 1. The second is strictly")
    print("  cheaper at every clock, so a sibling is never in the minimal")
    print("  set -- for ANY tie-break, from ANY seed.\n")
    print("  %-14s %-13s %s" % ("seed", "rule", "dominations exercised"))
    tot = 0
    for seed, sname in seeds:
        for rule in TIE_RULES:
            f, log, dom = greedy_run(seed, rule)
            tot += dom
            print("  %-14s %-13s %d" % (sname, rule, dom))
    check(tot > 0, "the domination was never exercised, so it is untested")

    print("\n  THE DENSITY of the greedy support, void run under 'lex':")
    f, log, dom = greedy_run({}, "lex")
    supp = sorted((g for g, e in f.items() if e), key=lambda h: (pdeg(h), h))
    print("  %-8s %-14s %-10s %s" % ("degree", "irreducibles", "seated", "missed"))
    for d in range(1, max(pdeg(g) for g in supp) + 1):
        n = irr_count(d)
        s = sum(1 for g in supp if pdeg(g) == d)
        print("  %-8d %-14d %-10d %d" % (d, n, s, n - s))
    check(all(sum(1 for g in supp if pdeg(g) == d) <= 1
              for d in range(1, 30)),
          "the void run seated two irreducibles of one degree")
    check(2 not in supp or 3 not in supp,
          "both degree-1 irreducibles were seated")
    print("\n  At most one per degree against N_2(d) ~ 2^d/d available, so the")
    print("  seated set has density ZERO among the irreducibles and infinitely")
    print("  many are never seated. The greedy limit therefore holds an")
    print("  infinite exponent and an infinite support that is NOT everything.")


# ================================================================== S8

def s8_size():
    section("S8  HOW BIG IS THE GREEDY IMAGE")
    print("  S7 showed the image is plural. Its SIZE follows from one lemma:")
    print("  every irreducible of a given degree contributes the SAME factor")
    print("  2^d - 1 to lambda, so the whole cost structure of a trajectory")
    print("  depends on the DEGREES it opens and not on WHICH member of each")
    print("  degree it opens. Two policies differing only in that choice run")
    print("  in lockstep -- and every fresh opening is then a free choice")
    print("  among all N_2(d) members of its degree.\n")

    a = greedy_run({}, "lex")[1]
    b = greedy_run({}, "sib")[1]
    check(len(a) == len(b), "the two runs took different move counts")
    sig_a = [(c, k, pdeg(g)) for g, r, k, c in a]
    sig_b = [(c, k, pdeg(g)) for g, r, k, c in b]
    check(sig_a == sig_b,
          "the cost/kind/degree sequences differ: %s vs %s"
          % (sig_a[:4], sig_b[:4]))
    diff = [i for i, (x, y) in enumerate(zip(a, b)) if x[0] != y[0]]
    print("  'lex' vs 'sib' over %d moves: the (cost, kind, degree) sequences"
          % len(a))
    print("  are IDENTICAL, and the two runs pick different irreducibles at")
    print("  %d of them. Lockstep, different limits." % len(diff))

    print("\n  THE FREE CHOICES. At each FRESH opening the whole degree class")
    print("  is unseated (S1's invariant), every member costs the same d, so")
    print("  every member is in the minimal set:\n")
    print("  %-6s %-8s %-14s %s" % ("move", "degree", "N_2(degree)", "seated"))
    f, choices, total = {}, [], 1
    for i in range(GREEDY_STEPS):
        g, r, kind, cost = tie_pick(f, "lex")
        if kind == "fresh":
            d = pdeg(g)
            n = irr_count(d)
            seated_d = sum(1 for h, e in f.items() if e and pdeg(h) == d)
            check(seated_d == 0, "the fresh degree %d was already occupied" % d)
            choices.append((i + 1, d, n))
            total *= n
            if len(choices) <= 9:
                print("  %-6d %-8d %-14d %d" % (i + 1, d, n, seated_d))
        f = mul_ff(f, {g: r})
    check(sum(1 for _, _, n in choices if n >= 2) >= 5,
          "too few multi-member fresh openings to read a product")
    print("  ... %d fresh openings in %d moves, %d of them with N_2(d) >= 2"
          % (len(choices), GREEDY_STEPS,
             sum(1 for _, _, n in choices if n >= 2)))
    print("\n  The image from the void therefore contains one limit per CHOICE")
    print("  FUNCTION over these classes -- distinct limits, because the")
    print("  starvation (S7) makes each choice permanent. The %d openings"
          % len(choices))
    print("  above already give a %d-digit number of distinct %d-move prefixes;"
          % (len(str(total)), GREEDY_STEPS))
    print("  the frontier degrees keep rising and N_2(d) ~ 2^d/d, so the")
    print("  product runs forever with every factor >= 2 from degree 3 on:")
    print("  THE GREEDY IMAGE HAS THE CARDINALITY OF THE CONTINUUM, where")
    print("  over Z it is a single point.")
    print("\n  And it is NOT an automorphism orbit, which was the natural")
    print("  guess: Aut(F_2[x]) = {x, x+1} has order 2 while the image is")
    print("  uncountable. The witness is concrete --")
    lexs = sorted((g for g, e in greedy_run({}, "lex")[0].items() if e),
                  key=lambda h: (pdeg(h), h))
    sibs = sorted((g for g, e in greedy_run({}, "sib")[0].items() if e),
                  key=lambda h: (pdeg(h), h))
    sig = sorted((sigma(g) for g in lexs), key=lambda h: (pdeg(h), h))
    check(sibs != lexs and sibs != sig,
          "the 'sib' limit is the lex limit or its automorphic image")
    print("  lex        %s" % lexs[:6])
    print("  sigma(lex) %s" % sig[:6])
    print("  sib        %s" % sibs[:6])
    print("  and 'sib' is neither. Ties here are COST COLLAPSE -- many places")
    print("  of equal norm -- and only some of that collapse is symmetry.")


def sigma(f):
    """The nontrivial F_2-automorphism of F_2[x], x -> x + 1."""
    r = 0
    for i in range(f.bit_length()):
        if (f >> i) & 1:
            r ^= ppow(3, i)
    return r


# ================================================================== main

def main():
    univ = irrs_upto(6)
    s1_control()
    if FAIL:
        print("\nCONTROL FAILED -- no image verdict is read.")
        sys.exit(1)
    s2_wall()
    atlas = s3_atlas()
    wit = {"depth_pos": {}, "supp_pos": {}, "finite_reach": {}}
    s4_reach(univ, wit)
    s5_closure(univ, wit)
    s6_table(atlas, wit)
    s7_greedy(univ)
    s8_size()

    section("SUMMARY")
    print("  checks passed: %d" % CHECKS)
    if FAIL:
        print("  FAILURES: %d" % len(FAIL))
        for m in FAIL:
            print("    " + m)
        sys.exit(1)
    print("  all clean")


if __name__ == "__main__":
    main()
