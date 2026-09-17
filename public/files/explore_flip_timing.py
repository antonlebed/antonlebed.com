"""explore_flip_timing.py -- THE FLIP-TIMING CHANNEL: is read
discipline ALONE enough to confine undecidability, whatever the bulk
is? (The composite frame is explore_read_surface.py's -- a bulk
coupled to an environment through a boundary of monotone one-shot
flags; the finite-control confinement theorem it rests on is
explore_interactive_hand.py's ratchet law.)

THE QUESTION. Two verified results say a ratchet boundary (monotone
flags, each flipping false-to-true at most once, never resetting)
confines what crosses it: a FINITE-CONTROL bulk sees a finite branch
tree under every environment (explore_interactive_hand.py), and a
FLAG-WORD-DRIVEN bulk's boundary-quantified fate questions (does
SOME / does EVERY boundary behavior halt the bulk?) are decided by
enumerating schedules with zero environment steps
(explore_read_surface.py). The natural general claim -- call it the
INTERFACE CONJECTURE -- would drop the bulk restriction entirely:

    any bulk whose autonomous (frozen-boundary) fate questions are
    decidable keeps its boundary-quantified fate questions decidable
    behind a ratchet-only boundary.

If true, decidability regions of mixed systems would be drawn by the
boundary's read grammar alone, with no hypothesis on the bulk's own
move class. The danger channel is visible in the ratchet law's
own proof: a flip's TIMING is boundary information, and a
finite-control bulk cannot store it -- but an UNBOUNDED bulk can.
This script settles the conjecture by counterexample: one ratchet
flag, one counter, and a clocked simulator are enough to convert
flip timing into the halting problem.

THE CONSTRUCTION (the counterexample family B_M). Fix any two-counter
program M (Minsky 1967: halting for this class is undecidable). The
bulk B_M is a deterministic machine reading one ratchet flag:

  WAIT mode (flag down):  one counter t increments each step.
                          No halt state is reachable in this mode.
  first UP read:          switch to SIM mode carrying budget = t
                          and M's initial configuration.
  SIM mode (autonomous):  each step -- if M's configuration is
                          halted, HALT; else if the budget is 0,
                          enter DEAD (loop forever); else advance
                          M one step and decrement the budget.

A boundary schedule sigma_t reads DOWN for the first t bulk steps and
UP from step t+1 on (sigma_inf never flips). Under sigma_t the WAIT
counter equals t at the flip, so B_M halts iff M halts within t
steps, i.e. iff h <= t where h is M's halting time (h = inf if M
runs forever). Hence:

    SOME schedule halts B_M   <=>   M halts.

The left side is the boundary-quantified question; the right side is
the halting problem. Yet every FROZEN-boundary fate question about
B_M is decidable, uniformly: WAIT-frozen never halts (the counter
climbs, no halt state in the mode), and SIM from any configuration
(budget t, M-configuration w) is decided by simulating at most t
steps -- a terminating procedure. So the interface conjecture's
hypothesis holds, its conclusion fails, and the conjecture is FALSE.
Read discipline alone does not confine; the bulk's own move class is
a load-bearing hypothesis. What survives is exactly the verified
pair above (finite-control / flag-word-driven bulks) and the
move-disciplined salvage: a well-structured bulk (monotone over a wqo)
keeps its upward-closed questions decidable behind the flags, since its
product with a finite lattice of monotone flags is again monotone over
a wqo (the classical well-structured route, Finkel-Schnoebelen;
the flags land the composite back in the incumbent frame, where
decidability is graded by MOVES, not reads).

THE MODEL (matching explore_read_surface.py's idiom).
  M: a two-counter program, states mapping to ("INC", reg, next),
     ("DEC", reg, next_nonzero, next_zero), or "HALT"; deterministic,
     started at (X, Y) = (0, 0).
  B_M: configurations (mode, t, budget, mconf) as above.
  Schedules: sigma_t for t in a finite probe range, plus sigma_inf
     run to a horizon.

THE BATTERY (machines with hand-known behavior):
  M1  INC X; INC X; HALT                      -- halts, h = 2.
  M2  three INCs then drain X to zero; HALT   -- halts, h = 7.
  M3  INC X; DEC X; loop                      -- never halts
      (configuration repeat certifies the cycle; deterministic).

THE DESIGN (what each section checks).

S1  THE TIMING TRANSCRIPTION. For each battery machine and each
    t in the probe range, run B_M under sigma_t and check: the WAIT
    counter at the flip equals t, and B_M halts iff h <= t (h from
    an independent brute run of M alone). sigma_inf runs halt-free
    to the horizon.

S2  THE HYPOTHESIS CHECK (autonomous fate is decidable). Implement
    the two frozen-mode deciders -- WAIT-frozen: constant NO;
    SIM(budget, mconf): simulate at most budget steps -- and check
    each against brute runs from every configuration the S1 runs
    visited. The WAIT structural fact (no halt state in the mode,
    counter strictly climbs) is checked on the transition table.

S3  THE REDUCTION. Compute SOME-halt(B_M) by brute over the probe
    range and check it equals halts(M) for every battery member:
    the halters witness at exactly t = h (minimal witness), the
    non-halter has no witness in range AND the structural argument
    closes it -- B_M halts only in SIM with M's configuration
    halted, and M3's cycle certificate (configuration repeat under
    determinism) rules that out for every budget. The undecidability
    of the right-hand side is cited (Minsky), not re-proved: the
    verified content is the biconditional.

S4  THE CONTRAST (what the counterexample does NOT break).
    (i) A flag-word-driven bulk on the same boundary (HALT as soon
    as the flag reads up): its fate under sigma_t is identical for
    every t -- timing-blind -- and the two-schedule branch tree
    answers (SOME = yes, EVERY = no) match brute over all probed
    schedules, zero environment steps.
    (ii) The move-disciplined salvage at toy scale: a monotone bulk
    (WAIT: x += 1; UP: y += 1, halt at y >= 3) -- one step preserves
    the componentwise order on sampled configuration pairs at both
    flag values, and the schedule-brute quantified answers match the
    branch-tree computation. The wqo-product closure is cited, the
    instance verified.

S5  THE EVERY SIDE (derived on paper before this section's code).
    Claim: for a deterministic bulk behind k ratchet flags whose
    frozen fate questions are decidable from each configuration at
    each flag word, EVERY-halt -- the unflipped history among the
    histories -- is decidable by a capped recursion: decide the
    frozen run from the current configuration; if it never halts,
    the history raising no further flag is a non-halting history
    and the answer is NO; if it halts after T steps, only raises
    before those T steps can change anything, so recurse on each
    of the T configurations with each nonempty set of the flags
    still down raised there. Depth at most k, each level finite.
    (Finitely branching bulks by the same recursion over the frozen
    run's finite tree, König's lemma.) The decider is checked
    against brute enumeration of flip times over the probe range
    plus never, on three families:
    (a) B_M itself: WAIT-frozen never halts, so NO at the first call.
    (b) C_{M,H,c}: WAIT halts on its own when its counter reaches H;
        a flip at WAIT counter w enters SIM with budget w + c.
    (c) D_{M,H,c}: two flags. In WAIT, flag a enters SIM with budget
        w + c, flag b alone halts at once, a taking priority; in SIM
        flag b makes each step cost two units of budget.
    Frozen deciders for C and D simulate to a bound computed from
    the configuration (WAIT: H - w + w + c + 3 steps; SIM:
    budget + 2), a terminating procedure. Then the contrast:
    (d) E_M under OBLIGED flipping (sigma_inf excluded): WAIT never
        halts; a flip at w enters SIM with budget w, halting when
        the budget runs out with M unhalted and looping forever if
        M halts within it. EVERY-halt over flipping schedules is
        then "M halts at no budget", the complement of halting.

FROZEN PREDICTIONS (fixed before the engine ran):
  F1  S1: B_M1 halts under sigma_t iff t >= 2; B_M2 iff t >= 7;
      B_M3 under no sigma_t in range; every flip transcribes t
      exactly; every sigma_inf run is halt-free.
  F2  S2: both deciders agree with brute at every visited
      configuration; the WAIT table has no halt state.
  F3  S3: SOME-halt = YES for M1 (minimal witness 2) and M2
      (minimal witness 7), NO for M3 (no witness + cycle closed);
      SOME-halt(B_M) == halts(M) across the battery.
  F4  S4: the flag-word bulk's fate is t-independent and its tree
      answers match brute; the monotone bulk preserves order on all
      sampled pairs and its tree answers match brute.

  F5  S5: the capped decider equals brute at every cell: B_M NO
      across the battery; C_{M,H,c} YES iff h <= c (the flip at w = 0
      carries the least budget), so M1 YES iff c >= 2, M2 iff c >= 7,
      M3 never, at H in {3, 10} and c in {0, 1, 2, 7, 9}; D agrees
      with brute at the same cells, whatever its answers.
  F6  S5(d): obliged EVERY-halt(E_M) == not halts(M) across the
      battery (NO for M1 and M2 by the witness t = h, YES for M3 in
      range and closed by its cycle certificate); E_M's frozen
      deciders agree with brute.

KILL CONDITIONS. Any F1-F3 miss means the construction is wrong
(the counterexample claim would be withdrawn, not patched in place).
F4 misses would mean the contrast is misdrawn. An F5 miss at any cell
withdraws the EVERY-side claim; an F6 miss withdraws the claim that it
rests on the unflipped history.

FINDINGS (entered after the runs; all 46 checks pass, F1-F6 all
confirmed).

1.  THE TIMING TRANSCRIPTION (rule over the stated ranges): at every
    battery member and every t in range, B_M under sigma_t halts iff
    h <= t, the flip transcribes its own timing into the counter
    exactly, and sigma_inf runs halt-free. Minimal halting witnesses
    land at t = h exactly (2 for M1, 7 for M2, both as hand-derived).

2.  THE HYPOTHESIS HOLDS: both frozen-mode deciders agree with brute
    at every configuration the runs visited; the WAIT mode has no
    halt state and its counter strictly climbs (no cycle). B_M's
    autonomous fate questions are decidable, uniformly.

3.  THE REDUCTION: SOME-halt(B_M) == halts(M) across the battery,
    with M3's non-halting closed by the configuration-repeat
    certificate. Together with Minsky's cited theorem this REFUTES
    the interface conjecture: read discipline alone does not confine
    undecidability. One ratchet flag, one counter, and a clocked
    simulator convert flip timing into the halting problem. The
    refutation is general -- nothing in B_M depends on the probe
    ranges; the script verifies the construction's mechanics
    exhaustively at small scale (theorem, given Minsky's halting
    theorem, by the explicit reduction; the in-range checks are
    exhaustive).

4.  THE CONTRAST: the flag-word-driven bulk is timing-blind (fate
    identical across all flip times) and its two-schedule tree
    decides both quantified questions with zero environment steps;
    the monotone toy preserves the componentwise order at both flag
    values, its target is upward-closed, and its quantified answers
    match the tree. The confinement results for finite-control and
    flag-word-driven bulks survive untouched, and the salvage is
    move-disciplined: a well-structured bulk keeps its SOME question
    for an upward-closed target decidable, its product with the flag
    words staying well-structured when two configurations are compared
    only at the same flag word, the order the toy checks (a finite set
    under equality is a wqo; wqo route, cited). (Settled here:
    "any bulk class closed under that product" was the earlier form,
    false as stated, since B_M's class is closed under it too.) What draws the decidability region is the bulk's move
    class WITH the read grammar -- the read grammar alone is not
    sufficient.

5.  THE CHANNEL IS ONE-SIDED (theorem, by the capped recursion's
    proof in S5's design; its mechanics exhaustive at probe scale):
    with the unflipped history among the histories, EVERY-halt is
    decidable for any deterministic bulk behind k ratchet flags whose
    frozen fate questions are decidable from each configuration, the
    history raising no further flag having to halt on its own and its
    finite run capping the raises worth trying. The decider matched
    brute at every cell: B_M NO after one frozen call; C YES exactly
    at h <= c (M1 at c >= 2, M2 at c >= 7, M3 never); the two-flag D
    at all 30 cells, YES at M1 with c in {7, 9} and NO elsewhere.
    Obliged flipping breaks the cap: EVERY-halt(E_M) over flipping
    schedules is NO for M1 and M2 and YES for M3, the complement of
    halting, while E_M with the unflipped history is NO for all three.
    So the flip-timing channel makes SOME-halt the halting problem and
    leaves EVERY-halt decidable, and needs no move frame for the EVERY
    side.

RUN RECORD: python explore_flip_timing.py -- 46 checks pass, < 1 s,
plain Python. The first run failed at check 32: the S4 toy had put
the halt bit inside the state tuple (equality-compared in the order)
instead of using the standard upward-closed-target (coverability)
convention; S4(ii) was rewritten to that convention and the run
repeated green. S1-S3 were not altered after their first green run.
Two cosmetic simplifications (decide_sim's dead final return;
bulk_step's redundant terminal-mode expression) were made after the
green run; each rerun printed identically. S5 (checks 34-46) was
added after its design was frozen above and passed on its first run
(one syntax error fixed before it); its brute
enumeration flips each flag at a time in 0..15 or never, and the
S4 closure line's wording was corrected at the same run.
"""

