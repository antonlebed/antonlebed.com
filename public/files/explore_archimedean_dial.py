"""
explore_archimedean_dial.py -- THE ARCHIMEDEAN DIAL / THE KNIFE EDGE
(sibling of explore_growth_machine.py).

THE QUESTION (descending from explore_growth_machine.py).
explore_growth_machine.py located Turing-completeness at the DECREMENT for ONE
machine (the growth machine: INC + presence-zero-test, no DEC, decidable;
restore DEC and it is Minsky-universal). Generalize to the WHOLE
finite-window family: is EVERY archimedean-free (multiply-only,
inter-window-carry-free) substrate on the tower provably sub-universal,
and where EXACTLY does universality re-enter?

ANSWER -- THE KNIFE EDGE. Universality has TWO ingredients (Minsky): an
exact ZERO-TEST (branch on "= 0", revisitably) AND a BORROW (a move that
LOWERS a counter). NEITHER alone is universal:
  - zero-test, NO borrow  -> the growth machine: counters only rise, each
    test flips once, DECIDABLE (explore_growth_machine.py).
  - borrow, NO zero-test  -> a vector addition system (VAS): reachability
    DECIDABLE (Leroux-Schmitz 2019). A borrow alone is harmless.
  - both                  -> Minsky, UNIVERSAL.
The tower NATIVELY supplies the exact zero-test -- channel presence
(p | N?) is reduction at the finite place p, an INTRA-window read, free --
and NATIVELY deletes the borrow -- size/carry/overflow live only at the
archimedean place, the one INTER-window coupling the tower removes.
So the tower's finite-window family sits EXACTLY ONE
archimedean import -- a single borrow -- below Turing-completeness: it
already owns the hard half (the zero-test) for free, and only the deleted
place stands between it and universality. Memory reading: the zero-test
READS magnitude (native, a residue); the borrow ACTS on magnitude
(archimedean, deleted). Universality = read AND destructively act on
magnitude; the tower reads freely and cannot act -- that IS its
decidability, and it IS the deleted place.

THE DIAL (how the damage of a borrow is graded, all rows standard):
  primitives (all have INC)      zero-test borrow      reach term halt
  ---------------------------------------------------------------------
  multiply-only + presence       one-shot  none        DEC  DEC  DEC   <- the tower
  + decrement, no zero-branch     no        dec         DEC  DEC  DEC   VAS
  + reset, no zero-branch         no        reset       UND  DEC  DEC   reset net
  + decrement + zero-branch       yes       dec         UND  UND  UND   Minsky
A borrow WITHOUT a zero-test is graded: a plain decrement (VAS) keeps
everything; a FORGETFUL borrow (reset -- clear an unbounded window, the
general overflow) already costs the exact-value questions (reachability,
boundedness undecidable; termination, coverability still decidable --
Dufourd-Finkel-Schnoebelen 1998). And a REMEMBERING borrow -- a plain
decrement -- paired with the tower's NATIVE zero-test is exactly Minsky:
universal (that is the knife edge; the reset+zero-test corner is not
claimed here). The tower is saved from the bottom row only because it
deletes every borrow entirely.

THE VERIFIABLE INVARIANT -- THE DOWN-FLIP. Along a run, count the
zero-test outcome transitions nonzero -> zero (a counter RETURNING to a
tested threshold). Multiply-only worlds: ZERO down-flips (the zero-pattern
is monotone -> boundedly many flips -> a finite quotient decides).
A borrow makes down-flips possible (a counter comes back down to a tested
value) -> unbounded flips -> the finite quotient goes unsound. The
down-flip is the borrow's fingerprint = the archimedean act read
dynamically.

FINDINGS (run record below; every section asserts).

1. THE ARCHIMEDEAN-FREE FLOOR IS DECIDABLE (rule, proved for the modelled
   class + standard WSTS; verified S1). A finite-window substrate whose
   moves are pushes (translations of the depth vector) and whose tests are
   monotone thresholds depth(p) >= c is monotone on (N^k, <=) -- a
   well-quasi-order (Dickson) -- so termination is decidable. Shown
   CONSTRUCTIVELY by a halting decider on the CAPPED-depth quotient
   Q x prod(C_p + 1), C_p the largest threshold on window p. (Design catch:
   the quotient tracks capped DEPTHS, not threshold BITS -- a bare bit
   "depth >= 3" cannot be flipped by a quotient that does not count the
   INCs; the capped counter counts to its cap then freezes.) The decider
   settles a battery including non-terminating programs, agreeing with the
   naive simulation wherever it halts. The growth machine's presence-test is
   the c = 1 case; the whole archimedean-free family sits on this floor.

2. THE DOWN-FLIP IS THE BORROW (rule; verified S2). Count the zero-test
   transitions nonzero -> zero along each run. Over the multiply-only
   battery (growth-machine programs): ZERO down-flips -- the zero-pattern
   only loses zeros, never regains them, so it is monotone and flips
   boundedly. On a Minsky machine with a decrement: down-flips OCCUR (a
   counter walked down returns to zero). A down-flip is precisely a
   counter returning to a tested threshold -- the archimedean act -- and
   it is exactly what un-bounds the flip count and defeats the finite
   quotient. The borrow's presence is visible as its down-flips.

3. UNIVERSALITY NEEDS BOTH INGREDIENTS (rule, proved; verified S3).
   (a) zero-test, NO borrow: the growth machine -- S1 decides it, zero
   down-flips (S2). (b) borrow, NO zero-BRANCH: neutralize a Minsky
   machine's JZ (send both branches to the same successor). The decrement
   still fires, but c0 = 2 and c0 = 3 now share a fate -- the magnitude is
   no longer READ. The zero-BRANCH is where the machine reads magnitude;
   the borrow is where it acts. (c) both: the halts-iff-even Minsky machine
   sends c0 = 2 to HALT and c0 = 3 to a forever-loop from the SAME
   (control, zero-pattern) quotient node -- the S1 decider is unsound.
   Neither (a) nor (b) alone is universal; their conjunction is.

4. THE DIAL (synthesis -- the headline; the decidability tiers
   CITED, the down-flip/zero-branch discriminators verified S2-S3). The
   four rows above, keyed by (zero-test?, borrow-kind). Reading: the borrow
   is the dangerous import -- even a forgetful borrow alone (reset net)
   already loses reachability and boundedness (DFS98); a plain decrement
   paired with the tower's NATIVE zero-test is exactly Minsky-universal
   (the knife edge). The tower keeps only the top row by deleting the borrow --
   the archimedean place -- entirely. Undecidability re-enters from the top
   down (exact-value questions first, then everything) as the borrow
   deepens from none to forgetful to remembering-with-a-zero-test.
   (Column reading, load-bearing: "halt" = control reaches the HALT state
   with ANY counter values = COVERABILITY of a control marking, decidable
   for reset nets; "reach" = an EXACT marking, undecidable for reset nets.
   The reset row's reach=UND with halt=DEC is not a contradiction -- they
   are different problems, coverability vs exact reachability.)
   Sources: VAS reachability decidable (Mayr 1981, Kosaraju 1982,
   Leroux-Schmitz 2019); reset nets (Dufourd-Finkel-Schnoebelen 1998):
   reach + bound undecidable, term + cover decidable; Minsky (1967):
   halting undecidable; WSTS framework (Finkel-Schnoebelen 2001).

5. CARRY-FREEDOM = INTER-WINDOW COUPLING (observation; verified S5). The
   tower's carry-freedom is CRT channel-independence: (a + b) mod p_i =
   (a mod p_i + b mod p_i) mod p_i -- addition never couples distinct
   windows (verified componentwise over a battery). Positional base-b
   addition DOES couple digits: a carry propagates from a window to its
   neighbour (verified: a battery of adds with >= 1 propagated carry). The
   deleted archimedean place is exactly this inter-window coupling; the
   borrow (reset = forget, decrement = remember) is the coupling read as an
   operation. The zero-test, by contrast, is intra-window (a residue) --
   which is why the tower keeps it for free.

SETTLING POINTER (explore_slack_machine.py). The down-flip invariant of
finding 2 is measured over the DEPTH counters, and that is its whole
scope: "multiply-only worlds have zero down-flips" holds of depths and
is FALSE of the world. A quantity derived from the state can down-flip
unboundedly with no borrow anywhere -- the slack
v_l(odd lambda(N)) - v_l(N) + 1 does, twice per cycle of a program that
interleaves its instructions -- and a Minsky machine is built on
exactly that. So the down-flip diagnoses a borrow only among
counters that are depths; the knife-edge location below survives with
that scope attached, and what actually separates the cases is whether
the machine may READ the derived counter.

SCOPE + HONESTY. The floor (finding 1) is proved for the modelled class
(pushes + monotone threshold tests) and shown constructively; the general
statement rests on standard WSTS theory + Dickson's lemma. The DIAL's
decidability/undecidability ENTRIES (finding 4) are CITED theorems by
others (DFS98; Mayr/Kosaraju/Leroux; Minsky) -- undecidability cannot be
run; what is run-verified is the DOWN-FLIP invariant (finding 2), the
two-ingredient decomposition (finding 3), and the floor decider (finding
1). The claim is the IDENTIFICATION of the tower's finite-window family
with the top row, the reading of the zero-test as the native finite-place
read and the borrow as the deleted archimedean act, and the KNIFE-EDGE
location: the tower is one borrow short of universal. Not a claim about
arbitrary oracle-equipped demands. OPEN EDGE: the reset-only + native
zero-test corner (a forgetful borrow, no plain decrement) is left
unresolved -- is INC + exact-zero-test + reset (no decrement) universal,
or does its halting stay decidable? If decidable, the tower admits a
genuine intermediate archimedean grade (a "safe" forgetful borrow); if
universal, then ANY borrow flips it and the knife edge is even sharper.
The decrement case is settled (Minsky); this corner was open at this
record's writing. (It has since settled DECIDABLE, and stronger,
finite-state -- the forgetful borrow is value-blind:
explore_reset_corner.py.)

PREDICTIONS (fixed before the run). Adjudication -- NO MISSES, all confirmed:
  PR1 floor decider ......... CONFIRMED (5-program battery all correct;
      P_A + P_C decided LOOP with no terminating forward simulation)
  PR2 down-flip census ...... CONFIRMED (multiply-only MO_1 up=1/down=0,
      MO_2 up=2/down=0 -> ZERO down-flips; Minsky OSC up=0/down=1 -- the
      decrement returns c0 to zero, the borrow's fingerprint)
  PR3 both ingredients ...... CONFIRMED ((a) multiply-only monotone, S1
      decides; (b) neutralized zero-branch: c0=2 and c0=3 both LOOP?
      SAME fate, decrement intact; (c) live: c0=2 HALT, c0=3 LOOP?,
      opposite fates from the shared quotient node)
  PR4 the dial ............. CONFIRMED (4 rows; fully-undecidable iff
      zero-branch AND borrow; the forgetful borrow (reset) loses reach
      but keeps term; the tower row all DEC)
  PR5 carry-freedom ........ CONFIRMED (CRT add over Z/2310 componentwise,
      no inter-window carry; positional base-10 add 9 carries over 5 pairs)

RUN RECORD (python prime/code/explore_archimedean_dial.py, <1 s, trivial
memory, 57 checks): S1 floor decider (capped-quotient DFS; 5-program
threshold battery agreeing with forward sim wherever it halts; P_A, P_C
decided LOOP though their naive simulation never ends); S2 down-flip census
(multiply-only MO_1/MO_2 -> 0 down-flips; Minsky OSC -> 1 down-flip, the
decrement returning c0 to zero); S3 two ingredients ((b) neutralized JZ ->
c0=2,3 both LOOP?; (c) live EVENODD -> c0=2 HALT, c0=3 LOOP?, shared
(control, zero-pattern) node); S4 the dial (4 cited rows; the two-ingredient
predicate verified against the tiers); S5 carry-freedom (CRT add
channel-independent over 5 cross pairs; positional base-10 add 9 propagated
carries). No pre-run adjudication drafted; verdicts frozen in code, numbers
copied from output.
"""

