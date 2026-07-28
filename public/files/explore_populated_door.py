"""explore_populated_door.py -- how far a ring's door runs above its
ladder's, and whether the excess has a formula.

THE QUESTION. A place P over p, seated at exponent e in a state st, has two
doors. The LONE door is what its own ladder charges: the least r with
lambda(P^(e+r)) not dividing lambda(P^e). The POPULATED door is what the
engine charges: the least r with lambda(P^(e+r)) not dividing lambda(state),
an LCM over every seated place, which can only run WIDER. The EXCESS is
their difference.

explore_tick_pump.py F11 checked the transfer that lets the product law be
read off a ring at all -- that the two doors agree -- at 472 readings over
two rings, found 0 off, and concluded a ring's populated door IS the
per-item clock. explore_headed_ladder.py F9 refuted the conclusion at the
third ring: Z[i]'s ramified place stands at exponent 3 with a lone-place
door of 5 and a populated door of 7, a number explore_gaussian_runaway.py
had already printed as that strand's price of 128 against 32, without
connecting it. F9 attributed the widening to the INERT place over 3, whose
residue field F_9 puts q - 1 = 8 into the state invariant, and left open
(F9 (v)) how far the excess can run and whether the state's own residue
characteristics bound it.

So: is the excess a function of what the other seated places supply, is
that supply computable from residue cardinalities, and is it bounded?

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. Every term here
is the ENGINE's -- lam_P, lam_state, door_r, seated, exponent -- and none
is the schedule family's (ladder, gap, price, head). That is deliberate and
it is the whole point of the question: F11's transfer claim is precisely
the assertion that the two vocabularies name one object, so a rig written
in the schedule's words could not see the seam it is testing.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 From ONE specimen to a carrier. "Cross-prime" is F9's name for the
    mechanism, read off the single Z[i] reading. It is a hypothesis about
    the carrier and is not assumed here; the hand-attack below says it is
    half the story and S4 is built to make both halves print.
 T2 Between the three columns. The three rings' lam_P tables are three
    separate hand-derivations. Z[i]'s ramified column is a PLATEAU brute-
    checked in its own file's S1; nothing about its shape is carried to
    the other rings' ramified columns, which are read from their own
    engines in S1 here.
 T3 From seated to unseated. F11's readings scan SEATED places only. The
    e = 0 column is a different object and S5 carries no expectation
    inherited from the seated sweep.

THE HAND-ATTACK, on paper before the engine, and it killed a prediction.

  Write q = N(P). The first draft of this slate predicted that an
  unramified column is lambda(P^a) = (q-1)*p^(a-1), giving a lone door of
  1 always and an excess of v_p(L) - (e-1). Reading the three engines
  refutes it pre-run: lam_P is the EXPONENT of (O/P^a)^*, not its ORDER,
  and the two part exactly where the local unit group stops being cyclic.
  Z[w]'s SPLIT places over 2 carry (1, 2, 2, 4, 8, ...) = 2^(a-2) for
  a >= 3 -- Q(sqrt-23) has -23 = 1 mod 8, so 2 splits, and Z_2^* is not
  cyclic. Unramified is no defence. Every ramified column is a staircase
  of step 2 besides.

  What survives is stronger than what died, and it is STRUCTURAL rather
  than a table fact. (O/P^a)^* is k^* x U_1/U_a with k^* cyclic of order
  q - 1 and U_1/U_a a p-group, so the exponent's PRIME-TO-p PART IS q - 1
  at every a >= 1, whatever shape the p-part takes. That is why the
  non-cyclic columns above cost nothing here: they differ from the
  standard ones only in the p-part, which is the half the door condition
  is about. All seven columns in play instance it -- Z[i] ram (2-powers,
  q-1 = 1), Z[sqrt-5] ram2 (2-powers, q-1 = 1) and ram5 (4*5^k, q-1 = 4),
  Z[w] ram23 (22*23^k, q-1 = 22) and split2 (2-powers, q-1 = 1), odd
  split ((p-1)p^(a-1)), inert ((q^2-1)p^(a-1)) -- and S1 checks them,
  which is a check on the ENGINES' hand-derived tables and not on the
  structure theory. So for a SEATED place (e >= 1) that factor already
  divides lambda(P^e) and hence L, the prime-to-p clause of the door
  condition is discharged for free at every column shape, and the door
  reduces to a single p-adic valuation:

      door_pop(P, e, st) = least r with v_p(lambda(P^(e+r))) > v_p(L)   (*)

  (*) is exact and general -- it needs no column shape. Its content is
  that THE STATE ENTERS A SEATED PLACE'S DOOR THROUGH ONE INTEGER, v_p(L),
  and every other fact about the state is invisible to that place.

  Decompose that integer. L is an lcm, so v_p(L) is a MAX over seated Q of
  v_p(lambda(Q^(e_Q))), and the terms sort into three kinds:
    - Q = P itself:      v_p(lambda(P^e)).
    - Q over p, Q != P:  v_p(lambda(Q^e_Q)), a pure p-power's valuation
      since N(Q) - 1 is prime to p. It moves with Q's DEPTH -- e_Q - 1
      where the column is standard, e_Q - 2 at Z[w]'s split places over
      2 -- so what enters is the depth and not any cardinality. Writing
      it as one formula is the error this slate had already killed. An
      EXPONENT route.
    - Q over l != p:     v_p(lambda(Q^(e_Q))) = v_p(N(Q) - 1), with the
      exponent ABSENT -- l^(e_Q - 1) is prime to p. A RESIDUE route,
      computable from residue cardinalities alone.
  F11 guessed the risk was places over the same rational prime; F9
  corrected it to cross-prime. The decomposition says both routes are real
  and they enter by different doors, which is why one specimen could name
  only one of them.

PREDICTIONS, fixed before the engine ran.
  P1  (*) holds at every seated reading in all three rings, from the void
      and from every planted ramified seed. 0 off.
  P2b The door depends on the state ONLY through v_p(L): two readings
      sharing a lambda column, an exponent e and a v_p(L) have equal
      doors -- ACROSS rings, not only within one.
  P2c The closed form door_pop = v_p(L) - e + 2 with door_lone = 1 holds
      at exactly the standard columns and FAILS at the five non-standard
      ones named above. Predicting where a formula breaks is the test; a
      formula scoped after the fact is not one.
  P2d The prime-to-p part of every column is constant = q - 1 over the
      swept range. (*) rests on this, so it is measured and not assumed.
  P3  The control fires clean: over Z[sqrt-5] and Z[w] -- the two rings
      F11 walks -- every SEATED reading has excess 0. A nonzero one there
      means the instrument is wrong rather than the transfer.
  P4  At Z[i] the seated ramified place at exponent 3 reads lone door 5,
      populated door 7, excess 2, with v_2(L) = 3 supplied by the inert
      place over 3 (N = 9, v_2(8) = 3).
  P5  Both routes fire somewhere in the sweep: at least one reading whose
      v_p(L) is set by a place over the SAME p, and at least one set by a
      place over a DIFFERENT one.
  P6  Unseated places widen, and more often than seated ones. The e = 0
      column is where the excess lives, which is why F11's seated scan
      read 0 everywhere.
  P7  The excess is UNBOUNDED and not bounded by the state's residue
      characteristics in any uniform way: v_2(N(Q) - 1) is unbounded over
      the places of a single ring, so a planted state drives Z[i]'s
      ramified door arbitrarily far past 5.

KILL-SHAPE, frozen as an OBSERVABLE and not an inference: the rig PRINTS a
seated reading where (*) fails, or two readings agreeing in (column, e,
v_p(L)) and disagreeing in door. What either would MEAN for the product
law is weighed after the run, not here.

POSITIVE CONTROL, run before any kill-or-survive result is read (S1). Each
ring's columns are read from its OWN engine and checked for the prime-to-p
invariant (*) rests on; each lone door is recomputed through the engine's
own door_r; and the sweep reproduces F11's own seated readings over the two
rings it walked. A rig that cannot reproduce the number it is auditing is
not auditing it.

THE SECTIONS.
  S1  positive control: the columns, the prime-to-p invariant, lone doors.
  S2  the sweep: three rings, void and planted, every seated reading, (*).
  S3  the formula: determinism in (column, e, v_p(L)); the closed form and
      where it is scoped to.
  S4  the routes: the decomposition, and the residue-cardinality reading
      of the cross-prime term.
  S5  the unseated column, which F11's readings never scanned.
  S6  how far it runs: the planted drive at F9 (v).

F1 A SEATED PLACE'S DOOR IS ONE p-ADIC VALUATION, AND THE STATE REACHES IT
   THROUGH ONE INTEGER (PROPERTY, not a range result -- it follows from the
   structure of (O/P^a)^*; the 96 (ring, kind, p) classes at depth 40 and
   the 717 seated readings, 0 off, check that the ENGINES implement that
   structure). (O/P^a)^* is k^* x U_1/U_a with k^* cyclic of order q - 1
   and U_1/U_a a p-group, so lambda's prime-to-p part is q - 1 at every
   a >= 1. For a seated place that factor already divides L, the door
   condition loses its prime-to-p clause entirely, and what is left is:

       door_pop(P, e, st) = least r with v_p(lambda(P^(e+r))) > v_p(L).

   Computed as a valuation predicate independent of the engine's
   divisibility test, it reproduces door_r at all 717. The content is the
   quantifier: v_p(L) is the ONLY thing a seated place can see of the state
   it sits in. S3 tests that directly by keying every reading on its lambda
   COLUMN, its exponent and v_p(L) -- not on its ring or its place -- and
   finds 188 distinct keys with 0 clashes, 60 of them hit by more than one
   ring, so the determinism is cross-ring rather than one walk's habit.
   AND BECAUSE IT IS A PROPERTY, ITS SCOPE IS NOT THESE THREE RINGS -- but
   it is not unconditional either. The splitting needs a FINITE residue
   field: it is what makes k^* cyclic of order q - 1 and what makes that
   order coprime to |1 + m|, so the two factors separate. Granted that, the
   identity is the door law at every place of every Dedekind domain with
   finite residue fields, which is every ring and every function field this
   corpus walks -- the three rings are where it is CHECKED, not where it is
   true. Drop finiteness and the argument goes, not merely the check. Which
   also means the widening cannot be escaped by choosing a friendlier ring:
   only a state whose invariant carries no surplus p-part escapes it.

F2 THE CLOSED FORM EXISTS AND ITS SCOPE IS THE CYCLIC UNIT GROUP (rule in
   range; 413 standard readings and 304 non-standard). Where the column is
   exactly (q-1)*p^(a-1), door_pop = v_p(L) - e + 2 and door_lone = 1, at
   all 413. It FAILS at 237 of the 304 non-standard readings, and the five
   non-standard columns were named at the freeze from the engines' own
   tables rather than found afterwards: Z[i]'s ramified plateau,
   Z[sqrt-5]'s two ramified columns, Z[w]'s ramified column, and -- the one
   that killed the first draft of the slate -- Z[w]'s SPLIT places over 2.
   lam_P is the EXPONENT of the unit group, not its order, and the two part
   where that group stops being cyclic, which happens at an UNRAMIFIED
   place whenever 2 splits. So "unramified" is not the boundary; cyclic is.

F3 THE CROSS-PRIME SUPPLY IS RESIDUE CARDINALITY AND NOTHING ELSE, WHICH IS
   THE QUESTION ANSWERED YES (rule in range; every cross-p term at all 717
   readings). v_p(L) is a max over seated places, and the terms sort into
   two kinds that enter by different mechanisms:
     - a place Q over the SAME p contributes v_p(lambda(Q^e_Q)), a pure
       p-power's valuation since N(Q) - 1 is prime to p, which moves with
       Q's own DEPTH -- e_Q - 1 at a standard column but e_Q - 2 at Z[w]'s
       split places over 2, so the route is named by what enters it and
       never by a single formula;
     - a place Q over a DIFFERENT prime contributes v_p(N(Q) - 1), its
       RESIDUE CARDINALITY, with its exponent absent -- l^(e_Q-1) is prime
       to p, so how deep Q stands is invisible.
   The second is checked against v_p(N(Q) - 1) at every cross-p term in the
   sweep and never differs. So the excess is computable from the state's
   residue cardinalities alone, it is a correction TERM and not a defeat,
   and the transfer is repairable rather than false.

F4 THE CARRIER F11 GUESSED IS UNREACHABLE AND THE ONE IT DID NOT NAME IS
   THE ONLY ONE A WALK CAN FIRE (rule in range; 0 of 717 states carry a
   same-characteristic seated pair, and the planted counter-state widens).
   F11 named the risk as "other places over the same rational prime" -- the
   exponent route. It fires at 0 readings. The first explanation this file
   printed for that was FLAT SUPPORT and the rig refuted it in the same
   run: 458 of the swept states carry two places above exponent 1, because
   a planted seed strands and the strand IS a second deep place. The
   histogram splits clean by seed -- void walks flat, planted walks carrying
   the strand -- so deep pairs are common and the route still never fires.
   The actual reason is narrower: no state carries two SEATED places of
   equal characteristic at all, a place and its conjugate having equal norm
   so the tie-break takes exactly one. The route is UNREACHABLE, not
   vacuous: planted directly -- Z[sqrt-5]'s split place over 41 at exponent
   1 beside its conjugate at 6 -- it widens the door from 1 to 6, an excess
   of 5, larger than anything the residue route reaches in a walk.

F5 WHAT F11 MEASURED WAS THE SEATED COLUMN, NOT ITS TWO RINGS (rule in
   range; 16363 unseated readings against 717 seated ones). Its 472
   agreeing readings scan SEATED places, and its conclusion was read as a
   fact about the two rings. It is not: unseated places widen in ALL THREE
   rings, at 20.0% in Z[sqrt-5] and 12.6% in Z[w] -- the two rings whose
   seated readings are 0 for 0 -- against 24.4% in Z[i]. The standing
   norm-5 specimen prints here as the two Z[i] splits going 1 -> 2, price
   25 rather than 5. So the transfer holds on the column F11 read and fails
   off it, in every ring including the ones that look clean.

F6 THE SEATED WIDENING IS ONE FACT, NOT A POPULATION, AND THE WALKED EXCESS
   IS 2 (rule in range; 717 readings). All 116 widened seated readings are
   one place at one exponent -- Z[i]'s ramified place stranded at exponent
   3 -- read once per step of the walks that reach it. Lone door 5 against
   populated 7, v_2(L) = 3 supplied by the inert place over 3 whose residue
   field F_9 carries q - 1 = 8, which is explore_headed_ladder.py F9's
   specimen reproduced through an independent predicate. So the corpus's
   exposure is one place in one ring, and the two rings F11 walked are
   genuinely clean at the column it read.

F7 THE EXCESS IS UNBOUNDED, AND THE BOUND F9 (v) ASKED FOR IS THE
   UNIVERSE'S RATHER THAN THE MECHANISM'S (rule in range; planted states,
   MAXP = 2000, door driven to 17 against a lone 5). F9 (v) left open how
   far a populated door can run above its ladder's and whether residue
   characteristics bound it. They do not bound it, they SET it: the door
   is a function of v_2(L), and one planted companion supplies
   v_2(N(Q) - 1) directly. Z[i]'s ramified place held at exponent 3 reads
   door 5 alone, 7 beside the inert place over 3, 9 beside a split place
   over 17, 11 over 97, 13 over 193 or the inert place over 31, and 17
   beside the split place over 257 -- an excess of 12 where the walk
   reaches 2. Since 2^k + 1 shaped primes are 1 mod 4 and split in Z[i],
   and v_2(p - 1) is unbounded over primes p = 1 mod 4 by Dirichlet, no
   bound in the state's residue characteristics exists. A PLANTED result:
   the question is about the family of states, and F6 reports what a walk
   reaches.

F8 WHAT IS LEFT OPEN. (i) The unboundedness argument leans on Z[i]'s
   ramified column being the engine's plateau at every depth, which its own
   file brute-checks to a finite depth -- the argument is complete for all
   k given the column, and the column is a rule in range. (ii) Everything
   here is the IDEAL world; an element move seats a bundle and no reading
   here covers it. (iii) The three rings are quadratic and imaginary; a
   place of residue degree above 2, where q - 1 can carry a large p-part at
   a SMALL rational prime, is not walked and is exactly where the residue
   route should bite hardest. (iv) Whether the correction term can be
   carried by any schedule the family admits is answered NO by F3's own
   shape -- an item's price there is a function of its own exponent -- but
   what a family that admits c(item, state) does to the four laws is a
   separate build and is not started here. (v) The sweep reads doors, not
   MENUS: whether a widened door ever changes which place a walk seats,
   rather than only what a stranded place is priced at, is unmeasured, and
   F6's single specimen is a strand precisely because it is never seated
   again.

RUN RECORD. One process, CPython, no BLAS. Wall 0.3 s, peak working set
23.9 MB against memwatch.py's 512 MB ceiling. 747 checks over three ring
engines -- explore_number_field_lock.py, explore_module_law.py and
explore_gaussian_runaway.py -- whose lam_P, lam_state, door_r, ideal_menu
and universes are imported rather than re-implemented, so their own asserts
fire underneath these. 717 seated readings and 16363 unseated ones over 7
ring-seeds, 60 moves each.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from math import gcd

import explore_gaussian_runaway as GI      # Z[i]
import explore_number_field_lock as K5     # Z[sqrt-5]
import explore_module_law as K23           # Z[w], w = (1+sqrt-23)/2

CHECKS = 0

WALK_MOVES = 60      # moves from each seed; past every lock these rings have
COL_DEPTH = 40       # column depths tabulated per place


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


def v_p(n, p):
    """p-adic valuation of a positive integer."""
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def prime_to_p(n, p):
    while n % p == 0:
        n //= p
    return n


# --------------------------------------------------------------- the rings
# One record per ring: its module, a label, and its ramified places, which
# are what F11 plants. Everything else is read through the module's own
# lam_P / lam_state / door_r / ideal_menu, never re-implemented here.
RINGS = [
    ("Z[sqrt-5]", K5, [('ram', 2), ('ram', 5)]),
    ("Z[w] (-23)", K23, [('ram', 23)]),
    ("Z[i]", GI, [('ram', 2)]),
]

# The two rings explore_tick_pump.py F11 walked, whose 472 readings are the
# control: the transfer is claimed there and refuted only at the third.
F11_RINGS = ("Z[sqrt-5]", "Z[w] (-23)")


def column(mod, pl, depth=COL_DEPTH):
    return tuple(mod.lam_P(pl, a) for a in range(1, depth + 1))


def lone_door(mod, pl, e):
    """The door the place's OWN ladder charges at exponent e."""
    return mod.door_r(pl, e, mod.lam_P(pl, e))