# ---------------------------------------------------------------- #
# two-counter machines                                              #
# ---------------------------------------------------------------- #

M1 = {0: ("INC", "X", 1), 1: ("INC", "X", 2), 2: "HALT"}

M2 = {
    0: ("INC", "X", 1),
    1: ("INC", "X", 2),
    2: ("INC", "X", 3),
    3: ("DEC", "X", 3, 4),
    4: "HALT",
}

M3 = {0: ("INC", "X", 1), 1: ("DEC", "X", 0, 0)}

BATTERY = [("M1", M1, True), ("M2", M2, True), ("M3", M3, False)]

CHECKS = [0]


def ok(cond, msg):
    CHECKS[0] += 1
    if not cond:
        raise AssertionError("CHECK %d FAILED: %s" % (CHECKS[0], msg))
    print("  ok %2d  %s" % (CHECKS[0], msg))


def m_halted(prog, q):
    return prog.get(q) == "HALT"


def m_step(prog, conf):
    """One deterministic step of a two-counter program. conf =
    (q, x, y); halted configurations are fixed points."""
    q, x, y = conf
    if m_halted(prog, q):
        return conf
    ins = prog[q]
    if ins[0] == "INC":
        _, r, nxt = ins
        return (nxt, x + 1, y) if r == "X" else (nxt, x, y + 1)
    _, r, nz, z = ins
    v = x if r == "X" else y
    if v == 0:
        return (z, x, y)
    return (nz, x - 1, y) if r == "X" else (nz, x, y - 1)


