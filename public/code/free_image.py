"""free_image.py -- the set of limits a growth demand reaches under
EVERY policy it admits, over Z and over F_2[x]: five demands, five
forms, one chain, and the one image the ring can reach.

QUESTION. image.py follows every tie of the GREEDY walk and finds a
point over Z, a finite count over an imaginary quadratic ring where
the walk locks and the continuum over a curve over F_2 with a second
rational place, at the corner, the ring's colouring pricing each
orbit. Drop greed. A POLICY may take any move the demand admits, and
the FREE IMAGE Im(L, s) of a demand L and a seed s is the set of limits
of all maximal runs from s under all policies. What is it for each of
the five demands growth.py runs, does the colour count price it as it
prices the greedy image, and what of the ring does it see?

THE OBJECTS. A RING here is Z or F_2[x]; a PLACE is a prime or a monic
irreducible, and places are listed in a CANONICAL ORDER: by size over
Z, by (degree, encoding) over F_2[x]. A state M is a nonzero element,
carried as its exponent function on the places; a move multiplies,
M -> M m, with m not a unit. lambda(M) is the exponent of the unit
group of the quotient ring, an lcm of place contributions lambda_P(a):
over Z (p - 1) p^(a-1) at odd p, and 1, 2, 2^(a-2) at 2 for a = 1, 2,
a >= 3; over F_2[x] (2^d - 1) 2^ceil(log2 a) at a place of degree d.
A LIMIT gives every place an exponent in {0, 1, 2, ...} or infinity;
it is FINITE when its support is finite and every exponent finite. The
five demands, each a condition on the extension from M to M m:
  INDEPENDENCE    -- m coprime to M;
  SEMISIMPLICITY  -- M m squarefree;
  NEW IDEMPOTENTS -- M m has more places than M;
  TRANSPARENCY    -- lambda(M m) = lambda(M);
  DYNAMICS        -- lambda(M m) > lambda(M).
And one built to test a reading, not a demand of growth.py:
  FRESH DYNAMICS  -- m a place not dividing M, and lambda rises.
W(L) is the WALL, the largest M with lambda(M) | L. G_s is the group of
all permutations of the places that fix the seed's exponent function;
it ignores the ring's colouring entirely, which over Z is the
trivial one (lambda_P reads p itself) and over F_2[x] is the degree.

THE ARGUMENT (written before the engine).
  (1) FIVE FORMS. From a seed s:
        transparency     { W(lambda(s)) }, one finite point;
        semisimplicity   s prod_{P in S} P, S an infinite set of places
                         off supp(s), at a squarefree s; { s } at any
                         other seed, where no move is admissible;
        independence     s prod_{P in S} P^(e_P), S infinite off
                         supp(s), every e_P finite and >= 1;
        new idempotents  every X >= s with infinite support;
        dynamics         every X >= s that is not finite.
      Each is a CLOSURE half and a REACH half. Closure: a coprime move
      carries no seated place, so seed and seated exponents are final;
      a squarefree product admits no second copy; a raised place count
      needs a new place, so the support is infinite; a dynamics run
      never halts, since a place P off M with lambda_P(1) > lambda(M)
      exists (finitely many places have any bounded size), and a run
      of infinitely many non-unit moves cannot converge to a finite
      limit. Transparency: lambda(lcm) = lcm(lambda) and lambda is
      monotone under divisibility (CRT), so {M : lambda(M) | L} is
      closed under lcm and finite, with maximum W(L); from s every
      reachable M divides W = W(lambda(s)) and has lambda(M) =
      lambda(s), and any M < W admits a place of W / M, so every
      maximal run stops at W. Reach: seat the least unseated support
      place at each step, at its target exponent (or 1 where the
      target is infinity), bring one seated place short of a finite
      target (a seed place among them) up to it, raise every seated
      infinite-target place by one (a move may hold several places),
      and at dynamics add a PAD when lambda has not
      risen -- a further unseated support place Q with lambda_Q(1) not
      dividing lambda (one exists when the support is infinite, by the
      size argument), or else an infinite-exponent place raised to the
      least exponent that lifts lambda (the ladder is unbounded). The
      least unseated support place rises strictly, so every support
      place is seated at a finite step. Nothing in (1) reads the ring
      beyond three facts: CRT, finitely many places of bounded size,
      and an unbounded ladder at each place.
  (2) THE CHAIN. At a squarefree seed the last four nest strictly,
      semisimplicity < independence < new idempotents < dynamics, the
      strictness witnessed by exponents 1..3 on an infinite support,
      one infinite exponent beside an infinite support, and one
      infinite exponent alone. The transparency point is finite and in
      none of them. At a non-squarefree seed semisimplicity is the
      finite point { s } and leaves the chain.
  (3) THE FATES ARE THE EXTREMES. BREADTH is the support maximal, DEPTH
      an exponent infinite, MORTALITY a finite limit: breadth and depth
      are FACES, each extreme in one coordinate with the other free,
      and mortality is the CORNER where both bottom out. A (demand,
      seed) is mortal exactly when its image holds the corner, since
      every move at least doubles the size. Breadth and depth can hold
      together (every odd prime seated beside 2 at infinity), and a
      generic member holds no fate. Two demands can agree on all three
      fates and differ as images: new idempotents and dynamics.
  (4) WHAT MAKES A DEMAND MORTAL is a finite reachable set, never a ban
      on depth: FRESH DYNAMICS bans depth (it never revisits a place)
      and reads lambda, and it lives forever from every seed, a place P
      off M with lambda_P(1) > lambda(M) always being admissible.
  (5) THE COLOUR COUNT, DEGENERATE. Every image but transparency's is
      described by predicates that read the seed's places and, off
      them, only the SHAPE of the exponent function. So each is a union
      of G_s-orbits, for the group that forgets the ring: the colour
      count prices the free image with the coarsest colouring there is,
      every place alike, and every live image holds a continuum orbit,
      but semisimplicity's at a seed that is not squarefree, the point
      s. Dynamics shows the gap between a law and its image: its
      admissibility reads lambda_P, which a colour-breaking permutation
      changes (over Z, from the void, 3 is admissible and 2 is not),
      while its image is invariant under all of G_s. Transparency's
      point is the only image that reads the ring, and the wall is
      where the ring's arithmetic sits.
  (6) GREED'S POINT. Greedy dynamics over Z runs from the void
      to 3^infinity, a limit on the corner of finite support and an infinite
      exponent, while a free policy reaches 2^infinity by refusing the
      least move (4, not 2, lifts lambda from the void). Over F_2[x]
      the greedy limit is exponent-maximal with an infinite support
      holding at most one place per degree, interior in the support
      coordinate (image.py, the sprawl in growth.py and sprawl.py).

TRANSPLANTS, marked. (T1) Over Z a re-push of a seated odd place
always lifts lambda; over F_2[x] only a push across a frontier 2^c + 1
does, so a depth construction there must JUMP to the least lifting
exponent, and the engine computes that exponent rather than stepping.
(T2) A pad chosen as the least place with size above lambda + 1 is
affordable over Z for a few steps and not beyond; the operative
condition is the weaker one, lambda_Q(1) not dividing lambda, with the
size bound kept only as the existence argument.

PREDICTIONS, frozen before the engine, each naming what the run PRINTS.
  C  CONTROLS, run first; any failure aborts. lambda against the unit
     group's exponent by brute force (Z, every n < 300; F_2[x], every
     monic f of degree 2 to 7); W(L) against a search for the largest M
     with lambda(M) | L (Z below 10^4; F_2[x] every monic of degree
     <= 10); the index conventions v_2 lambda(2^a) = a - 2 (a >= 3) and
     v_2 lambda_P(a) = ceil(log2 a) over F_2[x], read off the engine;
     greedy dynamics from the void over Z moving by 3 at each of 10
     steps.
  K1 CLOSURE. Over a battery of states and every move up to a cap (Z:
     m <= 400; F_2[x]: every monic of degree <= 7), the count of
     admissible moves that touch a seated place (independence), leave
     squarefreeness (semisimplicity), seat nothing (new idempotents),
     and the count of states with no admissible dynamics move. KILL:
     any of the four counts above 0.
  K2 TRANSPARENCY. From seeds 2, 6, 12, 30 over Z and 1, x, x^2,
     x^2 + x + 1 over F_2[x], the reachable set by depth-first search
     over single-place moves, and every scanned move from every
     reachable state. KILL: a reachable set other than the multiples of
     s dividing W(lambda(s)), a scanned admissible move landing off
     W's divisors, or a reachable state other than W with no move.
  K3 REACH. For each live demand, a battery of in-image targets per
     ring, from the void and from a squarefree seed, run 12 steps:
     every move admissible, the state dividing the target, and the
     least unseated support place strictly rising; and in every run,
     read off the recorded states, every place bound for infinity
     rising at every step after its seating. The battery holds a
     target with every place off the seed at infinity, whose final
     state must hold each place seated at step j at exponent 12 - j,
     and one raising the seed's places to 3; and under dynamics every
     target of finite support with exponents 0, 1, 2 or infinity on the
     first five places off the seed, at least one infinite. KILL: any
     step failing any of these, or either final state short. CONTROLS:
     a final state with one place one step short must fail the depth
     check, and a run with one infinite exponent held at its last step
     must fail the rise check.
  K4 INVARIANCE. The permuted targets pi X, pi a transposition of two
     places off the seed's support that breaks the ring's colouring,
     run under dynamics as in K3 (of the six dynamics targets three are
     moved by the transposition; the other three, every place at 1,
     every place at infinity and the seed raised to 3, it fixes, and
     those runs repeat K3's); and over the closure battery, the
     count of (state, move) pairs whose dynamics admissibility changes
     under pi, printed beside the same count under a degree-preserving
     pi over F_2[x]. KILL: a permuted target failing K3, or the
     degree-preserving count above 0.
  K5 FRESH DYNAMICS alive 20 steps from the void and from 12 over Z
     and from the void and x^2 over F_2[x], every place it seats at
     exponent 1 (the demand's own definition), and over F_2[x] no two
     of its places of one degree. KILL: a step with no admissible move.
  K6 THE CHAIN, read off the characterisation in (1) over five
     described limits, each strictness witness also reached in K3.
     KILL: an inclusion failing, or a witness not reached.
  K7 GREED'S POINT. Greedy dynamics from the void over Z reaches only
     3 for 10 steps while the free policy reaches 2^infinity (a K3
     target). KILL: either fails.

POSITIVE CONTROL for the verdicts: K3 is also run on four
OUT-OF-IMAGE targets per ring from the squarefree seed (independence
asked for a seed exponent raised; semisimplicity asked for an exponent
2; new idempotents asked for a finite support; dynamics asked for a
finite limit), and must stall on each, printing the step and the
reason, so a construction that passes everything is caught.

FINDINGS (entered after the run, from its printed output).
  F1 THE FIVE FORMS, both rings (every kill missed). Closure: 0 of
     5,586 (state, move) pairs over Z and 0 of 3,048 over F_2[x]
     break an invariant; the three blind zeros are the demands read
     back and cannot be otherwise, so the closure's content is (1)'s
     proof and the fourth zero, every battery state with a dynamics
     move, the size argument's instance. Transparency
     reaches exactly the multiples of s dividing W(lambda(s)) at all
     eight seeds, every run ending at W. Reach: 14 targets per seed
     over the four live demands, from the void and a squarefree seed
     on each ring, every step admissible (below the target and rising
     hold by the construction's own steps);
     under dynamics all 3,124 finite-support targets run 12 steps
     clean; every place bound for infinity rose at every step after
     its seating in every run, 51,029 rises read;
     at the every-place-at-infinity target each of 111 seated places
     sat at 12 minus its seating step (8 runs), and from the squarefree
     seed every seed place bound for 3 reached it; the depth check
     fails a place one step short, and the rise check passes the run
     that made the history and fails it with one exponent held; and
     the positive control stalls on all eight out-of-image targets,
     each printing its step and reason.
  F2 THE CHAIN, each strictness witness reached under its demand on
     both rings; that it lies outside the smaller image is (2)'s
     argument, and the positive control's stalls run it for two of the
     three links (exponents 1, 2, 3 under semisimplicity; one place at
     infinity alone under new idempotents). The finite element is in
     no live image.
  F3 THE IMAGE FORGETS WHAT THE LAW READS. A transposition breaking
     the ring's colouring changes dynamics admissibility at 161 tested
     (state, move) pairs over Z and 96 over F_2[x], and changes no
     blind demand's;
     a degree-preserving one over F_2[x] changes nothing. Yet the
     construction toward each of the six dynamics targets with the
     pair exchanged, three of them moved by the exchange, runs 12
     steps, every step admissible, at all four (ring, seed) starts:
     the law has the ring's symmetry and its image has all of G_s, as
     (5) argues.
  F4 FRESH DYNAMICS is alive 20 steps from all four seeds, every
     place it seats at exponent 1, over F_2[x] no two of one degree: a
     demand with no depth that never dies.
  F5 GREED'S POINT. Greedy dynamics from the void over Z moves by 3 at
     all 10 steps, and the free policy reaches 2^infinity alone.

RUN RECORD. One process, CPython, no numpy: 54,558 checks, 3.3 s,
peak 15.4 MB under a memory guard. Two earlier constructions were
wrong and the battery now holds what caught each. One raised the
infinite exponents one at a time in rotation, which starves all but
one when infinitely many places target infinity. The next, lacking a
pad, pushed only a SEATED infinite exponent, and so stalled when the
least unseated place had a finite target, every other unseated place
Q had lambda_Q(1) dividing lambda, and no place bound for infinity
was seated yet: x (x+1)^infinity over F_2[x] from the void, and 9 of
the 3,124 finite-support targets. The pad now pushes the least place
bound for infinity, seated or not.
"""

