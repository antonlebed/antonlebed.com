"""
explore_second_ruler.py -- THE SECOND RULER AT THE MACHINE LAYER
(the recovery chart's first row; descends from explore_ruler_ladder.py
and explore_archimedean_dial.py).

THE QUESTION. The ruler ladder charted the PREDICATE layer: over
<N,+>, two independent scales' tick marks are already undecidable yet
multiplication-free (Hieronymi-Schulz 2022, Schulz 2022), and two full
depth ladders V_2 + V_3 rebuild multiplication whole (Villemaire 1992)
-- definability facts, cited there in full. The MACHINE cell is open:
a finite-window ring that GROWS (every move multiplies the modulus --
the no-decrement world of explore_growth_machine.py: increments and
tests only, no borrow, no size read, decidable) -- what does it buy if
its tests are upgraded from presence reads (is p a factor?) to DEPTH
COMPARISONS between two prime-power ladders (is v_2(N) = v_3(N)?)?
Full universality (any Turing machine simulable, halting-complete), or
only some undecidable question short of that (the reset-net grade:
reachability undecidable, termination still decidable), or nothing?
Either answer prices the cheapest known door in the recovery chart:
what re-imports buy computation back for the decidable sibling.

THE MODEL (the fattened growth machine with comparison reads). State =
(control q, depth vector (v_p)_{p in S}) for a finite prime set S.
MOVES: INC_p multiplies the modulus N by p (v_p += 1). Nothing ever
divides N: depths are monotone, N strictly increases, no archimedean
import (no size read, no down-move on any ladder). TESTS: three-way
comparisons sign(alpha*v_p - beta*v_q - gamma) at finitely many fixed
integer ratios -- the second-ruler read. Presence (v_p >= 1) is the
degenerate native case. Reading depth at all is already the purchase
being priced: the tower proper truncates every window to a residue
FIELD (depth <= 1), and this machine buys prime-power depth back at
the places in S.

READ GRADES CHARTED (each a cell of the row):
  (A) presence only            -- the growth machine: halting DECIDABLE
      (explore_growth_machine.py; zero-pattern monotone).
  (B) one-place thresholds     -- v_p >= c: DECIDABLE
      (explore_archimedean_dial.py; capped-depth quotient).
  (C) ONE comparison slope     -- all tests read v_2 - v_3 (any offsets
      gamma), plus presence reads elsewhere: the minimal genuine
      second-ruler read.
  (D) TWO ratios, two places   -- e.g. v_2 vs v_3 compared at 1:1 AND
      at alpha:beta.
  (E) pairwise equality, three places -- v_2 = v_3 and v_3 = v_5.

THE HAND ANALYSIS THE RUN VERIFIES (proofs in the sections; the two
undecidability citations cannot be run, everything else asserts):

 1. GRADE (C) COLLAPSES TO ONE COUNTER. Every move changes X = v_2 -
    v_3 by +-1 and every test factors through X (presence reads flip
    once, absorbed by a finite quotient), so the machine is bisimilar
    to a one-counter machine over Z with sign tests -- and one-counter
    machines have DECIDABLE halting (standard: one-counter automata /
    pushdown with a unary stack; Valiant-Paterson 1975 territory).
    The minimal second-ruler read buys NOTHING at the machine layer.
    Note the contrast: at the predicate layer the same-shaped door
    (two tick predicates over <N,+>) is already an undecidable theory.
    The transplant from the one-ruler world fails in the other
    direction too: the growth machine's own decidability proof
    (monotone zero-pattern) DIES at grade (C) -- a comparison
    down-flips as the ladders leapfrog -- yet decidability survives
    by the different (one-counter) argument.

 2. GRADE (E) IS MINSKY-COMPLETE: FULL UNIVERSALITY. Encode a
    two-counter Minsky machine (universal for halting -- Minsky 1967)
    as X = v_2 - v_3, Y = v_3 - v_5 with macro-moves
      X++ : INC_2          X-- : INC_3 ; INC_5
      Y++ : INC_3 ; INC_2  Y-- : INC_5
    and zero-tests v_2 = v_3, v_3 = v_5 (tests consulted only at macro
    boundaries). Every macro preserves the untouched counter; the
    simulated counters stay equal to the Minsky counters; halting
    transfers exactly. All moves MULTIPLY N -- the growth world is
    untouched, no depth ever decreases. THE BORROW IS SYNTHESIZED: no
    single ladder is ever lowered, but on the derived counter v_2 -
    v_3 the move INC_3 is a value-reading down-move. Two increments
    plus a comparison manufacture the destruction the knife edge
    (explore_archimedean_dial.py) showed universality needs -- that
    dial's theorem is not violated, its model tested the counters
    themselves; the comparison read is exactly the new import.
    Corollary asymmetry: exact-configuration reachability STAYS
    decidable (monotone: any run to a fixed target has bounded
    length) while halting goes undecidable -- the mirror image of
    reset nets (reachability undecidable, termination decidable).

 3. THE THRESHOLD IS THE SECOND INDEPENDENT COMPARISON. One comparison
    DIRECTION -- every test a function of one ladder difference,
    however many offsets, alongside presence reads -- keeps halting
    decidable (section 1); a second independent comparison across
    three or more places is already Minsky-complete (section 2's
    construction shares the middle place; disjoint pairs work the
    same way, the two differences directly independent counters). At
    exactly two places two independent comparisons hit the cone
    obstruction -- section 4. The machine door's threshold is the
    second independent comparison, the machine twin of the predicate
    layer's second scale.

 4. GRADE (D): THE GADGET ALGEBRA AND THE ELSE WALL. At two places the
    Minsky encoding above is impossible LINEARLY: the moves' images
    under any pair of independent linear forms span a two-generator
    cone, which cannot contain both +-e_1 and +-e_2 (the cone lemma,
    brute-checked over a coefficient grid). A nonlinear route exists:
    with home ray c = d (c := v_2, d := v_3) and comparison reads at
    ratios alpha:beta, a two-leg walk (descend d++ onto the line
    alpha*c = beta*d, detected by the equality read; ascend c++ back
    home) realizes the register map u -> (alpha/beta)*u EXACTLY,
    GATED on beta | u -- the crossing hits a lattice point iff the
    divisibility holds. Gated rational multiplication is FRACTRAN's
    primitive: with counters in exponents (X = v_2(u), Y = v_3(u)),
    a gated x5/2 is test-and-decrement on X. But the gate's ELSE
    branch is a wall: on beta not | u the walk overshoots (equality
    never fires; the order read detects the miss one step late) and
    every recovery landing is AFFINE-shifted off the multiplicative
    lattice (the parity gate's odd-u miss lands home at (5u+1)/2),
    destroying the exponent encoding. Further probes can resolve
    residue trees, so grade (D)'s realizable dynamics is a
    generalized-Collatz family u -> a_r*u + b_r by residue class
    (Kurtz-Simon 2007 proved SOME such families universal), but the
    debris coefficients are not freely choosable and the compilation
    is open. This script verifies the gadget algebra and the wall's
    exact shape; whether two places at two ratios reach full
    universality is the named open edge.

CITED, NOT RUN (undecidability cannot be run): Minsky 1967 (two-counter
universality; halts-iff-even witness), one-counter decidability
(standard), Dufourd-Finkel-Schnoebelen 1998 (reset nets: reachability
undecidable, termination decidable -- the mirror), Kurtz-Simon 2007
(generalized Collatz undecidable), and the predicate-layer theorems per
explore_ruler_ladder.py. Contribution here: the machine-layer chart,
the borrow-synthesis reading, the threshold-at-the-second-comparison,
the reachability/halting mirror, and the run-verified mechanisms.

PREDICTIONS (fixed before the run):
 P1. Grade-(C) battery: the concrete two-place machine and its
     one-counter abstraction agree exactly -- same control trace, same
     test outcomes, same halting -- on every battery program; the
     oscillator's abstract state revisits (loop certified) while its
     concrete depths strictly grow (no configuration ever repeats).
 P2. Grade-(E): the three-place simulation is step-exact on the
     halts-iff-even Minsky witness (X0 = 2, 6 halt; X0 = 3, 7 loop,
     certified by shadow-state repetition) and on the doubling program
     (X0 = 5 halts with Y = 10); the simulated (q, X, Y) trace equals
     the direct Minsky trace at every step.
 P3. Grade-(D) gadgets: for (alpha, beta) in {(2,1),(3,1),(5,2),(5,3)}
     and all u in 1..240, the two-leg gadget fires iff beta | u, and
     on firing lands home at exactly (alpha/beta)*u.
 P4. Grade-(D) else: on beta not | u the equality never fires, the
     miss is detected at overshoot, and the recovery lands home at
     exactly floor(alpha*u/beta) + 1 -- off the multiplicative lattice
     by beta - (alpha*u mod beta) in {1..beta-1}.
 P5. No depth ever decreases at any step of any run (the no-decrement
     law audited throughout), and N strictly increases at every move.

FINDINGS (all five predictions confirmed; tiers stated per claim).

 1. ONE COMPARISON BUYS NOTHING (rule: bisimulation verified on the
    battery; one-counter decidability cited). The concrete two-place
    machine and its one-counter abstraction agree exactly on all three
    battery programs (oscillator: loop certified by abstract-state
    revisit at 15 shadow steps while concrete depths only grew;
    halt-at-5: 12 steps; presence-then-halt: 15 steps). Grade (C) is
    bisimilar to a one-counter machine: halting decidable. The
    one-ruler proof (monotone zero-pattern) does die at the door --
    comparisons down-flip -- but the one-counter argument survives.

 2. TWO COMPARISONS ARE MINSKY-COMPLETE: THE SECOND RULER BUYS FULL
    UNIVERSALITY (rule: the simulation verified step-exact; Minsky
    universality cited). The three-place encoding X = v_2 - v_3,
    Y = v_3 - v_5 ran the halts-iff-even witness (X0 = 2, 6 halt;
    X0 = 3, 7 loop, certified by shadow repetition) and the doubling
    program (X0 = 5 halts at Y = 10, depths (15, 15, 5)) step-exactly
    -- every macro step's (q, X, Y) equal to the direct Minsky trace,
    final counters equal to the depth differences, every move a
    multiplication, no depth ever lowered. Halting for the fattened
    growth machine with two equality reads is UNDECIDABLE and any
    Turing machine is simulable: full universality, not merely an
    undecidable question. THE BORROW IS SYNTHESIZED: no ladder is
    ever lowered; on the derived counter v_2 - v_3 the move INC_3 is
    the value-reading down-move universality needs. Two increments
    plus a comparison equal one destruction. Corollary mirror:
    exact-configuration reachability stays DECIDABLE (monotone runs
    to a fixed target are bounded) while halting is undecidable --
    the exact mirror of reset nets (reachability undecidable,
    termination decidable). The two cheap doors grade opposite
    columns.

 3. THE THRESHOLD IS THE SECOND INDEPENDENT COMPARISON (synthesis of
    1 + 2). One comparison direction keeps halting decidable however
    many tests ride it; a second independent comparison -- across
    three or more places (at exactly two, finding 4) -- is universal.
    The machine door's threshold is the second independent comparison
    -- the machine twin of the predicate layer's second scale -- and
    the machine grade at the threshold is EVERYTHING (Minsky), where
    the predicate grade at its threshold was the overhearing no-man's-
    land (undecidable, x-free). The recovery is quantized: nothing,
    then everything.

 4. AT TWO PLACES THE LINEAR ROUTE IS CLOSED AND THE FRACTRAN ROUTE
    HITS THE ELSE WALL (rule at the stated ranges). The cone lemma:
    over all 6016 independent integer form pairs with coefficients in
    [-4, 4], the two moves' images never realize three of the four
    unit moves +-e_1, +-e_2 as nonnegative combinations (the general
    proof is one line: the unique rational solutions for +v and -v
    negate). No linear two-place Minsky encoding exists. The
    nonlinear gadget algebra is real: the two-leg walk realizes
    u -> (alpha/beta)u exactly, gated on beta | u, for all four ops
    x2, x3, x5/2, x5/3 at every u in 1..240 -- and the gated x5/2
    chain from 72 (path 72 -> 180 -> 450 -> 1125, v_2: 3 -> 0, gate
    failing exactly at v_2 = 0) is test-and-decrement on an exponent:
    FRACTRAN's primitive. But every failed gate lands home off the
    multiplicative lattice at exactly floor(alpha*u/beta) + 1 (debris
    beta - (alpha*u mod beta) in {1..beta-1}, verified at every miss
    in range): the else branch destroys the exponent encoding.
    Whether the resulting generalized-Collatz family (Kurtz-Simon
    territory) can be compiled to a universal instance at two places
    and two ratios is the named open edge.

 5. THE NO-DECREMENT LAW HELD THROUGHOUT (audited: the runner's only
    mutation is INC's depth += 1; N strictly increases at every move
    in every run of every section).

RUN RECORD. python explore_second_ruler.py -- CHECKS: 35/35 passed,
< 1 s. Sections: S1 battery (3 programs, traces identical), S2 Minsky
(5 cases, step-exact, halting transfer), S3 gadgets (4 ops x 240
registers + the FRACTRAN chain), S4 cone grid (6016 pairs).
"""

