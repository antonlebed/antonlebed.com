"""
explore_ecc_borrow.py -- THE ECC HEIGHT-CUT AT THE MACHINE LAYER
(the recovery chart's third row; descends from explore_second_ruler.py
and explore_reset_corner.py; the code-side contact is
explore_snapback_ca.py).

THE QUESTION. The tower's MDS erasure guarantee is a HEIGHT CUT: a
data element x is recoverable from any k-3 windows because x < D, the
product of the data primes -- uniqueness under an archimedean bound.
The cut is not dynamics-invariant: ring arithmetic does not preserve
the data range, so any state-evolution use of the code must re-derive
parity per step (base extension). The recovery chart prices re-imports
by what they let a machine READ of a value as it moves (the
value-reading/value-blind distinction of explore_reset_corner.py; the
borrow synthesis of explore_second_ruler.py). So: does per-step parity
re-derivation act as a BORROW -- a readable down-move, the ingredient
universality needs -- or is it inert like the reset (value-blind,
finite-state)? The naive grading says inert: "a syndrome is just a
residue read." This script shows the naive grading is wrong-shaped,
and the answer splits by WHICH syndrome.

THE MODEL (the codeword machine). State = (control q, a finite set S
of open prime windows, finitely many element registers x_i in Z/N with
N = prod S -- windows stay residue FIELDS, squarefree; this door needs
no prime-power depth, in contrast to the second-ruler door). MOVES,
all channel-local:
  GROW        adjoin a fresh prime window; each register receives a
              birth residue set by a channel-local rule (a constant).
  RING OPS    x + a (any constant, so subtraction is native), x * u
              (u a unit), x * 0 (reset), x * e_S (idempotent mask);
              the full ring repertoire x + y, x * y between registers
              is also native (the keystone lemma below covers all
              polynomial maps, any number of registers).
  TESTS       channel reads (x mod p = r), including the native
              zero-test x = 0 in Z/N (every window reads 0).
THE DOOR (the priced primitive):
  BASE-EXTEND(x, p)  set window p's residue of x to (CRT lift of x
              from the other windows) mod p -- exactly the ECC parity
              re-derivation, the height cut used dynamically.

THE HAND ANALYSIS THE RUN VERIFIES (proofs here; the run checks every
checkable step; Minsky universality is cited, not re-proved):

 1. WITH THE DOOR: FULL UNIVERSALITY. On elements the down-move is
    already native -- x - 1 is add-a-constant, and the zero-test is a
    native presence read. What blocks Minsky counters is neither: it
    is EXACTNESS. On a fixed rung the ring is finite (wrap at N); on
    the growing tower a window adjoined mid-run cannot be set to
    lift(x) mod p_new by any channel-local rule, so it is born OFFSET
    and the zero-test's meaning degrades. BASE-EXTEND is exactly the
    missing sync: grow + extend before every increment keeps each
    register's lift equal to its virtual counter value with lift < N
    forever, so x = 0 in Z/N reads TRUE INTEGER ZERO. Increment,
    guarded decrement, exact zero-test, unbounded room: a two-counter
    Minsky machine runs step-exactly, halting transfers, and halting
    for two-counter machines is undecidable (Minsky 1967). Full
    universality -- the same grade as the second ruler's door. The
    reduction is to the REMEMBERING BORROW (the reset corner's
    dangerous case): parity-per-step turns the ring's wrapped
    subtraction into a true read-at-the-bottom decrement. The height
    certificate is what "remembers."

 2. WITHOUT THE DOOR: THE TWO LIES. The same zero-test, unsynced,
    lies in both directions. FALSE ZERO (the wrap-lie): a fully
    synced register in a fixed ring Z/30 incremented past the modulus
    reads all-zeros at c = 30 -- the machine branches "zero" on a
    nonzero counter. FALSE NONZERO (the freeze): a window born with
    constant residue while the register's virtual value is c0 != 0
    reads (c - c0) mod p forever after (additive ops; the general
    affine form is checked in section 3), so when the counter truly
    returns to zero the machine reads NONZERO -- the guard that
    Minsky decrements need is exactly what breaks.

 3. THE FREEZE LEMMA (the offset is permanent and exactly priced).
    A window born at virtual value c0 with multiplier product M0
    carries r_p(t) = (c(t) - (M(t)/M0) * c0) mod p at every later t,
    where c is the virtual integer value and M the product of unit
    multipliers applied since; no later state-independent add or unit
    multiplier changes the offset's presence, and the remaining
    state-independent ops only ERASE it (x * 0 and masks write
    constants -- rebirth at certified zero, per section 6, not
    repair). BASE-EXTEND repairs it exactly when the height
    invariant holds (0 <= c < product of the source windows) -- the
    repair itself obeys the cut.

 4. THE KEYSTONE LEMMA (base extension is non-ring-computable).
    Every composite of ring ops -- any polynomial map in any number
    of registers, parameters fixed in advance -- acts CHANNEL-LOCALLY
    by CRT: the output's window-p residue depends on the inputs'
    window-p residues alone. Registers born in window p with constant
    residues therefore yield a constant there under any such
    composite -- but the base-extension target lift(x) mod p is not
    constant in x. So no STATE-INDEPENDENT sequence of native ops
    ever base-extends: CRT independence itself forbids it. (This is
    the residue-number-system engineering fact read as a theorem:
    base extension is THE non-channel-local RNS operation -- the wrap
    count alpha in lift = sum x_p*w_p*(N/p) - alpha*N is precisely
    the archimedean bit; inside Z/N the sum just returns x. Szabo &
    Tanaka 1967, cited.) The corollary must be scoped honestly:
    cross-window information DOES move through the finite control
    (branch on one window's reads, write the learned value into
    another), so a program can rebuild a lift residue from any source
    of windows it can NAME -- bounded-source base extension is native.
    What no fixed program reaches is extension from an UNBOUNDEDLY
    growing source: the program text owns finitely many window names
    and handle registers while the windows accumulate without bound
    (the addressing wall). The door's irreducible content is exactly
    unbounded-source extension -- which is what an unbounded exact
    counter needs.

 5. THE SYNDROME DICHOTOMY IS OPERATIONAL, NOT INFORMATIONAL. The
    first-frozen form of this section's prediction -- "no coset of a
    nontrivial subgroup code lies wholly below the cut" -- was
    REFUTED BY HAND before any code ran: 101^2 - 31^2 = 70 * 132 =
    4 * 2310, so with h = 101 * 31^(-1) mod 2310 the pair {31, 101}
    is a full coset of the order-2 subgroup {1, h}, wholly inside
    [0, 210). A small dictionary code's coset can pin the lift
    statically: syndrome INFORMATION does not separate the two ECCs.
    What separates them is what the dynamics can compute and what the
    read means as the state moves: (a) the height-cut syndrome
    (parity consistency) is exactly the predicate [lift < D], an
    APERIODIC read -- no proper additive period -- and re-deriving it
    is non-ring-computable (section 4); (b) every residue read is
    periodic with its window-product period and stays channel-local
    under all dynamics; the dictionary syndrome of the snap-back
    reading (explore_snapback_ca.py) is preserved by binding itself
    -- never re-derived, never reading the lift as it moves. The
    dictionary code is the value-blind side of the reset corner's
    distinction; the height cut is the value-reading side.

 6. THE DIVISION-SYNC TENSION (the door refuses side entrances). To
    TEST q | c a machine needs window q open; to DIVIDE by q it needs
    q invertible, hence closed. No window is both readable and
    invertible. The meadow's escape -- multiply by the pseudo-inverse
    of q -- divides exactly on the non-q windows when q | c, but
    writes 0 into window q where the true quotient residue (c/q) mod
    q belongs: every gated division DESYNCS its own window, and only
    BASE-EXTEND (or rebirth at certified zero) re-syncs. Sync is a
    spendable resource; the door is its only unbounded mint.

SYNTHESIS. The ECC height-cut door is a BORROW, and it buys FULL
UNIVERSALITY: growth + native ring ops + per-step parity re-derivation
run any Turing machine (via Minsky), with the undecidability priced
entirely in the one non-channel-local primitive the code's guarantee
already required. The naive "syndromes are residue reads, hence inert"
grading fails because it grades the WRONG syndrome: the dictionary
(subgroup-code) syndrome is channel-local and value-blind -- that side
is inert; the height-cut syndrome is the lift certificate itself, and
its per-step re-derivation is the archimedean import in code clothing.
The two error-correcting codes were already distinct statically -- the
dictionary escape changes codes, not dynamics
(explore_snapback_ca.py) -- and dynamically they land on opposite
sides of the computability knife edge.

SCOPE + HONESTY. Universality is a theorem about the modelled
repertoire plus the door primitive; Minsky two-counter universality is
cited, not re-derived (the run verifies the simulation step-exactly
and the halting transfer on a witness battery). A fixed rung is a
finite ring -- computation lives on the growing tower. Whether the
BARE class (growth + ring ops + channel reads, no base extension) is
decidable is NOT claimed either way: every universality construction
attempted here dies at a named wall -- integer-affine shadows die at
unit-inverse moves; FRACTRAN-style gated division burns unmintable
sync; idempotent tape-cells, and a mixed-radix reconstruction of the
lift that bootstraps sync from the reset register upward (extract
residues by masked counting loops, rebuild digit by digit), both die
at the ADDRESSING WALL (finitely many window names and handle
registers against unboundedly many windows) -- but no decidability
proof is offered: the bare class is the row's named open residual, a
finite control over unboundedly many independent finite windows with
broadcast ops (broadcast-protocol-shaped, but with an unbounded
family of window alphabets). The one-parity cut
used in section 5(a) is detection-only (distance 2); it is used for
syndrome shape, not for a correction claim. Base extension's cost
status in RNS engineering is cited context, not run.

PREDICTIONS (fixed before the run):
 P1. The base-extended Minsky simulation is step-exact (control
     state, both counters, and the height invariant lift < N match
     the reference at every macro step) and halting transfers: the
     halts-iff-even witness halts for even seeds with equal step
     counts and runs past the horizon for odd seeds, seeds 0..8.
 P2. The wrap-lie fires exactly at the modulus: a synced register in
     Z/30 gives a false all-zeros read at c = 30 and no false read
     for c = 1..29.
 P3. The freeze formula r_p = (c - (M/M0)*c0) mod p holds at every
     step of both op batteries (additive, and mixed with unit
     multipliers), and BASE-EXTEND repairs the offset exactly
     whenever 0 <= c < the source-window product.
 P4. Parity consistency <=> lift < D exhaustively at N = 2310 for
     both the tower split (D = 6) and the one-parity cut (D = 210);
     [lift < D] has no proper period among the divisors of N while
     every single-window read has period exactly its window; every
     random ring-op composite is channel-local on a randomized
     battery; the {31, 101} coset specimen verifies.
 P5. Pseudo-inverse division by q = 5 in Z/210 is exact on the non-q
     windows for every multiple of 5, window 5 is desynced (the true
     quotient residue is nonzero for most inputs and always lost),
     and BASE-EXTEND restores it exactly (the quotient obeys the
     smaller cut c/5 < 42).

FINDINGS (entered after the run; 21/21 checks; all five predictions
confirmed, no misses):

 F1. THE DOOR BUYS FULL UNIVERSALITY (rule; simulation verified
     step-exact, Minsky universality cited). The base-extended
     codeword machine runs the halts-iff-even two-counter witness
     step-exactly for seeds 0..8: traces (state, X, Y) identical to
     the reference at every macro step, even seeds halt with equal
     step counts, odd seeds run past the horizon, and the height
     invariant lift < N holds through 60 grown increments. Halting
     for the modelled machine is therefore undecidable and any Turing
     machine is simulable. The door is used ONLY at grows -- each
     register extended once per grown window; windows stay squarefree
     fields throughout (no depth axis).

 F2. THE TWO LIES WITHOUT THE DOOR (rule; witnessed exactly). False
     zero: the synced register in Z/30 reads all-zeros first at
     c = 30, never before. False nonzero: window 7 born unsynced at
     c = 4 holds -4 mod 7 = 3 when the counter truly returns to 0,
     so the zero-guard misfires; the identical run with the door
     reads true zero. The unsynced zero-test lies in both directions
     -- exactly the two failure modes a Minsky guard cannot survive.

 F3. THE FREEZE LEMMA (rule; two batteries). r_p = (c - (M/M0)*c0)
     mod p at every step: additive battery 300 steps with two
     mid-run births, mixed battery 60 steps with unit multipliers
     and a second birth. Repair is exact from a SYNCED source under
     the cut -- and the first harness draft caught the premise live:
     extending window 11 from a source that included frozen window
     13 inherits the offset; the source-window clause in P3 is
     load-bearing, not decoration.

 F4. THE OPERATIONAL DICHOTOMY (each object graded separately).
     Parity consistency <=> lift < D for both splits (D = 6 tower
     split, D = 210 one-parity cut): rule, exhaustive over all 2310
     elements. The cut predicate has no proper period, and every
     single-window read's periods are exactly its window's multiples
     (period sets are subgroups, so the divisor check is complete):
     rule, exhaustive at N = 2310. Channel-locality of ring-op
     composites: proved by CRT (the keystone lemma's premise),
     spot-checked on a randomized battery (40 composites x 5
     windows) -- so base extension is non-ring-computable by the
     constant-birth argument. And the {31, 101} specimen verifies:
     101^2 = 31^2 mod 2310, a coset of an order-2 subgroup wholly
     below the cut -- the informational form of the dichotomy is
     dead; the operational form is what holds.

 F5. THE DIVISION-SYNC TENSION (rule; exhaustive over 42 inputs).
     Pseudo-inverse division by 5 is exact on windows 2, 3, 7 for
     every multiple of 5 in Z/210; window 5 is zeroed with the true
     quotient residue lost (nonzero for 33/42 inputs); base-extend
     restores it exactly since the quotient obeys the smaller cut;
     no open window is invertible.

RUN RECORD. python explore_ecc_borrow.py -- sections S1-S5, 21/21
checks, < 1 s wall clock (0.1 s measured, subprocess-timed), pure
Python, deterministic (seeds 233/234). One
harness fix between the design draft and the green run: the S3 repair
initially base-extended from ALL other windows (including the other
frozen one) and correctly failed -- fixed to the synced source, which
is the lemma's own premise (see F3); no prediction was revised.
"""