def pop_door(mod, pl, e, L):
    """The door the engine charges against the whole state's invariant."""
    return mod.door_r(pl, e, L)


def star_door(mod, pl, e, L):
    """(*) computed independently of door_r: the least r whose column entry
    outruns v_p(L) in the p-adic valuation ALONE. Deliberately a different
    predicate from door_r's divisibility test, so agreement is evidence."""
    p = mod.place_char(pl)
    target = v_p(L, p)
    r = 1
    while v_p(mod.lam_P(pl, e + r), p) <= target:
        r += 1
        assert r < 500, "star door runaway"
    return r


def walk(mod, seed, moves=WALK_MOVES):
    """Greedy ideal walk from a seed state, yielding (step, st, L) at every
    state including the seed itself. The move rule is the engine's own
    ideal_menu, first tie by place_key -- the walker S7 of
    explore_headed_ladder.py uses, not a re-implementation."""
    st = dict(seed)
    L = mod.lam_state(st)
    yield 0, dict(st), L
    for step in range(1, moves + 1):
        _, ties = mod.ideal_menu(st, L)
        q, r = ties[0]
        st[q] = st.get(q, 0) + r
        L = mod.lam_state(st)
        yield step, dict(st), L


def seeds_for(mod, rams):
    """The void, plus one planted seed per ramified place -- F11's own
    setup, so the control reproduces its readings rather than resembling
    them."""
    out = [("void", {})]
    for pl in rams:
        out.append(("planted %s" % (pl,), {pl: 1}))
    return out


