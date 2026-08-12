r"""explore_ram_tie.py -- THE RAMIFIED VOID TIE: ONE NORM, TWO KINDS,
AND A DEEP PLACE THAT LOST THE VOID.

THE QUESTION. The cross-kind settlement (explore_cross_kind_tie.py)
walked the void tie between two norms of one kind -- norm 2 beside
norm 4, both unramified -- and found the greedy limit multivalued. Its
own left-open cell is the mirror: one norm, two KINDS. A cubic ring can
stage 5 = P*Q^2 -- P unramified of residue degree 1, Q RAMIFIED with
e = 2, both of norm 5, both at door 1 -- with 2 and 3 inert (norms 8 and
27), so the void menu ties at exactly 5 across the unramified/ramified
seam. The winner-kind trichotomy reads paid direction off the winner's
kind: CONSTANT at an unramified non-norm-2 winner, RISING through a
ramified winner's transient. This tie pits those two rows against each
other at one void. Does the tie-break choose between fate DIRECTIONS --
and what does the ramified branch actually do once risen: keep its
runaway, or get undercut by a place that lost the void?

WHOSE VOCABULARY. Engine observables, re-derived from
explore_cross_kind_tie.py's WHOSE VOCABULARY block rather than memory:
lam_P(pl, a) is the exponent of (O/P^a)^*; L = the lcm of lam_P(pl, e_pl)
over everything seated, each read at its seated depth; door_r(pl, e, L) =
the least r >= 1 with lam_P(pl, e+r) not dividing L; a move at pl costs
norm(pl)^r and raises the exponent by r; greedy takes the menu minimum,
first tie member by place_key, and the walker branches on ties instead
of breaking them silently.

WHY THE RAMIFIED QUOTIENT IS COMPUTABLE WITHOUT THE FIELD. Q here is
TAMELY ramified (e = 2, p = 5, gcd(e, p) = 1, e < p - 1), so the
completion O_Q is a ramified quadratic extension of Z_5 -- one of the
two classes Q_5(sqrt(5)) and Q_5(sqrt(5u)), u a non-residue -- and
O/Q^a is presentable concretely: Q^(2b) = (5^b) gives
(Z/5^b)[x]/(x^2 - 5u), and Q^(2b+1) gives pairs (c0 mod 5^(b+1),
c1 mod 5^b) under the relation x^2 = 5u. The closed form for the unit
exponent, from the tame filtration (raising a 1-unit to the p-th power
lifts its level by exactly e = v(p), and the Teichmueller lift carries
F_5^*):

    lam_Q(a) = lcm(4, 5^ceil((a-1)/2))  -- 4, 20, 20, 100, 100, 500, ...

the pair-repeat ramp, brute-verified below on BOTH uniformizer classes
(u = 1 and u = 2) before any walk reads it deeper. Unramified places are
Galois rings GR(p^a, d) exactly as in the sibling rigs.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 The tie-tree frame is imported from the cross-kind rig, where the
    even tie crossed NORMS within one kind. This tie crosses KINDS
    within one norm -- the exact complement. The frame is used only to
    ENUMERATE branches; every branch claim is derived per-branch below.
 T2 The constant and rising signatures are the trichotomy's per-kind
    rows, read at neighbouring cells (quadratic hosts; the cross-kind
    cubic). They are predictions here, not inheritances: no walked ring
    has ever run the ramified row from a TIE, and no walked ring has
    ever been undercut mid-transient.
 T3 "Deep place", "runaway", "stranded" are the ideal-limit vocabulary
    (one runaway coordinate plus strands). The rig prints exponents and
    last-mover data; which coordinate is "the" deep one is weighed
    after the run.

THE HAND-ATTACK, on paper before any engine code. Setup: cubic K with
5 = P*Q^2 tame -- f(P) = f(Q) = 1, e(Q) = 2, both norm 5 -- 2 and 3
inert, no other prime below 31 dividing disc. Columns: P's is
lam_P(a) = lcm(4, 5^(a-1)) = 4, 20, 100, 500, ... strict from depth 1;
Q's is the ramp above; the inert-2 place T (norm 8) carries
7, 14, 28, 56, ... = lcm(7, 2^(a-1)); the inert-3 place carries
26, ... (26 = 2 * 13 never divides any L this walk builds, so its
door-1 cost 27 > 25 never fires).

 A. THE VOID MENU. L = 1. P: lam(4) does not divide 1 -- door 1, cost
    5. Q: lam(4) likewise -- door 1, cost 5. T: 7 does not divide 1,
    door 1, cost 8. Everything else >= 7. The void minimum is 5 at
    exactly {P, Q}: a two-member tie, SAME norm, ACROSS kinds. Nothing
    at 4 or less exists: a norm-2, -3, or -4 place would need 2 or 3
    non-inert, and the fibre over 5 is exhausted by P*Q^2.
 B. BRANCH A (seat P, exponent 1, L = 4). Step 2: P at door 1 cost 5
    (lam_P(2) = 20 does not divide 4); Q at door 2 cost 25 (lam_Q(2) =
    20 likewise, after lam_Q(1) = 4 divides). No tie. P pays 5 forever:
    at {P:a}, L = lcm(4, 5^(a-1)), lam_P(a+1) never divides. Q's
    opening door is exactly 2a (lam_Q(r) divides L iff
    ceil((r-1)/2) <= a-1 iff r <= 2a-1), priced out unboundedly. T and
    every norm-7..29 place hold costs at their norms or above,
    7..29 > 5, throughout (a cost is norm^r, r >= 1).
    Paid constant 5; support {P}; the trichotomy's CONSTANT row.
 C. BRANCH B (seat Q, exponent 1, L = 4). Step 2: Q at door 1 cost 5
    (lam_Q(2) = 20 does not divide 4); P at door 2 cost 25. No tie.
    State {Q:2}, L = 20. Step 3 is where the kinds' shared norm runs
    out: Q's next rung reads door 2, cost 25 (lam_Q(3) = 20 divides
    20, lam_Q(4) = 100 does not) -- the ramified rise -- and the menu
    UNDERCUTS it. T reads door 1 cost 8 against every invariant the
    ramified column alone builds (7 never divides lcm(4, 5^k)); an
    f = 1 place over p in {7, 13, 17, 19, 23} reads door 1 cost p
    whenever p - 1 fails to divide L -- all five fail at the undercut
    step's L = 20, while p = 11 is the exception (10 divides 20) and
    stays harmless forever. A degree-1 member over 7..23, once
    cheapest, holds door 1 from then on -- each rung past its first
    carries one more power of its own prime, which nothing else here
    supplies to the invariant -- and
    undercuts every rival thereafter (a rival's door can even rise off
    1: 12 divides the L = 60 a seated norm-7 place builds, so a
    norm-13 rival's door becomes 2). T is the one door-1 member that
    cannot hold: its second rung 14 divides any L carrying 4 and the 7
    its own seat supplies, so a T seat buys one move and strands.
    Three classes:
      CHEAP-7 (a root mod 7): the norm-7 place R pays 7 at step 3 and
        forever (lam_R(a) = lcm(6, 7^(a-1)); once seated, each next
        rung adds one factor 7 to its own L). T is never seated
        (8 > 7). Paid 5 5 7 7 7 ...; support {Q:2, R runaway}; the
        VOID LOSER is the deep place and the ramified winner strands.
      CHEAP-13/17/19/23 (no root mod 7, a root mod the class prime p):
        T pays 8 at step 3 (8 < 13 <= p); L picks up 7, but p - 1
        still fails to divide it, so R_p pays p at step 4 and forever.
        Paid 5 5 8 p p p ...; support {Q:2, T:1, R_p runaway}: THREE
        seatings, both tie members stranded beside an inert strand --
        the deep place lost the void, and so did every other seat.
      NOCHEAP (no root mod any of 7, 13, 17, 19, 23): T pays 8 at
        step 3, then Q RECLAIMS the runaway: at {Q:2k, T:1},
        L = lcm(4 * 5^k, 7), Q reads door 2 cost 25 while every rival
        is derived out -- T door >= 2 (14 and 28 divide L), P's
        opening door exactly k + 2, R11 door 2 cost 121, norm-29
        door 2 once L carries 7 (28 = 4*7), norm-27 door 1 cost
        27 > 25. Paid 5 5 8 25 25 ...; support {Q runaway, T:1}; the
        ramified transient risen to its own norm^2 plateau.
 D. WHAT THE TREE SAYS. The tie never recurs (both step-2 menus are
    tie-free), the branches never merge (branch A's support is {P},
    branch B never seats P -- its door only grows), and the two
    branches disagree in every observable: paid tail 5 against
    7/8-then-p/25, support {P} against Q-and-friends, deep place P
    against R or Q. Branch A runs the trichotomy's CONSTANT row and
    branch B its RISING row -- the same ring runs both, the break
    deciding. And in the CHEAP classes the runaway is a place the void
    REJECTED: winning the void does not appoint the deep place.
 E. WHY THE PURE PLATEAU CANNOT BE ESCAPED BY DESIGN. A specimen with
    branch B all-{Q} needs no place of door-1 cost below 25 in range,
    and T alone forbids that: the void tie forces 2 inert (a norm-2 or
    norm-4 place would undercut the tie itself at 4 or less), so T
    exists with lam_T(1) = 7, and 7 divides no lcm(4, 5^k). The
    undercut at 8 is FORCED by the same inertness the tie needs --
    NOCHEAP is the closest the family gets, and there the ramified
    place pays the 8-detour and then holds the runaway.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run. Hand specimens were
located pre-engine by a throwaway scratch search (the freeze predates
every engine file; the scratch found candidates and brute-verified the
ramified column, nothing else).

PR1 CONTROL (the walker against three published cells). The generic
    machinery here reprints: d = -7 (x^2+x+2, 2 split) -- void minimum
    4 at a two-member same-norm tie, both branches paid 4 4 2 2 2 ...,
    one seating each; d = -19 (x^2+x+5, 2 inert) -- one-member menu,
    constant 4, one seating; and the cross-kind cubic x^3+x^2+x+2
    (disc -83) -- three terminal behaviours, paid 4 4 2 2 2 ... /
    4 4 4 2 2 ... / constant 4, with the A2 = B2 merge. The controls
    exercise the same Field/menu/walker path with more modeled places
    (norms <= 30); nothing extra can fire below the published paids,
    every added place costing at least its norm >= 5 > 4. KILL: any
    control print off the published values -- the walker is wrong,
    nothing downstream is read.
PR2 THE COLUMNS, BRUTE-FORCED. Unramified cells on GR quotients as in
    the sibling rigs -- (2,1), (2,2), (2,3), (5,1), and every odd-norm
    cell the menus range over, each asserted against
    lcm(q-1, p^(a-1)) (with the p = 2 exceptions) on its brute window.
    THE RAMIFIED CELL on the concrete quotients above: both u = 1 and
    u = 2 print 4 20 20 100 100 500 to depth 6, asserted against
    lcm(4, 5^ceil((a-1)/2)) -- the closed form is read deeper only
    after this window passes. KILL: one cell off.
PR3 SPECIMENS EXIST, IN EVERY CLASS THE HAND-ATTACK NAMES. The box
    |a|,|b|,|c| <= 60 contains at least 9000 CHEAP and at least 20
    NOCHEAP defining polynomials with the full signature (2 and 3
    inert, 5 of type (1)(1^2) with 5 || disc, no other prime below 31
    dividing disc), including the four scratch-found hand specimens:
    x^3-6x^2-x+1 (disc 985, cheapest undercutter 7), x^3-4x^2-x-1
    (disc -335, cheapest 13), x^3-12x^2+41x+25 (disc -99095, NOCHEAP),
    x^3-3x^2-40x-5 (disc 258385, NOCHEAP). Distinct discriminants are
    counted and printed as the honest lower bound on distinct rings --
    polynomial counts are polynomial counts. KILL: a named specimen
    missing or misclassified, or either class count short.
PR4 THE VOID TIE. At every walked specimen: the void menu minimum is 5
    at exactly the two-member tie {P (e=1), Q (e=2)} -- one norm, two
    kinds -- with every other member at 7 or above. KILL: a third
    member, a different minimum, or a tie-free void.
PR5 THE TREE, PER CLASS. At every walked specimen the tie tree prints
    exactly two void branches, no later tie except same-norm undercutter
    ties (two or three roots mod the class prime; the sub-branches print
    identical signatures), and no merge -- branch supports disjoint.
    Branch A: paid constant 5 over 40 moves, support {P}, Q unseated
    with its opening door printed equal to 2 * exp(P) at the end.
    Branch B by class: CHEAP-7 paid 5 5 then constant 7, seatings
    {Q, R7}, T unseated, Q stranded at exponent 2; CHEAP-13/17/19/23
    paid 5 5 8 then constant p, seatings {Q, T, R_p} -- THREE -- T
    stranded at exponent 1, Q at 2;
    NOCHEAP paid 5 5 8 then constant 25, seatings {Q, T}, Q the
    runaway with T stranded and P's opening door printed equal to
    exp(Q)/2 + 2 at the end. KILL: any branch's paid, seating set,
    strand exponent, or door figure off its derived value -- each kills
    the specific hand step it contradicts, printed beside it.
PR6 THE DEEP PLACE SPLITS, AND IN THE CHEAP CLASSES IT LOST THE VOID.
    In every branch exactly one place moves over the last 10 of 40
    moves; branch A's is P; branch B's is the class runaway (R_p, or Q
    at NOCHEAP); the two branches' deep places DIFFER at every
    specimen. In the CHEAP classes the deep place is not a tie member:
    the void rejected it at 7-or-worse against 5, and it owns the
    limit anyway, both tie members ending stranded or unseated. KILL:
    a non-unique last-10 mover, or equal deep places across branches.
PR7 MONOTONE IN SITU. Across every trajectory this file records, an
    unseated place's cost never falls while it stays unseated (Lemma
    B's in-situ form). PRINTS: pairs checked, violations. KILL: one
    violation.

RUN RECORD. python prime/code/memwatch.py prime/code/explore_ram_tie.py
-- peak working set 31.1 MB, wall 10.8 s, every assertion green.
Findings entered post-run from the printed output (the two-write mint).

FINDINGS.

F1 CONTROL GREEN (PR1). The generic walker reprints all three published
   cells with the wider menu modeled: d = -7 prints the void minimum 4
   at the two-member same-norm tie, both branches paid 4 4 2 2 2 ...
   with one seating and deep exponent 42; d = -19 prints a one-member
   menu, constant 4, deep exponent 40; the cross-kind cubic (disc -83)
   prints its three terminal shapes -- 4 4 2 2 ... / 4 4 4 2 ... (both
   mixed orders, seatings 2) / constant 4 -- exactly as its own rig
   published them.
F2 THE COLUMNS (PR2). Unramified cells brute on GR quotients: (2,1) to
   depth 17, (2,2) to 8, (2,3) to 5 (7 14 28 56 112), (5,1) to 7
   (4 20 100 500 ...), and every odd-norm cell the menus range over on
   its window. THE RAMIFIED CELL: both uniformizer classes pi^2 = 5 and
   pi^2 = 10 print 4 20 20 100 100 500 to depth 6, matching
   lcm(4, 5^ceil((a-1)/2)) cell for cell -- the pair-repeat ramp is the
   same for both ramified quadratic extensions of Q_5.
F3 SPECIMENS (PR3). The box holds 9,478 defining polynomials with the
   full signature over 2,577 distinct |disc| -- 9,450 CHEAP (by
   cheapest undercutter: 6,118 at 7; 2,182 at 13; 800 at 17; 268 at
   19; 82 at 23) and 28 NOCHEAP over exactly 5 distinct discriminants
   (-27261335, -2623295, -99095, 258385, 26872465), all four hand
   specimens present in their predicted classes.
F4 THE VOID TIE (PR4). At every one of the 1,132 walked specimens (the
   box-30 subset plus every NOCHEAP plus the hand specimens): void
   minimum 5 at exactly the two-member tie {norm 5 f=1, norm 5 e=2} --
   one norm, two kinds -- everything else at 7 or above.
F5 THE TREE (PR5). Every walked branch matches its derived signature:
   branch A paid constant 5, support {P}, deep exponent 40, Q's opening
   door printed at exactly 2 * exp(P) = 80; branch B CHEAP-7 paid
   5 5 7 7 ... with R7 deep at exponent 38 and Q stranded at 2 (T never
   seated); CHEAP-13/17/19/23 paid 5 5 8 p p ... with THREE seatings --
   Q stranded at 2, T at 1, R_p deep at 37 -- and same-norm undercutter
   ties (up to three roots mod p) branching into identical signatures;
   NOCHEAP paid 5 5 8 25 25 ... with Q deep at exponent 76, T stranded
   at 1, and P's opening door printed at exactly exp(Q)/2 + 2 = 40. No
   branch ever seats P alongside Q: the tree has no merge, and the tie
   never recurs.
F6 THE DEEP PLACE (PR6) -- the headline. In every branch exactly one
   place moves over the last 10 of 40; branch A's is always P and
   branch B's is never P, so the greedy limit is MULTIVALUED at every
   one of the 1,132 voids -- and the break chooses between the
   trichotomy's ROWS: branch A runs the constant row, branch B rises
   off 5 in every class. In the CHEAP classes (9,450 of 9,478
   polynomials) the deep place is a VOID LOSER -- a degree-1 place over
   one of 7..23 that the tie rejected at 7-or-worse against 5 owns the
   limit while BOTH tie members end stranded or unseated: winning the
   void does not appoint the deep place.
F7 MONOTONE IN SITU (PR7). 954,324 unseated-cost pairs across every
   recorded trajectory (controls included), 0 violations.

TIERS. F1-F7 are rules in range (asserted on every printed cell and
branch); the hand-attack's branch arithmetic (A, B, C, E) is proved
from the three columns and holds for EVERY ring meeting the signature
(5 = P*Q^2 tame, 2 and 3 inert, no other prime below 31 dividing disc),
the columns themselves being the closed forms verified in F2 -- so the
bifurcation claim is a rule: proved mechanism, witnesses at 9,478
defining polynomials (at least 2,577 distinct rings by discriminant).
The forced-undercut lemma (E) is proved outright: the tie needs 2
inert, inertness prices T at 8 against lcm(4, 5^k), so no specimen's
ramified branch holds the tie price past move 2, and the pure
{Q}-plateau without the 8-detour does not exist in this family. What is NOT
claimed: wild ramification (e = p), ramified ties at other primes or
higher degree, seeded (non-void) cross-kind ties, or any statement
about the walked classes beyond the stated signature.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
from math import gcd
from functools import lru_cache

def lcm(a, b):
    return a * b // gcd(a, b)

# ---------------------------------------------------------------- polys mod p

def poly_trim(u):
    while len(u) > 1 and u[-1] == 0:
        u = u[:-1]
    return u

def poly_mod_p(f, p):
    return poly_trim([c % p for c in f])

def poly_eval_mod(f, x, m):
    acc = 0
    for c in reversed(f):
        acc = (acc * x + c) % m
    return acc

def roots_mod(f, p):
    return [x for x in range(p) if poly_eval_mod(f, x, p) == 0]

def factor_type_cubic(f, p):
    """For monic cubic f mod p: list of (root, multiplicity) for linear
    factors, plus the leftover degree (0, 2, or 3 for irreducible)."""
    rs = roots_mod(f, p)
    if not rs:
        return [], 3
    fp = [(i * f[i]) % p for i in range(1, len(f))]
    out = []
    tot = 0
    for r in rs:
        m = 1
        if poly_eval_mod(fp, r, p) == 0:
            fpp = [(i * fp[i]) % p for i in range(1, len(fp))]
            m = 3 if (p > 2 and poly_eval_mod(fpp, r, p) == 0) else 2
        out.append((r, m))
        tot += m
    assert tot <= 3, ("multiplicity bookkeeping", f, p, out)
    return out, 3 - tot

def cubic_disc(a, b, c):
    return 18 * a * b * c - 4 * a**3 * c + a * a * b * b - 4 * b**3 - 27 * c * c

def quad_disc(b, c):
    return b * b - 4 * c

def has_rational_root(f):
    c = f[0]
    if c == 0:
        return True
    divs = set()
    for t in range(1, abs(c) + 1):
        if c % t == 0:
            divs.add(t); divs.add(-t)
    return any(sum(co * r**i for i, co in enumerate(f)) == 0 for r in divs)

def is_prime(n):
    return n >= 2 and all(n % q for q in range(2, int(n ** 0.5) + 1))

def next_prime(p):
    n = p + 1
    while not is_prime(n):
        n += 1
    return n

# ------------------------------------------------- Galois ring GR(p^a, d)

IRRED = {  # a fixed monic irreducible of degree d mod p, low->high
    (2, 2): [1, 1, 1],
    (2, 3): [1, 1, 0, 1],
    (3, 2): [1, 0, 1],
    (3, 3): [1, 2, 0, 1],
    (5, 2): [2, 0, 1],
    (7, 2): [1, 0, 1],
}

def gr_mul(u, v, h, m):
    d = len(h) - 1
    prod = [0] * (2 * d - 1)
    for i, ui in enumerate(u):
        if ui:
            for j, vj in enumerate(v):
                prod[i + j] = (prod[i + j] + ui * vj) % m
    for i in range(len(prod) - 1, d - 1, -1):
        cc = prod[i]
        if cc:
            prod[i] = 0
            for j in range(d):
                prod[i - d + j] = (prod[i - d + j] - cc * h[j]) % m
    return tuple(prod[:d])

def gr_pow(u, e, h, m):
    d = len(h) - 1
    acc = tuple([1] + [0] * (d - 1))
    base = u
    while e:
        if e & 1:
            acc = gr_mul(acc, base, h, m)
        base = gr_mul(base, base, h, m)
        e >>= 1
    return acc

def _prime_factors(n):
    out = []
    dd = 2
    while dd * dd <= n:
        if n % dd == 0:
            out.append(dd)
            while n % dd == 0:
                n //= dd
        dd += 1
    if n > 1:
        out.append(n)
    return out

def brute_unit_exponent(p, d, a):
    m = p ** a
    if d == 1:
        h = [0, 1]
        elems = [(x,) for x in range(m)]
    else:
        h = IRRED[(p, d)]
        def vectors(k):
            if k == 0:
                yield ()
                return
            for rest in vectors(k - 1):
                for x in range(m):
                    yield rest + (x,)
        elems = list(vectors(d))
    one = tuple([1] + [0] * (d - 1))
    order = (p ** d - 1) * p ** (d * (a - 1))
    E = 1
    for u in elems:
        if all(c % p == 0 for c in u):
            continue
        if gr_pow(u, E, h, m) == one:
            continue
        o = order
        for q in _prime_factors(order):
            while o % q == 0 and gr_pow(u, o // q, h, m) == one:
                o //= q
        E = lcm(E, o)
    return E

def brute_ram_exponent(u_class, a):
    """Exponent of (O/Q^a)^* for O = Z_5[pi], pi^2 = 5*u_class (tame,
    e = 2, f = 1). Concrete quotient: a = 2b -> c0, c1 mod 5^b;
    a = 2b+1 -> c0 mod 5^(b+1), c1 mod 5^b."""
    if a % 2 == 0:
        m0 = m1 = 5 ** (a // 2)
    else:
        m0, m1 = 5 ** (a // 2 + 1), 5 ** (a // 2)
    def mul(x, y):
        c0 = (x[0] * y[0] + 5 * u_class * x[1] * y[1]) % m0
        c1 = (x[0] * y[1] + x[1] * y[0]) % m1 if m1 > 1 else 0
        return (c0, c1)
    one = (1 % m0, 0)
    def powr(x, e):
        acc = one
        base = x
        while e:
            if e & 1:
                acc = mul(acc, base)
            base = mul(base, base)
            e >>= 1
        return acc
    order = 4 * 5 ** (a - 1)
    E = 1
    for c0 in range(m0):
        if c0 % 5 == 0:
            continue
        for c1 in range(max(m1, 1)):
            uu = (c0, c1)
            if powr(uu, E) == one:
                continue
            o = order
            for q in (2, 5):
                while o % q == 0 and powr(uu, o // q) == one:
                    o //= q
            E = lcm(E, o)
    return E

# ------------------------------------------------------- columns (lambda)

def closed_form_lam_unram(p, d, a):
    q = p ** d
    if p == 2 and d == 1:
        if a == 1:
            return 1
        if a in (2, 3):
            return 2
        return 2 ** (a - 2)
    if p == 2:
        if a == 1:
            return q - 1
        return lcm(q - 1, 2 ** (a - 1))
    return lcm(q - 1, p ** (a - 1))

def closed_form_lam_ram5(a):
    # lcm(4, 5^ceil((a-1)/2)) -- the tame pair-repeat ramp
    return lcm(4, 5 ** (a // 2))

def brute_window(p, d, cap=200_000):
    a = 1
    while p ** ((a + 1) * d) <= cap:
        a += 1
    return max(a, 2)

_verified_unram = set()
_verified_ram = False

def verify_columns_unram(p, d):
    if (p, d) in _verified_unram:
        return
    w = brute_window(p, d)
    if p == 2 and d == 1:
        w = max(w, 14)
    brute = [brute_unit_exponent(p, d, a) for a in range(1, w + 1)]
    closed = [closed_form_lam_unram(p, d, a) for a in range(1, w + 1)]
    print(f"  column (p={p}, d={d}, norm {p**d}, unram) brute to depth {w}: "
          f"{brute}")
    assert brute == closed, (p, d, brute, closed)
    _verified_unram.add((p, d))

def verify_columns_ram():
    global _verified_ram
    if _verified_ram:
        return
    for u_class in (1, 2):
        brute = [brute_ram_exponent(u_class, a) for a in range(1, 7)]
        closed = [closed_form_lam_ram5(a) for a in range(1, 7)]
        print(f"  column (p=5, e=2, f=1, norm 5, ram, pi^2=5*{u_class}) "
              f"brute to depth 6: {brute}")
        assert brute == closed, (u_class, brute, closed)
    _verified_ram = True

@lru_cache(maxsize=None)
def lam(p, d, e, a):
    if e == 1:
        return closed_form_lam_unram(p, d, a)
    assert (p, d, e) == (5, 1, 2), "ramified column only derived for 5, e=2"
    return closed_form_lam_ram5(a)

# ------------------------------------------------------------------ fields

class Field:
    """Places of norm <= normcap. Unramified from factor_type_cubic off
    disc; the one permitted ramified prime is 5 with type (1)(1^2). A
    place is (norm, p, d, idx, e). Any prime below 31 dividing disc
    other than 5 is rejected at construction (the search guarantees it);
    the excluded-norm floor is what keeps the menu truncation sound."""

    def __init__(self, name, f, disc, normcap=30, ram_ok=False):
        self.name = name
        self.f = f
        self.disc = disc
        self.normcap = normcap
        self.places = []
        floor = 31  # every place over p >= 31 has norm >= 31
        deg = len(f) - 1
        p = 2
        while p <= normcap:
            if disc % p == 0:
                if ram_ok and p == 5:
                    lins, left = factor_type_cubic(f, p)
                    mults = sorted(m for r, m in lins)
                    assert mults == [1, 2] and left == 0, (
                        "5 not of type (1)(1^2)", lins, left)
                    self.places.append((5, 5, 1, 0, 1))   # P, unramified
                    self.places.append((5, 5, 1, 1, 2))   # Q, e = 2
                else:
                    assert not ram_ok, (
                        "unhandled ramified prime in menu range", p, name)
                    floor = min(floor, p)  # ramified place, norm >= p
            else:
                if deg == 2:
                    rs = roots_mod(f, p)
                    kinds = [1] * len(rs) if rs else [2]
                else:
                    lins, left = factor_type_cubic(f, p)
                    assert all(m == 1 for r, m in lins), (
                        "multiplicity off disc", p, name)
                    kinds = [1] * len(lins) + ([left] if left else [])
                for idx, dd in enumerate(kinds):
                    nrm = p ** dd
                    if nrm <= normcap:
                        self.places.append((nrm, p, dd, idx, 1))
                    else:
                        floor = min(floor, nrm)
            p = next_prime(p)
        self.excluded_floor = floor
        self.places.sort()

# ------------------------------------------------------------------ walker

def door_r(pl, e, L):
    nrm, p, d, idx, ram_e = pl
    r = 1
    while r <= 200:
        if L % lam(p, d, ram_e, e + r) != 0:
            return r
        r += 1
    raise AssertionError("door beyond 200")

def menu(field, state):
    L = 1
    for pl, e in state.items():
        nrm, p, d, idx, ram_e = pl
        L = lcm(L, lam(p, d, ram_e, e))
    out = []
    for pl in field.places:
        e = state.get(pl, 0)
        r = door_r(pl, e, L)
        out.append((pl[0] ** r, pl, r))
    out.sort(key=lambda t: (t[0], t[1]))
    return out, L

def walk_tree(field, moves=40, branch_levels=4):
    results = []

    def go(state, paid, seatings, label, step, mover_log, cost_log):
        if step == moves:
            m, L = menu(field, state)
            results.append((label, paid, seatings, dict(state), mover_log,
                            cost_log, {t[1]: t[2] for t in m}, L))
            return
        m, L = menu(field, state)
        best = m[0][0]
        tied = [t for t in m if t[0] == best]
        snapshot = {t[1]: t[0] for t in m if state.get(t[1], 0) == 0}
        branches = tied if (len(tied) > 1 and step < branch_levels) else [m[0]]
        for k, (cost, pl, r) in enumerate(branches):
            st = dict(state)
            fresh = pl not in st
            st[pl] = st.get(pl, 0) + r
            lb = label + (f".{'PQRS'[k]}{step+1}" if len(branches) > 1 else "")
            go(st, paid + [cost],
               seatings + ([(step + 1, pl, cost)] if fresh else []),
               lb, step + 1,
               mover_log + [pl], cost_log + [snapshot])

    go({}, [], [], "t", 0, [], [])
    return results

def monotone_check(traj):
    label, paid, seatings, state, movers, cost_log = traj[:6]
    pairs = 0
    bad = 0
    last = {}
    for snap in cost_log:
        for pl, c in snap.items():
            if pl in last:
                pairs += 1
                if c < last[pl]:
                    bad += 1
            last[pl] = c
    return pairs, bad

def kind_tag(pl):
    nrm, p, d, idx, e = pl
    return f"norm {nrm}" + (f" e={e}" if e > 1 else f" f={d}")

def describe(field, moves=40, verbose=True):
    if verbose:
        print(f"\n== {field.name}  (disc {field.disc}, menu "
              f"{[kind_tag(pl) for pl in field.places]}, "
              f"excluded-norm floor {field.excluded_floor})")
    for nrm, p, d, idx, e in field.places:
        if e == 1:
            verify_columns_unram(p, d)
        else:
            verify_columns_ram()
    m0, _ = menu(field, {})
    best = m0[0][0]
    tie = [t for t in m0 if t[0] == best]
    if verbose:
        print(f"  void menu minimum {best} at {len(tie)} member(s): "
              f"{[kind_tag(pl) for _, pl, _ in tie]}")
    trajs = walk_tree(field, moves)
    max_paid = 0
    all_pairs = all_bad = 0
    for traj in trajs:
        label, paid, seatings, state, movers, cost_log, doors, L = traj
        max_paid = max(max_paid, max(paid))
        pairs, bad = monotone_check(traj)
        all_pairs += pairs
        all_bad += bad
        if verbose:
            tail_movers = sorted(set(movers[-10:]))
            deep = sorted(state.items(), key=lambda kv: -kv[1])[0]
            print(f"  {label}: paid {paid[:6]}... tail {paid[-3:]}, "
                  f"seatings {[(s, kind_tag(pl)) for s, pl, c in seatings]}, "
                  f"last-10 movers {[kind_tag(pl) for pl in tail_movers]}, "
                  f"deep ({kind_tag(deep[0])}) at exponent {deep[1]}")
    assert max_paid < field.excluded_floor, (
        "truncation unsound", max_paid, field.excluded_floor)
    if verbose:
        print(f"  max paid {max_paid} < excluded-norm floor "
              f"{field.excluded_floor}; monotone pairs {all_pairs}, "
              f"violations {all_bad}")
    return trajs, (all_pairs, all_bad), (best, tie)

# --------------------------------------------------------- classification

CHEAP_PRIMES = (7, 13, 17, 19, 23)

def classify(f):
    """Cheapest undercutting prime for branch B, or None (NOCHEAP)."""
    for p in CHEAP_PRIMES:
        if roots_mod(f, p):
            return p
    return None

def assert_tree(field, trajs, cheapest, void_tie):
    """PR4/PR5/PR6 asserts for one ramified-tie specimen."""
    best, tie = void_tie
    assert best == 5 and len(tie) == 2, ("PR4 kill: void", best, tie)
    kinds = sorted((pl[0], pl[4]) for _, pl, _ in tie)
    assert kinds == [(5, 1), (5, 2)], ("PR4 kill: members", kinds)

    P = next(pl for _, pl, _ in tie if pl[4] == 1)
    Q = next(pl for _, pl, _ in tie if pl[4] == 2)
    T = next((pl for pl in field.places if pl[0] == 8), None)
    assert T is not None, "2 not inert?"

    a_br = [t for t in trajs if t[4][0] == P]
    b_br = [t for t in trajs if t[4][0] == Q]
    assert a_br and b_br and len(a_br) + len(b_br) == len(trajs)

    for label, paid, seatings, state, movers, cost_log, doors, L in a_br:
        assert set(paid) == {5}, ("PR5 kill: branch A paid", label, paid[:8])
        assert set(state) == {P}, ("PR5 kill: branch A support", label)
        assert doors[Q] == 2 * state[P], (
            "PR5 kill: Q opening door", label, doors[Q], state[P])
        tail = set(movers[-10:])
        assert tail == {P}, ("PR6 kill: A last-10", label)

    for label, paid, seatings, state, movers, cost_log, doors, L in b_br:
        assert P not in state, ("PR5 kill: merge", label)
        assert paid[:2] == [5, 5] and state[Q] >= 2, (
            "PR5 kill: branch B prefix", label, paid[:4])
        tail = set(movers[-10:])
        assert len(tail) == 1, ("PR6 kill: B last-10 not unique", label)
        deep = next(iter(tail))
        if cheapest == 7:
            assert paid[2] == 7 and set(paid[3:]) == {7}, (
                "PR5 kill: CHEAP-7 paid", label, paid[:6])
            assert deep[0] == 7 and state[Q] == 2 and T not in state, (
                "PR5 kill: CHEAP-7 shape", label)
            assert len(seatings) == 2, ("PR5 kill: CHEAP-7 seatings", label)
        elif cheapest is not None:
            assert paid[2] == 8 and paid[3] == cheapest, (
                "PR5 kill: CHEAP-p prefix", label, paid[:6])
            assert set(paid[4:]) == {cheapest}, (
                "PR5 kill: CHEAP-p tail", label, paid[-4:])
            assert deep[0] == cheapest and state[Q] == 2 and state[T] == 1, (
                "PR5 kill: CHEAP-p strands", label)
            assert len(seatings) == 3, ("PR5 kill: three seatings", label)
        else:
            assert paid[2] == 8 and set(paid[3:]) == {25}, (
                "PR5 kill: NOCHEAP paid", label, paid[:6])
            assert deep == Q and state[T] == 1, (
                "PR5 kill: NOCHEAP shape", label)
            assert doors[P] == state[Q] // 2 + 2, (
                "PR5 kill: P opening door", label, doors[P], state[Q])
            assert len(seatings) == 2, ("PR5 kill: NOCHEAP seatings", label)
        # deep places differ across the void break
        for _, _, _, sa, ma, _, _, _ in a_br:
            assert deep != next(iter(set(ma[-10:]))), (
                "PR6 kill: same deep place across branches", label)

# ------------------------------------------------------------------ search

def search_cubics(box):
    """Monic irreducible cubics with 2, 3 inert, 5 of type (1)(1^2),
    5 || disc, and no other prime below 31 dividing disc. Returns
    (a, b, c, disc, cheapest-or-None)."""
    found = []
    for a in range(-box, box + 1):
        for b in range(-box, box + 1):
            for c in range(-box, box + 1):
                if c % 2 == 0 or (a + b) % 2 == 0:
                    continue  # 2 inert iff c odd and a+b odd
                f = [c, b, a, 1]
                if roots_mod(f, 3):
                    continue  # cubic with no root mod 3 = irreducible
                disc = cubic_disc(a, b, c)
                if disc == 0 or disc % 5 != 0 or disc % 25 == 0:
                    continue
                ok = True
                for p in (7, 11, 13, 17, 19, 23, 29):
                    if disc % p == 0:
                        ok = False
                        break
                if not ok:
                    continue
                lins, left = factor_type_cubic(f, 5)
                mults = sorted(m for r, m in lins)
                if mults != [1, 2] or left != 0:
                    continue
                if has_rational_root(f):
                    continue
                found.append((a, b, c, disc, classify(f)))
    return found

# -------------------------------------------------------------------- main

def main():
    print("S1 CONTROL -- the walker against three published cells")
    ctrl_split = Field("Q(sqrt(-7)) via x^2+x+2", [2, 1, 1], quad_disc(1, 2))
    ctrl_inert = Field("Q(sqrt(-19)) via x^2+x+5", [5, 1, 1], quad_disc(1, 5))
    ts, _, _ = describe(ctrl_split)
    for traj in ts:
        label, paid, seatings = traj[0], traj[1], traj[2]
        assert paid[:5] == [4, 4, 2, 2, 2] and set(paid[5:]) == {2}, paid
        assert len(seatings) == 1, seatings
    ti, _, _ = describe(ctrl_inert)
    for traj in ti:
        label, paid, seatings = traj[0], traj[1], traj[2]
        assert set(paid) == {4}, paid
        assert len(seatings) == 1, seatings
    ctrl_cubic = Field("cross-kind cubic x^3+x^2+x+2", [2, 1, 1, 1],
                       cubic_disc(1, 1, 2))
    tc, _, _ = describe(ctrl_cubic)
    shapes = set()
    for traj in tc:
        label, paid = traj[0], traj[1]
        shapes.add((tuple(paid[:4]), paid[-1]))
    assert shapes == {((4, 4, 2, 2), 2), ((4, 4, 4, 2), 2),
                      ((4, 4, 4, 4), 4)}, shapes
    print("  control: both quadratic cells and the cross-kind tree "
          "reprint their published signatures")

    print("\nS2 THE COLUMNS -- brute vs closed form; the ramified cell "
          "on both uniformizer classes")
    verify_columns_unram(2, 3)
    verify_columns_unram(5, 1)
    verify_columns_ram()

    print("\nS3 SPECIMEN SEARCH -- the box |a|,|b|,|c| <= 60")
    found = search_cubics(60)
    cheap = [t for t in found if t[4] is not None]
    nocheap = [t for t in found if t[4] is None]
    discs_all = sorted(set(abs(d) for _, _, _, d, _ in found))
    discs_nc = sorted(set(d for _, _, _, d, _ in nocheap))
    hist = {}
    for *_, ch in cheap:
        hist[ch] = hist.get(ch, 0) + 1
    print(f"  {len(found)} defining polynomials with the full signature: "
          f"{len(cheap)} CHEAP {dict(sorted(hist.items()))}, "
          f"{len(nocheap)} NOCHEAP")
    print(f"  distinct |disc| overall {len(discs_all)}; NOCHEAP discs "
          f"{discs_nc}")
    for a, b, c, disc, ch in nocheap:
        print(f"    NOCHEAP x^3{a:+d}x^2{b:+d}x{c:+d}, disc {disc}")
    assert len(cheap) >= 9000 and len(nocheap) >= 20, (
        "PR3 kill: class counts", len(cheap), len(nocheap))
    for hand, want in [((-6, -1, 1, 985), 7), ((-4, -1, -1, -335), 13),
                       ((-12, 41, 25, -99095), None),
                       ((-3, -40, -5, 258385), None)]:
        got = [ch for a, b, c, d, ch in found if (a, b, c, d) == hand]
        assert got == [want], ("PR3 kill: hand specimen", hand, got)

    print("\nS4 THE TIE TREE -- full prints at the four hand specimens "
          "and every NOCHEAP; assert-only sweep over the box-30 CHEAP "
          "subset (the wider box's cheap classes are the same derivation; "
          "the sweep bound is named in the scope)")
    total_pairs = total_bad = 0
    hand_keys = {(-6, -1, 1), (-4, -1, -1), (-12, 41, 25), (-3, -40, -5)}
    printed = 0
    swept = 0
    for a, b, c, disc, ch in found:
        in_box30 = max(abs(a), abs(b), abs(c)) <= 30
        verbose = (a, b, c) in hand_keys or ch is None
        if not (verbose or in_box30):
            continue
        fld = Field(f"cubic x^3{a:+d}x^2{b:+d}x{c:+d}", [c, b, a, 1],
                    disc, ram_ok=True)
        trajs, (pairs, bad), void_tie = describe(fld, verbose=verbose)
        total_pairs += pairs
        total_bad += bad
        assert_tree(fld, trajs, ch, void_tie)
        printed += verbose
        swept += 1
    print(f"  {swept} specimens walked and asserted ({printed} with full "
          f"prints)")

    print("\nS5 MONOTONE IN SITU across every recorded trajectory")
    print(f"  pairs {total_pairs}, violations {total_bad}")
    assert total_bad == 0, "PR7 kill"

    print("\nS6 SUMMARY -- one norm, two kinds: what the break buys")
    print("  branch A (unramified member): constant 5, support {P} -- "
          "the trichotomy's CONSTANT row")
    print("  branch B (ramified member): rises off 5 in every class; "
          "runaway = cheapest of (R_p at door-1 p, Q at 25), with the "
          "forced inert-2 undercut at 8 where no R_p exists")

if __name__ == "__main__":
    main()