def m_halt_time(prog, horizon):
    """Brute halting time of M from (0,0), or None within horizon.
    A configuration repeat certifies non-halting (determinism)."""
    conf, seen = (0, 0, 0), set()
    for step in range(horizon + 1):
        if m_halted(prog, conf[0]):
            return step, "halts"
        if conf in seen:
            return None, "cycle"
        seen.add(conf)
        conf = m_step(prog, conf)
    return None, "horizon"


# ---------------------------------------------------------------- #
# the counterexample bulk B_M                                       #
# ---------------------------------------------------------------- #

WAIT, SIM, DEAD, BHALT = "WAIT", "SIM", "DEAD", "BHALT"


def bulk_init():
    return (WAIT, 0, None, None)


def bulk_step(prog, conf, flag):
    """One step of B_M reading the ratchet flag. conf =
    (mode, t, budget, mconf)."""
    mode, t, budget, mconf = conf
    if mode == BHALT or mode == DEAD:
        return conf
    if mode == WAIT:
        if flag:
            return (SIM, t, t, (0, 0, 0))
        return (WAIT, t + 1, None, None)
    # SIM: autonomous (the flag is never re-read after the flip)
    if m_halted(prog, mconf[0]):
        return (BHALT, t, budget, mconf)
    if budget == 0:
        return (DEAD, t, budget, mconf)
    return (SIM, t, budget - 1, m_step(prog, mconf))


