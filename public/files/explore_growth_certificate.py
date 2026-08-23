"""
explore_growth_certificate.py -- CERTIFYING INFINITE GROWTH: the one
residual the born-at-zero normal form leaves, attacked with a derived
certificate battery. (Sibling of explore_born_at_zero.py, whose VM,
supplies and program battery this file reuses verbatim.)

THE SETTING. The growing-window machine: windows are copies of Z/m_j
with moduli drawn from a supply, appended by GROW with every register
born 0; ADD/SUB/MUL/write-constant are componentwise and BROADCAST to
every window at once; the one cross-window read is a global 1-bit
zero-test (register a zero in ALL windows); finite program-counter
control. The born-at-zero normal form (theorem, explore_born_at_zero.py)
says a window born at op-index b with modulus m holds E(w_{b..t}) mod m,
E the free integer evaluation of that suffix from all-zero. Off that
normal form, deciding halting REDUCES to semi-deciding "the run grows
infinitely often": the plain decider is complete for every run with
finitely many grows, so if every forever-growing program admitted a
finite certificate of growing forever, the whole sublinear side would be
decidable. THAT RESIDUAL IS THIS FILE'S QUESTION. Two facts bound the
answer from outside and are not re-derived here: the certificate cannot
be supply-uniform (the adversarial supply, explore_pending_fires.py),
and on the linear-rate side certifying growth would decide the simulated
machine.

THE QUESTION. Is there a SOUND finite certificate of infinite growth,
what does it cover, and where exactly does it stop?

THE HAND ATTACK (on paper, before this file's engine; the derivation
this rig then checks). A candidate certificate is a SEGMENT of the run
between two op-times t1 < t2 with equal program counter and at least one
GROW inside it. The segment repeats forever iff every TEST inside it
reads the same bit on every future repetition -- so the whole question
is which test bits are FORCED. The normal form gives three forcings,
and the derivation of each is that it survives the pool only GROWING:

  LOCK-ONE (bit forced 1). The last write to the tested register inside
  the segment is write-constant 0. Then every window born before that
  op carries the WC in its suffix and reads 0, and every window born
  after it was born 0 with the register untouched -- so ALL windows
  read 0, at any age, any modulus, any pool. Adding windows preserves
  it, since a fresh window also reads 0.

  LOCK-ZERO-C (bit forced 0). The last write inside the segment is
  write-constant c != 0, and some window already in the pool at t1 has
  m not dividing c. That window reads c mod m != 0 at the corresponding
  offset of EVERY repetition (the last write is segment-local), and a
  window never leaves the pool, so the AND is 0 forever. Adding windows
  preserves a 0.

  LOCK-ZERO-F (bit forced 0, and this one SPENDS THE SUPPLY). Let the
  window born at the last GROW before the test have modulus m. Its
  suffix is exactly the segment word from that grow to the test, so its
  content is a FIXED integer E_a -- the same integer on every
  repetition. If E_a != 0 and m > |E_a| then m does not divide E_a and
  the AND is 0. On a NON-DECREASING unbounded supply the modulus at
  that grow only rises, so checking it once at t1 certifies every later
  repetition. On a bounded supply the lock is unavailable by
  construction -- the certificate is supply-specific, which is the shape
  the adversarial-supply result already demanded.

  THE ASYMMETRY THE DERIVATION EXPOSES, and the reason the residual is
  hard: forcing a ZERO needs ONE witness window and witnesses persist,
  while forcing a ONE needs EVERY window -- including windows of
  unbounded age whose suffixes lengthen by a whole segment at each
  repetition, and whose contents this normal form gives no handle on
  beyond replaying them. So the two directions are not symmetric and the
  difficulty of the residual is entirely in the forced-ONE direction.

  WHAT THE CERTIFICATE THEREFORE CANNOT BE. It is SOUND, never complete:
  a program whose growth is gated by a test reading an age-dependent
  value (a counter, a t mod m clock, the Fibonacci window of
  explore_born_at_zero.py S3) has bits that genuinely move with the
  pool, and no segment-local forcing applies.

THE DESIGN (findings enter by a separate post-run edit; kills are frozen
as OBSERVABLES, never as inferences).

D1  SOUNDNESS, the positive control that gates everything. Every
    program this rig CERTIFIES is then simulated far past the
    certifying segment; it must still be running and must reach a grow
    count far above the one the segment was found at.
    KILL (prints as UNSOUND): a certified program that halts, or that
    fails to reach 600 grows, inside the soundness cap. The derivation
    above is then false and nothing else in the run may be read.

D2  THE BATTERY, the second positive control. The corpus's three known
    programs (explore_born_at_zero.py S2): a halting program, a
    frozen-pulse non-halter with finitely many grows, and a
    forever-growing loop. Expected: NO CERTIFICATE for the first two
    (neither grows forever), CERTIFICATE for the third. A fourth,
    built here: a DATA-GATED grower whose loop tests a register the
    ops write, which the derivation says is outside every lock.
    KILL (prints as MISFIRE): a certificate for the halting program or
    the frozen pulse.

D3  COVERAGE. A random population on the sqrt supply, each program
    classified by simulation into halts / loops (configuration repeat
    with no grow between) / GROW-HEAVY (120 grows reached inside the
    cap -- an OBSERVATION and never a decision, since "grows forever"
    is exactly the undecided predicate). Over the grow-heavy class,
    what share does the certificate cover, by which lock, and -- read
    separately, because it is the share that costs the derivation
    nothing -- how much of that share is segments holding NO TEST at
    all. A branch-free cycle repeats because nothing in it can branch;
    that costs the normal form nothing and is not a lock.
    KILL (prints as VACUOUS): the certificate covers ZERO grow-heavy
    programs -- the scheme is empty in practice whatever its
    derivation.
    PREDICTION FROZEN: a MINORITY, under half, because a random loop's
    test reads a register the ops write and no lock is segment-local
    there.

D4  THE RESIDUE'S SHAPE. For every uncovered grow-heavy program, the
    reason its segment failed, tallied as a PAIR because the two
    dimensions are independent and a single label would hide one of
    them: HOW the tested register was last written inside the segment
    (data op / write-constant / not written there) CROSSED WITH what
    the fresh window's integer reads (0, non-zero but not smaller than
    the modulus, or past the magnitude guard).
    PREDICTION FROZEN: the dominant cell is the forced-ONE direction --
    a fresh integer of 0, under any write kind -- and not the
    magnitude guard.

D7  THE ROBUSTNESS SWEEP, which the coverage census cannot do without.
    D3 is ONE draw, and every number it reports is a statistic of that
    draw; the split it exists to report is worth nothing until the draw
    is varied. Three dials, one at a time: the STEP CAP behind the
    grow-heavy label (which is the one that could bias the population,
    since a loop with more tests takes more steps per grow and a low
    cap would drop exactly the programs the census is about), the SEED,
    and the PROGRAM LENGTH.
    KILL (prints as DRAW-BOUND), frozen as a printed number and not as
    a judgement: the trivial share of certificates spans more than 25
    points across the cells, or the forced-ONE share of the uncovered
    spans more than 15 -- D3 and D4 are then statements about a seed and
    not about the certificate. Both spans are printed whether or not the
    kill fires.
    KILL (prints as SWEEP-BUG): any cell where a lock forces a bit the
    machine did not read. The census arm prints its own; without this
    the sweep would swallow one.
    Reported as RANGES, and any figure quoted from a single draw is
    quoted with its range beside it.

D6  THE DESIGNED ARM, one program per lock. A random population cannot
    be relied on to exercise a lock at all: a lock's antecedent is a
    conjunction, and a population that never meets it says nothing
    about the lock and equally nothing about D5's supply comparison,
    which is a DIFFERENCE between two certified sets and is empty
    whenever the supply-spending lock is unreached. So each lock gets a
    program built to make it the ONLY one available:
      ONE     loop { GROW; WC(a,0); TEST a }        -- every window 0
      ZERO-C  loop { GROW; WC(a,3); TEST a }        -- an old window
                                                       reads 3 mod 2
      ZERO-F  loop { GROW; WC(b,1); ADD a,b,b; TEST a }
                                                    -- a is DATA-written,
                                                       the fresh window
                                                       reads the integer 2
    Expected: each is CERTIFIED on the sqrt supply with exactly its own
    lock firing and no other. The ZERO-F program is then re-certified
    on the BOUNDED supply, where the lock is unavailable by
    construction.
    KILL (prints as ARM-MISS): a designed program that fails to fire
    the lock it was built for -- the lock is then unreachable and the
    derivation that introduced it is decoration.
    KILL (prints as BOUNDED-CERT): the ZERO-F program certified on the
    bounded supply too -- the lock does not in fact spend the supply.

D5  SUPPLY-SPECIFICITY, read rather than argued. Two arms, and only one
    of them can carry a kill. The POPULATION arm certifies the same
    random programs against the BOUNDED supply and reports the
    difference -- but that difference is a DIAGNOSTIC and not a test,
    because it is empty by arithmetic whenever LOCK-ZERO-F fires zero
    times on that population, and a population is not built to make a
    lock's antecedent reachable. The kill therefore sits on D6's
    DESIGNED arm, where the antecedent is built: it prints as
    BOUNDED-CERT and fires if the ZERO-F program certifies on the
    bounded supply too.

FINDINGS (entered post-run, from the printed output).

SETTLING POINTER (explore_forced_one.py, which supersedes
the two coverage readings below). What survives here
unchanged: the three locks and their soundness, the supply-specificity
witnessed at the designed arm, and every number this file prints, which
are all statements about THIS lock set. What does NOT survive as a
statement about the certificate: F4's split (93-100% of certificates
holding no test) and F5's one-directional residue are properties of the
three locks, not of the scheme -- the forced-ONE direction turned out to
be an instrument this file lacked rather than a wall, and with it
attached the same draw certifies 102 of 109 and the residue is ONE once
the certifier's arbitrary choice of segment is swept. Two things read
here as harder than they are: the D2 battery's "data-gated" grower
writes its constant to an EMPTY POOL, so every window increments by zero
and it is data-gated in name only; and this file's own F6 lesson about
the arbitrary CUT POINT has a second level it did not reach -- which
repeat of a program counter the segment is taken at is equally the
certifier's choice, and sweeping it moves the residue from 7 to 1.

F1  THE CERTIFICATE EXISTS AND IT IS SOUND (rule; the derivation above
    is the ground, this run its cross-check). Three locks, each
    derived from the normal form and each surviving the pool only
    growing. 56 certified programs -- 52 from the random population, 3
    designed, and the battery's forever-growing loop -- replayed to 600
    grows apiece: 0 UNSOUND, no halt and no stall. The certifier also
    cross-checks each forcing against the bit the run actually read, at
    every call it makes: 0 disagreements. Count the forcings before
    reading that as reach -- the census cell makes SIX (3 in the
    population, 1 per designed arm), because a certified segment holding
    no test forces nothing and 49 of the 52 hold none, and D7's six
    further populations repeat the check at their own lock-carried
    counts. It is a cross-check on the locks and never evidence of how
    far they reach.

F2  EACH LOCK IS REACHABLE, AND EACH FIRES ALONE (property by
    construction, the designed arm). The ONE, ZERO-C and ZERO-F
    programs certify with exactly their own lock firing and the other
    two at zero. None of the three is decoration.

F3  THE SCHEME SPENDS THE SUPPLY, AND THAT IS WITNESSED RATHER THAN
    ARGUED (rule at the designed arm). The ZERO-F program is CERTIFIED
    on the sqrt supply and NO-CERTIFICATE on the bounded one, failing
    there with "fresh non-zero, modulus too small" -- the lock needs a
    modulus that outgrows a fixed integer, so a bounded supply cannot
    carry it. The certificate is therefore supply-specific in exactly
    the place the adversarial-supply result demands, and the
    specificity has a program rather than an argument behind it. THE
    POPULATION ARM OF D5 SAYS NOTHING EITHER WAY, and the first version
    of this file mis-specified it as a kill: the bounded supply
    certifies exactly the same random programs as sqrt, but LOCK-ZERO-F
    fires ZERO times on that population, so the comparison is empty by
    arithmetic rather than uniform by fact. The design above now carries
    the kill where its antecedent is built.

F4  COVERAGE IS ALMOST ENTIRELY THE TRIVIAL CASE, AND THE SPLIT IS THE
    FINDING (observation; 600 random programs, 109 grow-heavy).
    52 of the 109 certify -- 47.7% -- but 49 of those 52 hold NO TEST
    in their segment, and a cycle with no branch in it repeats for the
    reason that it has no branch -- no lock, no normal form, and no
    pigeonhole either (the corpus's pigeonhole certifies a LOOP with no
    grow, which is the opposite case). LOCK-CARRIED coverage in this draw
    is 3 of 109, all of it LOCK-ONE, and ZERO-C and ZERO-F fire zero
    times off the designed arm. READ THAT 3 AGAINST D7'S RANGE AND
    NEVER ALONE: across the six sweep cells the lock-carried count runs
    0 to 3 per ~110 grow-heavy programs, so at another seed this
    population would have printed VACUOUS, and the honest reading of
    the census is that lock-carried coverage is NIL to a handful, not
    2.8%. What is stable is the SPLIT: 93-100% of every draw's
    certificates hold no test. The frozen prediction (a minority, under
    half) held on the loose reading and held by an order of magnitude
    on the tight one.

F5  THE RESIDUE IS ONE-DIRECTIONAL, EXACTLY AS THE ASYMMETRY DERIVED
    (observation; the prediction held; stable across D7's dials at
    97-99%). 56 of the 57 uncovered
    grow-heavy programs fail with the fresh window reading 0 -- the
    forced-ONE direction, the one the hand attack derived as having no
    instrument, because forcing a ONE needs EVERY window while forcing
    a ZERO needs one witness. The remaining 1 is a near-miss for
    ZERO-F, its modulus too small at that grow. THE MAGNITUDE GUARD
    FIRES ZERO TIMES: the obstruction is structural and not arithmetic
    size, so a bigger integer budget buys nothing here.

F6  THE CUT POINT WAS THE CERTIFIER'S AND NOT THE PROGRAM'S (a rig
    correction, entered before F5 was read). A cycle may be entered at
    any of its own program counters, and the first version cut it
    wherever the pc first repeated -- which left 15 of the 57 failing
    for the reason "no grow before the test", a statement about where
    the certifier cut and not about the program. Rotating the segment
    to start at a GROW raises the forced-ONE total from 41 to 56 --
    exactly the 15 -- and changes the certified count by ZERO. The
    per-cell attribution moved too (data-written with a fresh read of 0
    ran 14 before and 10 after, const-written with a fresh read of 0
    ran 2 and then 0), so this is a change in the TOTAL and not a
    traceable per-program transfer, which the tallies cannot establish.
    The cut never cost a certificate. It mis-attributed a quarter of
    the residue, and a residue tally is the whole output of D4.

F7  THE CENSUS IS NOT A STATEMENT ABOUT A SEED (observation; the sweep,
    one dial at a time off the census cell). The STEP CAP behind the
    grow-heavy label -- the dial that could have biased the population,
    since a loop carrying more tests takes more steps per grow -- moves
    NOTHING: 4,000, 12,000 and 30,000 give the identical 109 / 52 / 49 /
    3 / 56. Seed and program length move the counts and leave both
    shares: trivial share of certified 93-100%, forced-ONE share of
    uncovered 97-99%, lock-carried count 0-3. So F4's split and F5's
    direction are properties of the certificate; F4's 3 is a property
    of a draw.

WHAT THIS LEAVES. A sound certificate of infinite growth EXISTS, so
"can one be built at all" is answered and the residual is not. The
residual asks whether EVERY forever-growing program is certifiable,
and what this file bounds is THIS scheme: where it stops is the
forced-ONE direction, with no claim that a different scheme meets the
same wall. The normal form sharpens that stopping point into two
halves that are not the same question: for a window ALREADY in the pool, the segment acts as a map
on (Z/m)^r and its orbit is eventually periodic, so "reads 0 at this
offset in every repetition" is DECIDABLE per window; for windows born
in LATER repetitions, the content is a free integer evaluation of a
word that lengthens by a whole segment each time, and forcing it to 0
for every repetition is a question about the segment word's action
over Z rather than over any Z/m. That second half is the sharp form of
where this scheme stops, and it is the next probe, not a claim made
here.

RUN RECORD: python explore_growth_certificate.py -> D2 battery pass
(halting and frozen-pulse NO-CERTIFICATE, forever-growing CERTIFIED,
data-gated NO-CERTIFICATE); D6 arm pass, all three locks firing alone,
ZERO-F NO-CERTIFICATE on the bounded supply; D3 109 grow-heavy of 600,
52 certified of which 49 branch-free, locks ONE 3 / ZERO-C 0 / ZERO-F 0;
D4 residue 46 unwritten-in-segment + 10 data-written with a fresh read
of 0, 1 const-written with the modulus too small; D5 population
diagnostic EMPTY (ZERO-F fires 0 times there); D1 0 UNSOUND of 52; D7
trivial share 93-100% (span 7 against a kill at 25), forced-ONE share
97-99% (span 1 against a kill at 15), lock-carried 0-3, the step cap
moving nothing;
VERDICT all pass, exit 0. Wall 2.7 s, memory trivial (no numpy).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_born_at_zero import (          # the machine, verbatim
    ADD, SUB, MUL, WC, GROW, TEST, JMP, HALT, SUPPLIES, VM,
)

MAG_GUARD = 4096          # bit-length ceiling for the free integer evaluation


# ------------------------------------------------- the free integer replay

def free_eval(word, r):
    """Free evaluation of an op word over Z from all-zero -- no modulus.
    Returns (cols, overflowed): the integer register vector, and whether
    any value passed the magnitude guard (in which case the vector is
    NOT trustworthy and the certifier must decline)."""
    col = [0] * r
    over = False
    for ins in word:
        op = ins[0]
        if op in (ADD, SUB, MUL):
            _, a, b, c = ins
            v = (col[b] + col[c]) if op == ADD else \
                (col[b] - col[c]) if op == SUB else (col[b] * col[c])
            if v.bit_length() > MAG_GUARD:
                over = True
                v = 0
            col[a] = v
        elif op == WC:
            col[ins[1]] = ins[2]
    return col, over


# ------------------------------------------------- the certifier

def find_segment(prog, supply, r, cap):
    """Run the machine; return the first segment (t1, t2) of EXECUTED
    steps with equal pc, at least one GROW between, and no halt --
    together with the executed instruction list and the pool at t1.
    Returns None if the run halts or no such segment appears."""
    vm = VM(prog, supply, r)
    seen = {}                # pc -> (step index, grows so far, pool then)
    executed = []            # (pc, instruction, bit-if-TEST)
    for t in range(cap):
        if vm.halted:
            return None
        pc = vm.pc
        if not (0 <= pc < len(prog)):
            return None
        ins = prog[pc]
        bit = None
        if ins[0] == TEST:
            bit = all(col[ins[1]] == 0 for col in vm.cols)
        if pc in seen:
            t1, g1, pool1 = seen[pc]
            if vm.g > g1:
                return (t1, t, executed, pool1)
        else:
            seen[pc] = (t, vm.g, list(vm.moduli))
        executed.append((pc, ins, bit))
        vm.step()
    return None


def certify(prog, supply, r, cap):
    """Search for a segment and try to force every TEST inside it.
    Returns (verdict, detail): CERTIFIED with the lock tally, or
    NO-CERTIFICATE with the first unforced reason."""
    seg = find_segment(prog, supply, r, cap)
    if seg is None:
        return "NO-CERTIFICATE", "no cycling segment with a grow"
    t1, t2, executed, pool = seg
    body = executed[t1:t2]
    if not any(ins[0] == GROW for _, ins, _ in body):
        return "NO-CERTIFICATE", "segment holds no grow"
    # THE CUT IS ARBITRARY: a cycle can be entered at any of its own
    # program counters, so rotate the body to start at a GROW. Every
    # test then has a fresh window behind it, and a test that failed
    # only for sitting ahead of the segment's grow fails no longer.
    rho = next(i for i, (_, ins, _) in enumerate(body) if ins[0] == GROW)
    g0 = sum(1 for _, i, _ in executed[:t1] if i[0] == GROW)
    for _, i, _ in body[:rho]:
        if i[0] == GROW:
            g0 += 1
            pool = pool + [supply(g0)]
    body = body[rho:] + body[:rho]
    # LOCK-ZERO-F needs the supply non-decreasing FOREVER; this is a
    # PREFIX check and the guarantee it gives is only as good as the
    # supply's closed form, which for the three supplies here is known.
    monotone = all(supply(g) <= supply(g + 1) for g in range(1, 400))
    unbounded = supply(400) > supply(1)
    locks = {"ONE": 0, "ZERO-C": 0, "ZERO-F": 0}
    word = [ins for _, ins, _ in body]
    for s, (_, ins, bit) in enumerate(body):
        if ins[0] != TEST:
            continue
        a = ins[1]
        # last write to register a inside the segment, before offset s
        last = None
        for u in range(s - 1, -1, -1):
            op = word[u]
            if op[0] in (ADD, SUB, MUL) and op[1] == a:
                last = ("data", None)
                break
            if op[0] == WC and op[1] == a:
                last = ("const", op[2])
                break
        forced = None
        if last is not None and last[0] == "const":
            c = last[1]
            if c == 0:
                forced = (True, "ONE")
            elif any(m and c % m != 0 for m in pool):
                forced = (False, "ZERO-C")
        if forced is None and monotone and unbounded:
            # LOCK-ZERO-F: the window born at the last grow before s
            gpos = None
            for u in range(s - 1, -1, -1):
                if word[u][0] == GROW:
                    gpos = u
                    break
            if gpos is not None:
                cols, over = free_eval(word[gpos + 1:s], r)
                if not over and cols[a] != 0:
                    # that window's modulus, as seen in this traversal
                    grows_before = g0 + sum(1 for _, i, _ in body[:gpos + 1]
                                            if i[0] == GROW)
                    m = supply(grows_before)
                    if m > abs(cols[a]):
                        forced = (False, "ZERO-F")
        if forced is None:
            kind = ("data-written" if (last is not None and last[0] == "data")
                    else "const-written" if last is not None
                    else "unwritten-in-segment")
            gpos = None
            for u in range(s - 1, -1, -1):
                if word[u][0] == GROW:
                    gpos = u
                    break
            if gpos is None:
                fresh = "no grow before the test"
            else:
                cols, over = free_eval(word[gpos + 1:s], r)
                fresh = ("past the magnitude guard" if over
                         else "fresh reads 0" if cols[a] == 0
                         else "fresh non-zero, modulus too small")
            return "NO-CERTIFICATE", kind + " / " + fresh
        if forced[0] != bit:
            return "BUG", "forced %s but the run read %s" % (forced[0], bit)
        locks[forced[1]] += 1
    return "CERTIFIED", locks


def still_growing(prog, supply, r, cap, target):
    """Simulate far past the certifying segment: does the run stay alive
    and reach TARGET grows inside the step cap?"""
    vm = VM(prog, supply, r)
    for t in range(cap):
        vm.step()
        if vm.halted:
            return False, t, vm.g
        if vm.g >= target:
            return True, t, vm.g
    return False, cap, vm.g


# ------------------------------------------------- D1 + D2: the battery

def battery(r=3):
    p_halt = [(GROW,), (GROW,), (GROW,), (WC, 1, 1)] + \
             [(ADD, 0, 0, 1)] * 5 + [(HALT,)]
    p_pulse = [(GROW,), (GROW,), (GROW,), (WC, 1, 1),
               (ADD, 0, 0, 1), (TEST, 0, 4), (JMP, 4)]
    p_grow = [(WC, 1, 1), (GROW,), (ADD, 0, 0, 1), (JMP, 1)]
    # data-gated grower: the loop's test reads a register the ops write
    p_gated = [(WC, 1, 1), (GROW,), (ADD, 0, 0, 1), (TEST, 0, 5),
               (JMP, 1), (JMP, 1)]
    cases = (("halting", p_halt, "NO-CERTIFICATE"),
             ("frozen-pulse", p_pulse, "NO-CERTIFICATE"),
             ("forever-growing", p_grow, "CERTIFIED"),
             ("data-gated", p_gated, "NO-CERTIFICATE"))
    ok = True
    misfire = False
    unsound = False
    for name, prog, expect in cases:
        v, d = certify(prog, SUPPLIES["sqrt"], r, cap=4000)
        print("D2 %s: %s  (%s)" % (name, v, d))
        if v == "CERTIFIED":
            alive, t, g = still_growing(prog, SUPPLIES["sqrt"], r,
                                        cap=40000, target=600)
            print("D1   soundness replay: reached-600-grows=%s, grows=%d "
                  "at step %d" % (alive, g, t))
            if not alive:
                unsound = True
            if name in ("halting", "frozen-pulse"):
                misfire = True
        ok = ok and v == expect
    if misfire:
        print("D2 ** MISFIRE **")
    if unsound:
        print("D1 ** UNSOUND **")
    return ok and not misfire and not unsound


# ------------------------------------------------- D7: the sweep

def sweep(r=3):
    """One dial at a time off the census cell (600 programs, seed 11,
    cap 4000, length 12). Prints the ranges every D3/D4 figure is to be
    read against."""
    import random
    rows = []
    any_bug = 0
    cells = ([("cap", c, 11, 12, c) for c in (4000, 12000, 30000)] +
             [("seed", sd, sd, 12, 4000) for sd in (23, 47)] +
             [("length", 20, 11, 20, 4000)])
    for dial, val, seed, length, cap in cells:
        rng = random.Random(seed)
        heavy = []
        for _ in range(600):
            prog = random_program(rng, r, length)
            if classify(prog, SUPPLIES["sqrt"], r, cap)[0] == "grow-heavy":
                heavy.append(prog)
        cert = triv = one = bugs = 0
        for prog in heavy:
            v, d = certify(prog, SUPPLIES["sqrt"], r, cap)
            if v == "CERTIFIED":
                cert += 1
                if not any(d.values()):
                    triv += 1
            elif v == "BUG":
                bugs += 1
                print("D7 ** SWEEP-BUG ** %s" % (d,))
            elif "fresh reads 0" in d:
                one += 1
        any_bug = any_bug or bugs
        rows.append((dial, val, len(heavy), cert, triv, cert - triv,
                     len(heavy) - cert, one))
        print("D7 %-6s=%-6s heavy %3d, certified %3d (trivial %3d, "
              "lock-carried %2d), uncovered %3d of which forced-ONE %3d"
              % (dial, val, rows[-1][2], cert, triv, cert - triv,
                 rows[-1][6], one))
    triv_share = [100.0 * t / c for _, _, _, c, t, _, _, _ in rows if c]
    one_share = [100.0 * o / u for _, _, _, _, _, _, u, o in rows if u]
    locks = [k for _, _, _, _, _, k, _, _ in rows]
    print("D7 RANGES: trivial share of certified %.0f-%.0f%% (span %.0f, "
          "kill at 25), forced-ONE share of uncovered %.0f-%.0f%% (span "
          "%.0f, kill at 15), lock-carried count %d-%d"
          % (min(triv_share), max(triv_share),
             max(triv_share) - min(triv_share), min(one_share),
             max(one_share), max(one_share) - min(one_share),
             min(locks), max(locks)))
    bound = (max(triv_share) - min(triv_share) > 25
             or max(one_share) - min(one_share) > 15)
    if bound:
        print("D7 ** DRAW-BOUND **")
    return not bound and not any_bug


# ------------------------------------------------- D6: the designed arm

def designed_arm(r=3, lead=30):
    """One program per lock, each built so that its lock is the only one
    available. LEAD grows run first so the pool at the segment's start is
    non-empty and the supply has climbed off its floor -- both are
    antecedents of a lock and neither is a property of the loop."""
    head = [(GROW,)] * lead
    b = lead - 1                       # the loop's own GROW sits here
    p_one = head + [(WC, 0, 0), (TEST, 0, b + 3), (JMP, b)]
    p_zc = head + [(WC, 0, 3), (TEST, 0, b + 3), (JMP, b)]
    p_zf = head + [(WC, 1, 1), (ADD, 0, 1, 1), (TEST, 0, b + 4), (JMP, b)]
    ok = True
    for name, prog, want in (("ONE", p_one, "ONE"),
                             ("ZERO-C", p_zc, "ZERO-C"),
                             ("ZERO-F", p_zf, "ZERO-F")):
        v, d = certify(prog, SUPPLIES["sqrt"], r, cap=4000)
        fired = [k for k, n in d.items() if n] if v == "CERTIFIED" else []
        hit = (v == "CERTIFIED" and fired == [want])
        print("D6 %-6s arm: %s  locks %s%s"
              % (name, v, d if v == "CERTIFIED" else d,
                 "" if hit else "  ** ARM-MISS **"))
        if hit:
            alive, t, g = still_growing(prog, SUPPLIES["sqrt"], r,
                                        cap=40000, target=600)
            print("D1   soundness replay: reached-600-grows=%s, grows=%d "
                  "at step %d" % (alive, g, t))
            if not alive:
                print("D1 ** UNSOUND **")
                ok = False
        ok = ok and hit
    vb, db = certify(p_zf, SUPPLIES["const"], r, cap=4000)
    bad = (vb == "CERTIFIED")
    print("D5 ZERO-F arm on the BOUNDED supply: %s (%s)%s"
          % (vb, db, "  ** BOUNDED-CERT **" if bad else ""))
    return ok and not bad


# ------------------------------------------------- D3 + D4 + D5

def random_program(rng, r, length):
    prog = []
    for _ in range(length):
        k = rng.random()
        if k < 0.34:
            op = rng.choice((ADD, SUB, MUL))
            prog.append((op, rng.randrange(r), rng.randrange(r), rng.randrange(r)))
        elif k < 0.50:
            prog.append((WC, rng.randrange(r), rng.randrange(-2, 4)))
        elif k < 0.66:
            prog.append((GROW,))
        elif k < 0.82:
            prog.append((TEST, rng.randrange(r), rng.randrange(length)))
        elif k < 0.96:
            prog.append((JMP, rng.randrange(length)))
        else:
            prog.append((HALT,))
    return prog


def classify(prog, supply, r, cap, grow_target=120):
    """halts / loops (config repeat, no grow between) / grow-heavy (the
    run reaches GROW_TARGET grows inside the step cap -- an observation,
    never a decision) / stalled (alive at the cap, grows short of it)."""
    vm = VM(prog, supply, r)
    seen = set()
    for t in range(cap):
        cfg = vm.config()
        if cfg in seen:
            return "loops", vm.g
        seen.add(cfg)
        gb = vm.g
        vm.step()
        if vm.halted:
            return "halts", vm.g
        if vm.g != gb:
            seen.clear()
            if vm.g >= grow_target:
                return "grow-heavy", vm.g
    return "stalled", vm.g


def population(trials=600, r=3, length=12, seed=11, cap=4000):
    import random
    rng = random.Random(seed)
    kinds = {}
    heavy = []
    for _ in range(trials):
        prog = random_program(rng, r, length)
        k, g = classify(prog, SUPPLIES["sqrt"], r, cap)
        kinds[k] = kinds.get(k, 0) + 1
        if k == "grow-heavy":
            heavy.append(prog)
    print("D3 population: " + ", ".join("%s %d" % (k, v)
                                        for k, v in sorted(kinds.items())))
    tally = {"ONE": 0, "ZERO-C": 0, "ZERO-F": 0}
    reasons = {}
    certified = []
    trivial = 0
    bugs = 0
    for prog in heavy:
        v, d = certify(prog, SUPPLIES["sqrt"], r, cap)
        if v == "CERTIFIED":
            certified.append(prog)
            if not any(d.values()):
                trivial += 1
            for k in tally:
                tally[k] += d[k]
        elif v == "BUG":
            bugs += 1
            print("D3 ** BUG ** %s" % (d,))
        else:
            reasons[d] = reasons.get(d, 0) + 1
    n = len(heavy)
    share = (100.0 * len(certified) / n) if n else 0.0
    print("D3 grow-heavy %d, CERTIFIED %d (%.1f%%), of which %d hold NO "
          "TEST (branch-free cycles) and %d fire a lock; "
          "locks fired %s%s"
          % (n, len(certified), share, trivial, len(certified) - trivial,
             tally, "  ** VACUOUS **" if n and not certified else ""))
    print("D4 residue by write-kind / fresh-read: " + ", ".join(
        "%s %d" % (k, v) for k, v in sorted(reasons.items(),
                                            key=lambda x: -x[1])))
    unsound = 0
    for prog in certified:
        alive, t, g = still_growing(prog, SUPPLIES["sqrt"], r,
                                    cap=20000, target=600)
        if not alive:
            unsound += 1
    print("D1 soundness over the certified population: %d UNSOUND of %d"
          % (unsound, len(certified)))
    # D5: the same population against the bounded supply
    cert_b = 0
    shared = 0
    for prog in heavy:
        if classify(prog, SUPPLIES["const"], r, cap)[0] != "grow-heavy":
            continue
        shared += 1
        if certify(prog, SUPPLIES["const"], r, cap)[0] == "CERTIFIED":
            cert_b += 1
    print("D5 population diagnostic: %d certified on the bounded supply of "
          "the %d that stay grow-heavy there, against %d of %d on sqrt%s"
          % (cert_b, shared, len(certified), n,
             "  -- EMPTY COMPARISON, ZERO-F fired 0 times here"
             if not tally["ZERO-F"] else ""))
    return bugs == 0 and unsound == 0 and (not n or bool(certified))


if __name__ == "__main__":
    ok1 = battery()
    print("D2 battery: " + ("pass" if ok1 else "KILL"))
    if not ok1:
        print("VERDICT: positive control failed -- nothing below is readable")
        sys.exit(1)
    ok3 = designed_arm()
    print("D6 designed arm: " + ("pass" if ok3 else "KILL"))
    ok2 = population()
    ok4 = sweep()
    print("VERDICT: battery %s, arm %s, population %s, sweep %s"
          % ("pass" if ok1 else "KILL", "pass" if ok3 else "KILL",
             "pass" if ok2 else "KILL", "pass" if ok4 else "KILL"))
    sys.exit(0 if (ok1 and ok2 and ok3 and ok4) else 1)