CHECKS = 0


def ok(cond, msg=""):
    global CHECKS
    if not cond:
        raise AssertionError("CHECK FAILED: " + msg)
    CHECKS += 1


# ------------------------------------------------------------------ #
# S1 -- THE ARCHIMEDEAN-FREE FLOOR IS DECIDABLE (finding 1):
# the capped-quotient decider for translations + monotone threshold tests.
# ------------------------------------------------------------------ #
print("S1 -- THE ARCHIMEDEAN-FREE FLOOR (capped-quotient decider)")

# A monotone-threshold counter machine. Control 0..Q-1 plus HALT.
# instr[q] one of:
#   ("INC", i, q')               counter i += 1, goto q'
#   ("JGE", i, c, q_ge, q_lt)    if counter i >= c goto q_ge else q_lt
# NO DEC, NO reset. Counters only rise; each threshold test flips lt->ge
# at most once. Decider works on the CAPPED-depth quotient.

def thresholds_per_counter(instr, ncount):
    caps = [0] * ncount
    for ins in instr.values():
        if ins[0] == "JGE":
            _, i, c, _, _ = ins
            caps[i] = max(caps[i], c)
    return caps


def run_forward_thr(instr, q0, counters, limit=200000):
    """Naive forward sim (may not terminate). Counters grow unboundedly;
    no full-config dedup possible."""
    q = q0
    c = list(counters)
    for step in range(limit):
        if q == "HALT":
            return "HALT", step
        ins = instr[q]
        if ins[0] == "INC":
            _, i, qp = ins
            c[i] += 1
            q = qp
        else:
            _, i, thr, qge, qlt = ins
            q = qge if c[i] >= thr else qlt
    return "LOOP?", limit