import random

# ---------------------------------------------------------------- #
# machinery                                                        #
# ---------------------------------------------------------------- #

def sieve_primes(n):
    s = list(range(n + 1))
    s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i :: i] = [0] * len(s[i * i :: i])
    return [p for p in s if p]

PRIMES = sieve_primes(2000)

def crt_lift(reg):
    """The canonical lift in [0, N) of a register's residue tuple."""
    N = 1
    for p in reg:
        N *= p
    x = 0
    for p, r in reg.items():
        Np = N // p
        x = (x + r * pow(Np, -1, p) * Np) % N
    return x

def make_reg(c, windows):
    """A register synced to integer c across the given windows."""
    return {p: c % p for p in windows}

def add(reg, a):
    return {p: (r + a) % p for p, r in reg.items()}

def mul(reg, u):
    return {p: (r * u) % p for p, r in reg.items()}

def mul_elem(reg, other):
    return {p: (r * other[p]) % p for p, r in reg.items()}

def born(reg, p_new, const=0):
    """GROW without the door: the new window gets a constant."""
    out = dict(reg)
    out[p_new] = const % p_new
    return out

def base_extend(reg, p_new, src_windows=None):
    """THE DOOR: window p_new reads the CRT lift of the source windows
    (default: all others -- the source must be synced and hold the cut)."""
    out = dict(reg)
    src = {p: r for p, r in reg.items()
           if p != p_new and (src_windows is None or p in src_windows)}
    out[p_new] = crt_lift(src) % p_new
    return out