def read_state(mod, ring, seedname, step, st, L):
    """Every SEATED place in one state, read twice. Returns a list of
    reading dicts; asserts nothing -- the sections do the judging."""
    rows = []
    for pl, e in sorted(st.items(), key=mod.place_key):
        if e < 1:
            continue
        p = mod.place_char(pl)
        lone = lone_door(mod, pl, e)
        pop = pop_door(mod, pl, e, L)
        rows.append(dict(
            ring=ring, seed=seedname, step=step, pl=pl, p=p,
            norm=mod.place_norm(pl), e=e, L=L, vpL=v_p(L, p),
            lone=lone, pop=pop, excess=pop - lone,
            col=column(mod, pl), st=dict(st),
        ))
    return rows


# ------------------------------------------------- S1 the positive control
def s1_control():
    section("S1  POSITIVE CONTROL: the columns, the prime-to-p invariant, "
            "and the lone doors")
    print("  (*) is only exact if every column's PRIME-TO-p part is constant")
    print("  at q - 1 for a >= 1. That is prediction P2d and it is measured")
    print("  here, per place kind per ring, before anything is concluded.")
    print()
    kinds = {}
    for ring, mod, _ in RINGS:
        for pl in mod.UNIVERSE[:60]:
            kinds.setdefault((ring, pl[0], mod.place_char(pl)), pl)
    bad = []
    for (ring, kind, p), pl in sorted(kinds.items()):
        mod = dict((r, m) for r, m, _ in RINGS)[ring]
        q = mod.place_norm(pl)
        parts = set(prime_to_p(mod.lam_P(pl, a), p)
                    for a in range(1, COL_DEPTH + 1))
        if parts != {q - 1}:
            bad.append((ring, kind, p, sorted(parts), q - 1))
    ok(not bad, "prime-to-p part is not constant q-1 at: %s" % bad)
    print("  %d (ring, kind, p) classes checked over depth %d: prime-to-p"
          % (len(kinds), COL_DEPTH))
    print("  part constant at q - 1 in every one. (*) is licensed.")

    print()
    print("  the non-standard columns, named at the freeze and now read off")
    print("  the engines -- a column is STANDARD iff lambda(P^a) is exactly")
    print("  (q-1)*p^(a-1), which is the exponent only where the local unit")
    print("  group is cyclic:")
    nonstd = []
    for ring, mod, _ in RINGS:
        seen = set()
        for pl in mod.UNIVERSE[:60]:
            key = (pl[0], mod.place_char(pl))
            if key in seen:
                continue
            seen.add(key)
            p, q = mod.place_char(pl), mod.place_norm(pl)
            std = all(mod.lam_P(pl, a) == (q - 1) * p ** (a - 1)
                      for a in range(1, COL_DEPTH + 1))
            if not std:
                nonstd.append((ring, pl[0], p, column(mod, pl, 10)))
    for ring, kind, p, col in nonstd:
        print("    %-11s %-6s over %-3d  %s ..." % (ring, kind, p, list(col)))
    ok(len(nonstd) == 5,
       "the freeze named 5 non-standard columns and the engines carry %d: %s"
       % (len(nonstd), [(r, k, p) for r, k, p, _ in nonstd]))
    print("  %d, exactly the five the freeze named." % len(nonstd))

    print()
    print("  and the lone doors, recomputed through each engine's own")
    print("  door_r, against the two the corpus states in prose:")
    lone_i = lone_door(GI, ('ram', 2), 3)
    print("    Z[i] ramified place at exponent 3, lone door : %d" % lone_i)
    ok(lone_i == 5, "Z[i]'s lone-place door at exponent 3 is %d, not the 5 "
                    "explore_headed_ladder.py F9 states" % lone_i)
    print("      (explore_headed_ladder.py F9's 5, and its price 2^5 = %d)"
          % 2 ** lone_i)
    return nonstd