def decide_halting_thr(instr, q0, counters):
    """DECIDE HALT/LOOP on the finite capped-depth quotient. Cap each
    counter at its largest tested threshold; capped depth rises
    monotonically to the cap then freezes; every threshold test reads it
    exactly (all thresholds <= cap). Node = (control, capped counters); a
    revisited node with no capped rise since = certified infinite loop."""
    ncount = len(counters)
    caps = thresholds_per_counter(instr, ncount)
    q = q0
    c = [min(counters[i], caps[i]) for i in range(ncount)]
    seen = set()
    while True:
        if q == "HALT":
            return "HALT"
        node = (q, tuple(c))
        if node in seen:
            return "LOOP"
        seen.add(node)
        ins = instr[q]
        if ins[0] == "INC":
            _, i, qp = ins
            if c[i] < caps[i]:
                c[i] += 1        # count toward the cap (a real transition)
                seen.clear()     # capped state rose: fresh regime
            q = qp
        else:
            _, i, thr, qge, qlt = ins
            q = qge if c[i] >= thr else qlt


# --- battery of monotone-threshold programs (verdicts FROZEN here) ---
P_A = {0: ("INC", 0, 0)}                                   # never halts
P_B = {0: ("JGE", 0, 3, "HALT", 1), 1: ("INC", 0, 0)}      # counts to 3
P_C = {0: ("JGE", 1, 2, "HALT", 1), 1: ("INC", 0, 0)}      # thr never met
P_D = {0: ("JGE", 0, 5, "HALT", 1),                        # two thresholds
       1: ("JGE", 0, 2, 2, 2),
       2: ("INC", 0, 0)}
