"""
explore_pending_fires.py -- THE PENDING FIRES: a sound decision procedure
for the sublinear-supply growing-window machine, and the true scope of its
decidability. (Sibling of explore_decidable_side.py -- which named the
growing-period residual -- and of explore_sqrt_supply.py,
explore_bit_supply.py, explore_growth_machine.py,
explore_minimal_carrier.py.)

THE SETTING. The supply law classifies the growing-window machine by the
growth rate of its modulus supply m_g: Omega(g) is universal, bounded is
finite-state, and the sublinear side m_g = o(g) is a third decidable
class (conjectured) -- a reset-broadcast system with bounded live
registers (explore_decidable_side.py). That script's decider was a
HEURISTIC: declare LOOP on the first repeated (control, zero-test-vector)
signature. Its named residual: a frontier-riding capped counter's
zero-test fires with unboundedly GROWING gaps (9, 24, 45, ...), so its
trajectory is not ultimately periodic and the first-repeat rule falsely
reports LOOP for a halt-on-fire program. This script attacks the
DECISION PROCEDURE itself: what does a SOUND decider need, does one
exist, and what -- exactly -- is the remaining undecidable content?

THE MACHINE CLASS (verbatim from explore_minimal_carrier.py). A growing
list of windows, window j a copy of Z/m_j (moduli from the SUPPLY);
r registers, each a residue tuple over the current windows, born 0 in
every fresh window (state-independent); native ops COMPONENTWISE -- add,
sub, mul, write-constant; GROW appends one fresh window and mints the
fresh-window singleton w = 1 - ONES (native at grow time); the ONE
cross-window read is the global 1-bit zero-test; finite control.

THE TERMS (this record's own vocabulary -- the object is the decision
procedure, not the class placement, which is settled).
  SIGNAL      the boolean stream a jz-register's zero-test produces.
  PENDING FIRE  at time t, a signal currently False whose next True is
              in the future. The sound decider's whole business is the
              question: does a given pending fire ever LAND?
  LANDING     that next True actually occurring.
  DESCRIPTOR  a finite exact summary of a register's future signal:
              frozen-window residues + riding value + frontier index --
              enough to compute the landing time or certify never-lands.
  Homonym watch (inherited): REGISTERS = the machine's fixed tuple of
  residue-vectors; WINDOWS = the growing coordinates.

THE HAND ATTACK (four results derived on paper before any engine code;
the run is the adjudicator).

(1) THE LANDING LEMMA (o(g) forces every riding fire to land). A riding
counter's stored residue evolves v_{t+1} = (v_t + 1) mod m(g_t): the
unary migration moves the residue losslessly (monotone supply, so
res < m_old <= m_new) and the wrap happens at the add. Fire = v == 0.
A pending fire after t0 lands when the elapsed count reaches the
creeping modulus; with any FIXED K grows per pass the threshold
n >= m(K*n + g0) - 1 is reachable on any o(g) supply (m(K*n) = o(n)),
and the landing itself is guaranteed by THE CROSSING ARGUMENT: v + 1
advances by exactly 1 per pass while m is non-decreasing, so at the
FIRST pass with v + 1 >= m equality holds (m > v and m <= v + 1 force
m = v + 1) -- the wrap cannot be skipped, and its time is computable by
direct evaluation of the supply. On the LINEAR side the same fire can hang PENDING FOREVER
(the faithful counter never re-zeros -- the successor supply's rider has
v_t = t exactly). So the o(g)/Omega(g) boundary is the same line a THIRD
time: capacity cap, class placement, and now fire landing -- and
landing-computability is exactly what a sound decider needs. A
multi-digit counter fires exactly at its top digit's wrap (the carry
chain synchronizes digits: the top wraps only when the low just
wrapped), so one landing lemma covers composite counters; a
data-dependent K is the regress, excluded as before.

(2) THE SIGNAL TAXONOMY (what a signal can be, in the fragment below):
  a. CONSTANT -- an untouched register (all-zero: fires always) or a
     provably-never-zero one.
  b. FROZEN-PERIODIC -- support on fixed frozen windows (saved
     singletons); per-window dynamics is a deterministic map on
     (Z/m)^r; the signal is periodic with period a program constant
     (lcm-scale, possibly large). NOTE: this yields a SECOND
     naive-killer, independent of the growing-period one: a
     halt-on-lcm-pulse program (period 60) shows all-False for 59
     passes, so the first-repeat rule declares LOOP long before the
     pulse; ground truth is HALT at t = 60.
  c. RIDING PULSE -- a sparse register migrating with the frontier;
     growing gaps; every pending fire lands, by (1).
  d. GROWING-UNIFORM -- touched only by uniform constants while the
     program keeps growing: the youngest window's content is a fixed
     short computation from birth (same body, same computation every
     pass); if nonzero, the AND never closes: NEVER FIRES, certified by
     one body-pass check (the CRT grow-every-step case).

(3) THE THREE-VERDICT ARCHITECTURE (the sound decider). Verdicts:
HALT(t) / LOOP(certificate) / SUPPLY-ARITHMETIC(extracted question).
The decider simulates DESCRIPTORS, not vectors: frozen residues
(bounded data), riding value + frontier index, pending fires
fast-forwarded to their computed landings. LOOP is declared only with a
certificate: (i) never-fires -- every signal is certified constant or
taxonomy-d, and the control cycle under the constant zero-test vector
is closed; (ii) ROUND SELF-SIMULATION -- a fire-and-reset lasso whose
post-fire bounded state repeats exactly and whose fire branch consults
no OTHER signal's phase: the round replays with dilated timing (fires
keep landing forever, by the landing lemma), so it never halts. Where a
fire branch DOES consult another signal's phase (detector-shaped
programs), the decider extracts the phase question and returns it: the
third verdict. The decider is SOUND everywhere and complete on the
fragment; its incompleteness is confined to the extracted supply
arithmetic -- and result (4) shows that confinement is ESSENTIAL, not a
weakness of this design.

(4) THE SUPPLY ORACLE (the crux's counterexample face, RESOLVED -- the
conjecture is supply-sensitive). The machine can read one bit per wrap
about the supply's fine structure: run a rider against a frozen clock
mod L. Design the supply's smooth part with every value a multiple of L
(gaps between fires = the wrapping modulus = 0 mod L, still o(g), still
computable): then every fire lands at clock phase 0. Switch the tail to
values = 1 mod L from some position onward, and the first post-switch
wrap lands at phase 1: the detector branches to HALT. So for the supply
family S_e = smooth track, switching iff Turing machine e ever halts
(each S_e computable and o(g)), the FIXED detector program halts on S_e
iff TM_e halts: halting on adversarial computable o(g) supplies is
UNDECIDABLE -- with the capacity caps fully intact (no faithful counter
is built; the machine merely reads the supply as an oracle stream, one
bit per landing). Rate-only decidability is therefore FALSE as a
general statement: the honest law is DECIDABILITY = RATE (which caps
the machine's own arithmetic and forces every fire to land) + SUPPLY
TAMENESS (the supply's fine arithmetic is the one remaining input
channel). The crux question of the sibling script answers BOTH ways,
properly split: the machine adds no undecidable content of its own
(conjectured, now correctly scoped); the supply can plant any.

THE FRAGMENT (what the mechanized decider covers, stated exactly):
lasso programs over the instruction set below whose jz-registers are
each touched in the loop body only by one of -- rider INCs (riding),
adds of setup-saved frozen singletons (frozen-periodic), uniform
constant adds in a growing body (growing-uniform), nothing (constant);
resets allowed on fire branches. Outside the fragment the decider
answers OUT-OF-FRAGMENT rather than guess. General o(g) programs on
TAME supplies are conjectured to reduce to this taxonomy; the extracted
supply arithmetic on the canonical sqrt supply is the WRAP-WORD RESIDUE
PROBLEM (S5), the sharpened residual.

THE DESIGN (what each section asks; findings enter post-run only).

S1  THE LANDING DICHOTOMY. Run the riding counter's supply-only
    recurrence v_{t+1} = (v_t + 1) mod m(g_t) on the sqrt supply at
    K = 1, 2, 4 grows per pass and on the log supply: every pending
    fire lands, at the time predicted by min{n : n >= m(K*n + g0) - 1}.
    On the successor supply (linear side): the armed fire stays pending
    over the whole horizon, and v_t = t exactly (the a priori
    never-lands argument, exhibited).

S2  THE TAXONOMY, BISIMULATED. For every battery program, the
    descriptor-predicted signal streams equal the concrete machine's
    jz streams pass for pass over a prefix (soundness is checked
    mechanically, not assumed): the frozen lcm-pulse fires at exactly
    60, 120, ...; the riding pulse fires with growing gaps; the
    growing-uniform register never fires (youngest-window check); the
    untouched register is constant.

S3  THE TWO NAIVE-KILLERS + THE SOUND DECIDER. (i) halt-on-lcm-pulse:
    the naive first-repeat decider declares LOOP; the concrete run
    HALTS at t = 60; the sound decider says HALT(60) by fast-forwarding
    the pending fire. (ii) halt-on-riding-fire (30 pregrows, so the
    wrap is late enough to matter): naive declares LOOP; concrete run
    HALTS at the first wrap; sound decider computes the same landing.
    Then the full battery: the sibling script's four programs
    (count_to_3 HALT, inc_forever LOOP, wrap_reset LOOP, reset_pulse
    LOOP) re-decided SOUNDLY with certificates -- never-fires for the
    pure cycles, round self-simulation for the fire-and-reset lasso.

S4  THE SUPPLY ORACLE, MECHANIZED. The detector program (rider + frozen
    clock mod 6) on the smooth multiples-of-6 supply: every fire at
    clock phase 0, no halt over the horizon; the sound decider returns
    the extracted phase question (the third verdict). On the switched
    supply (tail = 1 mod 6 from position 100): the concrete run HALTS
    at the first post-switch wrap, at clock phase 1. One bumped track,
    one bit read, halt iff switch: the reduction's engine, exhibited.

S5  THE WRAP-WORD RESIDUE PROBLEM (the sharpened residual, measured).
    On the pure sqrt supply, compute the rider's wrap times t_k far out
    (k in the thousands): the gap word (gaps = the wrapping moduli) is
    non-decreasing with each value appearing a bounded number of times
    (quasi-Beatty); the residues t_k mod 6 and mod 60 populate many
    classes and keep recurring (no absorbing class). The open content
    of completeness on the sqrt supply is exactly the arithmetic of
    this word -- a supply question, not a machine question.

PREDICTIONS (fixed before the run; adjudication added post-run).
  PR1  Sqrt supply at K = 1, 2, 4 and log supply: every pending fire
       lands, at the a priori landing time; successor supply: the fire
       stays pending over the whole horizon with v_t = t exactly.
  PR2  Descriptor streams == concrete jz streams for every battery
       program over the checked prefix; lcm-pulse fires at exactly
       60 and 120; riding gaps grow; growing-uniform never fires.
  PR3  Both naive-killers: naive says LOOP, ground truth is HALT
       (t = 60 for the pulse; the first wrap for the rider), the sound
       decider returns HALT with the correct time on both.
  PR4  The sound decider reproduces all four sibling-battery verdicts
       with certificates (never-fires / round self-simulation), zero
       false verdicts across the battery.
  PR5  The detector loops on the smooth supply (all fire phases 0;
       decider verdict = the extracted supply question) and HALTS on
       the switched supply at the first post-switch wrap (phase 1).
  PR6  The sqrt wrap word: gaps non-decreasing, each gap value's
       multiplicity small (about two); residues mod 6 populate at least
       4 classes over k <= 2000 with at least 2 classes still recurring
       in the second half (no absorbing class).

PREDICTIONS ADJUDICATED (post-run): all six CONFIRMED on the first clean
run (23 checks). One hand-bound correction preceded it: the pre-run
landing bound (the threshold n* alone) was too tight -- the first assert
showed the landing arrives within one further modulus-length past the
threshold (the phase; a bound valid for the smooth supplies used here,
whose post-threshold increments stay below 1 per pass -- the GENERAL
landing guarantee is the crossing argument); the kill logic was
untouched, the margin was the vibes part. Two decider-implementation corrections
also preceded the clean run (the frozen-mask fixpoint for compound
singletons; tick-indexed bisimulation + the exact descriptor walk
replacing a blanket all-False walk) -- caught by the script's own
asserts, before any finding was written. PR1 (landings at t = 2/2/4/2
vs bound 5; successor v_t = t for 4000 passes, pending forever); PR2
(bisimulation clean on every program; lcm fire at tick 60 exactly;
riding gaps 7, 8, 8, 9, 9 non-decreasing; youngest window holds 1);
PR3 (killer 1: naive LOOP at step 15 vs truth HALT at step 250, sound
HALT at tick 60; killer 2: naive LOOP at step 6 vs truth HALT at step
29, sound HALT at rider tick 7 = the computed landing); PR4 (all four
sibling verdicts reproduced with certificates; count_to_3 halts at
rider tick 1 BEFORE the first landing at tick 2 -- a fall-through halt);
PR5 (smooth track: 4000 steps, no halt; switched track: HALT at step
559 = the first post-switch wrap, landing 109 = 1 mod 6; the sound
decider returns the extracted phase question); PR6 (2437 landings, gaps
non-decreasing, multiplicity <= 2; residues mod 6: 5 classes hit --
class 4 EMPTY, class 5 triple-weight 1011 vs ~400 -- 5 recurring in the
second half; mod 60: 38 of 60 classes).

FINDINGS (entered after the run; every number below is from the printed
output; run record at the end).

1. THE LANDING DICHOTOMY -- o(g) forces every riding fire to land; the
   linear side lets it hang forever (rule, proved by the crossing
   argument and mechanized; S1). A riding counter's pending fire lands
   at the first elapsed count meeting the creeping modulus; on any o(g)
   supply with any FIXED grows-per-pass K this is forced by the
   CROSSING ARGUMENT (v + 1 advances by exactly 1 while m is
   non-decreasing, so the first pass with v + 1 >= m has equality --
   the wrap cannot be skipped; landings at t = 2/2/4 for K = 1/2/4 on
   sqrt, t = 2 on log, within the smooth-supply bound threshold + one
   modulus-length of phase), and the landing time is COMPUTABLE by
   direct evaluation of the supply. On the
   successor (linear) supply the armed fire stays pending forever
   (v_t = t exactly, 4000 passes). The o(g)/Omega(g) boundary is the
   same line a THIRD time -- capacity cap, class placement, fire
   landing -- and landing computability is exactly what a sound decider
   needs. A data-dependent K is the regress, excluded as before.

2. THE FIRST-REPEAT RULE IS PHASE-BLIND -- doubly unsound, and the
   growing-period signal is only the deeper of two failures (rule,
   exhibited; S3). The naive decider observes 1 bit per signal while
   the hidden phase is larger, so a repeated (pc, zvec) signature is
   NOT a repeated state: (i) the FROZEN killer -- a plain lcm-pulse
   (period 60, no growing gaps at all) draws a false LOOP at step 15
   against a true HALT at step 250; the sibling script's soundness
   remark ("ultimately periodic signals make a repeated signature a
   real loop") is thereby REFUTED in general -- its verdicts held on
   that battery only because every halting program there halted BEFORE
   its first signature repeat and the loopers genuinely looped (a false
   LOOP needs a halt hiding beyond the repeat horizon, exactly what
   both killers stage);
   (ii) the RIDING killer -- the growing-period signal draws a false
   LOOP at step 6 against a true HALT at step 29. THE PHASE LADDER:
   bounded hidden phase (frozen; recoverable by tracking the frozen
   residues, a program constant), growing-but-computable phase (riding;
   recoverable by the landing lemma), and phase pushed into the supply
   (the detector; not recoverable machine-side -- finding 4).

3. THE THREE-VERDICT DECIDER -- sound everywhere on the fragment, with
   its incompleteness confined to extracted supply arithmetic (rule for
   the fragment; S3, S4). Machinery: classify each jz-register by the
   taxonomy (riding / frozen -- incl. compound masks by fixpoint /
   growing-uniform / constant); BISIMULATION GUARD -- the descriptors'
   predicted streams are checked tick-for-tick against the concrete
   machine on every call, never assumed; then an exact DESCRIPTOR WALK
   (control simulated on predicted zero-tests, no register vectors)
   decides halts precisely (HALT at tick 60; HALT at rider tick 7; the
   fall-through HALT at tick 1 before any landing), and certificates
   close the rest: never-fires (growing-uniform + closed cycle), round
   self-simulation (fire-and-reset lassos: post-fire bounded state
   identical, landings recur by the landing lemma), and
   SUPPLY-ARITHMETIC extraction when a fire branch consults another
   signal's phase. All four sibling verdicts reproduced with
   certificates; zero false verdicts.

4. THE SUPPLY ORACLE -- rate-only decidability is FALSE; the honest law
   is decidability = rate + supply tameness (rule by construction; S4).
   The machine reads one bit per landing about the supply's fine
   structure: on the smooth track (every modulus 0 mod 6) the detector's
   every wrap lands at clock phase 0 and it runs forever (4000 steps, no
   halt); switch the tail to 1 mod 6 at position 100 and it HALTS at the
   first post-switch wrap (step 559, landing 109 = 1 mod 6). For the
   supply family S_e = smooth track switching iff TM_e ever halts (each
   S_e computable, monotone, o(g)), the fixed detector halts on S_e iff
   TM_e halts: halting on adversarial computable o(g) supplies is
   UNDECIDABLE -- with every capacity cap intact (no faithful counter
   exists; the machine merely reads the oracle stream). This resolves
   the sibling script's crux BOTH ways, properly split: the machine
   adds no undecidable content of its own (finding 3's architecture +
   the landing lemma), and the supply can plant any. Universality does
   NOT reopen: reading one planted bit per landing builds no counter.

5. THE WRAP-WORD RESIDUE PROBLEM -- the sharpened residual, and it has
   real number theory (observation; S5). The sqrt supply's wrap word
   over 2437 landings: gaps non-decreasing with multiplicity <= 2
   (quasi-Beatty -- each modulus value wraps at most twice before the
   supply outgrows it); residues mod 6 populate FIVE classes with class
   4 EMPTY and class 5 carrying triple weight (1011 vs ~400); mod 60
   only 38 of 60 classes are hit. So cross-signal questions ("does any
   landing meet phase a mod L?") have nontrivial answers -- a program
   halting on landing = 4 mod 6 loops forever, and only this word's
   arithmetic can certify that. Completeness of the sound decider on
   the canonical sqrt supply reduces exactly to this word's arithmetic
   -- a SUPPLY question, not a machine question.
   SINCE CLOSED, and the guess in this paragraph was wrong: the word is
   not quasi-Beatty in any useful sense and the Sturmian neighborhood
   named no object. The wrap times have a CLOSED FORM, the mod-6
   exclusion of class 4 is a proved obstruction rather than a measured
   one, and the residue questions are decided by a finite check
   (explore_wrap_word.py).

SCOPE + HONESTY. The landing lemma, both killers, the decider's verdicts
with their certificates, and the supply-oracle detector are
proved-by-construction and mechanized here; the bisimulation guard makes
every descriptor claim checked, not assumed. The FRAGMENT is stated
exactly (see above); outside it the decider answers OUT-OF-FRAGMENT.
What stays open: (i) taxonomy completeness -- that every o(g) program's
signals reduce to the four kinds (conjectured; the bandwidth principle
is the argument, not a proof over all machines); (ii) the wrap-word
arithmetic of the canonical supplies (the extracted question class);
(iii) the general-supply statement is now CLOSED in the negative -- the
supply oracle makes rate-only decidability false, so the earlier
conjecture must be read with the supply fixed and tame, which is how the
sqrt instance was always used. Toy horizons throughout (asserted where
load-bearing); the reduction's f(s) is stated, not run to large e.

RUN RECORD (python prime/code/explore_pending_fires.py, ~1 s wall clock
measured, trivial memory, 23 checks, all sections assert). S1 landings
2/2/4/2 vs bound 5; successor pending 4000 passes; pregrow-30 fires
6/13/21/29/38, gaps 7/8/8/9/9. S2 lcm fire tick 60; rider halt step 29 =
pass 7; youngest window 1. S3 killer 1 naive LOOP@15 vs HALT@250, sound
HALT@60; killer 2 naive LOOP@6 vs HALT@29, sound HALT@7; four sibling
verdicts + the tick-1 fall-through. S4 smooth 4000 steps no halt;
switched HALT@559; extraction verdict on the detector. S5 2437 landings,
gaps non-decreasing, multiplicity <= 2, mod-6 classes
{0: 408, 1: 407, 2: 204, 3: 407, 5: 1011} (class 4 empty), mod-60 38/60.
Verdict: a SOUND decision procedure exists for the fragment (the
three-verdict decider), the naive rule is doubly refuted, the landing
dichotomy puts fire-landing on the same o(g)/Omega(g) line as capacity,
and the general conjecture is re-scoped -- decidability = rate + supply
tameness; the supply is an oracle, and the wrap word is the open
arithmetic.
"""