# ------------------------------------------------------------- S2 the sweep
def s2_sweep():
    section("S2  THE SWEEP: three rings, void and planted, every seated "
            "place read twice")
    rows = []
    for ring, mod, rams in RINGS:
        for seedname, seed in seeds_for(mod, rams):
            for step, st, L in walk(mod, seed):
                rows.extend(read_state(mod, ring, seedname, step, st, L))
    print("  %d seated readings over %d ring-seeds."
          % (len(rows), sum(len(seeds_for(m, r)) for _, m, r in RINGS)))

    off = [r for r in rows
           if star_door(dict((x, m) for x, m, _ in RINGS)[r['ring']],
                        r['pl'], r['e'], r['L']) != r['pop']]
    ok(not off, "(*) fails at %d readings, first: %s" % (len(off), off[:1]))
    print("  P1: (*) reproduces the engine's door at all %d, 0 off." % len(rows))

    print()
    print("  the excess, by ring:")
    for ring, _, _ in RINGS:
        rr = [r for r in rows if r['ring'] == ring]
        wide = [r for r in rr if r['excess'] > 0]
        print("    %-11s %4d readings, %3d with excess > 0, max excess %d"
              % (ring, len(rr), len(wide),
                 max([r['excess'] for r in rr], default=0)))

    print()
    print("  and which places those are -- a widened SEATED reading is the")
    print("  whole object of the audit, so it is named rather than counted:")
    by_pl = {}
    for r in rows:
        if r['excess'] > 0:
            k = (r['ring'], r['pl'])
            lo, hi, n = by_pl.get(k, (99, 0, 0))
            by_pl[k] = (min(lo, r['e']), max(hi, r['e']), n + 1)
    for (ring, pl), (lo, hi, n) in sorted(by_pl.items(), key=lambda x: -x[1][2]):
        print("    %-11s %-16s %3d readings, exponent %d..%d"
              % (ring, str(pl), n, lo, hi))

    ctl = [r for r in rows if r['ring'] in F11_RINGS and r['excess'] != 0]
    print()
    print("  P3, the control -- the two rings F11 walked, over seated")
    print("  places, where it reports 472 of 472 agreeing:")
    if ctl:
        for r in ctl[:6]:
            print("    %-11s %-14s step %2d  %s at e=%d : lone %d pop %d"
                  % (r['ring'], r['seed'], r['step'], r['pl'], r['e'],
                     r['lone'], r['pop']))
        print("    %d readings with excess > 0 -- P3 FALSIFIED." % len(ctl))
    else:
        print("    0 readings with a nonzero excess. The instrument agrees")
        print("    with F11 where F11 looked.")

    print()
    print("  P4, the Z[i] specimen F9 refuted the transfer with:")
    spec = [r for r in rows
            if r['ring'] == "Z[i]" and r['pl'] == ('ram', 2) and r['e'] == 3]
    if spec:
        r = max(spec, key=lambda x: x['step'])
        print("    state %s"
              % ", ".join("norm %d at exponent %d" % (GI.place_norm(k), v)
                          for k, v in sorted(r['st'].items(),
                                             key=GI.place_key)))
        print("    ramified place at exponent 3: lone door %d (price %d),"
              % (r['lone'], 2 ** r['lone']))
        print("    populated door %d (price %d), excess %d, v_2(L) = %d"
              % (r['pop'], 2 ** r['pop'], r['excess'], r['vpL']))
        ok((r['lone'], r['pop'], r['vpL']) == (5, 7, 3),
           "the Z[i] specimen reads (lone %d, pop %d, v_2(L) %d) where F9 "
           "states (5, 7, 3)" % (r['lone'], r['pop'], r['vpL']))
    return rows