P_E = {0: ("JGE", 0, 2, "HALT", 1), 1: ("INC", 0, 0)}      # already past

battery = [
    ("P_A c=(0)",   P_A, 0, (0,)),
    ("P_B c=(0)",   P_B, 0, (0,)),
    ("P_C c=(0,0)", P_C, 0, (0, 0)),
    ("P_D c=(0)",   P_D, 0, (0,)),
    ("P_E c=(4)",   P_E, 0, (4,)),
]
expect = {"P_A c=(0)": "LOOP", "P_B c=(0)": "HALT", "P_C c=(0,0)": "LOOP",
          "P_D c=(0)": "HALT", "P_E c=(4)": "HALT"}
n_nonterm = 0
for name, instr, q0, counters in battery:
    verdict = decide_halting_thr(instr, q0, counters)
    fwd, steps = run_forward_thr(instr, q0, counters, limit=5000)
    ok(verdict == expect[name], "decider verdict %s for %s" % (verdict, name))
    if fwd == "HALT":
        ok(verdict == "HALT", "decider matches terminating sim %s" % name)
    if verdict == "LOOP":
        ok(fwd == "LOOP?", "decider LOOP where naive sim never ends: %s" % name)
        n_nonterm += 1
    print("  %-14s decider=%-4s  naive-sim=%s" % (name, verdict, fwd))