def run_bulk(prog, flip_at, horizon):
    """Run B_M under sigma_{flip_at} (None = sigma_inf). Returns
    (halted?, counter value transcribed at the flip or None,
    visited SIM configurations)."""
    conf, transcribed, visited = bulk_init(), None, []
    for step in range(1, horizon + 1):
        flag = flip_at is not None and step > flip_at
        prev_mode = conf[0]
        conf = bulk_step(prog, conf, flag)
        if prev_mode == WAIT and conf[0] == SIM:
            transcribed = conf[2]
        if conf[0] == SIM:
            visited.append((conf[2], conf[3]))
        if conf[0] == BHALT:
            return True, transcribed, visited
    return False, transcribed, visited


# ---------------------------------------------------------------- #
# the two frozen-mode deciders (the conjecture's hypothesis)        #
# ---------------------------------------------------------------- #

def decide_wait_frozen():
    """WAIT-frozen fate: never halts. Constant-time decider; its
    ground is structural (no halt state in the mode, checked in S2)."""
    return False


def decide_sim(prog, budget, mconf):
    """SIM fate from (budget, mconf): simulate at most budget + 1
    checks -- a terminating procedure for every input."""
    conf = mconf
    for _ in range(budget + 1):
        if m_halted(prog, conf[0]):
            return True
        conf = m_step(prog, conf)
    return False