# ----------------------------------------------------------- S3 the formula
def s3_formula(rows, nonstd):
    section("S3  THE FORMULA: the door as a function of (column, e, v_p(L))")
    print("  P2b says the state reaches a seated place through ONE integer.")
    print("  Key every reading by its lambda COLUMN (not its ring, not its")
    print("  place -- two places with one column must answer alike), its")
    print("  exponent, and v_p(L). A clash is the kill-shape.")
    memo, clash = {}, []
    for r in rows:
        key = (r['p'], r['col'], r['e'], r['vpL'])
        if key in memo and memo[key][0] != r['pop']:
            clash.append((key[:1] + key[2:], memo[key], (r['pop'], r['ring'])))
        memo.setdefault(key, (r['pop'], r['ring']))
    ok(not clash, "the door is not a function of (column, e, v_p(L)): %s"
                  % clash[:2])
    print("  %d distinct keys over %d readings, 0 clashes."
          % (len(memo), len(rows)))
    cross = {}
    for r in rows:
        cross.setdefault((r['p'], r['col'], r['e'], r['vpL']), set()).add(
            r['ring'])
    shared = [k for k, v in cross.items() if len(v) > 1]
    print("  %d of those keys are hit by more than one ring, so the claim is"
          % len(shared))
    print("  cross-ring and not a restatement of one walk's determinism.")

    print()
    print("  P2c, the closed form. Where the column IS (q-1)*p^(a-1) the")
    print("  hand-attack gives door_pop = v_p(L) - e + 2 and door_lone = 1.")
    nonstd_keys = set((r, k, p) for r, k, p, _ in nonstd)
    std_rows = [r for r in rows
                if (r['ring'], r['pl'][0], r['p']) not in nonstd_keys]
    ns_rows = [r for r in rows
               if (r['ring'], r['pl'][0], r['p']) in nonstd_keys]
    bad = [r for r in std_rows
           if r['pop'] != r['vpL'] - r['e'] + 2 or r['lone'] != 1]
    ok(not bad, "the closed form fails at %d STANDARD readings: %s"
                % (len(bad), bad[:1]))
    print("    holds at all %d standard readings." % len(std_rows))
    broke = [r for r in ns_rows
             if r['pop'] != r['vpL'] - r['e'] + 2 or r['lone'] != 1]
    print("    fails at %d of %d non-standard readings, which is the half of"
          % (len(broke), len(ns_rows)))
    print("    P2c that had to be predicted rather than observed.")
    ok(broke, "the closed form did not fail at ANY non-standard reading, so "
              "the freeze's scoping was not load-bearing")
    for r in ns_rows[:0] or broke[:4]:
        print("      %-11s %-10s e=%d v_p(L)=%d : lone %d pop %d, form says %d"
              % (r['ring'], str(r['pl']), r['e'], r['vpL'], r['lone'],
                 r['pop'], r['vpL'] - r['e'] + 2))