ok(n_nonterm >= 1, "at least one non-terminating program decided")
print("  threshold-test halting DECIDED on the capped-depth quotient")
print("  (%d of %d programs have no terminating forward simulation)"
      % (n_nonterm, len(battery)))
print()


# ------------------------------------------------------------------ #
# S2 -- THE DOWN-FLIP IS THE BORROW (finding 2)
# ------------------------------------------------------------------ #
print("S2 -- THE DOWN-FLIP IS THE BORROW (zero-test flip census)")

# Count zero-test outcome transitions nonzero->zero (down-flips) and
# zero->nonzero (up-flips) along a run. Multiply-only worlds cannot
# down-flip; a borrow (decrement) can.

def flip_census_multiply_only(instr, q0, counters, limit=20000):
    """Run a threshold machine; census flips of every (JGE i c) test
    outcome. Multiply-only: outcomes only go lt->ge (up), never back."""
    q = q0
    c = list(counters)
    last = {}                       # (i,c) -> last outcome bool
    up, down = 0, 0
    for _ in range(limit):
        if q == "HALT":
            break
        ins = instr[q]
        if ins[0] == "INC":
            _, i, qp = ins
            c[i] += 1
            q = qp
        else:
            _, i, thr, qge, qlt = ins
            out = c[i] >= thr
            key = (i, thr)
            if key in last and last[key] != out:
                if out:
                    up += 1
                else:
                    down += 1
            last[key] = out
            q = qge if out else qlt
    return up, down


# multiply-only battery: a program that INCs and repeatedly tests the same
# threshold (so the test is evaluated many times) -- count its down-flips.
MO_1 = {0: ("JGE", 0, 4, "HALT", 1), 1: ("INC", 0, 0)}     # tests thr 4 each loop
MO_2 = {0: ("JGE", 0, 1, 1, 2),                            # presence-test style
        1: ("JGE", 0, 3, "HALT", 2),
        2: ("INC", 0, 0)}
total_down_mo = 0
for name, instr, c0 in [("MO_1", MO_1, (0,)), ("MO_2", MO_2, (0,))]:
    up, down = flip_census_multiply_only(instr, 0, c0)
    ok(down == 0, "multiply-only: no down-flips in %s" % name)
    total_down_mo += down
    print("  %-6s up-flips=%d  down-flips=%d" % (name, up, down))
ok(total_down_mo == 0, "multiply-only battery: ZERO down-flips (monotone)")


# a Minsky machine WITH a decrement: census down-flips of its zero-test.
def flip_census_minsky(instr, q0, counters, limit=20000):
    q = q0
    c = list(counters)
    last = {}
    up, down = 0, 0
    for _ in range(limit):
        if q == "HALT":
            break
        ins = instr[q]
        if ins[0] == "INC":
            _, i, qp = ins; c[i] += 1; q = qp
        elif ins[0] == "DEC":
            _, i, qp = ins
            if c[i] > 0:
                c[i] -= 1
            q = qp
        else:  # JZ
            _, i, qz, qn = ins
            out = (c[i] == 0)       # zero-test outcome (True == "is zero")
            if i in last and last[i] != out:
                # down-flip of the PRESENCE bit = counter RETURNS to zero
                if out:
                    down += 1      # became zero again = a return = a borrow
                else:
                    up += 1
            last[i] = out
            q = qz if out else qn
    return up, down


# a machine that grows c0 then decrements it back to zero, testing en route
# -> the zero-test returns to True (down-flip of presence).
OSC = {0: ("INC", 0, 1),
       1: ("INC", 0, 2),
       2: ("JZ", 0, "HALT", 3),    # is c0 zero? (no) -> q3
       3: ("DEC", 0, 4),
       4: ("JZ", 0, "HALT", 2)}    # is c0 zero? -> back to q2 until zero
up_m, down_m = flip_census_minsky(OSC, 0, (0,))
ok(down_m >= 1, "Minsky (decrement) shows >= 1 down-flip: the borrow's return")
print("  OSC    up-flips=%d  down-flips=%d  (decrement returns c0 to zero)"
      % (up_m, down_m))