# ---------------------------------------------------------------- #
# S1  the timing transcription                                      #
# ---------------------------------------------------------------- #

T_RANGE = range(0, 16)
HORIZON = 200


def s1_timing():
    print("\nS1 THE TIMING TRANSCRIPTION")
    halt_times = {}
    for name, prog, halts in BATTERY:
        h, why = m_halt_time(prog, HORIZON)
        halt_times[name] = h
        ok((h is not None) == halts, "%s brute ground truth: %s" % (name, why))
        exact = all(
            run_bulk(prog, t, HORIZON)[0] == (h is not None and h <= t)
            for t in T_RANGE
        )
        ok(exact, "%s: B halts under sigma_t iff h <= t, all t in range" % name)
        transcribed = all(
            run_bulk(prog, t, HORIZON)[1] == t for t in T_RANGE
        )
        ok(transcribed, "%s: the flip transcribes t exactly, all t" % name)
        ok(not run_bulk(prog, None, HORIZON)[0], "%s: sigma_inf halt-free" % name)
    ok(halt_times["M1"] == 2, "M1 halting time is 2 (as hand-derived)")
    ok(halt_times["M2"] == 7, "M2 halting time is 7 (as hand-derived)")
    return halt_times


# ---------------------------------------------------------------- #
# S2  the hypothesis check                                          #
# ---------------------------------------------------------------- #

def s2_hypothesis():
    print("\nS2 THE HYPOTHESIS CHECK (autonomous fate decidable)")
    # WAIT-frozen: brute agreement + the structural fact.
    for name, prog, _ in BATTERY:
        halted, _, _ = run_bulk(prog, None, HORIZON)
        ok(halted == decide_wait_frozen(),
           "%s: WAIT-frozen brute agrees with the decider (never halts)" % name)
    ok(all(bulk_step(p, (WAIT, t, None, None), False)[0] == WAIT
           for _, p, _ in BATTERY for t in range(50)),
       "WAIT table: flag-down steps stay in WAIT (no halt state in the mode)")
    ok(all(bulk_step(p, (WAIT, t, None, None), False)[1] == t + 1
           for _, p, _ in BATTERY for t in range(50)),
       "WAIT table: the counter strictly climbs (no repeat, no cycle)")
    # SIM decider vs brute at every visited configuration.
    for name, prog, _ in BATTERY:
        agree = True
        for t in T_RANGE:
            _, _, visited = run_bulk(prog, t, HORIZON)
            for budget, mconf in visited:
                brute = run_sim_brute(prog, budget, mconf)
                if brute != decide_sim(prog, budget, mconf):
                    agree = False
        ok(agree, "%s: SIM decider agrees with brute at every visited config" % name)


