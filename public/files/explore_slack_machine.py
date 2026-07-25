"""
explore_slack_machine.py -- CAN THE SLACK BE PROGRAMMED? (sibling of
explore_growth_machine.py, explore_genome_fibre.py,
explore_archimedean_dial.py).

THE QUESTION. The growth world's filed obstruction to universality is
that NOTHING DECREMENTS: every move multiplies the state N, so every
window depth rises and a counter machine built from depths has INC and
a zero-test but no DEC, which is decidable. But the SLACK

    delta_l = v_l(odd lambda(N)) - v_l(N) + 1

FALLS. It is a countdown of free pushes of l before l starts writing
into the genome odd(lambda(N)), and the countdown is spent one step per
push. A quantity that decrements inside a world whose whole obstruction
is that nothing decrements cannot leave both claims standing. So: is
delta a PROGRAMMABLE counter -- can a two-counter machine be built out
of it using nothing but growth pushes -- and if it can, what is left of
the non-universality verdict?

THE MODEL (unchanged from the growth machine). A state is a positive
integer N; every move multiplies it. Write c_l = v_l(N) and
d_l = v_l(odd lambda(N)) for an odd prime l. The genome formula

    d_l = max(0, c_l - 1, max{ v_l(q-1) : q | N, q != l })

makes d_l a MAX over what the present primes' predecessors carry, run
against l's own depth.

THE DESIGN, in seven sections. S1-S6 are the slate as frozen before
any engine code; S7 was added AFTER the run, to answer an objection the
run itself raised. Where the run contradicted the frozen framing the
framing is left standing and flagged, not quietly rewritten -- a slate
that is edited to match its results records nothing.

S1 POSITIVE CONTROL. Before any verdict is read, the engine's own
   Carmichael lambda must reproduce two things it did not compute here:
   the filed slack-law datum (states 1 and 3 share the genome 1, yet a
   push of 3^2 sends them to genomes 3 and 9), and the hand-derived
   five-move word of S4 below, checked move by move against figures
   fixed on paper before this file existed.

S2 THE LOSSY LAW. The slack law gives Delta d_l = max(0, e - delta_l)
   on a push of l^e. Substituting into the definition predicts

       delta_l' = max(0, delta_l - e)

   -- TRUNCATED SUBTRACTION, the primitive lossy counter machines are
   built from. Re-derived here from the engine's lambda rather than
   from the algebra, exhaustively over a battery of states, counter
   primes and exponents. PREDICTION P1: no exceptions.

S3 THE INSTRUCTION SET. Two instructions have to be built out of
   pushes, and the hard requirement on both is NO CROSS-TALK: an
   operation on counter l must leave every other counter's slack
   exactly where it was.
     INC: d_l is a max, so importing a fresh prime q with
       v_l(q-1) = j > d_l SETS d_l to j. The import also credits d_r at
       every r dividing odd(q-1) -- spurious raises of the other
       counters, fatal to the simulation. They vanish exactly when
       odd(q-1) is a pure power of l, i.e. when q = l^j * 2^a + 1 is a
       PROTH PRIME. So the clean increment exists at level j iff some a
       makes l^j * 2^a + 1 prime.
     DEC: a push of l when l is already present. A repeat push enters
       no new predecessor, so it credits nothing anywhere.
   The section searches for the Proth witnesses at both counter primes
   over a range of levels and checks the cross-talk requirement
   directly. PREDICTION P2: witnesses exist at every level in range,
   with odd(q-1) exactly l^j.

S4 THE SIMULATION. The two instructions above are Minsky's, and the
   DEC is already FUSED with its test: pushing l when delta_l > 0
   lowers it by one and leaves the genome alone (a transparent push),
   while pushing l when delta_l = 0 leaves it at zero and RAISES d_l --
   the genome MOVES. One move, test and decrement, and the two cases
   leave different genomes.
   The program frozen here is the growth machine's own witness against
   itself: the HALTS-IFF-EVEN machine that the filed threshold argument
   uses to show the decidable quotient goes unsound once a decrement
   exists. Two labels, one counter:
       L0: DEC(x): if x > 0 { x--; goto L1 } else HALT
       L1: DEC(x): if x > 0 { x--; goto L0 } else LOOP
   Even starts halt, odd starts loop. It is simulated twice over: once
   by a reference interpreter on plain integers, and once on the growth
   world by pushes alone, with the branch at every step taken from
   whether the engine's genome moved. PREDICTIONS P3/P4: the two runs
   agree step for step; the idle counter is never perturbed; and the
   parity separation appears at states differing only in magnitude.
   (Two further programs were added after the run: this one decrements
   ONE counter and never increments, so on its own it exercises a
   fraction of the instruction set it is used to justify. Transfer and
   roundtrip cover both instructions on both counters.)

S5 THE DOWN-FLIP COUNT. The decidability of the depth machine rests on
   a FINITE QUOTIENT: depths only rise, so each depth's zero-test flips
   once, the zero-pattern changes at most k times, and the run is
   decided on control x zero-pattern. The section counts how many times
   the delta zero-test flips along the S4 runs, against how many times
   the depth zero-pattern flips on the same runs. PREDICTION P5: the
   depth count saturates at the number of windows while the delta count
   grows with the program, so the quotient that decides the depth
   machine does not decide this one.

S6 THE READ. Everything above is the machine's ARITHMETIC. Whether the
   machine can USE it is a separate question, and it is the one that
   decides the verdict: a fused test-and-decrement is only an
   instruction if the control can see which branch it took. The filed
   probe repertoire is the three demand laws' admissibility predicates
   -- independence (gcd), new-idempotents, semisimplicity (coprime and
   squarefree). [THE FRAMING IS WRONG HERE, and finding 6 is where it
   is corrected: those three are not the whole repertoire. A FOURTH
   demand law -- the dynamics law, whose admissible moves are the ones
   that RAISE lambda -- reads the guard exactly. The error was
   enumerating a repertoire from the section being read rather than
   from the object, and it inverted this section's conclusion.]
   The section asks whether ANY of them can separate the
   two branches, by searching for pairs of states with IDENTICAL prime
   support and identical squarefreeness but DIFFERENT slack at a
   counter prime. Any such pair is a certificate that no probe built
   from the filed repertoire evaluates a slack guard, since all three
   predicates are functions of support and squarefreeness alone.
   PREDICTION P7: such pairs exist, densely.

WHAT WOULD KILL WHAT (observables, not inferences). P1 dies if the rig
prints one triple with delta' != max(0, delta - e). P2 dies if it
prints a level with no witness in range. P3/P4 die if it prints a step
where the growth-world counter differs from the reference counter, or
an instruction that moves the idle counter's slack. P5 dies if the
printed delta flip count saturates. P7 dies if the pair search returns
empty. What a surviving P4 MEANS -- whether "universal" is then the
right word for the growth world -- is weighed after the run and is not
frozen here.

FINDINGS.

1. THE LOSSY LAW (theorem, a corollary of the slack law; verified over
   750 (state, counter, exponent) triples with 0 exceptions, and the
   genome formula re-derived alongside it with 0 violations). A push of
   l^e sends

       delta_l  ->  max(0, delta_l - e),

   TRUNCATED SUBTRACTION. Substituting the slack law's
   Delta d_l = max(0, e - delta_l) into the definition gives it in one
   line. The name matters more than the derivation: truncated
   subtraction is the primitive lossy counter machines are built from,
   so "the growth world has no decrement" is false of the slack in the
   strongest sense available -- not merely a quantity that happens to
   fall, but the exact decrement primitive.

2. THE INSTRUCTION SET, AND IT IS UNCONDITIONAL (rule; verified).
   DEC is a bare push of the counter prime once that prime is seated: a
   repeat push enters no new predecessor into the lcm, so it perturbs
   nothing anywhere. INC is an import of a fresh prime q with
   v_l(q-1) exactly j = d_l + 1, chosen also to miss every sibling
   counter (q not congruent to 1 mod any of them). All the conditions
   are coprime congruences, so Dirichlet supplies infinitely many q and the
   instruction set carries NO open-problem dependency. The stronger
   variant that disturbs no odd prime at all needs odd(q-1) to be a
   pure power of l -- a Proth prime l^j * 2^a + 1 -- and THAT is
   Sigma_1-gated, a Sierpinski base having no witness at all. Witnesses
   found at every level j = 1..12: least a = 1,1,2,1,1,1,3,3,1,3,6,4
   for l = 3 and 1,2,1,8,17,2,31,20,5,8,23,20 for l = 5, with zero
   perturbation of the idle counter across the range. So the
   number-theoretic gate is real but optional: a machine on k counters
   needs only the k-1 sibling sides kept clean, which is a finite set of
   coprime congruences and therefore free.

3. THE FUSED TEST, AND ITS EXACT SCOPE (theorem; verified 47 pairs, 0
   disagreements). For an odd prime l ALREADY PRESENT in N,

       lambda(N*l) != lambda(N)   <=>   delta_l = 0.

   Proof: the push moves l's own prime-power contribution to the lcm
   from l^(c-1)(l-1) to l^c(l-1), leaving the (l-1) factor untouched,
   so the lcm can only move at l itself; and v_l(lambda) = d_l for odd
   l, which rises exactly when the slack is spent. The scope is not
   decoration. If l is ABSENT the push enters odd(l-1) into the lcm for
   the first time and lambda can rise for a completely different reason
   (53 such pairs tested, 35 of them raising lambda with slack to
   spare). A machine that seats its counter primes before it starts
   issues only repeat pushes, so it lives inside the scope.

4. THE SIMULATION (rule; verified at probe scale, three programs). A
   Minsky machine runs on the growth world using pushes and nothing
   else, at any number of counters. A counter is the SLACK at a seated
   odd prime; the branch at every step is taken from whether the genome
   moved. Three programs, each run step for step against a reference
   interpreter on plain integers.
     HALTS-IFF-EVEN -- the same witness the decrement-threshold
       argument uses to show a decidable quotient goes unsound -- runs
       for inputs 0..8 and reproduces the separation ON THE GROWTH
       WORLD: input 2 halts, input 3 diverges, from states differing
       only in magnitude. It decrements one counter and never
       increments, so on its own it exercises a fraction of the
       instruction set it is used to justify.
     TRANSFER empties one counter into the other, landing (0, n)
       exactly for n = 0..6. It adds the increment, but only ever
       increments the second counter.
     ROUNDTRIP moves x into y and y back into x, returning x to its
       starting value for 0..5. It is the one that closes the
       instruction set: both instructions run on BOTH counter primes,
       so the decrement on the second counter is measured rather than
       assumed by symmetry.
   All three also run unchanged on the Dirichlet imports of finding 2,
   with no Proth prime used anywhere.

   The construction is NOT limited to two counters, and that matters
   for what "universal" is allowed to mean. Two-counter universality
   carries a well-known encoding caveat; more counters remove it, and
   more counters are free here, because the conditions on an imported
   prime are congruences to coprime moduli and missing any finite set
   of sibling counters stays satisfiable. Verified at 2, 3, 4 and 5
   counters -- 70 increments in total, not one of them perturbing a
   sibling's slack. One honest wrinkle: beyond two counters the primes
   no longer all SEAT at zero (7 - 1 = 6 carries a factor 3, so counter
   3 starts at slack 1 once 7 joins). That is a startup detail, not an
   obstruction -- the seating offsets are fixed finite numbers set by
   the chosen primes, so a bounded prefix of decrements zeroes every
   counter before the program proper begins.

5. THE DOWN-FLIP EXISTS AFTER ALL (rule; verified). Decidability of the
   depth machine rests on a finite quotient: depths only rise, so a
   k-counter machine's zero-pattern flips at most k times and the run
   is decided on control x zero-pattern. Measured over the SAME two
   counter primes: the depth zero-tests flip 0 times (bound 2, both
   primes seated from the start and never leaving), while the slack
   zero-test flips twice per cycle -- 24 flips over 12 cycles and
   still climbing, linear in program length. A program that STAGES its
   instructions, every increment before any decrement, flips once at
   every length; that is a fact about staging, and reading it as a fact
   about the slack is the mistake this section was rebuilt to avoid.
   The verifiable fingerprint that "multiply-only worlds cannot
   down-flip" is a statement about DEPTHS wearing the clothes of a
   statement about worlds.

6. THE VERDICT IS DEMAND-LAW-RELATIVE (rule; the headline). Everything
   above is the machine's arithmetic; whether the machine can USE it
   turns on one bit per push -- can the control see which branch it
   took? Against the support-blind demand chain (independence,
   new-idempotents, semisimplicity) the answer is NO, and provably so:
   all three admissibility predicates are functions of prime support
   and squarefreeness alone, so any two states agreeing on those are
   indistinguishable to every probe. 14 such pairs disagree on the
   slack guard, N = 855 and N = 2565 among them -- same support, both
   non-squarefree, slacks 1 and 0. But that chain is not the whole
   repertoire. The DYNAMICS demand law takes its admissible moves to be
   exactly the ones that RAISE lambda, and by finding 3 its
   admissibility probe answers the slack guard exactly, before the push
   rather than after.

   One objection has to be answered here, because it looks fatal and is
   not. Under that law a TRANSPARENT push is by definition INADMISSIBLE
   -- it does not raise lambda -- and the transparent push is exactly
   the decrement. If the demand law also chose the moves, the machine
   could not issue its own DEC. It does not choose them: the observer's
   gifts are separate, and this machine uses two. The HAND injects moves
   irrespective of admissibility, which is what a hand is for; the PROBE
   asks whether an offered move is admissible and gets one bit back. So
   the law never gates the move here, only reads it, and the machine is
   a hand-driven push schedule with the law's probe wired to its branch.
   A machine RESTRICTED to admissible moves is a different machine, and
   would indeed have no decrement.

   So the growth machine is sub-universal under the
   support-blind laws and UNIVERSAL under the dynamics law (given
   Minsky's theorem, cited), and the obstruction was never "there is no
   decrement": it is that the reading of the decrement is not in every
   probe repertoire. One demand law supplies it.

   (SETTLED FURTHER by explore_demand_reading.py, and two sentences
   above are narrower than the truth. A machine RESTRICTED to admissible
   moves is NOT left without a decrement: a move may be any m, so
   padding the push as l*q with a junk prime -- fresh, missing every
   counter prime, and with q-1 not dividing lambda -- decrements the
   slack exactly while raising lambda in BOTH branches. The machine is
   therefore law-autonomous under the dynamics law rather than dependent
   on a hand. And universality is not the dynamics law's alone: once a
   hand supplies the moves it belongs to EVERY sighted law, transparency
   included, which hosts no increment at all yet drives these same three
   programs step for step. What survives here verbatim is the
   blind/sighted classification, the one-bit price, and the instrument.)

   Blind and sighted are decided by ONE instrument on ONE test object,
   so the classification is a property of the predicate rather than of
   how each case was argued: over the pair 855 / 2565, independence,
   new-idempotents and semisimplicity each score 0 disagreements across
   398 offered moves, while the dynamics predicate scores 17. Ordering
   a further demand law by reading power is a matter of handing
   blind_score another predicate.

   Where this lands against the read-import law: the slack is
   d_l - c_l + 1, a valuation of lambda compared against a valuation of
   N -- depth compared across windows, which is the second door
   already charted (explore_archimedean_dial.py, the predicate dial).
   The law that every depth-face universality purchase is a read import
   therefore SURVIVES, and gains its sharpest instance: the price is
   one bit per push, and one demand law pays it as a side effect of
   what it means by admissible.

SCOPE AND CAVEATS. The simulation is verified at probe scale on three
programs; universality is then Minsky's theorem applied to a verified
instruction set, not an exhaustive claim over all programs. Imports
beyond about 3.3e24 are strong probable primes -- the deterministic
Miller-Rabin base set does not certify above that -- and the
interleaved run's largest import is 6.15e35. The monotonicity
observable is present but minor: a slack guard is enabled at N = 1 and
disabled at its multiple N = 3, so a slack-guarded transition is not
monotone in the divisibility order. That breaks a well-structured
reading, but the well-structured reading was never the load-bearing
argument -- the finite quotient was, and finding 5 is what actually
threatens it.

RUN RECORD. Python 3, no third-party dependencies, 0.05 s wall clock,
negligible memory. The speed is the design, not luck: the state is a
dict of prime to exponent and never a factored integer, so reading the
genome off the depth vector keeps a product of 24 large imports
tractable where trial division would not finish, and the only heavy
arithmetic left is Miller-Rabin on numbers of at most a few hundred
bits. Seven sections, all checks pass. The positive control runs first
and the run aborts before any verdict is read if it fails.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
from math import gcd, lcm

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("  FAIL: " + msg)
    return cond


# ---------------------------------------------------------------- arithmetic

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


def lam(n):
    """Carmichael lambda of a positive integer."""
    L = 1
    for q, a in factorint(n).items():
        L = lcm(L, lam_pp(q, a))
    return L


def oddpart(n):
    while n % 2 == 0:
        n //= 2
    return n


def v_p(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def genome(n):
    """The genome: the odd part of the Carmichael lambda."""
    return oddpart(lam(n))


def c_of(N, l):
    return v_p(N, l)


def d_of(N, l):
    return v_p(genome(N), l)


def delta(N, l):
    """The slack at l: free pushes of l left before l writes to the genome."""
    return d_of(N, l) - c_of(N, l) + 1


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


# ---------------------------------------------------- S1  positive control

def s1_positive_control():
    print("S1  POSITIVE CONTROL -- the engine reproduces figures fixed on paper")
    # The filed slack-law datum: same genome, different slack, different answer.
    ok = True
    ok &= check(genome(1) == 1 and genome(3) == 1, "S1 states 1 and 3 share genome 1")
    ok &= check(delta(1, 3) == 1, "S1 delta_3(1) == 1")
    ok &= check(delta(3, 3) == 0, "S1 delta_3(3) == 0")
    ok &= check(genome(1 * 9) == 3, "S1 push 3^2 on state 1 gives genome 3")
    ok &= check(genome(3 * 9) == 9, "S1 push 3^2 on state 3 gives genome 9")
    print("    same genome, slacks 1 and 0, push 3^2 -> genomes %d and %d"
          % (genome(9), genome(27)))

    # The hand-derived word, move by move, against figures fixed before the file.
    # (state, x=delta_3, y=delta_5) after each move, from the paper derivation.
    word = [(15, 0, 0), (105, 1, 0), (1995, 2, 0),
            (5985, 1, 0), (17955, 0, 0), (53865, 0, 0)]
    for N, x, y in word:
        ok &= check(delta(N, 3) == x, "S1 hand word: delta_3(%d) == %d" % (N, x))
        ok &= check(delta(N, 5) == y, "S1 hand word: delta_5(%d) == %d" % (N, y))
    # the last move is the one at zero: it must MOVE the genome.
    ok &= check(v_p(genome(17955), 3) == 2 and v_p(genome(53865), 3) == 3,
                "S1 hand word: the push at slack zero raises the genome")
    print("    hand word 15 -> 105 -> 1995 -> 5985 -> 17955 -> 53865 reproduced")

    # The simulation sections read the genome off a depth vector rather than
    # off the integer, to avoid factoring a product of large Proth primes back
    # out. That second path has to agree with the first wherever both run.
    disagree = 0
    for N in (15, 105, 1995, 5985, 17955, 53865, 9, 27, 45, 315, 1155, 255255):
        vec = factorint(N)
        for l in (3, 5, 7, 11):
            if d_vec(vec, l) != d_of(N, l) or delta_vec(vec, l) != delta(N, l):
                disagree += 1
    ok &= check(disagree == 0,
                "S1 the depth-vector reading agrees with the integer reading")
    print("    vector and integer readings of the genome agree: %d disagreements"
          % disagree)
    print("    control %s\n" % ("PASSES" if ok else "FAILS"))
    return ok


# ------------------------------------------------------------ S2  lossy law

def s2_lossy_law():
    print("S2  THE LOSSY LAW -- delta' = max(0, delta - e) from the engine's lambda")
    primes = [3, 5, 7, 11, 13]
    # a battery of states with assorted supports and depths
    states = [1, 2, 3, 4, 5, 7, 9, 15, 21, 27, 35, 45, 63, 81, 105, 165,
              231, 315, 495, 693, 1155, 1995, 3465, 5985, 10395, 17955,
              45045, 53865, 135135, 255255]
    tested = 0
    worst = None
    for N in states:
        for l in primes:
            dl = delta(N, l)
            for e in range(1, 6):
                pred = max(0, dl - e)
                got = delta(N * l ** e, l)
                tested += 1
                if pred != got and worst is None:
                    worst = (N, l, e, dl, pred, got)
                check(pred == got,
                      "S2 delta'(%d, %d^%d): predicted %d, got %d"
                      % (N, l, e, pred, got))
                # and the slack law it was derived from, independently
                dd = d_of(N * l ** e, l) - d_of(N, l)
                check(dd == max(0, e - dl),
                      "S2 slack law at (%d, %d^%d): Delta d = %d, expected %d"
                      % (N, l, e, dd, max(0, e - dl)))
    print("    %d (state, counter, exponent) triples, %d exceptions"
          % (tested, 0 if worst is None else 1))
    # the genome formula itself, over the same battery
    bad = 0
    for N in states:
        for l in primes:
            other = max([v_p(q - 1, l) for q in factorint(N) if q != l] or [0])
            if d_of(N, l) != max(0, c_of(N, l) - 1, other):
                bad += 1
    check(bad == 0, "S2 genome formula holds over the battery")
    print("    genome formula d_l = max(0, c_l - 1, max_q v_l(q-1)): %d violations\n"
          % bad)
    return not FAIL


# ------------------------------------------------------ S3  instruction set

def proth_witness(l, j, amax=4000):
    """Least a with l^j * 2^a + 1 prime -- the clean increment at level j."""
    base = l ** j
    for a in range(1, amax + 1):
        q = base * (1 << a) + 1
        if is_prime(q):
            return a, q
    return None, None


def s3_instruction_set():
    print("S3  THE INSTRUCTION SET -- DEC is a bare push; the INC that disturbs"
          " NO odd prime wants a Proth prime")
    witnesses = {}
    ok = True
    for l in (3, 5):
        row = []
        for j in range(1, 13):
            a, q = proth_witness(l, j)
            ok &= check(a is not None, "S3 no Proth witness for %d^%d" % (l, j))
            if a is None:
                continue
            witnesses[(l, j)] = q
            ok &= check(oddpart(q - 1) == l ** j,
                        "S3 witness %d has odd(q-1) == %d^%d" % (q, l, j))
            row.append(a)
        print("    l=%2d  least a per level j=1..12: %s" % (l, row))
    print("    every witness has odd(q-1) a pure power of its counter prime: %s"
          % ("yes" if ok else "NO"))

    # cross-talk: an INC at one counter must not move the other counter's slack.
    N = 15
    moved = 0
    for j in range(1, 7):
        for l, other in ((3, 5), (5, 3)):
            q = witnesses.get((l, j))
            if q is None or N % q == 0:
                continue
            before = delta(N, other)
            after = delta(N * q, other)
            if before != after:
                moved += 1
    check(moved == 0, "S3 cross-talk: an INC moved the idle counter %d times" % moved)
    print("    cross-talk over the level range: %d perturbations of the idle counter\n"
          % moved)
    return ok and moved == 0


# -------------------------------------------------------- S4  the simulation

# Programs are Minsky programs over two counters. An instruction is either
#   ("DEC", counter, goto_if_positive, goto_if_zero)   -- the fused test
#   ("INC", counter, goto)
# PARITY is the witness the filed threshold argument uses: it decrements one
# counter twice per loop, so even starts halt and odd starts diverge.
PARITY = {"L0": ("DEC", "x", "L1", "HALT"),
          "L1": ("DEC", "x", "L0", "LOOP")}
# TRANSFER exercises BOTH counters and both instructions: it empties x into y.
TRANSFER = {"T0": ("DEC", "x", "T1", "HALT"),
            "T1": ("INC", "y", "T0")}
# ROUNDTRIP is the one that closes the instruction set: it moves x into y and
# then y back into x, so DEC and INC each run on BOTH counter primes. Without
# it the second counter is only ever incremented, and "the decrement works
# there too, by symmetry" would be an assumption rather than a measurement.
ROUNDTRIP = {"R0": ("DEC", "x", "R1", "R2"),
             "R1": ("INC", "y", "R0"),
             "R2": ("DEC", "y", "R3", "HALT"),
             "R3": ("INC", "x", "R2")}


def reference_run(x0, program=PARITY, budget=200):
    """The machine on plain integers -- the thing the growth world must match."""
    cnt = {"x": x0, "y": 0}
    pc, trace = sorted(program)[0], []
    for _ in range(budget):
        if pc in ("HALT", "LOOP"):
            return pc, trace
        ins = program[pc]
        if ins[0] == "DEC":
            _, c, nz, z = ins
            if cnt[c] > 0:
                cnt[c] -= 1
                pc = nz
            else:
                pc = z
        else:
            _, c, nxt = ins
            cnt[c] += 1
            pc = nxt
        trace.append((pc, cnt["x"], cnt["y"]))
    return "BUDGET", trace


def d_vec(state, l):
    """The genome exponent at l, read off a depth vector.

    The machine builds its state by pushing primes it names, so it holds the
    factorization already; reading the genome off the vector avoids factoring
    a product of large Proth primes back out again.
    """
    return max([0, state.get(l, 0) - 1] +
               [v_p(q - 1, l) for q in state if q != l])


def delta_vec(state, l):
    return d_vec(state, l) - state.get(l, 0) + 1


def push(state, q, e=1):
    s = dict(state)
    s[q] = s.get(q, 0) + e
    return s


def growth_inc(state, l, other, proth=True):
    """Raise the slack at l by one, without disturbing any sibling counter."""
    j = d_vec(state, l) + 1
    q = proth_witness(l, j)[1] if proth else dirichlet_witness(l, j, other)
    return push(state, q), q


def growth_run(x0, program=PARITY, budget=200, proth=True):
    """The same machine on the growth world: pushes only, branch from the genome.

    A counter is the SLACK at a seated odd prime. INC imports a fresh prime
    that raises the slack at one counter and misses its siblings; DEC is a
    bare push of the counter prime, and the branch is read off whether the
    genome moved. Nothing here leaves the growth world -- every move
    multiplies. This runner wires two counters because the programs below
    use two; the construction itself is not limited to two (see S7).
    """
    PR = {"x": 3, "y": 5}
    state = {3: 1, 5: 1}  # both counters seated at zero
    biggest = 0
    for _ in range(x0):   # build the input by clean increments
        state, q = growth_inc(state, PR["x"], PR["y"], proth)
        biggest = max(biggest, q)
    pc, trace, flips = sorted(program)[0], [], 0
    prev_zero = (delta_vec(state, PR["x"]) == 0)
    for _ in range(budget):
        if pc in ("HALT", "LOOP"):
            return pc, trace, flips, state, biggest
        ins = program[pc]
        if ins[0] == "DEC":
            _, c, nz, z = ins
            l = PR[c]
            before = d_vec(state, l)
            state = push(state, l)   # one move: a push of the counter prime
            pc = z if d_vec(state, l) != before else nz   # the genome branches
        else:
            _, c, nxt = ins
            state, q = growth_inc(state, PR[c], PR["y" if c == "x" else "x"], proth)
            biggest, pc = max(biggest, q), nxt
        trace.append((pc, delta_vec(state, PR["x"]), delta_vec(state, PR["y"])))
        now_zero = (delta_vec(state, PR["x"]) == 0)
        if now_zero != prev_zero:
            flips += 1
        prev_zero = now_zero
    return "BUDGET", trace, flips, state, biggest


def sawtooth_run(cycles, l=3, idle=5):
    """A program that INTERLEAVES the two instructions instead of staging them.

    Each cycle raises the counter twice and spends it to zero three times, so
    the slack's zero-test is driven back and forth once per cycle. Returns the
    zero-test flip count, the window count, and the largest prime imported.
    """
    state = {3: 1, 5: 1}
    flips, biggest, idle_moves, depth_flips = 0, 0, 0, 0
    prev_zero = (delta_vec(state, l) == 0)
    # the DEPTH zero-pattern, over the same two counter primes
    prev_depth = tuple(state.get(p, 0) == 0 for p in (l, idle))
    for _ in range(cycles):
        ops = ["INC", "INC", "DEC", "DEC", "DEC"]
        for op in ops:
            idle_before = delta_vec(state, idle)
            if op == "INC":
                j = d_vec(state, l) + 1
                _, q = proth_witness(l, j)
                state, biggest = push(state, q), max(biggest, q)
            else:
                state = push(state, l)
            if delta_vec(state, idle) != idle_before:
                idle_moves += 1
            now_zero = (delta_vec(state, l) == 0)
            if now_zero != prev_zero:
                flips += 1
            prev_zero = now_zero
            now_depth = tuple(state.get(p, 0) == 0 for p in (l, idle))
            if now_depth != prev_depth:
                depth_flips += 1
            prev_depth = now_depth
    return flips, depth_flips, len(state), biggest, idle_moves


def s4_simulation():
    print("S4  THE SIMULATION -- Minsky programs on pushes alone")
    ok = True
    for name, program, span in (("halts-iff-even", PARITY, range(0, 9)),
                                ("transfer x to y", TRANSFER, range(0, 7)),
                                ("roundtrip x->y->x", ROUNDTRIP, range(0, 6))):
        print("    program: %s" % name)
        for x0 in span:
            ref_fate, ref_trace = reference_run(x0, program)
            got_fate, got_trace, _, _, _ = growth_run(x0, program)
            ok &= check(ref_fate == got_fate,
                        "S4 %s x0=%d: reference %s, growth world %s"
                        % (name, x0, ref_fate, got_fate))
            ok &= check(ref_trace == got_trace,
                        "S4 %s x0=%d: traces agree step for step" % (name, x0))
            end = got_trace[-1] if got_trace else (None, 0, 0)
            print("      x0=%d  reference %-5s  growth world %-5s  %2d steps"
                  "  ending counters (%d, %d)"
                  % (x0, ref_fate, got_fate, len(got_trace), end[1], end[2]))
    # the separation the threshold argument turns on
    f2 = growth_run(2)[0]
    f3 = growth_run(3)[0]
    ok &= check(f2 == "HALT" and f3 == "LOOP",
                "S4 the parity separation: 2 -> HALT, 3 -> LOOP")
    print("    the filed witness reproduced on the growth world: 2 -> %s, 3 -> %s"
          % (f2, f3))
    print("    transfer moves a counter it can only read through the genome and")
    print("    lands the value in the other exactly; roundtrip brings it back,")
    print("    which is what puts both instructions on both counters.\n")
    return ok


# ------------------------------------------------------- S5  the down-flip

def s5_flip_count():
    print("S5  THE DOWN-FLIP COUNT -- what the finite quotient has to survive")
    ok = True
    # First, the S4 program. It STAGES its instructions -- every increment
    # happens before any decrement -- so its slack can only run down once.
    # A single-phase program cannot answer the flip question; recorded here
    # because it is what the prediction was frozen against.
    print("    staged program (the S4 machine: all increments, then decrements)")
    print("      x0   delta flips   windows opened")
    for x0 in (2, 6, 12):
        _, _, flips, state, _ = growth_run(x0)
        print("      %2d   %10d   %14d" % (x0, flips, len(state)))
    print("      one flip at every length: staging, not a property of the slack")

    # The flip question needs a program that INTERLEAVES the two instructions.
    # The comparison that matters is at a FIXED counter count: the decidability
    # argument bounds the flips of a k-counter machine by k, so both columns
    # below count zero-test flips over the SAME two counter primes.
    print("    interleaved program (two increments and three decrements per cycle)")
    print("      cycles   delta flips   depth flips (same 2 counters)   largest import")
    rows = []
    for cycles in (1, 2, 4, 8, 12):
        flips, depth_flips, _, biggest, idle_moves = sawtooth_run(cycles)
        rows.append((cycles, flips, depth_flips))
        ok &= check(idle_moves == 0,
                    "S5 the idle counter moved %d times at %d cycles"
                    % (idle_moves, cycles))
        ok &= check(depth_flips <= 2,
                    "S5 depth flips over 2 counters stayed within the bound 2")
        print("      %6d   %10d   %30d   %14d"
              % (cycles, flips, depth_flips, biggest))
    growing = all(rows[i][1] < rows[i + 1][1] for i in range(len(rows) - 1))
    ok &= check(growing, "S5 the delta flip count grows with the program")
    ok &= check(rows[-1][1] > 2, "S5 the delta zero-test flips more than twice")
    print("    two counters, so the decidability argument allows at most 2 depth")
    print("    flips EVER, and that bound holds. The same two counters' slack")
    print("    zero-test flips %d times and keeps going: it RETURNS to zero,"
          % rows[-1][1])
    print("    which is the down-flip a multiply-only world was said not to have.")
    print("    (Imports beyond ~3.3e24 are strong probable primes, not certified.)\n")
    return ok


# ------------------------------------------------------------- S6  the read

def sqfree(n):
    return all(a == 1 for a in factorint(n).values())


# The demand laws' admissibility predicates as (name, predicate) pairs, so the
# blindness test runs against ANY predicate rather than these four. A predicate
# takes (state, offered move) and returns whether the move is admissible;
# classifying a further demand law means appending one row here.
DEMAND_PROBES = [
    ("independence", lambda N, m: gcd(N, m) == 1),
    ("new-idempotents", lambda N, m: any(N % p != 0 for p in factorint(m))),
    ("semisimplicity",
     lambda N, m: gcd(N, m) == 1 and sqfree(m) and sqfree(N)),
    ("dynamics", lambda N, m: lam(N * m) != lam(N)),
]


def blind_score(pred, A, B, moves=range(2, 400)):
    """How often a predicate distinguishes two states -- 0 means blind to them.

    A pair (A, B) agreeing on prime support and squarefreeness but differing on
    the slack guard is a TEST OBJECT: a predicate scoring 0 on it cannot
    evaluate the guard, hence cannot drive a fused test-and-decrement, while a
    predicate scoring above 0 is a candidate reader. This is the instrument for
    ordering demand laws by reading power -- hand it a predicate.
    """
    return sum(1 for m in moves if pred(A, m) != pred(B, m))


def s6_the_read():
    print("S6  THE READ -- can the filed probe repertoire evaluate a slack guard?")
    # All three demand laws' admissibility predicates are functions of
    # (prime support, squarefreeness) alone:
    #   independence      gcd(N, m) == 1
    #   new idempotents   some prime of m absent from N
    #   semisimplicity    coprime, and both squarefree
    # So a pair of states agreeing on support and squarefreeness is
    # INDISTINGUISHABLE to every probe. Find such a pair disagreeing on slack.
    pairs = []
    pool = []
    for a in range(1, 7):
        for extra in (1, 7, 19, 7 * 19, 163):
            N = 3 ** a * 5 * extra
            pool.append(N)
    for i in range(len(pool)):
        for j in range(i + 1, len(pool)):
            A, B = pool[i], pool[j]
            if set(factorint(A)) != set(factorint(B)):
                continue
            if sqfree(A) != sqfree(B):
                continue
            if (delta(A, 3) == 0) != (delta(B, 3) == 0):
                pairs.append((A, B))
    ok = check(len(pairs) > 0, "S6 a probe-blind pair with different slack exists")
    print("    probe-blind pairs disagreeing on the slack guard at 3: %d" % len(pairs))
    if pairs:
        A, B = pairs[0]
        print("    e.g. N=%d and N=%d: same support %s, both non-squarefree,"
              % (A, B, sorted(factorint(A))))
        print("         slack at 3 is %d and %d -- the guard differs, and each"
              " law below\n         is classified by whether it can tell"
              " these two apart" % (delta(A, 3), delta(B, 3)))
        # every probe run through the SAME instrument, so the classification
        # is a property of the predicate and not of how it was tested
        blind = [(n, blind_score(pr, A, B)) for n, pr in DEMAND_PROBES
                 if n != "dynamics"]
        for n, score in blind:
            print("      %-16s %-7s (%d disagreements over 398 offered moves)"
                  % (n, "BLIND" if score == 0 else "SIGHTED", score))
        disagreements = sum(score for _, score in blind)
        # the fourth law, on the SAME test object -- the classification is one
        # measurement, not two arguments
        dyn = dict(DEMAND_PROBES)["dynamics"]
        dyn_score = blind_score(dyn, A, B)
        ok &= check(dyn_score > 0,
                    "S6 the dynamics probe separates the pair the others cannot")
        print("      %-16s %-7s (%d disagreements over 398 offered moves)"
              % ("dynamics", "SIGHTED" if dyn_score else "BLIND", dyn_score))
        ok &= check(disagreements == 0,
                    "S6 the three probes agree on the pair over every offered move")
        print("    the three support-blind laws together: %d disagreements --"
              " the guard is\n    invisible to all of them, and visible to the"
              " fourth" % disagreements)
    # the monotonicity observable, in passing
    A = 1
    B = 3
    guard_at_A = delta(A, 3) > 0
    guard_at_B = delta(B, 3) > 0
    ok &= check(A * 3 == B and guard_at_A and not guard_at_B,
                "S6 a slack guard is enabled at a state and disabled at a multiple")
    print("    monotonicity: N=%d divides N=%d, guard enabled %s, then %s"
          % (A, B, guard_at_A, guard_at_B))

    # ...but that chain is not the whole repertoire. A FOURTH demand law
    # takes its admissible moves to be the ones that RAISE the Carmichael
    # lambda. Its admissibility predicate is a lambda-move detector, and on
    # a counter prime a lambda-move detector IS the slack guard: pushing l
    # changes only l's own contribution to the lcm, and for odd l the
    # lambda-valuation at l is exactly d_l, which rises iff the slack is 0.
    # The equivalence has a SCOPE, and the scope is exactly the machine's.
    # If l is already present, its contribution to the lcm goes from
    # l^(c-1)(l-1) to l^c(l-1) -- the (l-1) factor is unchanged, so the lcm
    # can only move at l itself, and it moves iff the slack is zero. If l is
    # ABSENT, the push enters odd(l-1) into the lcm for the first time, and
    # lambda can rise for that entirely different reason. The machine seats
    # both counter primes before it starts, so every decrement it issues is a
    # repeat push and lands inside the scope.
    print("    the dynamics demand law (admissible = raises lambda):")
    repeat_n, repeat_bad, first_n, first_raise = 0, 0, 0, 0
    for N in [1, 2, 3, 5, 9, 15, 27, 45, 105, 225, 315, 855, 1995, 2565,
              5985, 17955, 45045, 53865, 135135, 255255]:
        for l in (3, 5, 7, 11, 13):
            raises = lam(N * l) != lam(N)
            if c_of(N, l) >= 1:
                repeat_n += 1
                if raises != (delta(N, l) == 0):
                    repeat_bad += 1
            else:
                first_n += 1
                if raises:
                    first_raise += 1
    ok &= check(repeat_bad == 0,
                "S6 on a repeat push, raising lambda is exactly slack zero")
    print("      repeat push (the counter is seated -- the machine's own case):")
    print("        'raises lambda' == 'slack is zero': %d pairs, %d disagreements"
          % (repeat_n, repeat_bad))
    print("      first push (out of scope: the push also enters odd(l-1)):")
    print("        %d pairs, %d of them raise lambda for that other reason"
          % (first_n, first_raise))
    print("      so on the moves the machine actually issues, this law's")
    print("      admissibility probe answers the guard exactly -- and answers it")
    print("      BEFORE the push rather than after.\n")
    return ok


# ------------------------------------------------ S7  the unconditional INC

def many_counter_probe(counters, levels=5):
    """How many counters does this construction support?

    Two-counter universality carries a well-known encoding caveat; the caveat
    disappears if the construction supplies as many counters as wanted. It
    does, and for the same reason the two-counter case works: the conditions
    on an imported prime are congruences to coprime moduli, so requiring it to
    miss ANY finite set of other counter primes stays satisfiable. Returns the
    number of (counter, level) increments checked and the number that
    perturbed some other counter's slack.
    """
    state = {p: 1 for p in counters}
    checked, perturbed = 0, 0
    for j in range(1, levels + 1):
        for l in counters:
            others = [p for p in counters if p != l]
            before = {p: delta_vec(state, p) for p in others}
            target = d_vec(state, l) + 1
            q = dirichlet_witness(l, target, others)
            if q is None:
                continue
            state = push(state, q)
            checked += 1
            if any(delta_vec(state, p) != before[p] for p in others):
                perturbed += 1
    return checked, perturbed, len(state)


def dirichlet_witness(l, j, other, tries=20000):
    """An increment needing no Proth prime.

    Wanted: a prime q with v_l(q-1) EXACTLY j, and q not congruent to 1 mod
    any sibling counter prime, so no other counter is touched. `other` takes
    a single prime or a list of them. Cross-talk lands on primes the machine
    does not use, which costs nothing. All the conditions are coprime
    congruences, so such primes are infinitely many at any number of
    counters.

    The search walks the progression q == 1 + l^j (mod l^(j+1)), which forces
    v_l(q-1) = j exactly. It is bounded by the number of CANDIDATES tried and
    not by their magnitude: the progression's terms grow like l^(j+1), so a
    magnitude cap silently starves the search at large j while looking like a
    generous bound.
    """
    others = [other] if isinstance(other, int) else list(other)
    base = l ** j
    step = base * l
    for k in range(tries):
        q = base + 1 + k * step
        if any((q - 1) % o == 0 for o in others):  # would credit that counter
            continue
        if is_prime(q) and v_p(q - 1, l) == j:
            return q
    return None


def s7_unconditional():
    print("S7  THE UNCONDITIONAL INCREMENT -- k counters need only k-1 clean sides")
    ok = True
    print("    l   j   Proth witness        Dirichlet witness   odd(q-1) pure?")
    for l, other in ((3, 5),):
        for j in range(1, 8):
            _, pq = proth_witness(l, j)
            dq = dirichlet_witness(l, j, other)
            ok &= check(dq is not None, "S7 no Dirichlet witness at %d^%d" % (l, j))
            if dq is None:
                continue
            ok &= check(v_p(dq - 1, l) == j and (dq - 1) % other != 0,
                        "S7 witness %d has exact level and misses the other counter"
                        % dq)
            pure = oddpart(dq - 1) == l ** j
            print("    %d  %2d   %18d   %17d   %s"
                  % (l, j, pq, dq, "yes" if pure else "no"))
    print("    the Proth route needs odd(q-1) to be a pure power -- zero cross-talk")
    print("    at EVERY odd prime, which is gated by open number theory (a")
    print("    Sierpinski base would have no witness at all). The Dirichlet route")
    print("    protects only the counters actually in use -- k-1 of them, a finite")
    print("    set of coprime conditions -- so its witnesses are unconditionally")
    print("    infinite however many counters there are. (The last column is")
    print("    a coincidence of small numbers -- the least Dirichlet witness")
    print("    happens to be pure this low down, but purity is never required and")
    print("    is not what the search enforces.)")

    # and all three programs run on it, with no Proth prime anywhere
    for name, program in (("halts-iff-even", PARITY), ("transfer", TRANSFER),
                          ("roundtrip", ROUNDTRIP)):
        fates = []
        for x0 in range(0, 7):
            fate, trace, _, _, _ = growth_run(x0, program, proth=False)
            ref_fate, ref_trace = reference_run(x0, program)
            fates.append(fate)
            ok &= check(fate == ref_fate and trace == ref_trace,
                        "S7 %s x0=%d matches the reference on Dirichlet imports"
                        % (name, x0))
        print("    %-15s on Dirichlet increments, x0=0..6: %s"
              % (name, " ".join(fates)))
    # how many counters the construction supports -- two-counter universality
    # carries an encoding caveat that more counters simply remove
    total_inc, total_bad = 0, 0
    for counters in ((3, 5), (3, 5, 7), (3, 5, 7, 11), (3, 5, 7, 11, 13)):
        checked, perturbed, _ = many_counter_probe(counters)
        total_inc, total_bad = total_inc + checked, total_bad + perturbed
        ok &= check(checked > 0 and perturbed == 0,
                    "S7 %d counters: %d increments, %d perturbed a sibling"
                    % (len(counters), checked, perturbed))
        print("    %d counters %-16s %2d increments, %d perturbed a sibling"
              % (len(counters), str(counters), checked, perturbed))
    print("    %d increments in total, %d perturbing a sibling"
          % (total_inc, total_bad))
    print("    so the construction is not limited to two counters: the conditions")
    print("    on an import are congruences to coprime moduli, and missing any")
    print("    finite set of siblings stays satisfiable.")
    print("    all three match the reference step for step with no Proth")
    print("    prime used anywhere: the instruction set carries no open-problem\n"
          "    dependency.\n")
    return ok


# ------------------------------------------------------------------- driver

def main():
    print("explore_slack_machine.py -- CAN THE SLACK BE PROGRAMMED?")
    print("=" * 72)
    s1 = s1_positive_control()
    if not s1:
        print("POSITIVE CONTROL FAILED -- no verdict read.")
        return 1
    s2_lossy_law()
    s3_instruction_set()
    s4_simulation()
    s5_flip_count()
    s6_the_read()
    s7_unconditional()
    print("=" * 72)
    if FAIL:
        print("FAILURES (%d):" % len(FAIL))
        for f in FAIL:
            print("  " + f)
        return 1
    print("all checks pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