import os
import sys
import time
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import growth as GR
import sprawl as SP

CHECKS = [0]
INF = float("inf")
STEPS = 12


def check(cond, msg):
    CHECKS[0] += 1
    if not cond:
        raise AssertionError(msg)


def lcm(a, b):
    return a // gcd(a, b) * b


# ------------------------------------------------------------- the rings

class Ring:
    """Places in canonical order, a local lambda, and moves to scan."""

    def __init__(self, name, places, lam_local, moves, show):
        self.name = name
        self.places = places
        self.index = {P: i for i, P in enumerate(places)}
        self.lam_local = lam_local
        self.moves = moves
        self.show = show

    def lam(self, st):
        L = 1
        for P, a in st.items():
            if a:
                L = lcm(L, self.lam_local(P, a))
        return L

    def text(self, st):
        if not st:
            return "1"
        out = []
        for P in sorted(st, key=self.index.get):
            a = st[P]
            b = self.show(P)
            if len(b) > 1 and self.name != "Z":
                b = "(" + b + ")"
            out.append(b if a == 1 else b + "^" + ("oo" if a == INF
                                                    else str(a)))
        return " ".join(out)


def z_lam_local(p, a):
    return GR.value(GR.lam_pp(p, a))


def f2_lam_local(g, a):
    return GR.lam_f2_pp(GR.pdeg(g), a)