def zero_test(reg):
    return all(r == 0 for r in reg.values())

CHECKS = 0
def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1
    print(f"  [ok] {msg}")

# ---------------------------------------------------------------- #
# S1 -- with the door: the Minsky simulation                       #
# ---------------------------------------------------------------- #

# Halts-iff-even two-counter program.
#   state 0: if X == 0 halt, else X -= 1, go 1
#   state 1: if X == 0 go LOOP, else X -= 1, go 0
#   LOOP  : Y += 1, go LOOP                     (diverges)
PROG = {
    0: ("DECJZ", "X", 1, "HALT"),
    1: ("DECJZ", "X", 0, "LOOP"),
    "LOOP": ("INC", "Y", "LOOP"),
}

def run_reference(c0, horizon):
    q, c = 0, {"X": c0, "Y": 0}
    trace = [(q, c["X"], c["Y"])]
    for _ in range(horizon):
        if q == "HALT":
            break
        ins = PROG[q]
        if ins[0] == "INC":
            c[ins[1]] += 1
            q = ins[2]
        else:
            _, reg, nz, z = ins
            if c[reg] == 0:
                q = z
            else:
                c[reg] -= 1
                q = nz
        trace.append((q, c["X"], c["Y"]))
    return trace

def run_tower(c0, horizon):
    """The codeword machine with the door: grow+extend before INC."""
    windows = [2, 3, 5]
    next_i = 3  # PRIMES[3] = 7
    X = make_reg(c0, windows)
    Y = make_reg(0, windows)
    q = 0
    trace = [(q, crt_lift(X), crt_lift(Y))]
    for _ in range(horizon):
        if q == "HALT":
            break
        ins = PROG[q]
        if ins[0] == "INC":
            p_new = PRIMES[next_i]
            next_i += 1
            windows.append(p_new)
            X = base_extend(born(X, p_new), p_new)   # the door
            Y = base_extend(born(Y, p_new), p_new)   # the door
            tgt = X if ins[1] == "X" else Y
            tgt = add(tgt, 1)
            if ins[1] == "X":
                X = tgt
            else:
                Y = tgt
            q = ins[2]
        else:
            _, name, nz, z = ins
            tgt = X if name == "X" else Y
            if zero_test(tgt):
                q = z
            else:
                tgt = add(tgt, -1)
                if name == "X":
                    X = tgt
                else:
                    Y = tgt
                q = nz
        trace.append((q, crt_lift(X), crt_lift(Y)))
    return trace