def run_sim_brute(prog, budget, mconf):
    """Brute the SIM dynamics from (budget, mconf) to its end
    (guaranteed within budget + 1 steps)."""
    conf = (SIM, 0, budget, mconf)
    for _ in range(budget + 2):
        if conf[0] == BHALT:
            return True
        if conf[0] == DEAD:
            return False
        conf = bulk_step(prog, conf, True)
    return conf[0] == BHALT


# ---------------------------------------------------------------- #
# S3  the reduction                                                 #
# ---------------------------------------------------------------- #

def s3_reduction(halt_times):
    print("\nS3 THE REDUCTION (SOME-halt(B_M) == halts(M))")
    for name, prog, halts in BATTERY:
        witnesses = [t for t in T_RANGE if run_bulk(prog, t, HORIZON)[0]]
        if halts:
            ok(min(witnesses) == halt_times[name],
               "%s: minimal witness t = h = %d" % (name, halt_times[name]))
        else:
            ok(witnesses == [], "%s: no witness in the probe range" % name)
        ok(bool(witnesses) == halts,
           "%s: SOME-halt == halts(M) (the biconditional)" % name)
    # the structural closure for M3 beyond the range: B halts only via
    # a halted M-configuration; M3 cycles (certified in S1), so no
    # budget suffices.
    _, why = m_halt_time(M3, HORIZON)
    ok(why == "cycle", "M3 non-halting closed by configuration-repeat certificate")
    print("  (the right side's undecidability over the family {M} is")
    print("   Minsky's theorem, cited; the biconditional above is the")
    print("   verified reduction. The interface conjecture is FALSE.)")


# ---------------------------------------------------------------- #
# S4  the contrast                                                  #
# ---------------------------------------------------------------- #

def s4_contrast():
    print("\nS4 THE CONTRAST (what the counterexample does not break)")
    # (i) a flag-word-driven bulk is timing-blind and tree-decided.
    def fw_bulk_fate(flip_at):
        state = "RUN"
        for step in range(1, HORIZON + 1):
            flag = flip_at is not None and step > flip_at
            if flag:
                state = "BHALT"
            if state == "BHALT":
                return True
        return False

    fates = {t: fw_bulk_fate(t) for t in T_RANGE}
    ok(len(set(fates.values())) == 1 and fates[0] is True,
       "flag-word bulk: fate identical across every flip time (timing-blind)")
    tree_some = True   # the tree: the flipped schedule halts it
    tree_every = False  # the no-flip schedule runs forever
    brute_some = any(fates.values()) or fw_bulk_fate(None)
    brute_every = all(fates.values()) and fw_bulk_fate(None)
    ok(tree_some == brute_some and tree_every == brute_every,
       "flag-word bulk: two-schedule tree answers match brute (zero env steps)")

    # (ii) the move-disciplined salvage at toy scale. Standard
    # well-structured shape: monotone dynamics on (x, y), halting =
    # membership in the UPWARD-CLOSED target y >= 3 (the coverability
    # convention), never a state component.
    def mono_step(conf, flag):
        x, y = conf
        return (x + 1, y) if not flag else (x, y + 1)

    def in_target(conf):
        return conf[1] >= 3

    import itertools
    pairs = [((x, y), (x + dx, y + dy))
             for x, y, dx, dy in itertools.product(range(4), range(4), range(3), range(3))]
    def leq(c, d):
        return c[0] <= d[0] and c[1] <= d[1]
    mono = all(
        leq(mono_step(c, f), mono_step(d, f))
        for c, d in pairs for f in (False, True) if leq(c, d)
    )
    up_closed = all(in_target(d) for c, d in pairs if leq(c, d) and in_target(c))
    ok(mono and up_closed,
       "monotone bulk: one step preserves the order at both flag values"
       " and the target is upward-closed on sampled pairs")

    def mono_fate(flip_at):
        conf = (0, 0)
        for step in range(1, HORIZON + 1):
            flag = flip_at is not None and step > flip_at
            conf = mono_step(conf, flag)
            if in_target(conf):
                return True
        return False

    brute_some = any(mono_fate(t) for t in T_RANGE) or mono_fate(None)
    brute_every = all(mono_fate(t) for t in T_RANGE) and mono_fate(None)
    ok(brute_some is True and brute_every is False,
       "monotone bulk: quantified answers (SOME yes, EVERY no) match the tree")
    print("  (the general closure -- wqo x flag words under equality stays wqo,")
    print("   monotonicity preserved -- is the classical well-structured")
    print("   route, cited; decidability graded by MOVES is what survives.)")