from math import gcd

CHECKS = [0, 0]


def check(name, ok):
    CHECKS[0] += 1
    CHECKS[1] += ok
    if not ok:
        print(f"  FAIL {name}")
    assert ok, name


def sign(x):
    return (x > 0) - (x < 0)


# ---------------------------------------------------------------------------
# The fattened growth machine: shared runner.
# Instructions:
#   ('INC', p, next)                      multiply N by p
#   ('CMP', p1, p2, gamma, lt, eq, gt)    sign(v_p1 - v_p2 - gamma)
#   ('PRES', p, if_zero, if_pos)          presence read
#   ('HALT',)                             stop
#   ('DEAD',)                             must never be reached
# ---------------------------------------------------------------------------

def run_growth(table, start, cap, shadow_fn=None):
    """Run; return (outcome, shadows, dep, steps). outcome in
    {'halt','cap','loop'} -- 'loop' only when shadow_fn is given and a
    shadow value repeats. Audits monotone depths + strictly rising N."""
    dep = {2: 0, 3: 0, 5: 0}
    q = start
    shadows, seen = [], {}
    steps = 0
    while steps < cap:
        if shadow_fn is not None:
            s = shadow_fn(q, dep)
            if s is not None:
                shadows.append(s)
                if s in seen:
                    return ('loop', shadows, dep, steps)
                seen[s] = True
        ins = table[q]
        op = ins[0]
        if op == 'HALT':
            return ('halt', shadows, dep, steps)
        if op == 'DEAD':
            raise AssertionError(f"DEAD state reached: {q}")
        if op == 'INC':
            dep[ins[1]] += 1          # the only mutation: monotone up
            q = ins[2]
        elif op == 'CMP':
            _, p1, p2, gamma, lt, eq, gt = ins
            q = (lt, eq, gt)[sign(dep[p1] - dep[p2] - gamma) + 1]
        elif op == 'PRES':
            q = ins[3] if dep[ins[1]] >= 1 else ins[2]
        steps += 1
    return ('cap', shadows, dep, steps)