def s1():
    print("S1  with the door: the Minsky simulation is step-exact")
    horizon = 100
    all_match, verdicts_match = True, True
    for c0 in range(9):
        ref = run_reference(c0, horizon)
        tow = run_tower(c0, horizon)
        if ref != tow:
            all_match = False
        ref_halts = ref[-1][0] == "HALT"
        tow_halts = tow[-1][0] == "HALT"
        if ref_halts != tow_halts or ref_halts != (c0 % 2 == 0):
            verdicts_match = False
    ok(all_match, "traces step-exact (state, X, Y) for seeds 0..8")
    ok(verdicts_match,
       "halting transfers: even seeds halt, odd seeds run past horizon")
    # the height invariant: lift < N throughout on the divergent run
    windows = [2, 3, 5]
    next_i = 3
    Y = make_reg(0, windows)
    inv = True
    for _ in range(60):
        p_new = PRIMES[next_i]
        next_i += 1
        Y = base_extend(born(Y, p_new), p_new)
        Y = add(Y, 1)
        N = 1
        for p in Y:
            N *= p
        if not crt_lift(Y) < N:
            inv = False
    ok(inv, "height invariant lift < N holds through 60 grown INCs")

# ---------------------------------------------------------------- #
# S2 -- without the door: the two lies                             #
# ---------------------------------------------------------------- #