# ------------------------------------------------------------ S4 the routes
def s4_routes(rows):
    section("S4  THE ROUTES: which seated place supplies v_p(L), and by "
            "which of the two mechanisms")
    print("  v_p(L) is a MAX over seated places. The hand-attack sorts the")
    print("  terms into an EXPONENT route (a place over the SAME p, whose")
    print("  contribution is a pure p-power's valuation and so moves with")
    print("  its own DEPTH) and a RESIDUE route (a place over another prime,")
    print("  which contributes v_p(N(Q) - 1) with its exponent ABSENT).")
    print("  F11 guessed the first, F9 named the second.")
    mods = dict((r, m) for r, m, _ in RINGS)
    same_hits, cross_hits, resid_bad = [], [], []
    for r in rows:
        mod, p, pl = mods[r['ring']], r['p'], r['pl']
        own = v_p(mod.lam_P(pl, r['e']), p)
        samep = [(v_p(mod.lam_P(q, ee), p), q) for q, ee in r['st'].items()
                 if q != pl and mod.place_char(q) == p and ee >= 1]
        crossp = [(v_p(mod.lam_P(q, ee), p), q) for q, ee in r['st'].items()
                  if mod.place_char(q) != p and ee >= 1]
        for val, q in crossp:
            if val != v_p(mod.place_norm(q) - 1, p):
                resid_bad.append((r['ring'], q, val))
        top = max([own] + [v for v, _ in samep] + [v for v, _ in crossp])
        ok(top == r['vpL'],
           "the route decomposition misses v_p(L): %d vs %d" % (top, r['vpL']))
        if top > own:
            if any(v == top for v, _ in samep):
                same_hits.append(r)
            if any(v == top for v, _ in crossp):
                cross_hits.append(r)
    ok(not resid_bad,
       "a cross-p term is not v_p(N(Q)-1) -- the residue reading fails at %s"
       % resid_bad[:2])
    print()
    print("  the cross-p term equals v_p(N(Q) - 1) at every reading, so the")
    print("  cross-prime supply IS computable from residue cardinalities")
    print("  alone, which is the question this file was opened to settle.")
    print()
    print("  P5, both routes firing:")
    print("    readings whose v_p(L) is set by a SAME-p place  : %d"
          % len(same_hits))
    print("    readings whose v_p(L) is set by a CROSS-p place : %d"
          % len(cross_hits))
    for lbl, hits in (("same-p", same_hits), ("cross-p", cross_hits)):
        if hits:
            r = hits[0]
            print("      %s specimen: %-11s %s at e=%d, v_p(L)=%d, excess %d"
                  % (lbl, r['ring'], r['pl'], r['e'], r['vpL'], r['excess']))

    # Why one route is empty. A same-p place's contribution moves with its
    # depth, so it can only set v_p(L) by standing DEEPER than the place
    # being read. The support shape decides whether any state has two.
    print()
    print("  WHY THE EXPONENT ROUTE IS EMPTY, measured rather than guessed --")
    print("  the first reading here refuted the obvious answer. A same-p")
    print("  place's contribution grows with its depth, so it can only set")
    print("  v_p(L) by standing DEEPER than the place read. The histogram is")
    print("  reason: count places above exponent 1, split by seed --")
    hist = {}
    for r in rows:
        deep = sum(1 for q, ee in r['st'].items() if ee > 1)
        key = ("void" if r['seed'] == "void" else "planted", deep)
        hist[key] = hist.get(key, 0) + 1
    for key in sorted(hist):
        print("    %-8s %d place(s) above exponent 1 : %4d states"
              % (key[0], key[1], hist[key]))
    print("  -- a VOID walk is flat, and a PLANTED one carries a second deep")
    print("  place, which is the STRAND the corpus already files. So deep")
    print("  pairs are common and the route still never fires.")
    print()
    print("  The actual reason is that the pair is never over ONE rational")
    print("  prime. Count states carrying two SEATED places of equal")
    print("  characteristic, which is what the exponent route needs:")
    pairs = 0
    for r in rows:
        chars = {}
        mod = mods[r['ring']]
        for q, ee in r['st'].items():
            if ee >= 1:
                chars[mod.place_char(q)] = chars.get(mod.place_char(q), 0) + 1
        if any(v > 1 for v in chars.values()):
            pairs += 1
    print("    %d of %d states." % (pairs, len(rows)))
    ok(pairs == 0,
       "%d states DO carry a same-characteristic seated pair, so the "
       "exponent route is empty for a third reason" % pairs)
    print("  None. A greedy walk seats ONE place per rational prime -- the")
    print("  strand is a second deep place but never a second place over the")
    print("  same p, because a place and its conjugate carry equal norm and")
    print("  the tie-break takes one. So the exponent route needs a state")
    print("  the walk cannot build, and F11's guessed carrier was not merely")
    print("  unobserved: it is unreachable, while the one it did not name is")
    print("  the only one a walk can fire.")

    print()
    print("  so the route is not VACUOUS, only unreachable: plant the state")
    print("  a walk cannot build -- two conjugate split places over one")
    print("  rational prime, one deeper than the other:")
    pl_a = ('split', 41, next(r for r in range(1, 41) if (r * r + 5) % 41 == 0))
    pl_b = K5.conj_place(pl_a)
    st = {pl_a: 1, pl_b: 6}
    L = K5.lam_state(st)
    lone = lone_door(K5, pl_a, 1)
    pop = pop_door(K5, pl_a, 1, L)
    print("    Z[sqrt-5], %s at exponent 1 beside its conjugate at 6:"
          % (pl_a,))
    print("      v_41(L) = %d, supplied by the conjugate's exponent alone"
          % v_p(L, 41))
    print("      lone door %d, populated door %d, excess %d"
          % (lone, pop, pop - lone))
    ok(pop > lone,
       "the planted same-p state does not widen, so the exponent route is "
       "vacuous rather than unreachable")
    ok(star_door(K5, pl_a, 1, L) == pop, "(*) fails at the planted same-p "
                                         "state")
    return same_hits, cross_hits