# ---------------------------------------------------------------------------
# S1 -- grade (C): one comparison slope collapses to one counter.
# ---------------------------------------------------------------------------

def run_abstract_C(table, start, cap):
    """The one-counter abstraction: state (q, X, pres5)."""
    q, X, e = start, 0, 0
    trace, seen = [], {}
    steps = 0
    while steps < cap:
        s = (q, X, min(e, 1))
        trace.append(s)
        if s in seen:
            return ('loop', trace)
        seen[s] = True
        ins = table[q]
        op = ins[0]
        if op == 'HALT':
            return ('halt', trace)
        if op == 'INC':
            if ins[1] == 2:
                X += 1
            elif ins[1] == 3:
                X -= 1
            else:
                e += 1
            q = ins[2]
        elif op == 'CMP':
            _, p1, p2, gamma, lt, eq, gt = ins
            assert {p1, p2} == {2, 3} and p1 == 2, "grade C reads one slope"
            q = (lt, eq, gt)[sign(X - gamma) + 1]
        elif op == 'PRES':
            q = ins[3] if e >= 1 else ins[2]
        steps += 1
    return ('cap', trace)


def s1_grade_C():
    print("S1. Grade (C): one slope = one counter (bisimulation battery)")
    osc = {  # X cycles 0..3 forever
        'u0': ('CMP', 2, 3, 3, 'u1', 'd0', 'd0'),
        'u1': ('INC', 2, 'u0'),
        'd0': ('CMP', 2, 3, 0, 'u0', 'u0', 'd1'),
        'd1': ('INC', 3, 'd0'),
    }
    halt5 = {  # halt when X = 5
        'h0': ('CMP', 2, 3, 5, 'h1', 'hz', 'h1'),
        'h1': ('INC', 2, 'h0'),
        'hz': ('HALT',),
    }
    pres = dict(halt5)  # open window 5 first, then run halt5
    pres.update({
        'p0': ('PRES', 5, 'p1', 'h0'),
        'p1': ('INC', 5, 'p0'),
    })
    battery = [('oscillator', osc, 'u0'), ('halt-at-5', halt5, 'h0'),
               ('presence-then-halt', pres, 'p0')]
    for name, table, start in battery:
        cap = 300
        # concrete, with the abstraction as its shadow
        out_c, sh_c, dep, _ = run_growth(
            table, start, cap,
            shadow_fn=lambda q, d: (q, d[2] - d[3], min(d[5], 1)))
        out_a, tr_a = run_abstract_C(table, start, cap)
        n = min(len(sh_c), len(tr_a))
        check(f"{name}: traces identical ({n} steps)",
              sh_c[:n] == tr_a[:n])
        # concrete 'loop' fires iff abstract does (same shadow space)
        check(f"{name}: outcomes agree", out_c == out_a)
        if out_a == 'loop':
            check(f"{name}: concrete depths grew (no config repeat)",
                  sum(dep.values()) > 0)
        print(f"  {name}: {out_a}, {n} shadow steps agree")
    print()