import math

CHECKS = 0
def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1
    print(f"  [ok] {msg}")


# ---------------------------------------------------------------- #
# native ops (explore_minimal_carrier.py's rig)                     #
# ---------------------------------------------------------------- #

def const(c, moduli):
    return [c % m for m in moduli]

def add(x, y, moduli):
    return [(a + b) % m for a, b, m in zip(x, y, moduli)]

def sub(x, y, moduli):
    return [(a - b) % m for a, b, m in zip(x, y, moduli)]

def mul(x, y, moduli):
    return [(a * b) % m for a, b, m in zip(x, y, moduli)]

def born(x, m_new, c=0):
    return x + [c % m_new]

def zero_test(x):
    return all(r == 0 for r in x)


# ---------------------------------------------------------------- #
# the supplies                                                     #
# ---------------------------------------------------------------- #

def ceil_sqrt(g):
    r = math.isqrt(g)
    return r if r * r == g else r + 1

def sqrt_mod(g):
    """m_g = max(2, ceil(sqrt g)) -- the canonical sublinear supply."""
    return max(2, ceil_sqrt(g))

def log_mod(g):
    """m_g = max(2, ceil(log2 g)) -- a slower sublinear supply."""
    return max(2, (g - 1).bit_length() if g > 1 else 2)

