"""explore_genome_fibre.py — THE GENOME FIBRE: what the genome forgets,
measured; and the slack law that turns "the functor is unfaithful" into an
arithmetic identity.

THE QUESTION. The growth world's genome map G(N) = oddpart(lambda(N)) is a
functor to the window-spectrum poset (spectrum(D) = {p : oddpart(p-1) | D},
monotone — explore_conjecture_bridge.py). On the intervention layer it is NOT
faithful: the same push applied to two states of the SAME genome lands on
different genomes, because a push reads v_l of the STATE while the genome
forgets it (the compounding, explore_phoenix_bill.py). That has been a
WITNESS — two numbers, 1 and 3, answering a push of 3^2 with genomes 3 and 9 —
and never a law. This run asks the question the witness leaves open: what
exactly is the FIBRE of G, and does the fibre's structure COMPUTE the
compounding rate, or merely accompany it? A second question rides along: the
reachable genomes have been filed as a WIDE SUBCATEGORY (all objects, only the
traversable arrows), which is only informative if the subcategory is PROPER.
Decide that too.

CONVENTIONS. State N a positive integer. Genome G(N) = oddpart(lambda(N)).
For an odd prime l, c_l = v_l(N) and d_l = v_l(G(N)). A PUSH is multiplication
of the state by one prime; a push of l^e is e unit pushes, since exponents add
(checked against the engine's own lambda in the control section, not assumed).
lambda's 2-part has oddpart 1, so the genome sees only the odd part of N.

THE HAND DERIVATION (fixed on paper before this file existed).

  L1 THE GENOME FORMULA. lambda is an lcm over prime powers and
     v_l(lcm) = max v_l, with lambda(q^a) = q^(a-1)(q-1) for odd q, so
        d_l = max( 0, c_l - 1, max{ v_l(p-1) : p | N odd prime, p != l } ).
     One slot for l's own depth, one for what the OTHER primes' predecessors
     carry.

  L2 THE SLACK. Define  delta_l(N) = d_l - c_l + 1.  L1 forces d_l >= c_l - 1,
     so delta_l >= 0 always, and delta_l = 0 exactly when l sits at its own
     depth with no other prime of N carrying l as deep.

  L3 THE PUSH LAW AT l. A push N -> N*l raises c_l by one and leaves the
     other-primes term alone, so the new d_l is max(d_l, c_l). Hence
       delta_l >= 1  =>  genome UNCHANGED at l, delta_l falls by one (a
                         TRANSPARENT push);
       delta_l  = 0  =>  d_l rises by exactly one, delta_l stays 0.
     delta_l is a COUNTDOWN — the number of free pushes of l remaining before
     l starts writing into the genome — and composing e of them gives
        Delta d_l = max(0, e - delta_l).

  L4 THE CREDIT LAW. A FIRST-TIME push of l (c_l = 0) also enters oddpart(l-1)
     into the lcm, so every other prime r gets d_r -> max(d_r, v_r(l-1)) with
     c_r untouched: delta_r RISES by the same amount. Pushing a new prime
     CREDITS slack at the primes dividing l-1; pushing an old prime SPENDS one
     credit at itself. The growth world's genome runs a credit economy.

  L5 THE COMPOUNDING IS THE SLACK. Two states of the same genome with slacks
     delta and delta' answer the same push l^e with genome exponents differing
     by |max(0,e-delta) - max(0,e-delta')|. The known witness is the case
     delta = 1 vs delta = 0 at e = 2.

  L6 THE FIBRE BOX. c_l <= d_l + 1, so over a genome D the fibre coordinate at
     l is delta_l in {0, 1, ..., v_l(D)+1}: exactly v_l(D)+2 push-response
     classes, and the maximum compounding gain anywhere in the fibre over D is
     v_l(D)+1. If this holds, the fibre coordinate does not merely relate to
     the compounding rate — it IS the rate.

  L7 THE ATOMS. G(N) = lcm over q^a || N of A(q,a) = q^(a-1) * oddpart(q-1):
     a genome is exactly an LCM OF ATOMS. Occupancy of the TOP cell
     (delta_l = d_l + 1, i.e. l absent from the state) needs D's l-part
     supplied by some other prime, so the top cell is a PROTH DISJUNCTION over
     the divisors m | D with v_l(m) = v_l(D): occupied iff some such m has
     m*2^a + 1 prime. Bridge B3 reappearing as fibre occupancy rather than as
     an edit. It also gives a realizability test: D is a genome iff every
     prime power l^j || D is covered either by deepening l (needs
     oddpart(l-1) | D) or by such an m.

PREDICTIONS F1-F8 (frozen before any engine code; findings enter by a separate
post-run edit copying printed output).
  F1 the genome formula L1 holds for every state in the sweep and every odd
     prime tested.
  F2 delta_l >= 0 always; Delta d_l = max(0, e - delta_l) with no exception;
     the countdown falls to 0 and pins there.
  F3 a first-time push of l credits delta_r by v_r(l-1) at every r | l-1; a
     REPEAT push of the same l credits nothing.
  F4 the known witness falls out of F2 as the case delta = 1 vs delta = 0, and
     the largest genome-exponent spread across a fibre at l is v_l(D)+1.
  F5 the fibre box of L6 is EXACT: no state anywhere in the sweep lands outside
     {0..v_l(D)+1}, and the top and bottom cells are both attained for the
     small genomes.
  F6 top-cell occupancy agrees with the Proth disjunction of L7 on every
     genome tested.
  F7 realizability is CHEAP: no non-realizable odd D below the search bound.
     The Sierpinski obstruction blocks an exact ONE-ATOM edit, not an object,
     because a composite genome can be assembled from several atoms.
  F8 the transitive reachability subcategory is IMPROPER — every divisibility
     arrow between realizable genomes is traversable, so the informative
     structure is the ONE-PUSH generating graph, which IS proper. The intended
     specimen: the Sierpinski number 78557 as a genome that no single push can
     reach (provably, by its covering set) but two pushes can.

KILL-SHAPES, as observables. F2 dies if the rig prints one triple (N, l, e)
with Delta d_l != max(0, e - delta_l). F8 dies if the rig prints a realizable
pair D | D' with no push word from any state of genome D to genome D'. What
either would MEAN is weighed after the run, not before.

POSITIVE CONTROL. Before any F-verdict is read, the rig reproduces the filed
witness from its own lambda — 1 and 3 share genome 1, and a push of 3^2 sends
them to genomes 3 and 9 — and checks that a push of l^e equals e unit pushes.

FINDINGS.

  CONTROL PASSED FIRST. States 1 and 3 both carry genome 1; a push of 3^2
  sends them to genomes 3 and 9. A push of l^e equals e unit pushes over the
  whole test battery, so the filed witness's l^e vocabulary and the growth
  machine's unit-push vocabulary agree, as flagged.

  1. THE SLACK LAW (theorem; the run is a control, not the evidence). L1-L3
     have a complete elementary proof for every state and every odd prime:
     lambda is an lcm over prime powers, v_l of an lcm is the max, and
     lambda(q^a) = q^(a-1)(q-1) contributes a-1 at q = l, v_l(q-1) at odd
     q != l, and nothing at q = 2. Hence d_l = max(0, c_l - 1, max_(q|N, q!=l)
     v_l(q-1)); hence delta_l = d_l - c_l + 1 >= 0; hence a push of l^e moves
     the genome's l-EXPONENT by exactly Delta d_l = max(0, e - delta_l) (the
     genome's other primes move too, by the credit law of finding 3). The
     sweep found 0
     mismatches with the formula over 3000 states, 0 negative slacks, 0
     violations of the push law over 40000 (state, l, e) triples, and 0
     violations of the countdown delta -> max(0, delta-1).

  2. THE COMPOUNDING IS THE FIBRE COORDINATE (theorem). delta is exactly what
     the genome forgets and exactly what the push reads, so the answer to the
     question this run was minted for is YES, and sharper than asked: the
     fibre's structure does not merely COMPUTE the compounding rate, the fibre
     coordinate IS the rate. The filed witness is the single case delta = 1
     versus delta = 0 at e = 2 (exponents 1 and 2, genomes 3 and 9) -- one cell
     of a lattice, not a curiosity. Over a genome D the coordinate at l runs in
     {0, ..., v_l(D)+1}: exactly v_l(D)+2 push-response classes, and the
     largest genome-exponent spread obtainable across a fibre is v_l(D)+1. The
     sweep put 0 states outside the box across 2345 (genome, l) boxes and
     filled 363 of them completely. The response spread is MEASURED by pushing
     each state and reading the move, not inferred from the slack range (which
     would only restate the box): 0 fibres exceed the cap, and 111 full boxes
     attain it exactly -- e.g. D = 9 at l = 3, slacks 0,1,2,3, spread 3.

  3. THE CREDIT ECONOMY (theorem). A FIRST push of l also enters oddpart(l-1)
     into the lcm, raising d_r without touching c_r: it CREDITS delta_r at
     every r | l-1. A repeat push of l credits nothing. So the growth world
     runs a ledger -- pushing a new prime buys transparent pushes at the primes
     dividing its predecessor, pushing an old prime spends one at itself, and
     the genome only moves when the account is empty. 0 violations, with 261
     actual credits observed in the sweep -- and every one of them minted by a
     push that MOVED the genome at r, never by a transparent one (0
     counterexamples). The two sides of the ledger run OPPOSITE ways: opening
     a window is what buys the free steps elsewhere. This is the same absorb-by-lcm
     accounting the transparency criterion runs on a fixed schedule: a push
     with e <= delta is a TRANSPARENT step, one with e > delta forces a window.

  4. GENOMES ARE LCMS OF ATOMS (theorem), so realizability reduces. With
     A(q,a) = q^(a-1)*oddpart(q-1), G(N) = lcm over q^a || N of A(q,a). A
     prime power l^j || D is therefore coverable either by DEEPENING l (free,
     but only if oddpart(l-1) | D) or by IMPORTING a prime whose predecessor
     carries l^j -- some m | D with v_l(m) = j and m*2^a + 1 prime. The top
     fibre cell (delta_l = v_l(D)+1, l absent from the state) is exactly that
     import clause: of 810 top cells checked, 161 are non-vacuous (l | D --
     the rest are free, since a prime absent from D never has to be hosted),
     and there are 0 disagreements with the Proth disjunction.

  5. F7 MISSED, AND THE MISS IS THE RESULT. The prediction asked for a count
     of non-realizable D. There is no such count to print: realizability is a
     Proth predicate, and "no witness below my bound" is not "no witness". The
     first instrument said 5 of the odd D <= 999 were non-realizable -- 47,
     383, 587, 631, 881 -- and every one of them was the bound talking. Given
     three honest tiers (witness / covering certificate / open) the census
     reads 495 realizable, 0 PROVABLY blocked, 5 open at a <= 64; reopening
     the five at a <= 1200 resolves four of them (47 at a = 583, 587 at 227,
     631 at 144, 881 at 1027) and leaves 383 open. That 47 is the straggler is
     a consistency check, not a coincidence: 583 is the same outlier the DNA
     price list records (explore_phoenix_bill.py). SCOPE: the large witnesses
     are strong probable primes, not certified primes -- the deterministic
     Miller-Rabin base set holds only below ~3.3e24, and 47*2^583+1 is far
     past it. TIER: the realizability criterion is a proved REDUCTION; the
     predicate it reduces to is open.

  6. THE WIDE-SUBCATEGORY CLAIM WAS THE WRONG SHAPE (F8 confirmed). If D | D'
     are both realizable, push the primes of a realization of D' on top of a
     realization of D: every atom then divides D', and the lcm is exactly D'.
     So EVERY divisibility arrow between realizable genomes is traversable and
     the reachability subcategory is IMPROPER -- it is the whole category
     (0 of the 136 divisibility arrows among the 60 smallest observed genomes
     failed). The carving is real only on the GENERATING arrows, and there it
     is exact: a single push of q sends the empty state to genome
     oddpart(q-1), so the one-push arrows out of the empty state ARE the Proth
     predicate, arrow by arrow. Even that carving is invisible across the
     whole observed range, not merely at its small end -- ALL 468 observed
     genomes are one-push reachable, every one realized by its own prime. The first provably absent arrow is the Sierpinski number
     78557 = 17 * 4621: its covering set {3,5,7,13,19,37,73} (period 36,
     re-derived here by a general cover finder rather than quoted) kills
     78557*2^a+1 for every a, so NO single push reaches that genome -- while
     two do, via 137 and 18927617, landing on state 2593083529. A genome
     unreachable in one move and reachable in two is the honest content of
     "prime existence carves the arrows".

  READING. The structural half of this question is finished and unblocked: the
  slack law, the box, the credit ledger and the atom decomposition are proved
  outright, and they turn a two-number witness into arithmetic. The number
  theory re-enters at exactly two places, both named above -- which fibre cells
  are OCCUPIED, and which single pushes EXIST -- and both are the same Proth
  question wearing different clothes.

RUN RECORD. 23 checks, 23 passed, 0 failed. Pure integer arithmetic, no
third-party imports, well under the memory ceiling; single process, 1s
wall-clock.
"""

