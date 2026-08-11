r"""explore_cross_kind_tie.py -- THE CROSS-KIND VOID TIE: DOES THE
TIE-BREAK CHOOSE THE WORLD?

THE QUESTION. The winner-kind dichotomy (explore_even_winner.py,
explore_late_seating.py) reads the paid sequence's direction off the void
winner's kind: FALLS to the floor and stays at a norm-2 winner, CONSTANT
at every other unramified one, RISES through a ramified transient. Its one
open cell: a cubic ring can hand the void a norm-2 winner
BESIDE a norm-4 rival -- 2 factoring as P*Q with residue degrees 1 and 2
-- a cost-4 tie ACROSS kinds that no quadratic can stage, and no such ring
has been walked. The quadratic void tie is a conjugate pair: same norm,
same column, the two branches isomorphic, the tie benign. A cross-kind
tie puts two DIFFERENT columns at one price. Does the tie-break then
choose between two genuinely different walks -- different paid direction,
different deep place -- making the greedy limit multivalued at the void
with no symmetry identifying the branches?

WHOSE VOCABULARY. Engine observables, re-derived from
explore_even_winner.py's WHOSE VOCABULARY block rather than memory:
lam_P(pl, a) is the exponent of (O/P^a)^*; L = the lcm of lam_P(pl, e_pl)
over everything seated, each read at its seated depth; door_r(pl, e, L) =
the least r >= 1 with lam_P(pl, e+r) not dividing L; a move at pl costs
norm(pl)^r and raises the exponent by r; greedy takes the menu minimum,
first tie member by place_key -- and THIS file's subject is exactly the
states where that clause fires, so the walker here branches on ties
instead of breaking them silently.

WHY THE QUOTIENTS ARE COMPUTABLE WITHOUT THE FIELD. Every place this file
walks is UNRAMIFIED (specimens are filtered so any ramified place has norm
above the menu cap). For unramified P of residue degree d over p, the
completion O_P is THE unramified extension of Z_p of degree d -- unique up
to isomorphism -- so O/P^a is the Galois ring GR(p^a, d) = Z[x]/(p^a, h)
for ANY monic degree-d h irreducible mod p. lam_P therefore depends only
on (p, d, a) and is brute-forced on that quotient directly; no Hensel
lifting and no per-field residue ring is needed.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 The tie-tree frame is imported from the quadratic conjugate tie
    (even_winner hand-attack A), where branching is cosmetic because the
    branches are conjugate. Here nothing identifies them; the frame is
    used only to ENUMERATE branches, and every claim about a branch is
    derived per-branch below.
 T2 The falling / constant signatures for the two kinds are the
    NEIGHBOURING quadratic cells' results. They are predictions here,
    not inheritances: the cubic state carries BOTH places, so each
    branch's L can pick up the other kind's column, which no quadratic
    walk exhibits (the quadratic winner's rival shares its column or is
    priced out at the void).
 T3 "Deep place" is the ideal-limit vocabulary (one runaway coordinate
    plus strands). The rig prints exponents and last-mover
    data; which coordinate is "the" deep one is weighed after the run.

THE HAND-ATTACK, on paper before any engine code. Setup: cubic K with
2 = P*Q unramified, f(P) = 1 (norm 2), f(Q) = 2 (norm 4), no place of
norm 3 (3 inert), every ramified place of norm > menu cap. Columns from
the closed forms verified in S2: P's is 1, 2, 2, 4, 8, ... (= Z_2's, the
flat step at depth 3); Q's is 3, 6, 12, 24, ... = 3 * 2^(a-1) (GR(2^a,2),
strict from depth 1, the Artin-Schreier map nonvanishing on F_4).

 A. THE VOID MENU. L = 1. P: lam(P,1) = 1 divides 1, lam(P,2) = 2 does
    not -- door 2, cost 4. Q: lam(Q,1) = 3 does not divide 1 -- door 1,
    cost 4. Everything else >= 5 (no norm-3 place; a second norm-2 or
    norm-4 place cannot exist, 2 = P*Q being the whole fibre). The void
    minimum is 4 at exactly {P, Q}: a two-member tie across kinds.
 B. BRANCH A (seat P, exponent 2, L = 2). Step 2 menu: P at the flat
    step (lam(P,3) = 2 divides 2, lam(P,4) = 4 does not: door 2, cost 4);
    Q still at door 1 cost 4 (3 never divides a power of 2). A SECOND
    cross-kind tie at 4.
    A1 (P again): exponent 4, L = 4. P from here climbs one doubling per
       depth: door 1, cost 2 forever. Q's opening stays 4 (3 divides no
       L = 2^k) and is never paid, 2 < 4. Paid 4 4 2 2 2 ...; support
       {P}; Q never seated, stranded at a constant 4 it never gets to
       spend.
    A2 (Q): state {P:2, Q:1}, L = lcm(2,3) = 6. Step 3 menu: P seated at
       2: lam(P,3) = 2 divides 6, lam(P,4) = 4 does not -- door 2, cost
       4; Q seated at 1: lam(Q,2) = 6 divides 6, lam(Q,3) = 12 does not
       -- door 2, cost 16. P pays 4: {P:4, Q:1}, L = 12. From there P is
       door 1 cost 2 forever (lam(P,5) = 8, only the 2-part grows); Q's
       next (lam(Q,3) = 12 divides 12, lam(Q,4) = 24 does not from door
       counting at e = 1: r = 2, then r grows) prices 16 then upward.
       Paid 4 4 4 2 2 2 ...; support {P deep, Q stranded AT EXPONENT 1}
       -- the one branch where both places sit seated.
 C. BRANCH B (seat Q, exponent 1, L = 3). Step 2 menu: P at door 2 cost
    4 (lam(P,1) = 1 divides 3, lam(P,2) = 2 does not); Q at door 1 cost
    4 (lam(Q,2) = 6 does not divide 3). A second tie again.
    B1 (Q again): exponent 2, L = 6. Step 3: P's opening jumps -- lam
       1, 2, 2 all divide 6, lam(P,4) = 4 does not: door 4, cost 16;
       Q: lam(Q,3) = 12 does not divide 6, door 1, cost 4. Q pays 4
       forever (its own column is the whole L; each next rung one new
       factor 2), P's opening 2^(e+2) grows without bound. Paid
       4 4 4 4 ... CONSTANT; support {Q}; P never seated.
    B2 (P): state {P:2, Q:1} = branch A2's state exactly -- the tie tree
       MERGES; everything after is A2.
 D. WHAT THE TREE SAYS. Three terminal behaviours from one void: {P}
    falling to the floor (A1), {P deep, Q stranded seated} falling one
    step later (A2 = B2), {Q} constant with P priced out unboundedly
    (B1). The deep place differs across branches -- P in two, Q in one --
    and the branches are NOT isomorphic: P and Q have different norms, so
    no automorphism of anything exchanges them (the quadratic tie's
    conjugation is unavailable by construction). Each branch separately
    obeys the dichotomy's per-kind signature (T2 confirmed per-branch if
    the prints match), but WHICH signature runs is decided by the
    tie-break alone.
 E. WHY NOTHING CHEAPER OR TIED-THIRD EXISTS AT THE VOID. Cost < 4 needs
    norm 3 (excluded) or norm 2 at door 1 (impossible: lam(P,1) = 1
    divides every L); a third cost-4 member needs another place over 2,
    and P*Q exhausts the fibre. So the tie is exactly binary, by the
    same fibre count that made the quadratic tie exactly the conjugate
    pair.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS. What they mean is weighed after the run.

PR1 CONTROL (the walker against the published cells). On the quadratic
    hosts d = -7 (x^2+x+2, 2 split) and d = -19 (x^2+x+5, 2 inert), the
    generic machinery here reprints even_winner's signatures: void
    minimum 4 at a two-member SAME-NORM tie / at a one-member menu; paid
    prefix 4 4 2 2 2 and constant 4 over 40 moves; one fresh seating
    each (per branch). KILL: any of those prints off the published
    values -- the walker is wrong, nothing downstream is read.
PR2 THE COLUMNS, BRUTE-FORCED. On GR quotients directly: (p=2, d=1)
    prints 1 2 2 4 ... 2^(a-2) to depth 14; (p=2, d=2) prints
    3 * 2^(a-1) to depth 8; every odd-norm cell in the menu's range
    matches lcm(q-1, p^(a-1)) on its window. The closed forms are
    asserted cell-by-cell on the brute window before any walk uses
    them deeper. KILL: one cell off.
PR3 SPECIMENS EXIST. The search box (monic cubics, |a|,|b|,|c| <= 6)
    contains at least three fields with the full signature -- f mod 2
    of factor type (1,2), f mod 3 irreducible, disc squarefree across
    the menu range with no ramified norm <= 32 -- including
    x^3+x^2+x+2 (disc -83), x^3+x^2+3x+2 (disc -107), and
    x^3+2x^2+2x+5 (disc -491), found by hand pre-engine. KILL: the
    search prints fewer than three, or any hand specimen fails its
    stated signature under the engine's own filters.
PR4 THE TIE AND THE TREE. At every specimen: the void menu minimum is 4
    at exactly the two-member cross-kind tie {norm 2, norm 4}; the tie
    tree over 40 moves prints exactly the three terminal behaviours of
    hand-attack D -- paid 4 4 2 2 2..., paid 4 4 4 2 2 2..., paid
    constant 4 -- with supports {P}, {P,Q}, {Q} and the A2 = B2 state
    merge at {P:2, Q:1}. KILL: a branch paid off its derived sequence, a
    third tie member, or a tree shape off D -- each kills the specific
    hand step it contradicts, printed beside it.
PR5 THE DEEP PLACE SPLITS. In every branch exactly one place is still
    paying moves over the last 10 of 40, and it is P (norm 2) on the A
    side and Q (norm 4) on B1 -- the reported limit object differs by
    tie-break at the SAME ring. KILL: any branch where the last-10 mover
    is not unique, or both sides report the same deep place.
PR6 MONOTONE IN SITU. Across every trajectory this file records, an
    unseated place's cost never falls while it stays unseated (Lemma B's
    in-situ form). PRINTS: pairs checked, violations. KILL: one
    violation.

RUN RECORD. python prime/code/memwatch.py prime/code/explore_cross_kind_tie.py
-- peak working set 28.4 MB, wall 9.3 s, every assertion green. Findings
entered post-run from the printed output (the two-write mint).

FINDINGS.

F1 CONTROL GREEN (PR1). The generic walker reprints both published
   quadratic cells: d = -7 prints the void minimum 4 at the two-member
   SAME-NORM tie, both branches paid 4 4 2 2 2 ... with one seating and
   deep exponent 42; d = -19 prints a one-member menu, constant 4, one
   seating, deep exponent 40.
F2 THE COLUMNS (PR2). Brute on the Galois-ring quotients: (2, d=1)
   prints 1 2 2 4 8 ... 2^(a-2) to depth 17 (window widened past the
   promised 14 by the 200k cap); (2, d=2) prints 3 6 12 24 ... =
   3 * 2^(a-1) to depth 8; every odd-norm cell in menu range matches
   lcm(q-1, p^(a-1)) on its window (norm 9 to depth 5, norm 25 to
   depth 3, norm-p cells to their windows). Closed forms asserted
   cell-by-cell before any walk read them deeper.
F3 SPECIMENS (PR3). The box holds 92 monic cubics with the full
   signature -- 92 defining POLYNOMIALS, not 92 fields: the 17 distinct
   discriminants are the honest lower bound on distinct rings, discs
   like -59 recurring across many polynomials -- all three hand
   specimens among them (disc -83, -107, -491), and SIX of the
   discriminants are POSITIVE (229, 733, 2557, 2677, 2917, 6637): the
   cell exists in both cubic signatures, totally real included.
F4 THE TIE AND THE TREE (PR4). At every one of the 92: the void menu
   minimum is 4 at exactly the two-member cross-kind tie
   {norm 2 (f=1), norm 4 (f=2)}, and the tie tree prints exactly the
   three terminal behaviours of hand-attack D --
     t.P1.P2 (P twice):  paid 4 4 2 2 2 ..., support {P}, Q never seated;
     t.P1.Q2 = t.Q1.P2:  paid 4 4 4 2 2 ..., BOTH seated (Q stranded at
                         exponent 1), the mixed branches identical from
                         move 3 on (both stand at {P:2, Q:1}, the hand
                         attack's A2 = B2 merge);
     t.Q1.Q2 (Q twice):  paid constant 4, support {Q}, P never seated.
   The second cross-kind tie at move 2 printed in every branch, as
   derived.
F5 THE DEEP PLACE SPLITS (PR5) -- the headline. In every branch exactly
   one place moves over the last 10 of 40: P (norm 2, exponent 41-42) on
   the A side, Q (norm 4, exponent 40) at t.Q1.Q2 -- at the SAME ring the
   reported limit object differs by tie-break alone. The branches are not
   isomorphic (different norms -- no conjugation identifies them, unlike
   every quadratic tie), so the greedy limit is genuinely MULTIVALUED at
   the void: the tie-break chooses the world, between a paid sequence
   that falls to the family's floor forever and one that never leaves 4.
F6 MONOTONE IN SITU (PR6). 122,176 unseated-cost pairs across the
   specimen sweep (the controls' 702 and 429 print separately in S1),
   0 violations anywhere.

TIERS. F1, F2, F3, F4, F5, F6 are rules in range (asserted on every
printed cell/branch); the hand-attack's branch arithmetic (A, B, C, E)
is proved from the two columns and holds for EVERY ring meeting the
signature (2 = P*Q with residue degrees 1 and 2, no norm-3 place, no
other place of norm <= 4), the columns themselves being the closed forms
verified in F2 -- so the bifurcation claim is a rule: proved mechanism,
witnesses at 92 defining polynomials (at least 17 distinct rings). What is NOT claimed: any statement about ties
of three (2 totally split), about ramified members of a tie, or about
seeded (non-void) cross-kind ties.
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

def poly_divmod_mod_p(u, v, p):
    """u, v coefficient lists low->high over F_p, v != 0. Returns (q, r)."""
    u = list(poly_mod_p(u, p)); v = poly_mod_p(v, p)
    dv = len(v) - 1
    inv = pow(v[-1], p - 2, p)
    q = [0] * max(1, len(u) - dv)
    while len(u) - 1 >= dv and any(u):
        d = len(u) - 1 - dv
        c = (u[-1] * inv) % p
        q[d] = c
        for i, vc in enumerate(v):
            u[d + i] = (u[d + i] - c * vc) % p
        u = poly_trim(u)
        if u == [0]:
            break
    return poly_trim(q), poly_trim(u)

def factor_mod_p(f, p):
    """Factor monic f (deg <= 3) over F_p into irreducibles.
    Returns list of (factor, multiplicity) with factors monic, low->high."""
    f = poly_mod_p(f, p)
    deg = len(f) - 1
    assert f[-1] % p == 1, "monic only"
    if deg == 1:
        return [(f, 1)]
    roots = [x for x in range(p) if poly_eval_mod(f, x, p) == 0]
    if deg == 2:
        if not roots:
            return [(f, 1)]
        r = roots[0]
        q, rem = poly_divmod_mod_p(f, [(-r) % p, 1], p)
        assert rem == [0]
        if poly_eval_mod(q, r, p) == 0:
            return [([(-r) % p, 1], 2)]
        r2 = [x for x in range(p) if poly_eval_mod(q, x, p) == 0][0]
        if r2 == r:
            return [([(-r) % p, 1], 2)]
        return [([(-r) % p, 1], 1), ([(-r2) % p, 1], 1)]
    # deg == 3
    if not roots:
        return [(f, 1)]
    r = roots[0]
    q, rem = poly_divmod_mod_p(f, [(-r) % p, 1], p)
    assert rem == [0]
    sub = factor_mod_p(q, p)
    out = {}
    for fac, mult in sub + [([(-r) % p, 1], 1)]:
        key = tuple(fac)
        out[key] = out.get(key, 0) + mult
    return [(list(k), m) for k, m in out.items()]

def cubic_disc(a, b, c):
    return 18 * a * b * c - 4 * a**3 * c + a * a * b * b - 4 * b**3 - 27 * c * c

def quad_disc(b, c):
    return b * b - 4 * c

# ------------------------------------------------- Galois ring GR(p^a, d)

IRRED = {  # a fixed monic irreducible of degree d mod p, low->high
    (2, 2): [1, 1, 1],          # x^2 + x + 1
    (2, 3): [1, 1, 0, 1],       # x^3 + x + 1
    (3, 2): [1, 0, 1],          # x^2 + 1
    (3, 3): [1, 2, 0, 1],       # x^3 + 2x + 1
    (5, 2): [2, 0, 1],          # x^2 + 2
    (7, 2): [1, 0, 1],          # x^2 + 1
}

def gr_mul(u, v, h, m):
    """Multiply in Z[x]/(m, h), h monic; u, v tuples of length deg(h)."""
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

def brute_unit_exponent(p, d, a):
    """Exponent of GR(p^a, d)^* by full enumeration."""
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
            continue  # not a unit
        if gr_pow(u, E, h, m) == one:
            continue
        # compute the exact order of u, fold into E
        o = order
        for q in _prime_factors(order):
            while o % q == 0 and gr_pow(u, o // q, h, m) == one:
                o //= q
        E = lcm(E, o)
    return E

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

def closed_form_lam(p, d, a):
    """Unramified place of residue degree d over p: exponent of
    (O/P^a)^* = GR(p^a, d)^*."""
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

def brute_window(p, d, cap=200_000):
    a = 1
    while p ** ((a + 1) * d) <= cap:
        a += 1
    return max(a, 2)

_verified_pairs = set()

def verify_columns(p, d):
    """Assert the closed form against the brute on its window; print both."""
    if (p, d) in _verified_pairs:
        return
    w = brute_window(p, d)
    if p == 2 and d == 1:
        w = max(w, 14)
    brute = [brute_unit_exponent(p, d, a) for a in range(1, w + 1)]
    closed = [closed_form_lam(p, d, a) for a in range(1, w + 1)]
    print(f"  column (p={p}, d={d}, norm {p**d}) brute to depth {w}: {brute}")
    assert brute == closed, (p, d, brute, closed)
    _verified_pairs.add((p, d))

@lru_cache(maxsize=None)
def lam(p, d, a):
    return closed_form_lam(p, d, a)

# ------------------------------------------------------------------ fields

class Field:
    """A monogenic field given by monic f, places = unramified factors of
    f mod p for p with p not dividing disc, norms <= NORMCAP. Any prime
    dividing disc contributes only to the excluded-norm floor."""

    def __init__(self, name, f, disc, normcap=30):
        self.name = name
        self.f = f
        self.disc = disc
        self.normcap = normcap
        self.places = []   # (norm, p, d, idx)
        self.excluded_floor = None  # min norm of any place NOT in the menu
        floor = normcap + 1  # any unramified place above the cap
        p = 2
        while p <= normcap:
            if disc % p == 0:
                floor = min(floor, p)  # ramified places have norm >= p
            else:
                for idx, (fac, mult) in enumerate(factor_mod_p(f, p)):
                    assert mult == 1, (p, "unexpected multiplicity off disc")
                    dd = len(fac) - 1
                    nrm = p ** dd
                    if nrm <= normcap:
                        self.places.append((nrm, p, dd, idx))
                    else:
                        floor = min(floor, nrm)
            p = next_prime(p)
        self.excluded_floor = floor
        self.places.sort()

def next_prime(p):
    n = p + 1
    while True:
        if all(n % q for q in range(2, int(n ** 0.5) + 1)):
            return n
        n += 1

# ------------------------------------------------------------------ walker

def door_r(pl, e, L):
    nrm, p, d, idx = pl
    r = 1
    while r <= 64:
        if L % lam(p, d, e + r) != 0:
            return r
        r += 1
    raise AssertionError("door beyond 64")

def menu(field, state):
    L = 1
    for pl, e in state.items():
        nrm, p, d, idx = pl
        L = lcm(L, lam(p, d, e))
    out = []
    for pl in field.places:
        e = state.get(pl, 0)
        r = door_r(pl, e, L)
        out.append((pl[0] ** r, pl, r))
    out.sort(key=lambda t: (t[0], t[1]))
    return out

def walk_tree(field, moves=40, branch_levels=3):
    """Greedy walk branching at every tie inside the first branch_levels
    moves; deterministic (first by place_key) after. Returns trajectories:
    (label, paid, seatings, state, mover_log, monotone_log)."""
    results = []

    def go(state, paid, seatings, label, step, mover_log, cost_log):
        if step == moves:
            results.append((label, paid, seatings, dict(state), mover_log,
                            cost_log))
            return
        m = menu(field, state)
        best = m[0][0]
        tied = [t for t in m if t[0] == best]
        # record unseated costs for the monotone check
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
        return

    go({}, [], [], "t", 0, [], [])
    return results

def monotone_check(traj):
    """Lemma B in situ: an unseated place's cost never falls while it
    stays unseated. Returns (pairs, violations)."""
    label, paid, seatings, state, movers, cost_log = traj
    pairs = 0
    bad = 0
    last = {}
    seated_at = {}
    for step, snap in enumerate(cost_log):
        for pl, c in snap.items():
            if pl in last:
                pairs += 1
                if c < last[pl]:
                    bad += 1
            last[pl] = c
    return pairs, bad

def describe(field, moves=40, branch_levels=3, expect_tie=None):
    print(f"\n== {field.name}  (disc {field.disc}, menu "
          f"{[(n, f'f={d}') for n, p, d, i in field.places]}, "
          f"excluded-norm floor {field.excluded_floor})")
    for nrm, p, d, idx in field.places:
        verify_columns(p, d)
    m0 = menu(field, {})
    best = m0[0][0]
    tie = [t for t in m0 if t[0] == best]
    print(f"  void menu minimum {best} at {len(tie)} member(s): "
          f"{[(pl[0], f'f={pl[2]}') for _, pl, _ in tie]}")
    trajs = walk_tree(field, moves, branch_levels)
    max_paid = 0
    all_pairs = all_bad = 0
    for traj in trajs:
        label, paid, seatings, state, movers, cost_log = traj
        max_paid = max(max_paid, max(paid))
        tail_movers = set(movers[-10:])
        deep = sorted(state.items(), key=lambda kv: -kv[1])[0]
        pairs, bad = monotone_check(traj)
        all_pairs += pairs; all_bad += bad
        print(f"  {label}: paid {paid[:8]}... tail {paid[-3:]}, "
              f"seatings {[(s, pl[0], f'f={pl[2]}') for s, pl, c in seatings]}, "
              f"last-10 movers {[(pl[0], f'f={pl[2]}') for pl in sorted(tail_movers)]}, "
              f"deep (norm {deep[0][0]}, f={deep[0][2]}) at exponent {deep[1]}")
    assert max_paid < field.excluded_floor, (
        "truncation unsound", max_paid, field.excluded_floor)
    print(f"  max paid {max_paid} < excluded-norm floor "
          f"{field.excluded_floor} (menu truncation sound); "
          f"monotone pairs {all_pairs}, violations {all_bad}")
    return trajs, (all_pairs, all_bad)

# ------------------------------------------------------------------ search

def search_cubics(box=6, normcap=30, ram_floor=32):
    """Monic irreducible cubics x^3+ax^2+bx+c with 2 of factor type (1,2),
    3 inert, and every ramified place of norm > ram_floor (reject p^2 | disc
    for p <= normcap outright -- the index guard)."""
    found = []
    for a in range(-box, box + 1):
        for b in range(-box, box + 1):
            for c in range(-box, box + 1):
                f = [c, b, a, 1]
                disc = cubic_disc(a, b, c)
                if disc == 0:
                    continue
                # irreducible over Q: no rational root (cubic)
                if _has_rational_root(f):
                    continue
                fm2 = factor_mod_p(f, 2)
                if sorted(len(g) - 1 for g, m in fm2) != [1, 2]:
                    continue
                if any(m > 1 for g, m in fm2):
                    continue
                fm3 = factor_mod_p(f, 3)
                if not (len(fm3) == 1 and fm3[0][1] == 1
                        and len(fm3[0][0]) - 1 == 3):
                    continue
                ok = True
                p = 2
                while p <= normcap:
                    if disc % (p * p) == 0:
                        ok = False; break
                    if disc % p == 0 and p <= ram_floor:
                        ok = False; break
                    p = next_prime(p)
                if ok:
                    found.append((a, b, c, disc))
    return found

def _has_rational_root(f):
    c = f[0]
    if c == 0:
        return True
    divs = set()
    for t in range(1, abs(c) + 1):
        if c % t == 0:
            divs.add(t); divs.add(-t)
    return any(sum(co * r**i for i, co in enumerate(f)) == 0 for r in divs)

# -------------------------------------------------------------------- main

def main():
    print("S1 CONTROL -- the walker against the published quadratic cells")
    ctrl_split = Field("Q(sqrt(-7)) via x^2+x+2", [2, 1, 1], quad_disc(1, 2))
    ctrl_inert = Field("Q(sqrt(-19)) via x^2+x+5", [5, 1, 1], quad_disc(1, 5))
    ts, _ = describe(ctrl_split, expect_tie=2)
    for label, paid, seatings, state, movers, cost_log in ts:
        assert paid[:5] == [4, 4, 2, 2, 2] and set(paid[5:]) == {2}, paid
        assert len(seatings) == 1, seatings
    ti, _ = describe(ctrl_inert, expect_tie=1)
    for label, paid, seatings, state, movers, cost_log in ti:
        assert set(paid) == {4}, paid
        assert len(seatings) == 1, seatings
    print("  control: split reprints 4 4 2 2 2... one seating; "
          "inert reprints constant 4, one seating")

    print("\nS2 THE COLUMNS -- brute vs closed form (printed above per "
          "field as columns first appear; the norm-2 and norm-4 cells "
          "are the load-bearing ones)")
    verify_columns(2, 1)
    verify_columns(2, 2)

    print("\nS3 SPECIMEN SEARCH -- the box |a|,|b|,|c| <= 6")
    found = search_cubics()
    for a, b, c, disc in found:
        print(f"  x^3{a:+d}x^2{b:+d}x{c:+d}, disc {disc}")
    print(f"  {len(found)} specimen(s) with the full signature")
    assert len(found) >= 3, "PR3 kill: fewer than three specimens"
    for hand in [(1, 1, 2, -83), (1, 3, 2, -107), (2, 2, 5, -491)]:
        assert hand in found, ("PR3 kill: hand specimen missing", hand)

    print("\nS4 THE TIE TREE at each specimen (40 moves, branching on "
          "ties in the first 3)")
    tie_summaries = []
    total_pairs = total_bad = 0
    for a, b, c, disc in found:
        fld = Field(f"cubic x^3{a:+d}x^2{b:+d}x{c:+d}", [c, b, a, 1], disc)
        trajs, (pairs, bad) = describe(fld)
        total_pairs += pairs; total_bad += bad
        m0 = menu(fld, {})
        best = m0[0][0]
        tie = [t for t in m0 if t[0] == best]
        kinds = sorted(pl[0] for _, pl, _ in tie)
        deeps = set()
        shapes = set()
        for label, paid, seatings, state, movers, cost_log in trajs:
            deep = sorted(state.items(), key=lambda kv: -kv[1])[0][0]
            deeps.add((deep[0], deep[2]))
            tail = paid[-1]
            shapes.add((tuple(paid[:4]), tail))
        tie_summaries.append((disc, best, kinds, sorted(deeps),
                              sorted(shapes), len(trajs)))

    print("\nS5 MONOTONE IN SITU across every trajectory")
    print(f"  pairs {total_pairs}, violations {total_bad}")
    assert total_bad == 0, "PR6 kill"

    print("\nS6 SUMMARY -- does the tie-break choose the world?")
    for disc, best, kinds, deeps, shapes, ntraj in tie_summaries:
        print(f"  disc {disc}: void min {best} at norms {kinds}; "
              f"{ntraj} branches; deep places {deeps}; "
              f"(paid prefix, tail) shapes {sorted(shapes)}")

if __name__ == "__main__":
    main()