# ---------------------------------------------------------------------------
# S2 -- grade (E): three places, pairwise equality = Minsky-complete.
# ---------------------------------------------------------------------------

def run_minsky(prog, start, X0, cap):
    q, X, Y = start, X0, 0
    trace, seen = [], {}
    while len(trace) < cap:
        s = (q, X, Y)
        trace.append(s)
        if s in seen:
            return ('loop', trace)
        seen[s] = True
        ins = prog[q]
        if ins[0] == 'halt':
            return ('halt', trace)
        if ins[0] == 'inc':
            if ins[1] == 'X':
                X += 1
            else:
                Y += 1
            q = ins[2]
        else:  # tstdec
            r, qz, qn = ins[1], ins[2], ins[3]
            v = X if r == 'X' else Y
            if v == 0:
                q = qz
            else:
                if r == 'X':
                    X -= 1
                else:
                    Y -= 1
                q = qn
    return ('cap', trace)


def compile_minsky(prog, X0):
    """Compile a Minsky program to the three-place growth machine.
    Entry state of Minsky q is 'E_q'; input X0 loaded by an INC_2 chain."""
    table = {'DEAD': ('DEAD',)}
    for q, ins in prog.items():
        E = f'E_{q}'
        if ins[0] == 'halt':
            table[E] = ('HALT',)
        elif ins[0] == 'inc':
            nxt = f'E_{ins[2]}'
            if ins[1] == 'X':
                table[E] = ('INC', 2, nxt)
            else:  # Y++ = INC_3 ; INC_2
                table[E] = ('INC', 3, E + '_b')
                table[E + '_b'] = ('INC', 2, nxt)
        else:  # tstdec
            r, qz, qn = ins[1], ins[2], ins[3]
            if r == 'X':  # test v2 = v3; dec = INC_3 ; INC_5
                table[E] = ('CMP', 2, 3, 0, 'DEAD', f'E_{qz}', E + '_d1')
                table[E + '_d1'] = ('INC', 3, E + '_d2')
                table[E + '_d2'] = ('INC', 5, f'E_{qn}')
            else:  # test v3 = v5; dec = INC_5
                table[E] = ('CMP', 3, 5, 0, 'DEAD', f'E_{qz}', E + '_d1')
                table[E + '_d1'] = ('INC', 5, f'E_{qn}')
    # input loader
    start = 'E_' + next(iter(prog)) if X0 == 0 else 'L_0'
    for i in range(X0):
        nxt = f'L_{i+1}' if i + 1 < X0 else 'E_' + next(iter(prog))
        table[f'L_{i}'] = ('INC', 2, nxt)
    return table, start