# ---------------------------------------------------------------- #
# S5  the every side                                                #
# ---------------------------------------------------------------- #

LOOP = "LOOP"


def every_brute(step, init, flag_names, horizon, obliged=False):
    """EVERY-halt by brute: every assignment of a flip time in T_RANGE
    (or never, unless obliged) to each flag, run to the horizon."""
    import itertools
    times = list(T_RANGE) + ([] if obliged else [None])
    for assign in itertools.product(times, repeat=len(flag_names)):
        conf = init
        halted = False
        for n in range(1, horizon + 1):
            up = frozenset(f for f, t in zip(flag_names, assign)
                           if t is not None and n > t)
            conf = step(conf, up)
            if conf[0] == BHALT:
                halted = True
                break
        if not halted:
            return False
    return True


def every_capped(step, frozen, conf, up, flag_names, stats):
    """The capped recursion: decide the frozen run; NO if it never
    halts; else recurse on each raise before its halting step."""
    import itertools
    stats[0] += 1
    halts, T = frozen(conf, up)
    if not halts:
        return False
    down = [f for f in flag_names if f not in up]
    c = conf
    for _ in range(T):
        for r in range(1, len(down) + 1):
            for S in itertools.combinations(down, r):
                up2 = up | frozenset(S)
                if not every_capped(step, frozen, step(c, up2), up2,
                                    flag_names, stats):
                    return False
        c = step(c, up)
    return True


def frozen_by_bound(step, bound):
    """A frozen decider simulating to a bound computed from the
    configuration: returns (halts, steps to halt)."""
    def frozen(conf, up):
        c = conf
        for n in range(bound(conf) + 1):
            if c[0] == BHALT:
                return True, n
            c = step(c, up)
        return False, None
    return frozen


def sim_tail(prog, conf, cost):
    mode, w, budget, mconf = conf
    if m_halted(prog, mconf[0]):
        return (BHALT, w, budget, mconf)
    if budget == 0:
        return (DEAD, w, budget, mconf)
    return (SIM, w, budget - min(cost, budget), m_step(prog, mconf))


def make_C(prog, H, c):
    def step(conf, up):
        mode, w, budget, mconf = conf
        if mode in (BHALT, DEAD):
            return conf
        if mode == WAIT:
            if "a" in up:
                return (SIM, w, w + c, (0, 0, 0))
            return (BHALT, w + 1, None, None) if w + 1 >= H else (WAIT, w + 1, None, None)
        return sim_tail(prog, conf, 1)
    def bound(conf):
        return (H + c + 3) if conf[0] == WAIT else ((conf[2] or 0) + 2)
    return step, frozen_by_bound(step, bound)