# ---------------------------------------------------------- S5 the unseated
def s5_unseated():
    section("S5  THE UNSEATED COLUMN, which F11's readings never scanned")
    print("  F11 reads SEATED places. A place at exponent 0 has a lone")
    print("  invariant of lambda(P^0) = 1, so its own ladder gives it the")
    print("  cheapest possible door, and the state can only widen it. If")
    print("  the excess lives anywhere it lives here (P6).")
    tot = wide = 0
    spec = []
    per_ring = {}
    for ring, mod, rams in RINGS:
        for seedname, seed in seeds_for(mod, rams):
            for step, st, L in walk(mod, seed):
                for pl in mod.UNIVERSE[:40]:
                    if st.get(pl, 0) >= 1:
                        continue
                    lone = lone_door(mod, pl, 0)
                    pop = pop_door(mod, pl, 0, L)
                    tot += 1
                    a, b = per_ring.get(ring, (0, 0))
                    per_ring[ring] = (a + 1, b + (1 if pop > lone else 0))
                    if pop > lone:
                        wide += 1
                        spec.append((ring, seedname, step, pl,
                                     mod.place_norm(pl), lone, pop))
    print()
    print("  %d unseated readings, %d widened (%.1f%%), against the seated"
          % (tot, wide, 100.0 * wide / max(tot, 1)))
    print("  column's own rate reported in S2.")
    print()
    print("  and by ring, which is where the blind spot actually shows:")
    for ring, _, _ in RINGS:
        n, w = per_ring.get(ring, (0, 0))
        print("    %-11s %5d unseated, %4d widened (%.1f%%)"
              % (ring, n, w, 100.0 * w / max(n, 1)))
    ok(all(per_ring[r][1] > 0 for r in per_ring),
       "some ring never widens an unseated place, so the blind spot is one "
       "ring's and not the transfer's")
    print("  Every ring widens here, INCLUDING the two whose seated readings")
    print("  are 0 for 0. So the transfer F11 measured was not true of those")
    print("  rings and false of Z[i]; it was true of the column F11 read.")
    ok(wide > 0, "no unseated place widened anywhere, so P6 is false and "
                 "F11's blind spot was empty")
    print()
    print("  and the standing specimen, Z[i]'s two norm-5 splits at 1 -> 2:")
    n5 = [s for s in spec if s[0] == "Z[i]" and s[4] == 5]
    if n5:
        for s in sorted(set((s[3], s[5], s[6]) for s in n5)):
            print("    %s : lone door %d, populated door %d, price %d not %d"
                  % (s[0], s[1], s[2], 5 ** s[2], 5 ** s[1]))
        ok(any(s[5] == 1 and s[6] == 2 for s in n5),
           "the norm-5 splits do not read 1 -> 2 anywhere in the Z[i] walk")
    return tot, wide