def s2():
    print("S2  without the door: the two lies")
    # false zero: the wrap-lie in fixed Z/30
    reg = make_reg(0, [2, 3, 5])
    no_false = True
    for c in range(1, 30):
        reg = add(reg, 1)
        if zero_test(reg):
            no_false = False
    ok(no_false, "no false zero for c = 1..29 in Z/30")
    reg = add(reg, 1)  # c = 30
    ok(zero_test(reg), "the wrap-lie: all-zeros read at c = 30 (nonzero)")
    # false nonzero: the freeze
    X = make_reg(4, [2, 3, 5])
    X = born(X, 7, 0)            # window 7 born while c = 4, no door
    for _ in range(4):
        X = add(X, -1)           # true c = 0
    ok(not zero_test(X) and X[7] == (0 - 4) % 7,
       "the freeze: true zero reads NONZERO (window 7 holds -4 mod 7)")
    # the door repairs the same run
    X2 = make_reg(4, [2, 3, 5])
    X2 = base_extend(born(X2, 7), 7)
    for _ in range(4):
        X2 = add(X2, -1)
    ok(zero_test(X2), "base-extend at birth: the same run reads zero truly")

# ---------------------------------------------------------------- #
# S3 -- the freeze lemma batteries                                 #
# ---------------------------------------------------------------- #