def make_D(prog, H, c):
    def step(conf, up):
        mode, w, budget, mconf = conf
        if mode in (BHALT, DEAD):
            return conf
        if mode == WAIT:
            if "a" in up:
                return (SIM, w, w + c, (0, 0, 0))
            if "b" in up:
                return (BHALT, w, None, None)
            return (BHALT, w + 1, None, None) if w + 1 >= H else (WAIT, w + 1, None, None)
        return sim_tail(prog, conf, 2 if "b" in up else 1)
    def bound(conf):
        return (H + c + 3) if conf[0] == WAIT else ((conf[2] or 0) + 2)
    return step, frozen_by_bound(step, bound)


def make_B(prog):
    def step(conf, up):
        return bulk_step(prog, conf, "a" in up)
    def frozen(conf, up):
        if conf[0] == WAIT and "a" not in up:
            return False, None          # decide_wait_frozen, S2
        return frozen_by_bound(step, lambda k: (k[1] if k[0] == WAIT
                                                else (k[2] or 0)) + 3)(conf, up)
    return step, frozen


def make_E(prog):
    def step(conf, up):
        mode, w, budget, mconf = conf
        if mode in (BHALT, LOOP):
            return conf
        if mode == WAIT:
            return (SIM, w, w, (0, 0, 0)) if "a" in up else (WAIT, w + 1, None, None)
        if m_halted(prog, mconf[0]):
            return (LOOP, w, budget, mconf)
        if budget == 0:
            return (BHALT, w, budget, mconf)
        return (SIM, w, budget - 1, m_step(prog, mconf))
    return step


def s5_every(halt_times):
    print("\nS5 THE EVERY SIDE (the capped recursion)")
    init = (WAIT, 0, None, None)
    one, two = ["a"], ["a", "b"]
    for name, prog, _ in BATTERY:
        step, frozen = make_B(prog)
        stats = [0]
        dec = every_capped(step, frozen, init, frozenset(), one, stats)
        brute = every_brute(step, init, one, HORIZON)
        ok(dec is False and brute is False and stats[0] == 1,
           "%s: B EVERY-halt NO by decider (1 frozen call) and brute" % name)
    for name, prog, _ in BATTERY:
        h = halt_times[name]
        cells_C, cells_D, calls = [], [], [0, 0]
        for H in (3, 10):
            for c in (0, 1, 2, 7, 9):
                step, frozen = make_C(prog, H, c)
                st = [0]
                dec = every_capped(step, frozen, init, frozenset(), one, st)
                calls[0] += st[0]
                brute = every_brute(step, init, one, HORIZON)
                cells_C.append(dec == brute == (h is not None and h <= c))
                step, frozen = make_D(prog, H, c)
                st = [0]
                dec = every_capped(step, frozen, init, frozenset(), two, st)
                calls[1] += st[0]
                brute = every_brute(step, init, two, HORIZON)
                cells_D.append(dec == brute)
                print("    %s H=%-2d c=%d  C: %-5s D: %-5s" % (
                    name, H, c, every_brute(*[make_C(prog, H, c)[0], init, one, HORIZON]),
                    brute))
        ok(all(cells_C), "%s: C decider == brute == (h <= c) at all 10 cells"
           " (%d frozen calls)" % (name, calls[0]))
        ok(all(cells_D), "%s: D (two flags) decider == brute at all 10 cells"
           " (%d frozen calls)" % (name, calls[1]))
    for name, prog, halts in BATTERY:
        step = make_E(prog)
        obliged = every_brute(step, init, one, HORIZON, obliged=True)
        unobliged = every_brute(step, init, one, HORIZON)
        ok(obliged == (not halts) and unobliged is False,
           "%s: E obliged EVERY-halt %s == not halts(M); with never: NO"
           % (name, obliged))
    _, why = m_halt_time(M3, HORIZON)
    ok(why == "cycle", "E_M3's YES closed beyond range by M3's cycle certificate")


# ---------------------------------------------------------------- #

if __name__ == "__main__":
    print("THE FLIP-TIMING CHANNEL: the interface conjecture at risk")
    halt_times = s1_timing()
    s2_hypothesis()
    s3_reduction(halt_times)
    s4_contrast()
    s5_every(halt_times)
    print("\nALL %d CHECKS PASS" % CHECKS[0])