print("  the down-flip = a counter returning to a tested threshold = a")
print("  BORROW; multiply-only cannot produce one -> its flips are bounded")
print()


# ------------------------------------------------------------------ #
# S3 -- UNIVERSALITY NEEDS BOTH INGREDIENTS (finding 3)
# ------------------------------------------------------------------ #
print("S3 -- UNIVERSALITY NEEDS BOTH (zero-test AND borrow)")

def run_minsky(instr, q0, counters, limit=200000):
    q = q0
    c = list(counters)
    for step in range(limit):
        if q == "HALT":
            return "HALT", step
        ins = instr[q]
        if ins[0] == "INC":
            _, i, qp = ins; c[i] += 1; q = qp
        elif ins[0] == "DEC":
            _, i, qp = ins
            if c[i] > 0:
                c[i] -= 1
            q = qp
        else:  # JZ
            _, i, qz, qn = ins
            q = qz if c[i] == 0 else qn
    return "LOOP?", limit


# (a) zero-test, NO borrow: covered by S1 (the growth machine floor is
# decidable) + S2 (zero down-flips). Re-assert the link here.
ok(total_down_mo == 0, "(a) zero-test without borrow: monotone, S1 decides it")

# HALTS iff counter 0 is EVEN, else loops (explore_growth_machine.py's witness).
EVENODD = {0: ("JZ", 0, "HALT", 1),
           1: ("DEC", 0, 2),
           2: ("JZ", 0, "odd", 3),
           3: ("DEC", 0, 0),
           "odd": ("INC", 0, "odd")}

# (b) borrow, NO zero-BRANCH: neutralize every JZ (both arms -> the nonzero
# arm), keeping the DECs. The decrement still fires but magnitude is never
# READ, so c0=2 and c0=3 must share a fate.
def neutralize_jz(instr):
    out = {}
    for q, ins in instr.items():
        if ins[0] == "JZ":
            _, i, qz, qn = ins
            out[q] = ("JZ", i, qn, qn)     # both branches -> nonzero arm
        else:
            out[q] = ins
    return out


NEUTRAL = neutralize_jz(EVENODD)
nb_even, _ = run_minsky(NEUTRAL, 0, (2,))
nb_odd, _ = run_minsky(NEUTRAL, 0, (3,))
ok(nb_even == nb_odd, "(b) borrow without a live zero-branch: c0=2,3 SAME fate")
# and the DECs are genuinely still present (borrow intact):
ok(any(ins[0] == "DEC" for ins in NEUTRAL.values()), "(b) decrement still present")
print("  (b) neutralized zero-branch: c0=2 -> %s, c0=3 -> %s  (SAME)"
      % (nb_even, nb_odd))

# (c) BOTH: the live machine reads magnitude via the zero-branch AND acts
# via the decrement -> opposite fates from a shared quotient node.
r_even, _ = run_minsky(EVENODD, 0, (2,))
r_odd, _ = run_minsky(EVENODD, 0, (3,))
ok(r_even == "HALT", "(c) even-counter halts")
ok(r_odd == "LOOP?", "(c) odd-counter loops")


def quotient_node(q, counters):
    return (q, tuple(c == 0 for c in counters))


ok(quotient_node(0, (2,)) == quotient_node(0, (3,)),
   "(c) c0=2 and c0=3 share the (control, zero-pattern) node")
ok(r_even != r_odd, "(c) yet fates differ -- S1 quotient decider UNSOUND")
print("  (c) live machine: c0=2 -> %s, c0=3 -> %s  (DIFFER, shared node)"
      % (r_even, r_odd))
print("  neither the zero-test alone (a) nor the borrow alone (b) is")
print("  universal; their conjunction (c) is -- the knife edge")
print()


# ------------------------------------------------------------------ #
# S4 -- THE DIAL (finding 4): borrow-kind + zero-test -> decidability tier
# ------------------------------------------------------------------ #
print("S4 -- THE DIAL (cited tiers; the tower keeps only the top row)")