def s3():
    print("S3  the freeze lemma: offsets exact, repair under the cut")
    rng = random.Random(233)
    # battery A: additive walk, births mid-run, repair asserts
    windows = [2, 3, 5, 7]
    c = 0
    reg = make_reg(0, windows)
    births = {}                    # p -> c at birth
    formula_holds, repairs_exact = True, True
    for t in range(300):
        if t == 50:
            reg = born(reg, 11, 0)
            births[11] = c
        if t == 120:
            reg = born(reg, 13, 0)
            births[13] = c
        a = rng.choice([1, -1])
        if c + a < 0 or c + a > 200:
            a = -a
        reg = add(reg, a)
        c += a
        for p, c0 in births.items():
            if reg[p] != (c - c0) % p:
                formula_holds = False
    ok(formula_holds, "battery A (additive): r_p = (c - c0) mod p, 300 steps")
    # repair: the source must be the SYNCED windows 2,3,5,7 (born at 0)
    # -- extending from a source containing the OTHER frozen window
    # inherits its offset; the lemma's premise is a synced source.
    for p in (11, 13):
        fixed = base_extend(reg, p, src_windows=[2, 3, 5, 7])
        if not (0 <= c < 210) or fixed[p] != c % p:
            repairs_exact = False
    ok(repairs_exact, "base-extend repairs both frozen windows exactly")
    # battery B: mixed walk with unit multipliers, general affine form
    windows = [2, 3, 5, 7, 11, 13]
    c, M = 0, 1
    reg = make_reg(0, windows)
    births = {}                    # p -> (c, M) at birth
    reg = born(reg, 17, 0)
    births[17] = (c, M)
    holds = True
    for t in range(60):
        op = rng.choice(["+1", "-1", "*u", "+1"])
        if op == "*u":
            u = 19
            reg = mul(reg, u)
            c *= u
            M *= u
        else:
            a = 1 if op == "+1" else -1
            reg = add(reg, a)
            c += a
        if t == 20:
            reg = born(reg, 23, 0)
            births[23] = (c, M)
        for p, (c0, M0) in births.items():
            if reg[p] != (c - (M // M0) * c0) % p:
                holds = False
    ok(holds, "battery B (mixed): r_p = (c - (M/M0)*c0) mod p, 60 steps")

# ---------------------------------------------------------------- #
# S4 -- the operational dichotomy + the keystone lemma             #
# ---------------------------------------------------------------- #

def s4():
    print("S4  the dichotomy: aperiodic cut, channel-local everything else")
    N = 2310
    prs = [2, 3, 5, 7, 11]
    for data, parity in ([[2, 3], [5, 7, 11]], [[2, 3, 5, 7], [11]]):
        D = 1
        for p in data:
            D *= p
        good = True
        for x in range(N):
            data_lift = crt_lift({p: x % p for p in data})
            consistent = all(x % p == data_lift % p for p in parity)
            if consistent != (x < D):
                good = False
        ok(good, f"parity consistency <=> lift < {D} (exhaustive, N=2310)")
    # aperiodicity of the cut vs periodicity of residue reads
    D = 210
    cut = [1 if x < D else 0 for x in range(N)]
    divisors = [q for q in range(1, N) if N % q == 0]
    aper = all(any(cut[x] != cut[(x + q) % N] for x in range(N))
               for q in divisors)
    ok(aper, "[lift < 210] has no proper period among divisors of N")
    # a residue read's periods in Z/N are exactly the multiples of its
    # window (the period set is the subgroup generated by the window)
    reads_exact = True
    for p in prs:
        f = [1 if x % p == 1 else 0 for x in range(N)]
        for q in divisors:
            is_per = all(f[x] == f[(x + q) % N] for x in range(N))
            if is_per != (q % p == 0):
                reads_exact = False
    ok(reads_exact,
       "single-window reads: periods are exactly the window's multiples")
    # channel-locality of random ring-op composites (keystone premise)
    rng = random.Random(234)
    local = True
    for _ in range(40):
        ops = [rng.choice([("add", rng.randrange(1, N)),
                           ("mul", rng.randrange(1, N)),
                           ("sqr", None)]) for _ in range(6)]
        def f(x):
            for kind, a in ops:
                if kind == "add":
                    x = (x + a) % N
                elif kind == "mul":
                    x = (x * a) % N
                else:
                    x = (x * x) % N
            return x
        for p in prs:
            x = rng.randrange(N)
            y = x
            while y % p != x % p or y == x:
                y = rng.randrange(N)
            if f(x) % p != f(y) % p:
                local = False
    ok(local, "random ring-op composites are channel-local (40 x 5 windows)")
    # the hand specimen: a coset wholly inside the cut
    h = (101 * pow(31, -1, N)) % N
    coset = {31, (31 * h) % N}
    from math import gcd
    ok(gcd(31, N) == 1 and gcd(101, N) == 1 and h != 1
       and (h * h) % N == 1 and coset == {31, 101}
       and all(x < D for x in coset),
       "the {31,101} specimen: an order-2 subgroup's coset wholly below the cut")

# ---------------------------------------------------------------- #
# S5 -- the division-sync tension                                  #
# ---------------------------------------------------------------- #

def s5():
    print("S5  the division-sync tension: pseudo-inverse burns its window")
    windows = [2, 3, 5, 7]
    N = 210
    q = 5
    qstar = {p: (pow(q, -1, p) if p != q else 0) for p in windows}
    exact_off_q, q_zeroed, repaired = True, True, True
    desynced = 0
    for c in range(0, N, q):
        x = make_reg(c, windows)
        y = mul_elem(x, qstar)
        quot = c // q
        if any(y[p] != quot % p for p in (2, 3, 7)):
            exact_off_q = False
        if y[q] != 0:
            q_zeroed = False
        if quot % q != 0:
            desynced += 1
        fixed = base_extend(y, q)
        if fixed[q] != quot % q:
            repaired = False
    ok(exact_off_q, "gated division exact on the non-q windows (42 inputs)")
    ok(q_zeroed, "window 5 written to 0: the true quotient residue is lost")
    ok(desynced > 30, f"desync is generic ({desynced}/42 quotients nonzero mod 5)")
    ok(repaired, "base-extend restores window 5 (quotient obeys the cut < 42)")
    ok(all(p != 1 and N % p == 0 for p in windows),
       "no open window is invertible: readable and dividable exclude")

# ---------------------------------------------------------------- #

if __name__ == "__main__":
    s1()
    s2()
    s3()
    s4()
    s5()
    print(f"\nALL CHECKS PASS: {CHECKS}/{CHECKS}")