def f2_show(g):
    terms = []
    for i in range(GR.pdeg(g), -1, -1):
        if g >> i & 1:
            terms.append("1" if i == 0 else "x" if i == 1 else "x^%d" % i)
    return "+".join(terms)


# F_2[x]: every irreducible of degree <= 10, then the least one of each
# degree 11..48, which the pads and the fresh walk reach for.
F2_PLACES = ([g for d in range(1, 11) for g in GR.IRR[d]]
             + [SP.extreme_irr(d, False) for d in range(11, 49)])
ZZ = Ring("Z", GR.PRIMES, z_lam_local,
          [GR.factor(m) for m in range(2, 401)], str)
F2 = Ring("F2[x]", F2_PLACES, f2_lam_local,
          [GR.pfactor(m) for m in range(2, 1 << 8)], f2_show)
RINGS = (ZZ, F2)


def mul(st, m):
    out = dict(st)
    for P, e in m.items():
        out[P] = out.get(P, 0) + e
    return out


# ------------------------------------------------------------ the demands

def independence(R, st, m):
    return not any(st.get(P, 0) for P in m)


def semisimplicity(R, st, m):
    return all(e <= 1 for e in mul(st, m).values())


def new_idempotents(R, st, m):
    return any(not st.get(P, 0) for P in m)