# -------------------------------------------------------- S6 how far it runs
def s6_how_far():
    section("S6  HOW FAR IT RUNS: the planted drive at "
            "explore_headed_ladder.py F9 (v)")
    print("  F9 (v) leaves open how far a populated door can run above the")
    print("  ladder's and whether the state's residue characteristics bound")
    print("  it. The decomposition answers it: the cross-p supply is")
    print("  v_2(N(Q) - 1), and over the places of ONE ring that is")
    print("  unbounded -- a split place over a prime p = 1 mod 4 supplies")
    print("  v_2(p - 1), and 2^k + 1 shaped primes make it as large as the")
    print("  universe reaches. A PLANTED state, not a walked one: the")
    print("  question is about the family of states, and S2 reports what a")
    print("  walk actually reaches.")
    ram = ('ram', 2)
    e = 3
    lone = lone_door(GI, ram, e)
    print()
    print("  Z[i]'s ramified place held at exponent %d, lone door %d:"
          % (e, lone))
    print("    %-26s %-8s %-6s %-6s %s"
          % ("planted companion", "v_2(N-1)", "v_2(L)", "door", "excess"))
    drives = []
    for pl in GI.UNIVERSE:
        if pl[0] == 'split' and pl[1] in (5, 13, 17, 97, 193, 257):
            pass
        elif pl == ('inert', 3) or pl == ('inert', 31):
            pass
        else:
            continue
        st = {ram: e, pl: 1}
        L = GI.lam_state(st)
        pop = pop_door(GI, ram, e, L)
        drives.append((pl, v_p(GI.place_norm(pl) - 1, 2), v_p(L, 2), pop))
        print("    %-26s %-8d %-6d %-6d %d"
              % (str(pl), v_p(GI.place_norm(pl) - 1, 2), v_p(L, 2), pop,
                 pop - lone))
        ok(star_door(GI, ram, e, L) == pop,
           "(*) fails at a planted state, %s" % (pl,))
    top = max(drives, key=lambda d: d[3])
    ok(top[3] > 7,
       "the planted drive never runs past the walked 7, so P7 is false and "
       "the excess may be bounded after all")
    print()
    print("  the door runs to %d against a lone %d -- an excess of %d, where"
          % (top[3], lone, top[3] - lone))
    print("  the walked state reaches 2. The bound is the UNIVERSE's, not")
    print("  the mechanism's: v_2(N(Q) - 1) is unbounded over primes")
    print("  p = 1 mod 4 by Dirichlet, and every unit of it is one more")
    print("  step of door.")
    return lone, top


def main():
    nonstd = s1_control()
    rows = s2_sweep()
    s3_formula(rows, nonstd)
    s4_routes(rows)
    s5_unseated()
    s6_how_far()
    print("\n  %d checks passed." % CHECKS)


if __name__ == "__main__":
    main()