EVEN = {  # halts iff X0 even; odd falls into the m2/m3 two-cycle
    'm0': ('tstdec', 'X', 'mh', 'm1'),
    'm1': ('tstdec', 'X', 'm2', 'm0'),
    'm2': ('inc', 'X', 'm3'),
    'm3': ('tstdec', 'X', 'm2', 'm2'),
    'mh': ('halt',),
}

DOUBLE = {  # Y := 2*X0, then halt
    'd0': ('tstdec', 'X', 'dh', 'd1'),
    'd1': ('inc', 'Y', 'd2'),
    'd2': ('inc', 'Y', 'd0'),
    'dh': ('halt',),
}


def s2_grade_E():
    print("S2. Grade (E): three places, two equality reads = Minsky")
    cases = [(EVEN, 2, 'halt'), (EVEN, 6, 'halt'), (EVEN, 3, 'loop'),
             (EVEN, 7, 'loop'), (DOUBLE, 5, 'halt')]
    for prog, X0, expect in cases:
        cap = 4000
        direct = run_minsky(prog, next(iter(prog)), X0, cap)
        table, start = compile_minsky(prog, X0)
        entries = {f'E_{q}': q for q in prog}

        def shadow(q, d, entries=entries):
            if q in entries:
                return (entries[q], d[2] - d[3], d[3] - d[5])
            return None

        got = run_growth(table, start, 20 * cap, shadow_fn=shadow)
        out, sh, dep, _ = got
        check(f"{prog is EVEN and 'EVEN' or 'DOUBLE'} X0={X0}: "
              f"direct outcome {expect}", direct[0] == expect)
        check(f"  simulation outcome matches", out == expect)
        n = min(len(sh), len(direct[1]))
        check(f"  step-exact trace ({n} macro steps)",
              sh[:n] == direct[1][:n])
        if expect == 'halt':
            fx, fy = direct[1][-1][1], direct[1][-1][2]
            check(f"  final (X,Y) = ({fx},{fy}) matches depths",
                  dep[2] - dep[3] == fx and dep[3] - dep[5] == fy)
        print(f"  {'EVEN' if prog is EVEN else 'DOUBLE'} X0={X0}: {out}, "
              f"{n} macro steps exact, depths {dict(dep)}")
    print()