def transparency(R, st, m):
    return R.lam(mul(st, m)) == R.lam(st)


def dynamics(R, st, m):
    return R.lam(mul(st, m)) > R.lam(st)


LAWS = {"independence": independence, "semisimplicity": semisimplicity,
        "new idempotents": new_idempotents, "transparency": transparency,
        "dynamics": dynamics}
LIVE = ("independence", "semisimplicity", "new idempotents", "dynamics")


# --------------------------------------------------------------- controls

def f2_unit_exponent_ok(f, E):
    """E is the exponent of (F_2[x]/f)^x: every unit has r^E = 1, and for
    each prime q | E some unit has r^(E/q) != 1."""
    def pw(r, n):
        out = 1
        while n:
            if n & 1:
                out = SP.pmod(GR.pmul(out, r), f)
            r = SP.pmod(GR.pmul(r, r), f)
            n >>= 1
        return out
    units = [r for r in range(1, 1 << GR.pdeg(f)) if SP.pgcd(f, r) == 1]
    if any(pw(r, E) != 1 for r in units):
        return False
    return all(any(pw(r, E // q) != 1 for r in units)
               for q in SP.prime_factors(E))


def section_c():
    print("C  CONTROLS")
    bad = [n for n in range(2, 300) if GR.lam_int(n) != GR.unit_exponent(n)]
    check(not bad, "lambda over Z: %s" % bad[:5])
    fs = range(4, 1 << 8)
    bad = [f for f in fs if not f2_unit_exponent_ok(f, GR.lam_f2(f))]
    check(not bad, "lambda over F2[x]: %s" % bad[:5])
    print("  lambda is the unit group's exponent: every n < 300 over Z, "
          "every monic of degree 2..7 over F2[x]")
    rows = 0
    for L in (1, 2, 4, 6, 8, 10):
        W = GR.wall(L)
        best = max(n for n in range(1, 10 ** 4)
                   if L % GR.lam_int(n) == 0)
        check(best == W, "wall over Z at L = %d" % L)
        rows += 1
    lam_f = {f: GR.lam_f2(f) for f in range(2, 1 << 11)}
    for L in range(1, 64):
        W = GR.wall_f2(L)
        if GR.pdeg(W) > 10:
            continue
        ok = [f for f in lam_f if L % lam_f[f] == 0]
        check(W in ok and all(GR.pdivides(f, W) for f in ok),
              "wall over F2[x] at L = %d" % L)
        rows += 1
    print("  W(L) against search: %d values of L, Z below 10^4 and "
          "F2[x] to degree 10" % rows)
    check([GR.v2(z_lam_local(2, a)) for a in range(3, 12)]
          == list(range(1, 10)), "v2 lambda(2^a) = a - 2")
    check(all(GR.v2(f2_lam_local(g, a)) == (a - 1).bit_length()
              for g in (2, 7, 11) for a in range(1, 18)),
          "v2 lambda_P(a) = ceil(log2 a)")
    print("  index conventions: v2 lambda(2^a) = a - 2 from a = 3 over Z; "
          "v2 lambda_P(a) = ceil(log2 a) over F2[x]; the brute range "
          "above holds 2^a to a = 8 and x^a to a = 7")
    st, picks = {}, []
    for _ in range(10):
        m = next(m for m in range(2, 10 ** 4)
                 if dynamics(ZZ, st, GR.factor(m)))
        picks.append(m)
        st = mul(st, GR.factor(m))
    check(picks == [3] * 10, "greedy dynamics from the void: %s" % picks)
    print("  greedy dynamics from the void over Z:", picks)


# ------------------------------------------------------------ the batteries

def z_states():
    return [GR.factor(n) if n > 1 else {} for n in
            (1, 2, 3, 4, 6, 8, 12, 30, 49, 210, 360, 1024, 2310, 9699690)]


def f2_states():
    sq = GR.pmul(7, 11)
    return [GR.pfactor(f) if f > 1 else {} for f in
            (1, 2, 4, 6, 7, 18, 20, 72, GR.pmul(18, sq),
             GR.ppow(2, 9), GR.pmul(GR.ppow(3, 5), 7), GR.pmul(sq, 13))]


STATES = {"Z": z_states(), "F2[x]": f2_states()}


def section_k1():
    print("\nK1  CLOSURE, every move to the cap from every battery state")
    for R in RINGS:
        touch = unsq = seatless = dead = n = 0
        for st in STATES[R.name]:
            live = False
            for m in R.moves:
                n += 1
                if independence(R, st, m) and any(st.get(P) for P in m):
                    touch += 1
                if semisimplicity(R, st, m) and any(
                        e > 1 for e in mul(st, m).values()):
                    unsq += 1
                if new_idempotents(R, st, m) and all(st.get(P) for P in m):
                    seatless += 1
                live = live or dynamics(R, st, m)
            dead += not live
        print("  %-6s %6d (state, move) pairs: independence touching a "
              "seated place %d, semisimplicity leaving squarefree %d, new "
              "idempotents seating nothing %d; states with no dynamics "
              "move %d" % (R.name, n, touch, unsq, seatless, dead))
        check(touch == unsq == seatless == dead == 0, "K1 at " + R.name)
    print("  The first three zeros are the demands read back, engine "
          "consistency; the fourth is the size argument's instance.")


def divisors(W):
    out = [{}]
    for P, a in W.items():
        out = [_with(d, P, k) for d in out for k in range(a + 1)]
    return out


def _with(d, P, k):
    e = dict(d)
    if k:
        e[P] = k
    return e


def key(st):
    return frozenset((P, a) for P, a in st.items() if a)


def leq(a, b):
    return all(e <= b.get(P, 0) for P, e in a.items() if e)


def section_k2():
    print("\nK2  TRANSPARENCY, the reachable set from each seed")
    cases = [(ZZ, n, GR.factor(n), GR.wall) for n in (2, 6, 12, 30)]
    cases += [(F2, f, GR.pfactor(f) if f > 1 else {}, GR.wall_f2)
              for f in (1, 2, 4, 7)]
    for R, label, s, wall in cases:
        L = R.lam(s)
        W = wall(L)
        Wst = GR.factor(W) if R is ZZ else GR.pfactor(W)
        cand = [P for P in R.places[:400] if L % R.lam_local(P, 1) == 0]
        seen, todo, stuck = {key(s)}, [s], []
        while todo:
            st = todo.pop()
            nxt = [mul(st, {P: 1}) for P in cand
                   if transparency(R, st, {P: 1})]
            if not nxt:
                stuck.append(st)
            for t in nxt:
                if key(t) not in seen:
                    seen.add(key(t))
                    todo.append(t)
            for m in R.moves:
                if transparency(R, st, m):
                    check(leq(mul(st, m), Wst), "K2: a move off W")
        want = {key(d) for d in divisors(Wst) if leq(s, d)}
        check(seen == want, "K2: reachable set at %s" % label)
        check([key(t) for t in stuck] == [key(Wst)], "K2: a run stops short")
        print("  %-6s seed %-18s lambda %-3d reached %3d states = the "
              "multiples of s dividing W = %s; every run ends there"
              % (R.name, R.text(s), L, len(seen), R.text(Wst)))


# ---------------------------------------------------------- the reach half

class Target:
    """A described limit: an exponent for every place, off a seed."""

    def __init__(self, name, R, seed, rule):
        self.name, self.R, self.seed = name, R, seed
        self.exp, i = {}, 0         # rule: (index off the seed, P) -> exp
        for P in R.places:
            if P in seed:
                r = rule(-1, P)
                self.exp[P] = seed[P] if r is None else max(seed[P], r)
            else:
                self.exp[P] = rule(i, P)
                i += 1

    def e(self, P):
        return self.exp[P]


def construct(law, T, steps=STEPS, verbose=False, out=None):
    """Run the construction toward T; return (steps made, reason or None).
    When out is a list, the final state, each place's seating step
    (places off the seed) and the states step by step are appended."""
    R = T.R
    st = dict(T.seed)
    order = [P for P in R.places if T.e(P)]
    seat, hist = {}, [dict(st)]
    for k in range(steps):
        unseated = [P for P in order if not st.get(P)]
        P0 = unseated[0] if unseated else None
        m = {}
        if P0 is not None:
            m[P0] = T.e(P0) if T.e(P0) != INF else 1
        todo = [P for P in order if st.get(P) and T.e(P) != INF
                and st[P] < T.e(P)]
        if todo:
            m[todo[0]] = m.get(todo[0], 0) + T.e(todo[0]) - st[todo[0]]
        deep = [P for P in order if T.e(P) == INF and st.get(P)]
        for P in deep:
            m[P] = m.get(P, 0) + 1
        if law is dynamics and not dynamics(R, st, m):
            pad = None
            L = R.lam(mul(st, m))
            for Q in unseated[1:]:
                if L % R.lam_local(Q, 1):
                    pad = Q
                    break
            if pad is not None:
                m[pad] = T.e(pad) if T.e(pad) != INF else 1
            else:
                bound = [P for P in order if T.e(P) == INF]
                jump = bound[0] if bound else None
                while jump is not None and not dynamics(R, st, m):
                    m[jump] = m.get(jump, 0) + 1
        if not m or not law(R, st, m):
            return k, "no admissible move of the construction"
        new = mul(st, m)
        if any(a > T.e(P) for P, a in new.items()):
            return k, "overshoots the target"
        if P0 is not None:
            left = [P for P in order if not new.get(P)]
            if left and R.index[left[0]] <= R.index[P0]:
                return k, "the least unseated place did not rise"
        elif not deep:
            return k, "no infinite exponent rose"
        for P in new:
            if new[P] and not st.get(P) and P not in T.seed:
                seat[P] = k
        st = new
        hist.append(dict(st))
    if out is not None:
        out.append((st, seat, hist))
    return steps, None


def targets(R):
    """(seed name, seed) and the in-image targets per law, off each seed."""
    two = R.places[:2]
    seeds = [("void", {}), (R.text({two[0]: 1, two[1]: 1}),
                            {two[0]: 1, two[1]: 1})]
    out = []
    for sname, s in seeds:
        first = next(P for P in R.places if P not in s)
        out.append((sname, s, {
            "every place at 1": lambda i, P: 1 if i >= 0 else None,
            "exponents 1, 2, 3 in turn":
                lambda i, P: i % 3 + 1 if i >= 0 else None,
            "one place at oo, the rest at 1":
                lambda i, P, f=first: INF if P == f else 1 if i >= 0
                else None,
            "one place at oo alone":
                lambda i, P, f=first: INF if P == f else 0 if i >= 0
                else None,
            "every place at oo": lambda i, P: INF if i >= 0 else None,
            "a seed place at 3, the rest at 1":
                lambda i, P: 3 if i < 0 else 1,
        }))
    return out


IN_IMAGE = {
    "independence": ("every place at 1", "exponents 1, 2, 3 in turn"),
    "semisimplicity": ("every place at 1",),
    "new idempotents": ("every place at 1", "exponents 1, 2, 3 in turn",
                        "one place at oo, the rest at 1",
                        "every place at oo",
                        "a seed place at 3, the rest at 1"),
    "dynamics": ("every place at 1", "exponents 1, 2, 3 in turn",
                 "one place at oo, the rest at 1", "one place at oo alone",
                 "every place at oo", "a seed place at 3, the rest at 1"),
}
OUT_OF_IMAGE = {
    "semisimplicity": "exponents 1, 2, 3 in turn",
    "new idempotents": "one place at oo alone",
}
REACHED = set()


def rises(T, hist):
    """Every place bound for infinity, once seated, rose at every later
    step of the recorded run; returns the number of rises read."""
    n = 0
    for P in T.R.places:
        if T.e(P) != INF:
            continue
        for a, b in zip(hist, hist[1:]):
            if a.get(P):
                check(b[P] > a[P], "K3 %s %s: an infinite exponent stalled"
                      % (T.R.name, T.name))
                n += 1
    return n


def reach_depths(R, s, law, tname, fin):
    """Every place seated off the seed at step j and bound for infinity
    sits at exponent STEPS - j, having risen at every later step; and a
    seed place bound for 3 got there."""
    st, seat = fin[:2]
    if tname == "every place at oo":
        check(seat and all(st[P] == STEPS - j for P, j in seat.items()),
              "K3 %s %s every place at oo: an exponent stalled"
              % (R.name, law))
        DEPTHS.append(len(seat))
        LAST[0] = fin
    if tname == "a seed place at 3, the rest at 1":
        check(all(st[P] == 3 for P in s),
              "K3 %s %s: a seed place short of 3" % (R.name, law))


DEPTHS = []
LAST = [None]
LAST_T = [None]
RISES = [0]
BOUNDED = 5


def finite_supports(R, s):
    """Dynamics targets of finite support: exponents in {0, 1, 2, oo} on
    the first BOUNDED places off the seed, at least one oo, 0 beyond."""
    for code in range(4 ** BOUNDED):
        v = [(0, 1, 2, INF)[code // 4 ** i % 4] for i in range(BOUNDED)]
        if INF in v:
            yield Target("finite support %s" % v, R, s,
                         lambda i, P, v=v: None if i < 0 else
                         v[i] if i < BOUNDED else 0)


def section_k3():
    print("\nK3  REACH, %d steps of the construction per target" % STEPS)
    for R in RINGS:
        for sname, s, rules in targets(R):
            for law in LIVE:
                for tname in IN_IMAGE[law]:
                    T = Target(tname, R, s, rules[tname])
                    fin = []
                    k, why = construct(LAWS[law], T, out=fin)
                    check(why is None, "K3 %s %s %s %s: step %s, %s"
                          % (R.name, sname, law, tname, k, why))
                    REACHED.add((R.name, sname, law, tname))
                    reach_depths(R, s, law, tname, fin[0])
                    if tname == "every place at oo":
                        LAST_T[0] = T
                    RISES[0] += rises(T, fin[0][2])
            print("  %-6s from %-9s %d targets over the four live "
                  "demands, every step admissible, below the target, "
                  "rising" % (R.name, sname,
                              sum(len(v) for v in IN_IMAGE.values())))
    print("  every place at oo: each of %d seated places sits at %d minus "
          "its seating step, %d runs; every seed place bound for 3 "
          "reached it" % (sum(DEPTHS), STEPS, len(DEPTHS)))
    print("  the free policy's corner over Z: 2^oo alone from the void,",
          ("Z", "void", "dynamics", "one place at oo alone") in REACHED)
    n = 0
    for R in RINGS:
        for sname, s, rules in targets(R):
            for T in finite_supports(R, s):
                fin = []
                k, why = construct(dynamics, T, out=fin)
                check(why is None, "K3 %s %s dynamics %s: step %s, %s"
                      % (R.name, sname, T.name, k, why))
                RISES[0] += rises(T, fin[0][2])
                n += 1
    print("  dynamics on finite supports: %d targets (exponents 0, 1, 2, oo "
          "on the first %d places off each seed, one oo at least), every "
          "one run clean for %d steps" % (n, BOUNDED, STEPS))
    print("  every place bound for oo rose at every step after its seating, "
          "in every run: %d rises read" % RISES[0])
    st, seat, hist = LAST[0]
    P = min(seat, key=seat.get)
    try:
        reach_depths(RINGS[0], {}, "control", "every place at oo",
                     ({**st, P: st[P] - 1}, seat))
        caught = False
    except AssertionError:
        caught = True
    check(caught, "control: one skipped step passed the depths")
    print("  POSITIVE CONTROL, one place one step short: the depth check "
          "fails it,", caught)
    T = LAST_T[0]
    rises(T, hist)
    frozen = [dict(h) for h in hist]
    frozen[-1][P] = frozen[-2][P]
    try:
        rises(T, frozen)
        caught = False
    except AssertionError:
        caught = True
    check(caught, "control: a stalled infinite exponent passed")
    print("  POSITIVE CONTROL, one infinite exponent held at the last step "
          "of the run that made it (%s from %s): the rise check passes the "
          "run and fails the held copy," % (T.R.name, T.R.text(T.seed)),
          caught)
    print("  POSITIVE CONTROL, out-of-image targets that must stall:")
    for R in RINGS:
        sname, s, rules = targets(R)[1]
        cases = [(law, tname, rules[tname])
                 for law, tname in OUT_OF_IMAGE.items()]
        cases.append(("independence", "a seed exponent raised to 2",
                      lambda i, P: 2 if i < 0 else 1))
        cases.append(("dynamics", "a finite target",
                      lambda i, P: None if i < 0 else 1 if i < 2 else 0))
        for law, tname, rule in cases:
            k, why = construct(LAWS[law], Target(tname, R, s, rule))
            check(why is not None, "control: %s reached %s" % (law, tname))
            print("    %-6s %-16s %-28s stalls at step %d: %s"
                  % (R.name, law, tname, k + 1, why))


class Swapped:
    """The target pi T, pi a transposition of two places off the seed."""

    def __init__(self, T, a, b):
        self.name, self.R, self.seed = T.name, T.R, T.seed
        self.base, self.pi = T, {a: b, b: a}

    def e(self, P):
        return self.base.e(self.pi.get(P, P))


def swap(st, pi):
    return {pi.get(P, P): a for P, a in st.items()}


def section_k4():
    print("\nK4  INVARIANCE under a permutation that forgets the ring")
    pairs = {("Z", "void"): (2, 3), ("Z", "2 3"): (5, 7),
             ("F2[x]", "void"): (2, 7), ("F2[x]", "x (x+1)"): (7, 11)}
    for R in RINGS:
        for sname, s, rules in targets(R):
            a, b = pairs[(R.name, sname)]
            check(R.lam_local(a, 1) != R.lam_local(b, 1)
                  and a not in s and b not in s, "K4: the pair")
            for tname in IN_IMAGE["dynamics"]:
                T = Swapped(Target(tname, R, s, rules[tname]), a, b)
                k, why = construct(dynamics, T)
                check(why is None, "K4 %s %s %s: %s"
                      % (R.name, sname, tname, why))
            print("  %-6s from %-9s the %d dynamics targets with %s and %s "
                  "exchanged: all clean for 12 steps" % (R.name, sname,
                                               len(IN_IMAGE["dynamics"]),
                                               R.show(a), R.show(b)))
    for R, pi, label in ((ZZ, {2: 3, 3: 2}, "2 <-> 3"),
                         (F2, {2: 7, 7: 2}, "x <-> x^2+x+1"),
                         (F2, {2: 3, 3: 2}, "x <-> x+1"),
                         (F2, {11: 13, 13: 11}, "x^3+x+1 <-> x^3+x^2+1")):
        changed = {name: 0 for name in LAWS}
        for st in STATES[R.name]:
            for m in R.moves:
                for name, law in LAWS.items():
                    if law(R, st, m) != law(R, swap(st, pi), swap(m, pi)):
                        changed[name] += 1
        keep = R.lam_local(list(pi)[0], 1) == R.lam_local(list(pi)[1], 1)
        print("  %-6s %-24s %s: admissibility changed at dynamics %d, "
              "transparency %d, the blind three %d"
              % (R.name, label, "keeps degree" if keep else "breaks colour",
                 changed["dynamics"], changed["transparency"],
                 changed["independence"] + changed["semisimplicity"]
                 + changed["new idempotents"]))
        blind = (changed["independence"] + changed["semisimplicity"]
                 + changed["new idempotents"])
        check(blind == 0, "K4: a blind demand read the ring")
        if keep:
            check(changed["dynamics"] == changed["transparency"] == 0,
                  "K4: a degree-preserving swap changed a sighted demand")
        else:
            check(changed["dynamics"] > 0, "K4: the swap changed nothing")


def fresh_dynamics(R, st, m):
    return (len(m) == 1 and all(e == 1 and not st.get(P)
                                for P, e in m.items())
            and dynamics(R, st, m))


def section_k5():
    print("\nK5  FRESH DYNAMICS: a new place that lifts lambda, 20 steps")
    for R, seeds in ((ZZ, ({}, {2: 2, 3: 1})), (F2, ({}, {2: 2}))):
        for s in seeds:
            st, picks = dict(s), []
            for _ in range(20):
                P = next((P for P in R.places
                          if fresh_dynamics(R, st, {P: 1})), None)
                check(P is not None, "K5: dead at %s" % R.text(st))
                picks.append(P)
                st = mul(st, {P: 1})
            check(all(st[P] == 1 for P in picks), "K5: depth")
            if R is F2:
                degs = [GR.pdeg(P) for P in picks]
                check(len(set(degs)) == len(degs),
                      "K5: two places of one degree")
            print("  %-6s from %-8s alive; picks of degree/size %s ... %s"
                  % (R.name, R.text(s),
                     [R.show(P) if R is ZZ else GR.pdeg(P)
                      for P in picks[:6]],
                     R.show(picks[-1]) if R is ZZ else GR.pdeg(picks[-1])))


def section_k6():
    print("\nK6  THE CHAIN, read off the five forms")
    rows = [("every place at 1", True, 1, False),
            ("exponents 1, 2, 3 in turn", True, 3, False),
            ("one place at oo, the rest at 1", True, 1, True),
            ("one place at oo alone", False, 0, True),
            ("a finite element", False, 1, False)]
    pred = {"semisimplicity": lambda i, x, h: i and x == 1 and not h,
            "independence": lambda i, x, h: i and not h,
            "new idempotents": lambda i, x, h: i,
            "dynamics": lambda i, x, h: i or h}
    print("  %-32s %-6s %-6s %-6s %-6s" % ("described limit", "semis",
                                           "indep", "newid", "dyn"))
    for name, i, x, h in rows:
        row = [pred[law](i, x, h) for law in pred]
        check(all(not a or b for a, b in zip(row, row[1:])),
              "K6: an inclusion fails at " + name)
        print("  %-32s %-6s %-6s %-6s %-6s"
              % ((name,) + tuple("in" if r else "-" for r in row)))
    for law, name in (("independence", "exponents 1, 2, 3 in turn"),
                      ("new idempotents", "one place at oo, the rest at 1"),
                      ("dynamics", "one place at oo alone")):
        check(all((R.name, "void", law, name) in REACHED for R in RINGS),
              "K6: witness " + name)
    print("  each strictness witness reached under its demand in K3, both "
          "rings; the finite element is in none")


def main():
    t0 = time.time()
    section_c()
    section_k1()
    section_k2()
    section_k3()
    section_k4()
    section_k5()
    section_k6()
    print("\nK7  greed's point over Z is 3^oo (control C); the free policy "
          "reaches 2^oo (K3)")
    print("\n%d checks, %.1f s" % (CHECKS[0], time.time() - t0))


if __name__ == "__main__":
    main()