# rows: (label, has_zero_branch, borrow_kind, {reach,term,halt}, substrate)
DIAL = [
    ("tower/growth", True,  "none",
     dict(reach="DEC", term="DEC", halt="DEC"), "WSTS"),
    ("VAS",          False, "dec",
     dict(reach="DEC", term="DEC", halt="DEC"), "Leroux'19"),
    ("reset net",    False, "reset",
     dict(reach="UND", term="DEC", halt="DEC"), "DFS'98"),
    ("Minsky",       True,  "dec",
     dict(reach="UND", term="UND", halt="UND"), "Minsky'67"),
]

# the tower's native capabilities: zero-test YES, borrow NONE -> the top row.
tower_row = DIAL[0]
ok(tower_row[1] is True and tower_row[2] == "none",
   "the tower has the zero-test natively and no borrow")
ok(all(v == "DEC" for v in tower_row[3].values()),
   "the tower row is fully decidable")

# a borrow with NO zero-branch is graded (VAS all DEC < reset loses reach):
vas, reset = DIAL[1], DIAL[2]
ok(vas[2] == "dec" and reset[2] == "reset", "two borrows without zero-branch")
ok(vas[3]["reach"] == "DEC" and reset[3]["reach"] == "UND",
   "the forgetful borrow (reset) already loses reachability; the plain "
   "decrement does not")
ok(vas[3]["term"] == "DEC" and reset[3]["term"] == "DEC",
   "both keep termination without a zero-branch")

# universality (all UND) requires BOTH a zero-branch and a borrow:
for label, zb, bk, tiers, src in DIAL:
    all_und = all(v == "UND" for v in tiers.values())
    ok(all_und == (zb and bk != "none"),
       "%s: fully undecidable iff zero-branch AND borrow" % label)
print("  row            zero? borrow   reach term halt   src")
for label, zb, bk, tiers, src in DIAL:
    print("   %-13s %-5s %-7s %-5s %-4s %-4s   %s"
          % (label, "yes" if zb else "no", bk,
             tiers["reach"], tiers["term"], tiers["halt"], src))
print("  the borrow is the dangerous import; a decrement + the tower's")
print("  native zero-test is exactly Minsky-universal. the tower deletes the")
print("  borrow = the archimedean place, and keeps only the top row.")
print()


# ------------------------------------------------------------------ #
# S5 -- CARRY-FREEDOM = INTER-WINDOW COUPLING (finding 5)
# ------------------------------------------------------------------ #
print("S5 -- CARRY-FREEDOM = INTER-WINDOW COUPLING")

PK = [2, 3, 5, 7, 11]
Npk = 1
for p in PK:
    Npk *= p


def crt_channels(x):
    return tuple(x % p for p in PK)


cross = [(17, 25), (100, 205), (1234, 999), (2309, 2), (7, 2303)]
for a, b in cross:
    s = (a + b) % Npk
    ca, cb, cs = crt_channels(a), crt_channels(b), crt_channels(s)
    for j, p in enumerate(PK):
        ok(cs[j] == (ca[j] + cb[j]) % p,
           "CRT add channel %d independent (no inter-window carry)" % p)
print("  CRT add over Z/%d: every channel (a+b) mod p = (a%%p + b%%p) mod p" % Npk)
print("  -- addition never couples distinct windows: carry-free (native)")

BASE = 10


def to_digits(n, width):
    d = []
    for _ in range(width):
        d.append(n % BASE)
        n //= BASE
    return d


def add_with_carries(x, y, width):
    dx, dy = to_digits(x, width), to_digits(y, width)
    carry = 0
    n_carry = 0
    for j in range(width):
        s = dx[j] + dy[j] + carry
        carry = s // BASE
        if carry:
            n_carry += 1
    return n_carry


pos_pairs = [(17, 25), (99, 1), (555, 555), (12, 34), (888, 222)]
total_carries = 0
for a, b in pos_pairs:
    total_carries += add_with_carries(a, b, 4)
ok(total_carries >= 1, "positional base-b add propagates >= 1 inter-window carry")
print("  positional base-%d add over %d pairs: %d inter-window carries"
      % (BASE, len(pos_pairs), total_carries))
print("  -- positional notation COUPLES windows; the carry (borrow) is the")
print("  archimedean coupling. the zero-test is intra-window (a residue) --")
print("  which is why the tower keeps it for free and deletes only the carry")
print()


print("ALL CHECKS PASS: %d" % CHECKS)