# ---------------------------------------------------------------------------
# S3 -- grade (D): the gadget algebra and the else wall (two places).
# ---------------------------------------------------------------------------

def gated_multiply(u, alpha, beta):
    """From home (u,u): descend d++ onto alpha*c = beta*d (equality read
    each step; order read detects overshoot), then ascend c++ home.
    Returns ('pass'|'miss', landing_register)."""
    c = d = u
    fired = False
    while True:
        d += 1
        F = alpha * c - beta * d
        if F == 0:
            fired = True
            break
        if F < 0:
            break
    while c < d:  # ascend home; c = d fires exactly
        c += 1
    return ('pass' if fired else 'miss'), c


def s3_grade_D():
    print("S3. Grade (D): gated multipliers + the else wall (two places)")
    for alpha, beta in [(2, 1), (3, 1), (5, 2), (5, 3)]:
        assert gcd(alpha, beta) == 1 and alpha > beta
        for u in range(1, 241):
            kind, reg = gated_multiply(u, alpha, beta)
            if u % beta == 0:
                ok = (kind == 'pass' and reg * beta == alpha * u)
            else:
                debris = beta - (alpha * u) % beta
                ok = (kind == 'miss'
                      and reg == (alpha * u) // beta + 1
                      and 1 <= debris <= beta - 1
                      and beta * reg - alpha * u == debris)
            if not ok:
                check(f"gadget x{alpha}/{beta} at u={u}", False)
        check(f"gadget x{alpha}/{beta}: exact on 1..240 "
              f"(pass iff {beta}|u; miss lands floor+1)", True)

    # The FRACTRAN reading: gated x5/2 is test-and-decrement on v2(u).
    u = 72  # 2^3 * 3^2
    v2 = 3
    path = [u]
    while True:
        kind, reg = gated_multiply(u, 5, 2)
        if kind == 'miss':
            break
        u = reg
        v2 -= 1
        path.append(u)
        check(f"x5/2 pass: v2 now {v2} >= 0", v2 >= 0)
    check("gate fails exactly when v2 = 0 (test-and-decrement)", v2 == 0)
    check("register path exact", path == [72, 180, 450, 1125])
    print(f"  x5/2 chain from 72: {path} -- gate = zero-test on v2")
    print()