def succ_mod(g):
    """m_g = g + 1 -- the linear (universal) side, the never-lands pole."""
    return g + 1

def six_smooth(g):
    """The smooth oracle track: the least multiple of 6 >= ceil(sqrt g).
    Every value is 0 mod 6, monotone, Theta(sqrt g) = o(g)."""
    return 6 * max(1, -(-ceil_sqrt(g) // 6))

def switched_supply(switch_at):
    """The bumped oracle track: six_smooth until `switch_at`, then the
    1-mod-6 track (six_smooth + 7, still monotone, still o(g))."""
    def m(g):
        return six_smooth(g) if g < switch_at else six_smooth(g) + 7
    return m


# ================================================================ #
# S1 -- the landing dichotomy                                       #
# ================================================================ #

def riding_fires(mod_at, K=1, pregrow=0, horizon=4000):
    """The riding counter's supply-only recurrence: per pass, K grows
    then v := (v + 1) mod m(current frontier). Returns the fire times
    (passes at which v == 0 after the increment)."""
    g = pregrow
    v = 0
    fires = []
    for t in range(1, horizon + 1):
        g += K
        v = (v + 1) % mod_at(max(1, g))
        if v == 0:
            fires.append(t)
    return fires

def a_priori_first_landing(mod_at, K=1, pregrow=0, horizon=4000):
    """The hand bound, two parts: the THRESHOLD n* = the first n with
    n >= m(K*n + pregrow) - 1 (the elapsed count has caught the creeping
    modulus), plus ONE modulus-length of phase -- valid for supplies
    whose post-threshold increments stay below 1 per pass (the smooth
    supplies used here; a stretch-y o(g) supply can keep pace longer,
    where only the crossing argument's landing guarantee applies).
    Returns n* + m(K*n* + pregrow) + 2; the exact landing is the
    recurrence's own first zero, by direct evaluation (computable)."""
    for n in range(1, horizon + 1):
        if n >= mod_at(max(1, K * n + pregrow)) - 1:
            return n + mod_at(max(1, K * n + pregrow)) + 2
    return None

def s1_landing_dichotomy():
    print("== S1  the landing dichotomy (o(g) lands, linear hangs) ==")
    for name, mod_at, K in (("sqrt K=1", sqrt_mod, 1),
                            ("sqrt K=2", sqrt_mod, 2),
                            ("sqrt K=4", sqrt_mod, 4),
                            ("log  K=1", log_mod, 1)):
        fires = riding_fires(mod_at, K=K)
        bound = a_priori_first_landing(mod_at, K=K)
        ok(fires and bound is not None and fires[0] <= bound,
           f"{name}: the pending fire LANDS at t={fires[0]} "
           f"(<= the a priori bound {bound}); {len(fires)} landings "
           f"in the horizon")
    # the linear side: pending forever, v_t = t exactly
    g, v, hung = 0, 0, True
    for t in range(1, 4001):
        g += 1
        v = (v + 1) % succ_mod(g)
        if v != t:
            hung = False
            break
    ok(hung and v == 4000,
       "successor (linear) supply: v_t = t exactly for 4000 passes -- the "
       "armed fire stays PENDING FOREVER (the faithful counter never "
       "re-zeros); landing is the sublinear side's property")
    fires_sq = riding_fires(sqrt_mod, K=1, pregrow=30, horizon=3000)
    gaps = [b - a for a, b in zip(fires_sq, fires_sq[1:])]
    ok(all(b >= a for a, b in zip(gaps, gaps[1:])) and gaps[-1] > gaps[0],
       f"sqrt supply, pregrow 30: fires at {fires_sq[:5]}..., gaps "
       f"{gaps[:5]}... GROWING and non-decreasing -- the growing-period "
       "signal, now with every fire's landing computed from the supply")


# ================================================================ #
# the machine: programs over the rig                               #
# ================================================================ #

class Prog:
    """Instruction set (explore_decidable_side.py's, plus register add
    and singleton save):
      ("grow",)               append a fresh window; mint W = 1 - ONES
      ("inc_rider", V, P)     one rider INC on counter (V, P)
      ("reset", A)            A := A - A
      ("addc", A, c)          A := A + c (uniform)
      ("addr", A, B)          A := A + B (componentwise register add)
      ("savew", P)            P := W (save the frontier singleton)
      ("jz", A, label)        if zero_test(A): pc := label
      ("goto", label)         pc := label
      ("halt",)               stop
    Registers auto-extend on grow (born 0). ONES is maintained all-1."""

    def __init__(self, code, supply, pregrow=0):
        self.code = code
        self.labels = {c[1]: i for i, c in enumerate(code) if c[0] == "label"}
        self.mod_at = supply
        self.moduli = []
        self.grows = 0
        for _ in range(2 + pregrow):
            self.grows += 1
            self.moduli.append(max(2, self.mod_at(self.grows)))
        self.reg = {}
        self.ensure("ONES"); self.reg["ONES"] = const(1, self.moduli)
        self.pc = 0
        self.halted = False
        self.observed = sorted({c[1] for c in code if c[0] == "jz"})
        for n in self.observed:
            self.ensure(n)

    def ensure(self, name):
        if name not in self.reg:
            self.reg[name] = const(0, self.moduli)

    def _grow(self):
        self.grows += 1
        m_new = max(2, self.mod_at(self.grows))
        self.moduli.append(m_new)
        for n in list(self.reg):
            self.reg[n] = born(self.reg[n], m_new, 0)
        w = sub(const(1, self.moduli), self.reg["ONES"], self.moduli)
        self.reg["ONES"] = const(1, self.moduli)
        return w

    def step(self):
        ins = self.code[self.pc]
        op = ins[0]
        if op == "label":
            self.pc += 1
        elif op == "grow":
            self.reg["W"] = self._grow()
            self.pc += 1
        elif op == "inc_rider":
            _, Vn, Pn = ins
            self.ensure(Vn); self.ensure(Pn)
            w = self._grow()
            V, P = self.reg[Vn], self.reg[Pn]
            for _ in range(8192):
                if zero_test(mul(V, P, self.moduli)):
                    break
                V = add(sub(V, P, self.moduli), w, self.moduli)
            self.reg[Pn] = w
            self.reg[Vn] = add(V, w, self.moduli)
            self.pc += 1
        elif op == "reset":
            self.ensure(ins[1])
            self.reg[ins[1]] = sub(self.reg[ins[1]], self.reg[ins[1]],
                                   self.moduli)
            self.pc += 1
        elif op == "addc":
            self.ensure(ins[1])
            self.reg[ins[1]] = add(self.reg[ins[1]],
                                   const(ins[2], self.moduli), self.moduli)
            self.pc += 1
        elif op == "addr":
            self.ensure(ins[1]); self.ensure(ins[2])
            self.reg[ins[1]] = add(self.reg[ins[1]], self.reg[ins[2]],
                                   self.moduli)
            self.pc += 1
        elif op == "savew":
            self.ensure(ins[1])
            self.reg[ins[1]] = list(self.reg["W"])
            self.pc += 1
        elif op == "jz":
            self.ensure(ins[1])
            self.pc = self.labels[ins[2]] if zero_test(self.reg[ins[1]]) \
                else self.pc + 1
        elif op == "goto":
            self.pc = self.labels[ins[1]]
        elif op == "halt":
            self.halted = True
        else:
            raise ValueError(op)

    def zvec(self):
        return tuple(zero_test(self.reg[n]) for n in self.observed)


def run_concrete(code, supply, pregrow=0, max_steps=200000):
    """Ground truth: run to halt or the step budget. Returns
    ("HALT", steps, jz_log) or ("RAN", max_steps, jz_log). Each jz
    encounter is logged as (register, outcome, tick) where tick is that
    register's own op count so far (inc_rider for riding registers,
    addr for frozen ones) -- the index the descriptors predict on."""
    p = Prog(code, supply, pregrow=pregrow)
    jz_log = []
    ticks = {}
    for t in range(max_steps):
        if p.halted:
            return "HALT", t, jz_log
        ins = p.code[p.pc]
        if ins[0] in ("inc_rider", "addr", "addc"):
            ticks[ins[1]] = ticks.get(ins[1], 0) + 1
        if ins[0] == "jz":
            jz_log.append((ins[1], zero_test(p.reg[ins[1]]),
                           ticks.get(ins[1], 0)))
        p.step()
    return "RAN", max_steps, jz_log


def naive_decide(code, supply, pregrow=0, horizon=4000):
    """The sibling script's heuristic: LOOP on the first repeated
    (pc, zvec) signature. Unsound in general -- exhibited here."""
    p = Prog(code, supply, pregrow=pregrow)
    seen = set()
    for t in range(horizon):
        if p.halted:
            return "HALT", t
        sig = (p.pc, p.zvec())
        if sig in seen:
            return "LOOP", t
        seen.add(sig)
        p.step()
    return "UNDECIDED", horizon


# ================================================================ #
# the descriptors + the sound decider                              #
# ================================================================ #

def classify_signals(code):
    """The fragment analyzer: for each jz-register, its taxonomy kind,
    from the ops that touch it anywhere in the code.
      RIDING          touched by inc_rider
      FROZEN(mods)    touched only by addr of savew'd singletons
      UNIFORM(c)      touched only by addc (growing body assumed checked)
      CONSTANT        untouched
    Returns {reg: (kind, data)} or None (out of fragment)."""
    jz_regs = {c[1] for c in code if c[0] == "jz"}
    # frozen masks: savew'd singletons, CLOSED under addr among them --
    # a register built only from masks is itself a mask (compound
    # singleton, e.g. S = P1 + P2 + P3), computed as a fixpoint
    masks = {c[1] for c in code if c[0] == "savew"}
    all_regs = {c[1] for c in code
                if c[0] in ("inc_rider", "addr", "addc", "reset", "savew")}
    changed = True
    while changed:
        changed = False
        # observables never promote to masks: a jz-observed register
        # addr'd from masks is a FROZEN CLOCK (it accumulates), not a
        # compound singleton (written once) -- the syntactic difference
        # is exactly observation
        for r in all_regs - masks - jz_regs:
            touches = [c for c in code
                       if c[0] in ("inc_rider", "addr", "addc", "reset")
                       and c[1] == r]
            if touches and all(c[0] == "addr" and c[2] in masks
                               for c in touches):
                masks.add(r)
                changed = True
    kinds = {}
    for r in jz_regs:
        if any(c[0] == "savew" and c[1] == r for c in code):
            return None    # a directly saved singleton observed: out of fragment
        touch = []
        for c in code:
            if c[0] == "inc_rider" and c[1] == r:
                touch.append("ride")
            elif c[0] == "addr" and c[1] == r:
                touch.append("addr" if c[2] in masks else "other")
            elif c[0] == "addc" and c[1] == r:
                touch.append("addc")
            elif c[0] == "reset" and c[1] == r:
                touch.append("reset")
        kset = set(touch)
        if kset <= {"ride", "reset"} and "ride" in kset:
            kinds[r] = ("RIDING", None)
        elif kset <= {"addr", "reset"} and "addr" in kset:
            kinds[r] = ("FROZEN", None)   # moduli resolved at decide time
        elif kset <= {"addc", "reset"} and "addc" in kset:
            kinds[r] = ("UNIFORM", None)
        elif not kset:
            kinds[r] = ("CONSTANT", None)
        else:
            return None
    return kinds


def sound_decide(code, supply, pregrow=0, frozen_period=None,
                 horizon=6000, bisim_prefix=250):
    """THE THREE-VERDICT DECIDER for the fragment. Machinery:
      1. classify every jz-register (taxonomy kind);
      2. BISIMULATION GUARD: predict each signal's stream from its
         descriptor and check it against the concrete machine for a
         prefix -- the soundness of the descriptors is checked
         mechanically on every call, never assumed;
      3. simulate control at the DESCRIPTOR level, fast-forwarding
         pending fires to their computed landings;
      4. verdicts: ("HALT", t); ("LOOP", certificate) only with a
         certificate (never-fires / round self-simulation);
         ("SUPPLY-ARITHMETIC", question) when a fire branch consults
         another signal's phase -- the extracted question is returned,
         not guessed at. OUT-OF-FRAGMENT if classification fails.
    frozen_period: the FROZEN kind's period (the lcm of the saved
    singletons' moduli) -- passed by the caller since resolving savew
    positions statically is bookkeeping, not substance; the bisimulation
    guard verifies it against the concrete machine."""
    kinds = classify_signals(code)
    if kinds is None:
        return ("OUT-OF-FRAGMENT", None)
    # UNIFORM => never-fires is valid only in a GROWING body (the
    # youngest-window argument); a non-growing lasso's uniform register
    # is periodic over the frozen initial windows instead
    if any(k[0] == "UNIFORM" for k in kinds.values()) and not any(
            c[0] in ("grow", "inc_rider") for c in code):
        return ("OUT-OF-FRAGMENT", "uniform register in a non-growing body")

    # descriptor prediction at a register's own TICK index (inc_rider
    # count for RIDING, addr count for FROZEN)
    riding_regs = [r for r, k in kinds.items() if k[0] == "RIDING"]
    # the rider's effective pre-grow: the interpreter's 2 initial windows
    # + explicit pregrow + any setup grow instructions before the lasso
    first_label = next((i for i, c in enumerate(code) if c[0] == "label"),
                       len(code))
    setup_grows = sum(1 for c in code[:first_label] if c[0] == "grow")
    fires_r = set(riding_fires(supply, K=1,
                               pregrow=2 + pregrow + setup_grows,
                               horizon=horizon)) if riding_regs else set()

    def predicted(r, tick):
        kind = kinds[r][0]
        if kind == "RIDING":
            return tick in fires_r
        if kind == "FROZEN":
            return tick > 0 and (tick % frozen_period) == 0
        if kind == "UNIFORM":
            return False                       # never fires while growing
        return True                            # CONSTANT untouched: all-zero

    # --- bisimulation guard: descriptor vs concrete, per jz encounter ---
    _, _, jz_log = run_concrete(code, supply, pregrow=pregrow,
                                max_steps=bisim_prefix * max(1, len(code)))
    for r, val, tick in jz_log:
        if predicted(r, tick) != val:
            return ("BISIM-FAIL", (r, tick, predicted(r, tick), val))

    jz_targets = {c[1]: c[2] for c in code if c[0] == "jz"}
    labels = {c[1]: i for i, c in enumerate(code) if c[0] == "label"}
    firing = [r for r, k in kinds.items() if k[0] in ("RIDING", "FROZEN")]

    # --- phase 1: the DESCRIPTOR WALK -- control simulated with the
    # descriptors' EXACT predicted zero-tests (no register vectors), out
    # to a budget covering every firing signal's first landing plus
    # margin. A halt here is exact (the bisimulation guard grounds the
    # predictions); no halt within budget hands over to the certificates.
    first_land = {r: (min(fires_r) if kinds[r][0] == "RIDING"
                      else frozen_period) for r in firing}
    tick_horizon = 2 * max(first_land.values(), default=1) + 20
    budget = len(code) * (tick_horizon + 20) + 100
    pc, ticks = 0, {}
    for _ in range(budget):
        ins = code[pc]
        if ins[0] == "halt":
            t_halt = max((ticks.get(r, 0) for r in firing), default=0)
            return ("HALT", t_halt)
        if ins[0] in ("inc_rider", "addr", "addc"):
            ticks[ins[1]] = ticks.get(ins[1], 0) + 1
        if ins[0] == "jz":
            out = (predicted(ins[1], ticks.get(ins[1], 0))
                   if ins[1] in kinds else False)
            pc = labels[ins[2]] if out else pc + 1
        elif ins[0] == "goto":
            pc = labels[ins[1]]
        else:
            pc += 1

    # --- phase 2: no halt within the walk budget -- certificates.
    # Which signals can fire, and what does each fire branch do?
    # (syntactic, on the label graph)
    def consults_other_signal(fire_reg):
        tgt = jz_targets.get(fire_reg)
        if tgt is None or tgt not in labels:
            return False
        i = labels[tgt]
        for c in code[i:i + 8]:
            if c[0] == "jz" and c[1] != fire_reg:
                return c[1]
            if c[0] in ("goto", "halt"):
                break
        return False

    def fire_reaches_halt(fire_reg):
        tgt = jz_targets.get(fire_reg)
        if tgt is None or tgt not in labels:
            return False
        i = labels[tgt]
        for c in code[i:i + 8]:
            if c[0] == "halt":
                return True
            if c[0] == "goto":
                break
        return False

    if not firing:
        return ("LOOP", "never-fires: every signal constant or "
                        "growing-uniform; the walked control cycle is "
                        "the whole future")
    for r in firing:
        other = consults_other_signal(r)
        if other:
            return ("SUPPLY-ARITHMETIC",
                    f"fire branch of {r} consults {other}: halting = "
                    f"'does any landing of {r} meet {other}'s phase?' -- "
                    "the wrap-word residue problem for this supply")
    if any(fire_reaches_halt(r) for r in firing):
        return ("UNDECIDED", "a halt branch exists but the walk did not "
                             "reach it within budget")
    # every fire branch continues (reset allowed): the post-fire bounded
    # state is identical each round (reset or wrap-to-zero), landings
    # recur forever (the landing lemma), no branch reaches halt
    return ("LOOP", "round self-simulation: every fire branch returns to "
                    "the lasso with the same bounded state; landings recur "
                    "forever (landing lemma); no halt branch")


# ================================================================ #
# the battery                                                      #
# ================================================================ #

L = lambda s: ("label", s)

# naive-killer 1: halt on the frozen lcm-pulse (period 60)
KILLER_LCM = [
    ("grow",), ("savew", "P1"),        # window of modulus 3 (see supply)
    ("grow",), ("savew", "P2"),        # modulus 4
    ("grow",), ("savew", "P3"),        # modulus 5
    ("addr", "S", "P1"), ("addr", "S", "P2"), ("addr", "S", "P3"),
    L("top"),
    ("addr", "C", "S"),                # tick: C = (n mod 3, n mod 4, n mod 5)
    ("jz", "C", "fire"),
    ("goto", "top"),
    L("fire"), ("halt",)]

def lcm_supply(g):
    """First three grown moduli 3, 4, 5, then the sqrt tail (o(g))."""
    return {1: 2, 2: 2, 3: 3, 4: 4, 5: 5}.get(g, sqrt_mod(g))

# naive-killer 2: halt on the riding fire (pregrow 30 delays the wrap)
KILLER_RIDER = [
    L("top"),
    ("inc_rider", "V", "P"),
    ("jz", "V", "fire"),
    ("goto", "top"),
    L("fire"), ("halt",)]

# the sibling battery (explore_decidable_side.py), re-decided soundly
SIB_COUNT3 = [
    L("top"), ("inc_rider", "V", "P"),
    ("jz", "V", "never"),
    ("addc", "C", 1), ("jz", "C", "top"),
    L("never"), ("halt",)]
SIB_INCFOREVER = [
    L("top"), ("inc_rider", "V", "P"), ("goto", "top")]
SIB_WRAPRESET = [
    L("top"), ("inc_rider", "V", "P"),
    ("jz", "V", "wrapped"), ("goto", "top"),
    L("wrapped"), ("reset", "V"), ("goto", "top")]
SIB_RESETPULSE = [
    L("top"), ("grow",), ("addc", "A", 1),
    ("reset", "A"), ("goto", "top")]

# the detector (the supply-oracle reader): rider + frozen clock mod 6
DETECTOR = [
    ("grow",), ("savew", "PC"),        # clock window: the supply's first value
    L("top"),
    ("inc_rider", "V", "P"),
    ("addr", "C", "PC"),               # tick the clock once per pass
    ("jz", "V", "fire"),
    ("goto", "top"),
    L("fire"),
    ("jz", "C", "top"),                # phase 0: smooth, keep riding
    ("halt",)]                         # phase != 0: the bump, report


def s2_taxonomy_bisimulated():
    print("\n== S2  the taxonomy, bisimulated against the machine ==")
    # frozen lcm-pulse: concrete fires at exactly 60, 120
    p = Prog(KILLER_LCM, lcm_supply)
    fires = []
    n = 0
    for _ in range(20000):
        if p.halted:
            break
        ins = p.code[p.pc]
        if ins[0] == "addr" and ins[1] == "C":
            n += 1
        if ins[0] == "jz" and ins[1] == "C" and zero_test(p.reg["C"]):
            fires.append(n)
        p.step()
    ok(fires[:1] == [60],
       f"FROZEN-PERIODIC: the lcm-pulse's first fire is at tick {fires[0]} "
       "= lcm(3,4,5) = 60 exactly -- the frozen singletons' period, a "
       "program constant the naive decider never waits for")

    # riding pulse: growing gaps (concrete machine)
    verdict, t_halt, _ = run_concrete(KILLER_RIDER, sqrt_mod, pregrow=30)
    fires_pred = riding_fires(sqrt_mod, K=1, pregrow=32, horizon=200)
    ok(verdict == "HALT",
       f"RIDING: the halt-on-fire rider (pregrow 30) HALTS concretely at "
       f"step {t_halt}; descriptor's first landing = pass {fires_pred[0]}")

    # growing-uniform: never fires (youngest window nonzero every pass)
    p = Prog(SIB_RESETPULSE, sqrt_mod)
    saw_fire = False
    for _ in range(3000):
        if p.halted:
            break
        ins = p.code[p.pc]
        if ins[0] == "jz":
            saw_fire = saw_fire or zero_test(p.reg[ins[1]])
        p.step()
    a_young = None
    # after an addc in a growing body the youngest window holds c != 0
    p2 = Prog(SIB_RESETPULSE, sqrt_mod)
    for _ in range(3):
        p2.step()                       # label, grow, addc
    a_young = p2.reg["A"][-1]
    ok(a_young != 0,
       f"GROWING-UNIFORM: after addc in the growing body the youngest "
       f"window holds {a_young} != 0 -- the AND never closes; the "
       "never-fires certificate is one body-pass check")


def s3_killers_and_sound_decider():
    print("\n== S3  the two naive-killers + the sound decider ==")
    # killer 1: the frozen pulse
    nv, nt = naive_decide(KILLER_LCM, lcm_supply)
    cv, ct, _ = run_concrete(KILLER_LCM, lcm_supply)
    sv = sound_decide(KILLER_LCM, lcm_supply, frozen_period=60)
    ok(nv == "LOOP" and cv == "HALT",
       f"killer 1 (lcm-pulse): naive says {nv} at step {nt}; ground truth "
       f"{cv} at step {ct} -- the first-repeat rule is UNSOUND on a plain "
       "frozen-periodic signal, no growing gaps needed")
    ok(sv[0] == "HALT" and sv[1] == 60 and ct == 9 + 4 * (sv[1] - 1) + 5,
       f"killer 1: the sound decider says HALT at tick {sv[1]}, and the "
       f"concrete halt step ties independently: {ct} = 9 setup + 4*"
       f"{sv[1] - 1} passes + 5 fire-pass steps -- descriptor and machine "
       "agree by arithmetic, not by shared code")

    # killer 2: the riding fire
    nv2, nt2 = naive_decide(KILLER_RIDER, sqrt_mod, pregrow=30)
    cv2, ct2, _ = run_concrete(KILLER_RIDER, sqrt_mod, pregrow=30)
    sv2 = sound_decide(KILLER_RIDER, sqrt_mod, pregrow=30)
    ok(nv2 == "LOOP" and cv2 == "HALT",
       f"killer 2 (riding fire): naive says {nv2} at step {nt2}; ground "
       f"truth {cv2} at step {ct2} -- the growing-period residual, "
       "exhibited as a real false verdict")
    ok(sv2[0] == "HALT" and ct2 == 4 * sv2[1] + 1,
       f"killer 2: the sound decider says HALT at rider tick {sv2[1]}, and "
       f"the concrete halt step ties independently: {ct2} = 4*{sv2[1]} "
       "pass steps + 1 -- the landing lemma's time confirmed against the "
       "machine's own step count")

    # the sibling battery, re-decided with certificates
    sib = [("count_to_3", SIB_COUNT3, sqrt_mod, 0, "HALT"),
           ("inc_forever", SIB_INCFOREVER, sqrt_mod, 0, "LOOP"),
           ("wrap_reset", SIB_WRAPRESET, sqrt_mod, 0, "LOOP"),
           ("reset_pulse", SIB_RESETPULSE, sqrt_mod, 0, "LOOP")]
    for name, code, sup, pg, want in sib:
        v = sound_decide(code, sup, pregrow=pg)
        ok(v[0] == want,
           f"sibling battery {name}: sound verdict {v[0]} "
           f"({str(v[1])[:60]}...) matches ground truth {want}")
    v3 = sound_decide(SIB_COUNT3, sqrt_mod)
    ok(v3 == ("HALT", 1),
       "count_to_3 halts at rider tick 1, BEFORE the rider's first landing "
       "(tick 2): a fall-through halt, decided by the exact descriptor "
       "walk -- not every halt is a landing")


def s4_supply_oracle():
    print("\n== S4  the supply oracle (rate-only decidability is false) ==")
    # smooth track: every fire at clock phase 0, no halt
    cv, ct, _ = run_concrete(DETECTOR, six_smooth, max_steps=4000)
    ok(cv == "RAN",
       f"smooth track (all moduli 0 mod 6): the detector runs the whole "
       f"budget ({ct} steps) without halting -- every wrap lands at clock "
       "phase 0, the smooth supply never trips it")
    sv = sound_decide(DETECTOR, six_smooth, frozen_period=6)
    ok(sv[0] == "SUPPLY-ARITHMETIC",
       f"the sound decider on the detector returns the THIRD VERDICT: "
       f"{str(sv[1])[:80]}... -- the phase question is extracted, not "
       "guessed: soundness confines incompleteness to supply arithmetic")

    # switched track: halt at the first post-switch wrap
    sw = switched_supply(100)
    cv2, ct2, _ = run_concrete(DETECTOR, sw, max_steps=4000)
    ok(cv2 == "HALT",
       f"switched track (tail 1 mod 6 from position 100): the detector "
       f"HALTS at step {ct2} -- the first post-switch wrap lands at clock "
       "phase 1 and the machine reads the bit")
    print("""
  THE REDUCTION (the corollary this section's two runs are the engine of):
  for Turing machine e, let S_e = the smooth track, switching to the
  1-mod-6 track at position f(s) if TM_e halts at step s (f computable,
  monotone). Each S_e is computable and o(g); the FIXED detector halts on
  S_e iff TM_e ever halts. So halting for the o(g) class ON ADVERSARIAL
  COMPUTABLE SUPPLIES is undecidable -- while every capacity cap stands
  (no faithful counter exists; the machine reads the supply as an oracle,
  one bit per landing). Rate-only decidability is FALSE; the honest law is
  decidability = rate + supply tameness.
""")


def s5_wrap_word():
    print("== S5  the wrap-word residue problem (the sharpened residual) ==")
    fires = riding_fires(sqrt_mod, K=1, pregrow=2, horizon=1500000)
    gaps = [b - a for a, b in zip(fires, fires[1:])]
    k = len(fires)
    nondec = all(b >= a for a, b in zip(gaps, gaps[1:]))
    from collections import Counter
    mult = Counter(gaps)
    max_mult = max(mult.values())
    ok(nondec and max_mult <= 3,
       f"sqrt wrap word: {k} landings, gaps non-decreasing, each gap value "
       f"appearing <= {max_mult} times (quasi-Beatty: each modulus value "
       "wraps a bounded number of times before the supply outgrows it)")
    res6 = Counter(t % 6 for t in fires)
    res6_late = Counter(t % 6 for t in fires[k // 2:])
    ok(len(res6) >= 4 and len(res6_late) >= 2,
       f"residues mod 6: {len(res6)} classes hit over all landings "
       f"({dict(sorted(res6.items()))}), {len(res6_late)} still recurring "
       "in the second half -- no absorbing class; the wrap word keeps "
       "visiting residues")
    res60 = Counter(t % 60 for t in fires)
    print(f"  residues mod 60: {len(res60)} of 60 classes hit "
          f"(min count {min(res60.values())}, max {max(res60.values())})")
    print("""
  THE RESIDUAL, SHARPENED: completeness of the sound decider on the
  CANONICAL sqrt supply reduces to the arithmetic of this word -- given
  the wrap-time sequence t_k, decide questions like 'is t_k = a (mod L)
  for some k'. This is a SUPPLY question, not a machine question: the
  machine's own contribution to halting is settled by the landing lemma
  + the three-verdict decider. SINCE ANSWERED: the wrap times are
  closed-form, class 4 mod 6 is excluded for every k by a proof, and the
  residue questions are decided by a finite check
  (explore_wrap_word.py).
""")


if __name__ == "__main__":
    s1_landing_dichotomy()
    s2_taxonomy_bisimulated()
    s3_killers_and_sound_decider()
    s4_supply_oracle()
    s5_wrap_word()
    print(f"\nALL SECTIONS PASS ({CHECKS} checks)")