import sys
from math import lcm


PASS = 0
FAIL = 0


def ok(cond, msg):
    global PASS, FAIL
    if cond:
        PASS += 1
    else:
        FAIL += 1
        print(f"  FAIL: {msg}")


# -- number-theory primitives (thin re-decl; mirror explore_conjecture_bridge.py) --

def is_primeZ(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def oddpart(n):
    while n % 2 == 0:
        n //= 2
    return n


def factorint(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def lam_pp(q, a):
    if q == 2:
        return 1 if a == 1 else (2 if a == 2 else 1 << (a - 2))
    return q ** (a - 1) * (q - 1)


def lam_of_factors(f):
    """Carmichael lambda from a factorization dict."""
    L = 1
    for q, a in f.items():
        L = lcm(L, lam_pp(q, a))
    return L


def lam(n):
    return lam_of_factors(factorint(n))


def genome(n):
    return oddpart(lam(n))


def genome_of_factors(f):
    return oddpart(lam_of_factors(f))


def v_p(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def divisors(n):
    ds = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            ds.append(d)
            if d != n // d:
                ds.append(n // d)
        d += 1
    return sorted(ds)


ODD_PRIMES = [p for p in range(3, 200, 2) if is_primeZ(p)]


# ── the derived quantities ────────────────────────────────────────────────

def d_of(f, l):
    """v_l of the genome, from a factorization dict."""
    return v_p(genome_of_factors(f), l)


def slack(f, l):
    """delta_l = d_l - c_l + 1."""
    return d_of(f, l) - f.get(l, 0) + 1


def formula_d(f, l):
    """L1: the hand formula for v_l(genome), for cross-checking."""
    best = 0
    c = f.get(l, 0)
    if c >= 1:
        best = max(best, c - 1)
    for p in f:
        if p == 2 or p == l:
            continue
        best = max(best, v_p(p - 1, l))
    return best


def pushed(f, l, e):
    g = dict(f)
    g[l] = g.get(l, 0) + e
    return g


# ── CONTROL: reproduce the filed witness before reading any verdict ───────

def section_control():
    print("-- POSITIVE CONTROL (read before any F-verdict) " + "-" * 22)
    g1, g3 = genome(1), genome(3)
    ok(g1 == 1 and g3 == 1, f"control: genomes of 1 and 3 are {g1}, {g3}, not 1, 1")
    p1, p3 = genome(1 * 9), genome(3 * 9)
    ok(p1 == 3 and p3 == 9, f"control: push 3^2 gives {p1}, {p3}, not 3, 9")
    print(f"    states 1, 3 -> genome {g1}, {g3};  after a push of 3^2 -> {p1}, {p3}")
    # a push of l^e equals e unit pushes (the transplant flag on the filed datum)
    same = True
    for N in (1, 3, 7, 12, 45, 100, 231):
        for l in (3, 5, 7):
            for e in (1, 2, 3, 4):
                step = N
                for _ in range(e):
                    step *= l
                if genome(step) != genome(N * l ** e):
                    same = False
    ok(same, "control: a push of l^e is NOT e unit pushes")
    print("    a push of l^e == e unit pushes (exponents add): confirmed")
    print()


# ── F1: the genome formula ────────────────────────────────────────────────

def section_F1(bound):
    print(f"-- F1  THE GENOME FORMULA (states 1..{bound}) " + "-" * 25)
    bad = []
    for N in range(1, bound + 1):
        f = factorint(N)
        tested = set(ODD_PRIMES[:12]) | {p for p in f if p != 2}
        for l in tested:
            if d_of(f, l) != formula_d(f, l):
                bad.append((N, l))
    ok(not bad, f"F1: formula L1 fails at {bad[:5]}")
    print(f"    v_l(genome) = max(0, c_l - 1, max_(p|N, p!=l) v_l(p-1))")
    print(f"    checked over {bound} states x (first 12 odd primes + N's own): "
          f"{len(bad)} mismatches")
    print()


# ── F2: the slack law and the push law ────────────────────────────────────

def section_F2(bound, ls, emax):
    print(f"-- F2  THE SLACK LAW (states 1..{bound}, l in {ls}, e<={emax}) " + "-" * 6)
    neg = []
    bad = []
    countdown_bad = []
    for N in range(1, bound + 1):
        f = factorint(N)
        for l in ls:
            dl = d_of(f, l)
            delta = dl - f.get(l, 0) + 1
            if delta < 0:
                neg.append((N, l, delta))
            for e in range(1, emax + 1):
                got = d_of(pushed(f, l, e), l) - dl
                want = max(0, e - delta)
                if got != want:
                    bad.append((N, l, e, got, want))
            # the countdown: delta falls by one per push until it pins at 0
            cur = delta
            g = f
            for _ in range(emax):
                g = pushed(g, l, 1)
                nxt = slack(g, l)
                if nxt != max(0, cur - 1):
                    countdown_bad.append((N, l, cur, nxt))
                cur = nxt
    ok(not neg, f"F2: delta < 0 at {neg[:5]}")
    ok(not bad, f"F2: push law fails at {bad[:5]}")
    ok(not countdown_bad, f"F2: countdown fails at {countdown_bad[:5]}")
    print(f"    delta_l = v_l(genome) - v_l(N) + 1 >= 0: {len(neg)} violations")
    print(f"    Delta v_l(genome) = max(0, e - delta_l): {len(bad)} violations "
          f"over {bound * len(ls) * emax} (state, l, e) triples")
    print(f"    countdown delta -> max(0, delta-1) per push: {len(countdown_bad)} violations")
    print()


# ── F3: the credit law ────────────────────────────────────────────────────

def section_F3(bound, ls):
    print(f"-- F3  THE CREDIT LAW (first push credits, repeat push does not) " + "-" * 3)
    bad_new = []
    bad_rep = []
    backwards = []
    credited = 0
    for N in range(1, bound + 1):
        f = factorint(N)
        for l in ls:
            for r in ODD_PRIMES[:8]:
                if r == l:
                    continue
                # a push of l moves d_r to max(d_r, v_r(l-1)) and leaves c_r,
                # so delta_r moves by exactly that much -- and only when l is NEW
                before = slack(f, r)
                after = slack(pushed(f, l, 1), r)
                dr = d_of(f, r)
                if l in f:
                    if after != before:
                        bad_rep.append((N, l, r, before, after))
                else:
                    want = before + (max(dr, v_p(l - 1, r)) - dr)
                    if after != want:
                        bad_new.append((N, l, r, after, want))
                    elif after > before:
                        credited += 1
                        # WHICH SIDE mints? A credit appears iff v_r(l-1)
                        # exceeds d_r, i.e. iff the genome MOVES at r -- so
                        # credit is minted by non-transparent pushes and spent
                        # by transparent ones. The two sides run opposite ways.
                        if d_of(pushed(f, l, 1), r) == dr:
                            backwards.append((N, l, r))
    ok(not bad_new, f"F3: first-push credit wrong at {bad_new[:5]}")
    ok(not bad_rep, f"F3: repeat push changed a foreign slack at {bad_rep[:5]}")
    ok(not backwards, f"F3: credit minted by a TRANSPARENT push at {backwards[:5]}")
    print(f"    first push of l: delta_r += max(d_r, v_r(l-1)) - d_r  "
          f"({len(bad_new)} violations, {credited} actual credits observed)")
    print(f"    repeat push of l: delta_r unchanged for r != l "
          f"({len(bad_rep)} violations)")
    print(f"    every credit was minted by a push that MOVED the genome at r, "
          f"never by a transparent one ({len(backwards)} counterexamples)")
    print()


# ── F4: the witness as a corollary, and the fibre spread ──────────────────

def section_F4(bound, ls):
    print("-- F4  THE COMPOUNDING IS THE SLACK " + "-" * 34)
    # the filed witness, re-derived from the law rather than observed
    d1, d3 = slack({}, 3), slack({3: 1}, 3)
    ok((d1, d3) == (1, 0), f"F4: witness slacks are {(d1, d3)}, not (1, 0)")
    ok((max(0, 2 - d1), max(0, 2 - d3)) == (1, 2),
       "F4: the law does not reproduce genomes 3 and 9")
    print(f"    the filed witness IS delta=1 vs delta=0 at e=2: "
          f"exponents {max(0, 2 - d1)} vs {max(0, 2 - d3)} -> genomes 3 and 9")
    # The RESPONSE spread across a fibre, measured by actually pushing -- not
    # the slack spread, which F5 already bounds and which would make this
    # check a restatement of that one. The response to l^e is the genome's
    # l-exponent MOVE, so it must be pushed and read, and it depends on e.
    fibres = {}
    for N in range(1, bound + 1):
        fibres.setdefault(genome(N), []).append(N)
    rows, bad, tight = [], [], 0
    for D in sorted(fibres)[:40]:
        for l in ls:
            cap = v_p(D, l) + 1
            deltas = sorted({slack(factorint(N), l) for N in fibres[D]})
            best = 0
            for e in range(1, cap + 3):
                moves = set()
                for N in fibres[D]:
                    f = factorint(N)
                    moves.add(d_of(pushed(f, l, e), l) - d_of(f, l))
                spread = max(moves) - min(moves)
                if spread > cap:
                    bad.append((D, l, e, spread, cap))
                best = max(best, spread)
            if best == cap and deltas == list(range(cap + 1)):
                tight += 1          # a full box attains the bound exactly
            if l == 3 and best:
                rows.append((D, best, cap, deltas))
    ok(not bad, f"F4: measured response spread exceeds v_l(D)+1 at {bad[:5]}")
    print(f"    genome-exponent response spread across a fibre, measured by "
          f"pushing: {len(bad)} exceed v_l(D)+1; {tight} full boxes attain it")
    for D, best, cap, ds in rows[:8]:
        print(f"      D={D:<6} l=3  slacks {ds}  max response spread "
              f"{best} (cap {cap})")
    print()


# ── F5: the fibre box ─────────────────────────────────────────────────────

def section_F5(bound, ls):
    print(f"-- F5  THE FIBRE BOX  delta_l in 0..v_l(D)+1 " + "-" * 25)
    fibres = {}
    for N in range(1, bound + 1):
        fibres.setdefault(genome(N), []).append(N)
    outside = []
    occupancy = []
    for D in sorted(fibres):
        for l in ls:
            cap = v_p(D, l) + 1
            deltas = {slack(factorint(N), l) for N in fibres[D]}
            for x in deltas:
                if not (0 <= x <= cap):
                    outside.append((D, l, x, cap))
            occupancy.append((D, l, len(deltas), cap + 1))
    ok(not outside, f"F5: states outside the box at {outside[:5]}")
    full = sum(1 for _, _, seen, cells in occupancy if seen == cells)
    print(f"    {len(occupancy)} (genome, l) boxes checked, {len(outside)} states "
          f"outside; {full} boxes fully occupied within the sweep")
    for D in sorted(fibres)[:6]:
        cells = [(l, sorted({slack(factorint(N), l) for N in fibres[D]}),
                  v_p(D, l) + 1) for l in ls[:3]]
        print(f"      D={D:<6} " + "  ".join(
            f"l={l}: {ds} (cap {cap})" for l, ds, cap in cells))
    print()


# ── F6: the top cell is a Proth disjunction ───────────────────────────────

def proth_witness(m, amax=64):
    """least a >= 0 with m*2^a + 1 prime, or None if none below the bound.
    None means NOT FOUND, never NOT EXISTS -- that distinction is the whole
    content of the three-tier verdict below."""
    for a in range(amax + 1):
        if is_primeZ(m * (1 << a) + 1):
            return a
    return None


def covering_set(m, periods=(2, 4, 6, 12, 24, 36, 48, 60, 72), plim=500):
    """A finite set of primes making m*2^a + 1 composite for EVERY a >= 1, or
    None. A cover found here is a PROOF (a Sierpinski certificate); its absence
    proves nothing. Greedy over residues mod a period L with ord_2(p) | L."""
    for L in periods:
        cands = []
        for p in (q for q in range(3, plim, 2) if is_primeZ(q)):
            if m % p == 0 or pow(2, L, p) != 1:
                continue
            res = {a for a in range(L) if (m * pow(2, a, p) + 1) % p == 0}
            if res:
                cands.append((p, res))
        need, chosen = set(range(L)), []
        while need and cands:
            p, res = max(cands, key=lambda pr: len(pr[1] & need))
            if not res & need:
                break
            chosen.append(p)
            need -= res
            cands = [c for c in cands if c[0] != p]
        if need:
            continue
        # a cover is only a proof if each hit is a PROPER divisor
        if all(any(v % p == 0 and v > p for p in chosen)
               for v in (m * (1 << a) + 1 for a in range(1, L + 1))):
            return L, sorted(chosen)
    return None


def proth_tier(m, amax):
    """'yes' (witness), 'blocked' (covering certificate), or 'open'."""
    if proth_witness(m, amax) is not None:
        return "yes"
    return "blocked" if covering_set(m) else "open"


def top_cell_predicted(D, l, amax=64):
    """L7: the top cell at l is occupied iff some m | D with v_l(m) = v_l(D)
    is oddpart(p-1) for a prime p. Three-valued, for the same reason."""
    j = v_p(D, l)
    if j == 0:
        return "yes"  # l absent from D: c_l = 0 is free
    tiers = [proth_tier(m, amax) for m in divisors(D) if v_p(m, l) == j]
    if "yes" in tiers:
        return "yes"
    return "blocked" if all(t == "blocked" for t in tiers) else "open"


def section_F6(bound, ls):
    print("-- F6  TOP-CELL OCCUPANCY = A PROTH DISJUNCTION " + "-" * 22)
    fibres = {}
    for N in range(1, bound + 1):
        fibres.setdefault(genome(N), []).append(N)
    bad = []
    checked = biting = 0
    for D in sorted(fibres):
        if D > 400:
            continue
        for l in ls:
            cap = v_p(D, l) + 1
            seen = any(slack(factorint(N), l) == cap for N in fibres[D])
            pred = top_cell_predicted(D, l)
            checked += 1
            # l absent from D makes the top cell free and the test VACUOUS:
            # count separately, or the headline flatters itself
            if v_p(D, l) > 0:
                biting += 1
            if seen and pred == "blocked":
                bad.append((D, l, "occupied but provably blocked"))
            # the "witnessed => seen" direction only bites when the realizing
            # prime m*2^a+1 is small enough to BE a state in the sweep
            if pred == "yes" and not seen and v_p(D, l) > 0:
                j = v_p(D, l)
                reach = [m * (1 << proth_witness(m)) + 1 for m in divisors(D)
                         if v_p(m, l) == j and proth_witness(m) is not None]
                if reach and min(reach) <= bound:
                    bad.append((D, l, "witnessed in-sweep but top cell empty"))
    ok(not bad, f"F6: disagreement at {bad[:6]}")
    print(f"    {checked} (genome, l) top cells, of which {biting} are "
          f"NON-VACUOUS (l | D); {len(bad)} disagreements with the Proth "
          f"disjunction")
    for D, l in ((3, 3), (9, 3), (7, 7), (5, 5), (15, 3)):
        wit = [(m, proth_witness(m)) for m in divisors(D)
               if v_p(m, l) == v_p(D, l)]
        print(f"      D={D:<4} l={l}: witnesses (m, least a) {wit}")
    print()


# ── F7: realizability ─────────────────────────────────────────────────────

def realizable(D, amax=64):
    """L7: D is a genome iff every prime power l^j || D is covered by an atom
    dividing D -- either deepening l (needs oddpart(l-1) | D) or some
    m | D with v_l(m) = j and m*2^a + 1 prime. THREE-VALUED: the second branch
    is a Proth predicate, which is not decidable at this desk."""
    if D == 1:
        return "yes"
    verdict = "yes"
    for l, j in factorint(D).items():
        if D % oddpart(l - 1) == 0:
            continue                       # deepening l covers l^j outright
        tiers = [proth_tier(m, amax) for m in divisors(D) if v_p(m, l) == j]
        if "yes" in tiers:
            continue
        if all(t == "blocked" for t in tiers):
            return "blocked"               # this prime power cannot be covered
        verdict = "open"
    return verdict


def section_F7(bound, dbound, amax, deep):
    print(f"-- F7  REALIZABILITY (odd D <= {dbound}) " + "-" * 30)
    seen = set()
    for N in range(1, bound + 1):
        seen.add(genome(N))
    tiers = {}
    for D in range(1, dbound + 1, 2):
        tiers.setdefault(realizable(D, amax), []).append(D)
    blocked, opens = tiers.get("blocked", []), tiers.get("open", [])
    ok(not [D for D in blocked if D in seen],
       f"F7: an OBSERVED genome declared provably unrealizable")
    print(f"    atoms A(q,a) = q^(a-1)*oddpart(q-1); a genome is an lcm of atoms")
    print(f"    at Proth bound a<={amax}: {len(tiers.get('yes', []))} realizable, "
          f"{len(blocked)} provably blocked, {len(opens)} OPEN {opens[:10]}")
    # the open band is a search-bound artifact, not an obstruction: reopen it
    resolved, still = [], []
    for D in opens:
        # only the divisors that can COVER an uncovered prime power count --
        # m must carry l to the full depth, so m = 1 is never a witness
        cands = set()
        for l, j in factorint(D).items():
            if D % oddpart(l - 1) == 0:
                continue
            cands |= {m for m in divisors(D) if v_p(m, l) == j}
        w = min((a for a in (proth_witness(m, deep) for m in sorted(cands))
                 if a is not None), default=None)
        (resolved if w is not None else still).append((D, w))
    print(f"    reopened at a<={deep}: {len(resolved)} resolved "
          f"{[(D, a) for D, a in resolved]}, {len(still)} still open "
          f"{[D for D, _ in still]}")
    ok(not blocked, f"F7 predicted none, but {blocked[:5]} carry covering certificates")
    print(f"    (states 1..{bound} realize {len(seen)} distinct genomes)")
    print()


# ── F8: the reachability subcategory ──────────────────────────────────────

SIERPINSKI = 78557
COVER = (3, 5, 7, 13, 19, 37, 73)


def section_F8(bound):
    print("-- F8  REACHABILITY: WHICH ARROWS ACTUALLY SURVIVE " + "-" * 19)
    # (a) transitive reachability over the observed genomes: is every
    #     divisibility arrow traversable?
    states = {}
    for N in range(1, bound + 1):
        states.setdefault(genome(N), N)
    Ds = sorted(states)[:60]
    unreached = []
    pairs = 0
    for D in Ds:
        f0 = factorint(states[D])
        for E in Ds:
            if E == D or E % D:
                continue
            pairs += 1
            # push the atoms of a realization of E on top of a realization of D
            g = dict(f0)
            for q, a in factorint(states[E]).items():
                g[q] = max(g.get(q, 0), a)
            if genome_of_factors(g) != E:
                unreached.append((D, E, genome_of_factors(g)))
    ok(not unreached, f"F8: arrows with no push word: {unreached[:5]}")
    print(f"    {pairs} divisibility arrows among the {len(Ds)} SMALLEST "
          f"observed genomes; {len(unreached)} not traversable")

    # (b) the one-push graph out of the EMPTY state, characterized exactly.
    # A single push of q sends state 1 to genome oddpart(q-1), so the arrow
    # 1 -> E exists iff E = oddpart(q-1) for some prime q, i.e. iff E*2^a + 1
    # is prime for some a: the arrow set out of 1 IS the Proth predicate.
    # (Enumerating q over a truncated prime list would measure the list, not
    # the graph -- the realizing prime for E = 19 is already 1217.)
    # swept over EVERY observed genome, not just the smallest ones -- the
    # claim is about how far down the scale the carving stays invisible, so
    # restricting it to the small end would be assuming the answer
    mismatch = []
    for E in sorted(states):
        if E == 1:
            continue
        a = proth_witness(E, 64)
        # confirm the witness really IS the push: below the trial-division
        # horizon take the independent route (factor the prime and take its
        # own genome); above it, fall back to primality + oddpart, since
        # factoring a large Proth prime by trial division would not return
        p = None if a is None else (E << a) + 1
        by_push = a is not None and (
            genome(p) == E if p < 10 ** 12
            else (is_primeZ(p) and oddpart(p - 1) == E))
        if by_push != (a is not None):
            mismatch.append(E)
    ok(not mismatch, f"F8: Proth witness does not realize the push at {mismatch[:5]}")
    pool = [E for E in sorted(states) if E != 1]
    reached = [E for E in pool if proth_witness(E, 64) is not None]
    missed = [E for E in pool if E not in reached]
    print(f"    arrows OUT OF THE EMPTY STATE are exactly the Proth predicate: "
          f"{len(reached)}/{len(pool)} of ALL observed genomes are one-push, "
          f"each realized by its own prime E*2^a+1")
    if missed:
        print(f"      no witness below a=64 (open, NOT absent): {missed[:8]}")

    # (c) the named specimen: a Sierpinski genome is unreachable in one push
    #     from the empty state, provably, but reachable in two
    covered = all(any((SIERPINSKI * pow(2, a, p) + 1) % p == 0 for p in COVER)
                  for a in range(1, 37))
    ok(covered, "F8: the covering set does not cover 78557*2^a+1 over a=1..36")
    ok(proth_witness(SIERPINSKI, 64) is None,
       "F8: found a Proth witness for 78557 -- covering argument contradicted")
    # the certificate DERIVED rather than quoted, by the general finder
    found = covering_set(SIERPINSKI)
    ok(found is not None and set(found[1]) == set(COVER),
       f"F8: the general cover finder returned {found}, not the known set")
    parts = factorint(SIERPINSKI)
    wits = {m: proth_witness(m) for m in parts}
    two = None
    if all(w is not None for w in wits.values()):
        primes = [m * (1 << wits[m]) + 1 for m in parts]
        st = 1
        for p in primes:
            st *= p
        if genome(st) == SIERPINSKI:
            two = (primes, st)
    ok(two is not None, "F8: 78557 not assembled from its atoms in two pushes")
    print(f"    78557 = {' * '.join(f'{m}^{e}' for m, e in parts.items())}; "
          f"covering set {COVER} kills every 78557*2^a+1 (a=1..36, one period)")
    print(f"    => NO single push reaches genome 78557 from the empty state")
    if two:
        print(f"    but two pushes do: primes {two[0]} -> state {two[1]}, "
              f"genome {genome(two[1])}")
    print()


def main():
    print("=" * 70)
    print("THE GENOME FIBRE")
    print("=" * 70)
    ls = [3, 5, 7, 11, 13]
    section_control()
    section_F1(3000)
    section_F2(2000, ls, 4)
    section_F3(600, [3, 5, 7])
    section_F4(4000, ls)
    section_F5(4000, ls)
    section_F6(4000, ls)
    section_F7(4000, 999, 64, 1200)
    section_F8(4000)
    print("=" * 70)
    print(f"CHECKS: {PASS} passed, {FAIL} failed")
    print("=" * 70)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