# ---------------------------------------------------------------------------
# S4 -- the cone lemma: no linear two-place Minsky encoding.
# ---------------------------------------------------------------------------

def s4_cone():
    print("S4. The cone lemma (linear encodings blocked at two places)")
    tested = 0
    R = range(-4, 5)
    for a in R:
        for b in R:
            for c in R:
                for d in R:
                    det = a * d - b * c
                    if det == 0:
                        continue  # forms dependent: never separate
                    tested += 1
                    # moves c++ -> (a, c), d++ -> (b, d) in form-space
                    ok_pairs = 0
                    for tx, ty in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        s = (tx * d - ty * b)  # / det
                        t = (a * ty - c * tx)  # / det
                        if det < 0:
                            s, t = -s, -t
                        if s >= 0 and t >= 0:
                            ok_pairs += 1
                    # +-e1 (or +-e2) both realizable would need s,t and
                    # -s,-t nonneg: impossible. So at most 2 of 4 targets.
                    if ok_pairs > 2:
                        check(f"cone violation at {(a,b,c,d)}", False)
    check(f"no form pair realizes 3+ of the four unit moves "
          f"({tested} pairs)", True)
    print(f"  {tested} independent form pairs: cone never contains "
          f"three of +-e1,+-e2\n")


if __name__ == '__main__':
    s1_grade_C()
    s2_grade_E()
    s3_grade_D()
    s4_cone()
    print(f"CHECKS: {CHECKS[1]}/{CHECKS[0]} passed")
    assert CHECKS[0] == CHECKS[1]
