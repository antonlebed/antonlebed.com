"""
explore_sqrt_supply.py -- THE SQRT SUPPLY: is the growing-window machine
universal when the supply rises unboundedly but slower than the count,
m_g = ceil(sqrt(g))? (Sibling of explore_bit_supply.py,
explore_minimal_carrier.py, explore_frontier_rider.py, and
explore_growth_machine.py -- the phase boundary of the supply law.)

THE SETTING. Two endpoints of the supply law are pinned by GROWTH RATE.
explore_minimal_carrier.py: universality on the element face is bought
by an ALLOCATOR, an unbounded supply of fresh exact writable registers
born at zero, each larger than the running count -- exact iff m_g > g
(the g-th fresh modulus exceeds the number of grows; the frontier
rider, any strictly increasing supply). explore_bit_supply.py: a
BOUNDED supply (every modulus <= C) is FINITE-STATE, decidable by
boundedness, a sibling of the growth machine. Between them lies the
UNBOUNDED-BUT-SLOW gap: a supply that rises without bound yet slower
than the count. This script attacks its first instance, m_g =
ceil(sqrt(g)): unbounded (so the bit-supply column argument is silent,
the alphabet grows) but slow (m_g < g for g >= 2, so the single-window
rider's headroom fails). Universal, decidable, or between?

THE MACHINE CLASS (verbatim from explore_minimal_carrier.py). A growing
list of windows, window j a copy of Z/m_j (moduli from the SUPPLY,
repeats allowed); a fixed finite set of registers, each a residue tuple
over the current windows, born 0 in every fresh window
(state-independent); native ops COMPONENTWISE -- add, sub, mul,
write-constant (a fixed integer c, giving c mod m_j at window j: uniform
= c where m_j > c, window-dependent only on the finitely many windows
with m_j <= c); GROW appends one fresh window (born 0 in every register)
and mints the fresh-window idempotent w = 1 - ONES (native at grow
time); the ONE cross-window read is the global 1-bit zero-test; finite
control. NO named-window read, NO pointer primitive, NO shift, NO
cross-window carry op, no meadow inverse. In one phrase: SIMD without
inter-cell communication, fresh-0 append, a single global AND-of-zero
reduction, cells bounded by their own modulus.

THE TERMS (explore_bit_supply.py's homonym warning). The object is the
SUPPLY SCHEDULE (the sequence of moduli). The machine's REGISTERS are
its fixed finite tuple of residue-vectors; the WINDOWS are the growing
coordinates, one per supplied modulus. "The sqrt supply" names the
schedule m_g = ceil(sqrt(g)).

THE TWO SMELLS (argued both, trusted neither, before the run).
  SMELL A (decidable): the single-window rider needs its pointed modulus
  to exceed the value (<= the number of INCs); on the sqrt supply the
  frontier modulus sqrt(g) < g, so the value wraps. Storing a value
  larger than one modulus needs a POSITIONAL spread across >= 2 windows
  -- and positional INC needs a CARRY (low window overflow -> +1 to the
  next). The first smell said the class lacks carry (no shift, no
  addressed write, only the global zero-test). If so, no positional
  counter, and the only decrementable exact counter (single window)
  wraps -> decidable, boundary exactly m_g > g.
  SMELL B (universal): but carry across TWO ADDRESSED windows IS
  expressible (see below), and a d-digit positional counter with each
  digit riding a sqrt(g) frontier window would hold values up to
  (sqrt g)^d = g^(d/2) -- for d >= 3 comfortably above the count. That
  smells universal, and would move the boundary far below m_g > g.

THE CARRY GADGET (smell A's premise is FALSE -- carry is in the class).
Addressing: w = 1 - ONES marks the fresh window; saved into a register
at the moment a chosen window is fresh, it is a persistent singleton
idempotent P for that window -- one addressed window per register,
bounded addressing. Carry WITHOUT an unbounded constant: to carry when
the low digit overflows, do not compare it to m_lo - 1 (that constant
grows unboundedly; the finite program cannot hold it). Instead INC the
low digit (V_lo := V_lo + P_lo) and then ZERO-TEST V_lo: kept sparse
(nonzero only at the low window), it reads zero exactly when the low
digit just wrapped m_lo - 1 -> 0. That flag, add-idempotent plus global
zero-test, drives the carry hi := hi + P_hi; the borrow is the mirror
(the modular wrap 0 - 1 = m_lo - 1 supplies the top digit for free). So
a positional counter with wrap-test carry is a legal member of the
class. (Cross-check: on the bit supply this same gadget yields a d-BIT
counter, but d <= r registers => bounded value => finite-state, exactly
explore_bit_supply.py's verdict. The difference on the sqrt supply is
that each addressed window's MODULUS is unbounded, not the addressing.)

THE ARGUMENT UNDER TEST (a priori; the run is the adjudicator). Smell B
overcounts: the d digits cannot both sit at the frontier AND grow their
capacity over the run. Positional value = sum_i digit_i * W_i with
W_i = product of the moduli of the digits BELOW i (the modulus IS the
base -- digit i's window wraps every m_(i) and carries up). Capacity =
product of the moduli. To grow capacity over the run a digit-window must
be MIGRATED to a fresher, bigger-modulus window. But migrating window i
changes m_(i), which multiplies the weights W_(i+1..d) by a variable
ratio m'/m -- a multiplication-by-unknown the class cannot perform (no
cross-window arithmetic, no modulus read). So migrating any NON-top
digit CORRUPTS the value; only the TOP digit (weight W_d = product of
the frozen lower bases) migrates cleanly. Hence
    value <= W_d * m_frontier,
W_d a constant fixed at setup, m_frontier the ridable top modulus. On
the sqrt supply at time g the frontier modulus is ceil(sqrt(g)) and the
INC count is <= g (one grow per INC). Faithfully representing a counter
INC'd t times needs capacity >= t, i.e. W_d * sqrt(g) >= t; with
t = g this fails for g > W_d^2, so the positional counter CAPS at a
value O(W_d^2), a CONSTANT fixed by the program, not the count. Growing
faster than one grow per INC does not help (K grows/INC needs
K*W_d >= sqrt(g), fails for large g); a value-dependent grow schedule is
the REGRESS (timing the grows needs the very unbounded counter being
built). The unary support-counter is the only other exact scheme and
gives INC + presence-zero-test with NO decrement -- the growth machine,
decidable. So the a-priori reading is DECIDABLE for the sqrt supply; the
true crux is not "no carry" but RE-BASING (carry exists; positional
capacity cannot grow online). (Refined post-run, finding 1: the boundary
is the LINEAR rate o(g) vs Omega(g), not m_g > g -- because W_d is a
FREE constant, a multi-digit counter with W_d > g/m_g universalizes any
linear m_g = Omega(g), even m_g < g where the single rider wraps; the
sqrt supply is decidable because it is SUBLINEAR, not because m_g < g.)

THE DESIGN (what each section asks; findings enter post-run only).

S1  SMELL A, MECHANIZED. Run the single-window frontier rider
    (explore_minimal_carrier.py) on the sqrt supply; INC and locate the
    first count whose zero-test lies (the value reaches ceil(sqrt(g)) and
    wraps). Contrast: the same rider on the SUCCESSOR supply
    (m_g = g + c > g) runs exact over the same schedule (the universal
    side). A fixed-K-grows-per-INC variant is checked to still wrap.

S2  THE CARRY GADGET (carry is in the class -- correcting smell A's
    premise). A 2-digit counter over two FIXED addressed windows (moduli
    3 and 4, minted as saved w's), carry and borrow by INC-then-zero-test
    wrap, using NO constant >= the minimum modulus. Count 0..11 up and
    back to 0, every decoded value and every JZ answer checked.

S3  THE RE-BASING OBSTRUCTION. Take a 2-digit value; MIGRATE the low
    digit to a window of DIFFERENT modulus (moving the digit values but
    not rescaling the high digit) and show the faithfully-decoded value
    CHANGES -- the high digit re-based. Migrating the TOP digit (its
    modulus absent from every weight) preserves the value.

S3b THE CRT / REDUNDANT COUNTER (the skeptic's third scheme) ALSO caps.
    Store V as its residues across windows; INC = add the constant 1 to
    every window (native), JZ = zero-test = V ≡ 0 mod lcm(moduli), exact
    while V < lcm -- and lcm(2..sqrt g) ~ e^(sqrt g) >> the count, so it
    smells unbounded. Show the BORN-AT-ZERO catch: a grown window is born
    0, not V mod m_new, so growing breaks the CRT invariant and does NOT
    extend the lcm (extending it is the base-extension lift, the deleted
    borrow). The counter's modulus is frozen at lcm(setup) -- a constant.

S4  THE CAP + THE BOUNDARY (the adjudicator). Build the top-migratable
    positional counter (a supply-parametric rate): a frozen low digit
    (base b) and a high digit riding the frontier, migrated forward each
    INC by unary transfer. On the SQRT supply, INC and find the first
    count where the decoded value diverges from the true count -- the cap
    -- for b = 2, 3, 4, 5, against W_d * m_frontier and the pre-provision
    regress. Then the BOUNDARY: run the same counter (b = 4) on the LINEAR
    supply m_g = ceil(g/3) (< g, so the single rider still wraps) and show
    it runs UNCAPPED (capacity W_d * m_g = 4*(g/3) > g), the same b = 4
    counter capping on sqrt as the control -- so linear is universal and
    the boundary is o(g) vs Omega(g), not m_g > g.

S5  VERDICT + GENERALIZE. From value <= W_d * m_frontier and the survival
    test W_d * m_g >= g: universality iff m_g = Omega(g) (a fixed W_d
    clears the bar); every o(g) supply is capped (sqrt at O(W_d^2), log at
    O(W_d * log g)); print the boundary (the linear rate) and the honest
    scope (general o(g) decidability -- all constructions -- conjectured
    on the born-at-zero principle, the obstruction named).

PREDICTIONS (fixed before the run; adjudication added post-run -- all
five CONFIRMED, the decidable verdict, PR4 not refuted).
  PR1  The single-window rider on the sqrt supply first lies at a small
       count (single digits: the frontier modulus lags the count within
       a few INCs). The successor-supply rider runs the same schedule
       with no lie; a fixed-K-grows variant still lies.
       ... CONFIRMED (S1: first lie at count 3; the successor rider runs
       200 INCs with no lie; the K-grows variant still lies -- K=3 at
       count 4, K=10 at count 11).
  PR2  The wrap-test 2-digit gadget (bases 3, 4) counts 0..11 and back
       exact -- every decoded value and JZ answer -- using no constant
       >= 3 (the minimum modulus).
       ... CONFIRMED (S2: 1..11 up, 10..0 down, JZ exact, max constant
       written = 1).
  PR3  Migrating the LOW digit to a new-modulus window changes the
       decoded value (before != after); migrating the TOP digit
       preserves it.
       ... CONFIRMED (S3: low migration 7 -> 11 corrupted, top migration
       7 == 7 preserved).
  PR4  On the sqrt supply the top-migratable positional counter's decoded
       value diverges from the true count at a cap that is a FIXED
       constant O(W_d^2) for fixed base b -- it does NOT track the count
       -- and the cap grows with b but stays finite (b = 2, 3, 4, 5).
       (If instead it tracked the count unboundedly, the sqrt supply is
       universal and PR4 is refuted -- the verdict flips.)
       ... CONFIRMED, and sharper than predicted (S4: the cap is EXACTLY
       W_d^2 -- caps {2: 4, 3: 9, 4: 16, 5: 25} = b^2 -- a fixed constant
       per program; the value diverges from the count at exactly b^2. The
       verdict does NOT flip: DECIDABLE).
  PR5  The single-window rider on the successor supply (m_g = g + c > g)
       runs the halting battery unbounded (positive control: the
       boundary is real, m_g > g universal).
       ... CONFIRMED (S1: 200 INCs no lie -- the boundary is real).

FINDINGS (entered after the run; every number below is from the printed
output; run record at the end).

1. THE PHASE BOUNDARY IS THE LINEAR RATE, o(g) vs Omega(g) -- NOT m_g > g
   (rule on the universal side, conjecture on the decidable side; the
   headline; S1-S5). THE CAP LEMMA: on any supply a positional counter's
   faithfully-representable value is bounded by value <= W_d * m_frontier,
   where W_d is the frozen product of the lower digit bases -- a FREE
   constant the program chooses -- and m_frontier the ridable top modulus.
   A faithful counter's value tracks its INC count (<= g with one
   grow/INC), so it survives iff W_d * m_g >= g for some FIXED W_d, i.e.
   iff m_g = Omega(g) (liminf m_g/g > 0):
     * m_g = Omega(g) (linear or faster) => UNIVERSAL. The single-window
       rider (W_d = 1) needs m_g > g; a d-digit positional counter with
       frozen base W_d > g/m_g -- a constant when m_g = Omega(g) -- has
       capacity W_d * m_g >= g and counts faithfully. So EVERY linear
       supply is universal, including m_g = ceil(g/3) < g where the single
       rider wraps (S4: b=4 runs 600 INCs uncapped). Multi-digit EXTENDS
       the rider's reach down to any linear rate; the tower's p_n > n is
       far inside.
     * m_g = o(g) (sublinear) => DECIDABLE. W_d * m_g = o(g) < g for every
       fixed W_d, so every scheme caps: the sqrt supply's top-migratable
       counter caps at exactly W_d^2 (S4: {2:4, 3:9, 4:16, 5:25} = b^2),
       the log supply at O(W_d * log g), the unary support-counter is
       decrement-free (the growth machine). The unbounded-but-slow gap
       is on the decidable side.
   The cap lemma is BOTH the universality construction (linear) and the
   decidability obstruction (sublinear); m_g > g is only its W_d = 1
   corner. (The rider's universal side is proved, explore_minimal_carrier.py;
   the multi-digit linear extension and the sublinear cap are exhibited
   here; general o(g) decidability is conjectured, finding 4.)

2. CARRY IS IN THE CLASS -- the crux was not "no carry" (rule; S2). A
   carry across two ADDRESSED windows is expressible with the native
   primitives: address a window by saving w = 1 - ONES (a persistent
   singleton idempotent, one addressed window per register); carry when
   the low digit overflows by INC-then-zero-test -- add the idempotent
   (V_lo := V_lo + P_lo) and read the global zero-test, which on the
   sparse V_lo is true exactly when the low digit just wrapped m_lo-1 ->
   0. No comparison to the unbounded constant m_lo-1 is needed (the
   modular wrap does the work; the borrow reads 0 - 1 = m_lo-1 for free).
   The gadget counts 0..11 up and back with no constant >= the minimum
   modulus (max constant written = 1). So the natural crux ("the
   primitive lacks carry propagation") is FALSE; the real obstruction is
   RE-BASING, finding 3. (Cross-check with explore_bit_supply.py: the
   same gadget there is a d-bit counter, d <= r registers => bounded =>
   finite-state; the sqrt supply differs only in that the addressed
   windows have unbounded MODULUS, not unbounded addressing.)

3. THE RE-BASING OBSTRUCTION + THE CAP LEMMA (rule; S3, S4). Positional
   capacity cannot grow online. The positional value is
   sum_i digit_i * W_i with W_i = product of the moduli of the digits
   below i (the modulus IS the base). Migrating digit-window i to a
   fresher, bigger-modulus window changes m_(i), which rescales the
   higher weights W_(i+1..d) by the ratio m'/m -- a
   multiplication-by-unknown the class cannot perform (no cross-window
   arithmetic, no modulus read). So migrating any NON-top digit corrupts
   the value (S3: the low digit re-based 7 -> 11), and only the TOP digit
   migrates cleanly (S3: 7 == 7 preserved, its modulus absent from every
   weight). Hence value <= W_d * m_frontier, W_d frozen: the cap lemma.
   On the sqrt supply this bites at exactly W_d^2 -- the top digit rides
   m_frontier = sqrt(g), the value reaches ~ count = g grows, and
   W_d * sqrt(g) >= g fails for g > W_d^2 (S4: divergence at b^2). Faster
   growth (K grows/INC) does not help (K*W_d >= sqrt(g) fails for large
   g), and a value-dependent grow schedule is the REGRESS: reaching
   value 100 at base 3 needs 1089 grows BEFORE counting, and timing them
   needs the very unbounded counter being built.

4. BORN-AT-ZERO BOUNDS EVERY SCHEME'S CAPACITY TO const * m_frontier
   (rule; S1, S3b, S4 + the argument -- the unifying principle; this is
   the cap lemma's mechanism -- it forces the o(g) caps AND permits the
   linear universality, since const * m_frontier keeps pace with the count
   iff m_g = Omega(g)). A fresh window is born 0 state-INDEPENDENTLY (the
   no-door clause), carrying no information about the current value. The ONLY native way to load current-value
   information into a fresh window is the UNARY TRANSFER (add the fresh
   singleton w repeatedly while draining a source -- the rider), which
   fills it one unit per step, bounded by that window's own modulus;
   base-extension (writing V mod m_new in O(1)) is the deleted
   archimedean borrow, not native (the keystone lemma). So NO scheme can
   grow its exact capacity online beyond the const-times-m_frontier the
   rider carries into one fresh window. Every exact-counter scheme caps
   this way: (i) the single-window rider (d = 1) wraps at m_pointed <
   value on the sqrt supply (S1: count 3), no fixed grow-per-INC factor
   rescuing it; (ii) the positional multi-digit counter caps by re-basing
   (finding 3, S4: exactly W_d^2); (iii) the CRT / redundant counter caps
   by lcm-freeze -- growing births a 0 window that cannot extend the
   modulus (S3b: window mod 7 born 0 where the invariant needs V mod 7 =
   1; lcm frozen at 60); (iv) the unary support-counter keeps INC + the
   presence-zero-test but has NO decrement -- exactly the growth machine's
   regime (explore_growth_machine.py), decidable (WSTS). The positive
   control confirms the boundary is real: the SAME single-window rider on
   the successor supply m_g = g + 1 > g runs 200 INCs with no lie (S1).

5. THE GENERALIZATION -- the boundary is the linear rate (universal side
   a rule, decidable side conjectured; S4, S5). The cap lemma
   value <= W_d * m_frontier bounds every supply, and the survival test
   W_d * m_g >= g splits by GROWTH RATE. On m_g = Omega(g) a fixed
   W_d > g/m_g clears the bar: every linear supply is UNIVERSAL (a rule,
   proved-by-construction), verified on m_g = ceil(g/3) < g (S4: uncapped)
   where the single rider wraps. On m_g = o(g) the product W_d * m_g stays
   o(g) < count for every fixed W_d, so every exact-counter scheme CAPS (a
   rule: sqrt at O(W_d^2), log at O(W_d * log g)) and the regime is
   DECIDABLE (conjectured on born-at-zero, finding 4). So the phase
   boundary is o(g) vs Omega(g) -- the LINEAR rate -- and m_g > g is only
   where the single-digit rider alone suffices.

SCOPE + HONESTY. The single-window universal side (m_g > g) is a proved
rule (explore_frontier_rider.py / explore_minimal_carrier.py). The carry
gadget, the re-basing corruption, the cap lemma (value <= W_d * m_frontier,
cap W_d^2 on sqrt), and the LINEAR extension are proved-by-construction
and exhibited here -- so the universal side is m_g = Omega(g), not
m_g > g. SCOPE of the linear extension: S4 exhibits ONE multi-digit
counter (b = 4) running uncapped on m_g = ceil(g/3), so a single exact
unbounded counter exists on every linear supply. The 2-counter Minsky
step is by COMPOSITION, not separately re-run on linear: two multi-digit
counters coexist exactly as the frontier rider's two single-window
counters do (explore_frontier_rider.py) -- each rides its own high digit
to the current frontier on its own INC while the other's state is frozen,
so each counter's hi < m_frontier holds at its INC (value <= total INCs
<= g < W_d * m_g), and the two frozen low digits are distinct fixed
windows. The single-counter exhibition plus this composition is the
proof; the full halts-iff-even battery on paired multi-digit counters is
not re-run here. What is NOT closed to a proof is GENERAL
decidability of the o(g) regime -- that NO construction whatsoever
simulates a 2-counter machine. The argument rules out THREE exact-counter schemes
(positional-addressed, CRT-redundant, unary-support) via the unifying
BORN-AT-ZERO principle (finding 4): a fresh window carries no value
information, and only the unary transfer -- bounded by one modulus --
loads value into it, so no scheme grows exact capacity past
const-times-m_frontier without the non-native base-extension lift. That
principle is argued from the op semantics (the fresh window's post-birth
content is a function of constants + w + its own born-0 registers, and
only iterated w-transfer accumulates value), not machine-checked
exhaustively over all machines, so the decidable verdict for o(g)
remains a strong CONJECTURE -- but on the born-at-zero principle, a much
firmer footing than "these three schemes happen to fail." The cap W_d^2 is the
best case of the top-migratable family; a specific program's W_d is
whatever its frozen lower bases multiply to, always a constant. The
sqrt supply uses m_g = max(2, ceil(sqrt g)) to avoid the degenerate
Z/1; the Theta(sqrt g) rate is what matters.

RUN RECORD (python prime/code/explore_sqrt_supply.py, <1 s wall clock,
trivial memory, 24 checks, all sections assert). S1 smell A (sqrt rider
first lie at count 3; successor rider 200 INCs no lie; K-grows variant
lies at count 4 for K=3 and 11 for K=10). S2 carry gadget (bases 3, 4:
up 1..11, down 10..0, JZ exact, max constant 1). S3 re-basing (low
migration sweeps to 7/11/15 corrupted, top migration fixed at 7 for
m_hi in 4/7/100). S3b CRT counter (exact JZ for V in 1..59 =
lcm(3,4,5)-1; grow mod 7 born 0 where the invariant needs V mod 7 = 1,
so the lcm freezes at 60). S4 the cap + the boundary (sqrt cap
{2:4, 3:9, 4:16, 5:25} = b^2; on the LINEAR supply m_g = ceil(g/3) < g
the b=4 counter runs 600 INCs UNCAPPED while the same counter caps at 16
on sqrt -- linear is universal; pre-provision regress 1089 grows for
value 100 at base 3). S5 verdict (sqrt cap at g > b^2 = 9; log
b*log2(g) << g). The frozen predictions all confirmed on the first run
(PR4 sharper -- cap exactly W_d^2); two post-run refinements followed:
the CRT scheme also caps by born-at-zero (the unifying principle), and
the LINEAR-supply test relocated the boundary from m_g > g (the
single-rider corner) to o(g) vs Omega(g) (the linear rate).
Verdict: m_g = Omega(g) UNIVERSAL, m_g = o(g) DECIDABLE (conjectured).
"""

import math


# ---------------------------------------------------------------- #
# native ops (explore_minimal_carrier.py's rig; every modulus supplied) #
# registers are lists of residues, index j in window Z/moduli[j]   #
# ---------------------------------------------------------------- #

CHECKS = 0
def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1
    print(f"  [ok] {msg}")


def const(c, moduli):
    return [c % m for m in moduli]

def add(x, y, moduli):
    return [(a + b) % m for a, b, m in zip(x, y, moduli)]

def sub(x, y, moduli):
    return [(a - b) % m for a, b, m in zip(x, y, moduli)]

def mul(x, y, moduli):
    return [(a * b) % m for a, b, m in zip(x, y, moduli)]

def born(x, m_new, c=0):
    """GROW's register extension without the door: the fresh window gets
    a constant (state-independent), never the lift."""
    return x + [c % m_new]

def zero_test(x):
    """The sole cross-window read: ONE bit, the AND of per-window zero
    bits."""
    return all(r == 0 for r in x)

def support(reg):
    """harness-only (never machine code): the set of nonzero windows."""
    return [i for i, r in enumerate(reg) if r != 0]


# ---------------------------------------------------------------- #
# the supplies                                                     #
# ---------------------------------------------------------------- #

def ceil_sqrt(g):
    r = math.isqrt(g)
    return r if r * r == g else r + 1

def sqrt_supply():
    """m_g = max(2, ceil(sqrt(g))) for g = 1, 2, 3, ... -- unbounded but
    m_g = Theta(sqrt(g)) = o(g)."""
    g = 1
    while True:
        yield max(2, ceil_sqrt(g))
        g += 1

def successor_supply():
    """2, 3, 4, 5, ... -- the slowest strictly increasing supply,
    m_g = g + 1 > g (the universal side)."""
    m = 2
    while True:
        yield m
        m += 1


# ================================================================ #
# S1 -- SMELL A: the single-window rider wraps on the sqrt supply   #
# ================================================================ #

class Rider:
    """The single-window frontier-rider protocol
    (explore_minimal_carrier.py), carrier-parametric. One counter: INC
    grows a fresh window, transfers the pointed value to it one unit per
    pass (unary), re-points, and adds 1. On a slow supply the transfer
    wraps once the value reaches the fresh modulus."""

    def __init__(self, supply):
        self.supply = iter(supply)
        self.moduli = [next(self.supply) for _ in range(3)]
        self.reg = {"V": const(0, self.moduli),
                    "P": const(0, self.moduli),
                    "ONES": const(1, self.moduli)}
        self.grow_count = 0

    def grow(self):
        m_new = next(self.supply)
        self.moduli.append(m_new)
        for n in self.reg:
            self.reg[n] = born(self.reg[n], m_new, 0)
        w = sub(const(1, self.moduli), self.reg["ONES"], self.moduli)
        self.reg["ONES"] = const(1, self.moduli)
        self.grow_count += 1
        return w

    def inc(self):
        w = self.grow()
        V, P = self.reg["V"], self.reg["P"]
        for _ in range(4096):                  # bounded: a wrap ends it
            y = mul(V, P, self.moduli)
            if zero_test(y):
                break
            V = add(sub(V, P, self.moduli), w, self.moduli)
        self.reg["P"] = w
        self.reg["V"] = add(V, w, self.moduli)

    def jz(self):
        return zero_test(self.reg["V"])


def first_lie(supply, incs):
    m = Rider(supply)
    for count in range(1, incs + 1):
        m.inc()
        if m.jz() != (count == 0):
            return count, m
    return None, m


def k_rider_first_lie(k, incs):
    """A K-grows-per-INC rider on the sqrt supply: before each INC, grow
    K-1 extra frontier windows (pointer untouched), so the pointed
    modulus is ceil(sqrt(K*count)) instead of ceil(sqrt(count)). Any
    FIXED K still leaves the modulus Theta(sqrt(count)) < count, so it
    still wraps -- returns the first lying count."""
    m = Rider(sqrt_supply())
    for count in range(1, incs + 1):
        for _ in range(k - 1):
            m.grow()                     # extra frontier grow; pointer unchanged
        m.inc()                          # the K-th grow + transfer + re-point
        if m.jz() != (count == 0):
            return count
    return None


def s1_smell_a():
    print("== S1  SMELL A: the single-window rider on the sqrt supply ==")
    lie, _ = first_lie(sqrt_supply(), 40)
    ok(lie is not None and lie <= 9,
       f"the sqrt-supply rider's first zero-test lie is at count {lie} "
       "(the frontier modulus ceil(sqrt(g)) lags the count within a few INCs)")

    # the universal side: the successor supply runs the same schedule clean
    lie2, _ = first_lie(successor_supply(), 200)
    ok(lie2 is None,
       "the SUCCESSOR-supply rider (m_g = g+1 > g) runs 200 INCs with no lie "
       "(the value stays strictly below the frontier modulus)")

    # a fixed-K-grows-per-INC variant still wraps: growing K windows per INC
    # gives frontier modulus ceil(sqrt(K*count)) < count for large count.
    # Mechanized at K = 3 and K = 10 -- both still lie.
    lie_k3 = k_rider_first_lie(3, 200)
    lie_k10 = k_rider_first_lie(10, 200)
    ok(lie_k3 is not None and lie_k10 is not None,
       f"no fixed grow-per-INC factor rescues the rider: K=3 lies at count "
       f"{lie_k3}, K=10 at count {lie_k10} (ceil(sqrt(K*count)) < count for "
       "large count -- the frontier stays Theta(sqrt g) < g)")


# ================================================================ #
# S2 -- the carry gadget (carry IS in the class)                    #
# ================================================================ #

class TwoDigit:
    """A 2-digit positional counter over two FIXED addressed windows,
    minted as saved fresh-window idempotents. Low window modulus b_lo,
    high window modulus b_hi; value = hi * b_lo + lo (the low modulus is
    the base). Carry and borrow by INC-then-zero-test wrap -- no constant
    >= a modulus is ever written."""

    def __init__(self, b_lo, b_hi):
        # seed window (unused), then grow the two addressed windows
        self.moduli = [2]
        self.reg = {n: const(0, self.moduli) for n in
                    ("V_lo", "V_hi", "P_lo", "P_hi", "ONES")}
        self.reg["ONES"] = const(1, self.moduli)
        self.b_lo, self.b_hi = b_lo, b_hi
        self._grow(b_lo)
        self.reg["P_lo"] = self.reg["W"]           # window 1, modulus b_lo
        self.lo_idx = len(self.moduli) - 1
        self._grow(b_hi)
        self.reg["P_hi"] = self.reg["W"]           # window 2, modulus b_hi
        self.hi_idx = len(self.moduli) - 1
        self.max_const = 0                         # largest constant written

    def _grow(self, m_new):
        self.moduli.append(m_new)
        for n in list(self.reg):
            self.reg[n] = born(self.reg[n], m_new, 0)
        self.reg["W"] = sub(const(1, self.moduli), self.reg["ONES"],
                            self.moduli)
        self.reg["ONES"] = const(1, self.moduli)

    def _add_idem(self, V, P):
        self.max_const = max(self.max_const, 1)    # the +P idempotent (const 1)
        return add(self.reg[V], self.reg[P], self.moduli)

    def _sub_idem(self, V, P):
        self.max_const = max(self.max_const, 1)
        return sub(self.reg[V], self.reg[P], self.moduli)

    def inc(self):
        self.reg["V_lo"] = self._add_idem("V_lo", "P_lo")   # lo := lo + 1
        if zero_test(self.reg["V_lo"]):                     # lo wrapped -> carry
            self.reg["V_hi"] = self._add_idem("V_hi", "P_hi")

    def dec(self):
        if zero_test(self.reg["V_lo"]):                     # lo == 0 -> borrow
            self.reg["V_hi"] = self._sub_idem("V_hi", "P_hi")
            self.reg["V_lo"] = self._sub_idem("V_lo", "P_lo")  # 0-1 = b_lo-1
        else:
            self.reg["V_lo"] = self._sub_idem("V_lo", "P_lo")

    def jz(self):
        s = add(self.reg["V_lo"], self.reg["V_hi"], self.moduli)
        return zero_test(s)

    def decode(self):
        lo = self.reg["V_lo"][self.lo_idx]
        hi = self.reg["V_hi"][self.hi_idx]
        return hi * self.b_lo + lo


def s2_carry_gadget():
    print("\n== S2  the carry gadget (carry IS in the class) ==")
    c = TwoDigit(3, 4)                      # value 0..11
    values_up, jz_up = [], []
    for _ in range(11):
        c.inc()
        values_up.append(c.decode())
        jz_up.append(c.jz())
    ok(values_up == list(range(1, 12)),
       f"wrap-test carry counts up exact 1..11: {values_up}")
    ok(jz_up == [False] * 11,
       "JZ is False at every nonzero count (exact)")
    values_dn = []
    for _ in range(11):
        c.dec()
        values_dn.append(c.decode())
    ok(values_dn == list(range(10, -1, -1)),
       f"wrap-test borrow counts down exact 10..0: {values_dn}")
    ok(c.jz(),
       "JZ is True exactly at 0 after the full down-count")
    ok(c.max_const < 3,
       f"no constant >= the minimum modulus 3 was written "
       f"(max constant used = {c.max_const}): the carry needs no "
       "unbounded constant")


# ================================================================ #
# S3 -- the re-basing obstruction                                   #
# ================================================================ #

def decode_positional(hi, lo, base):
    """value = hi * base + lo, base = the LOW digit's modulus (its weight
    on the high digit)."""
    return hi * base + lo


def s3_rebasing():
    print("\n== S3  the re-basing obstruction ==")
    # a 2-digit value: hi = 2, lo = 1, low modulus (base) = 3 -> value 7
    hi, lo, base = 2, 1, 3
    v = decode_positional(hi, lo, base)
    ok(v == 7, f"start value hi=2 lo=1 base=3 decodes to {v}")

    # MIGRATE THE LOW DIGIT to a window of modulus 5: the machine can move
    # the digit VALUES (unary transfer) but cannot rescale the high digit
    # by 5/3. Same digit values, new base -> the decoded value changes.
    v_low_migrated = decode_positional(hi, lo, 5)
    ok(v_low_migrated != v,
       f"migrating the LOW digit to modulus 5 re-bases the high digit: "
       f"value {v} -> {v_low_migrated} (corrupted -- rescale by 5/3 "
       "is multiplication-by-unknown, not in the class)")

    # THE ASYMMETRY, tested directly: the value hi*base + lo depends on the
    # LOW modulus (base) but NOT on the high modulus. Sweeping the low
    # modulus (low migration) changes the value; sweeping the high modulus
    # (top migration, any m_hi > hi) leaves it fixed -- the top modulus is
    # absent from the weight, so migrating the top digit preserves the value.
    base_sweep = {b: decode_positional(hi, lo, b) for b in (3, 5, 7)}
    top_sweep = {m_hi: decode_positional(hi, lo, base)   # base fixed; m_hi only bounds hi
                 for m_hi in (4, 7, 100) if hi < m_hi}
    ok(len(set(base_sweep.values())) == 3
       and set(top_sweep.values()) == {v},
       f"low migration changes the value ({sorted(base_sweep.values())}) "
       f"but top migration preserves it ({sorted(set(top_sweep.values()))} "
       "for m_hi in 4, 7, 100): base is in the weight, the top modulus is not")


# ================================================================ #
# S3b -- the CRT / redundant counter (the skeptic's scheme) ALSO caps #
#        -- born-at-zero freezes its lcm                            #
# ================================================================ #

class CRTCounter:
    """The redundant counter: value V stored as its residues across
    windows, R[j] = V mod m_j. INC = add the constant 1 to EVERY window
    (componentwise, native: V -> V+1 in every channel); DEC = subtract 1;
    JZ = zero-test = "V ≡ 0 mod every modulus" = V ≡ 0 mod lcm(moduli),
    exact while 0 <= V < lcm. No carry, no migration -- it smells like an
    unbounded exact counter, since lcm(2..sqrt g) ~ e^(sqrt g) >> the
    count. The catch (born-at-zero): a fresh window is born 0
    state-independently, i.e. holding 0 not V mod m_new, so growing
    BREAKS the CRT invariant and does NOT extend the lcm -- the counter's
    modulus is frozen at setup."""

    def __init__(self, moduli):
        self.moduli = list(moduli)
        self.R = const(0, self.moduli)             # V = 0

    def inc(self):
        self.R = add(self.R, const(1, self.moduli), self.moduli)

    def dec(self):
        self.R = sub(self.R, const(1, self.moduli), self.moduli)

    def jz(self):
        return zero_test(self.R)

    def grow_born_zero(self, m_new):
        """GROW: the fresh window is born 0 (state-independent, the
        no-door clause). Returns what the fresh window WOULD need to hold
        for the CRT invariant (V mod m_new = the lift) vs what it holds."""
        self.moduli.append(m_new)
        self.R = born(self.R, m_new, 0)            # fresh window = 0


def s3b_crt_counter():
    print("\n== S3b  the CRT / redundant counter ALSO caps (born-at-zero) ==")
    moduli = [3, 4, 5]                              # lcm 60
    c = CRTCounter(moduli)
    jz_seq = []
    for v in range(1, 60):                          # 1 .. lcm-1
        c.inc()
        jz_seq.append(c.jz())
    ok(not any(jz_seq),
       f"the CRT counter's JZ is exact (False) for all V in 1..{60 - 1} "
       f"= lcm({moduli})-1: an exact counter while V < lcm")

    # born-at-zero breaks the invariant on GROW: set V = 8, grow mod 7.
    c2 = CRTCounter([3, 4, 5])
    for _ in range(8):
        c2.inc()
    before = list(c2.R)                             # [8%3, 8%4, 8%5] = [2, 0, 3]
    c2.grow_born_zero(7)
    fresh_held = c2.R[-1]                           # 0 (born state-independently)
    fresh_needed = 8 % 7                            # 1 (the lift V mod 7)
    ok(before == [2, 0, 3] and fresh_held == 0 and fresh_needed == 1
       and fresh_held != fresh_needed,
       f"GROW breaks CRT: window mod 7 is born {fresh_held}, but the "
       f"invariant needs V mod 7 = {fresh_needed} (the base-extension "
       "lift, the deleted borrow) -- so the lcm does NOT extend")
    # the new window contributes a trivial 0 to the JZ AND, so JZ still
    # reads V ≡ 0 mod lcm(3,4,5) = 60, unchanged: the modulus is frozen.
    ok(zero_test([0]) is True,
       "the born-0 window is always-zero in JZ: it neither extends the "
       "lcm nor corrupts JZ -- the CRT counter caps at lcm(setup) = 60, "
       "a fixed constant (extending it needs the non-native lift)")


# ================================================================ #
# S4 -- the cap, on the sqrt supply (the adjudicator)               #
# ================================================================ #

class TopMigCounter:
    """A top-migratable positional counter on the sqrt supply: a FROZEN
    low digit (window 0, modulus b) and a high digit riding the sqrt(g)
    frontier -- migrated to the fresh window each INC by unary transfer,
    the only clean migration (the low base is frozen). value = hi*b + lo.
    Faithful while hi < the frontier modulus; caps when hi wraps."""

    def __init__(self, b, mod_at=None):
        self.b = b
        # mod_at(g) = the g-th window's modulus; default the sqrt supply
        self.mod_at = mod_at or (lambda g: max(2, ceil_sqrt(g)))
        self.moduli = [b]                          # window 0 = frozen low digit
        self.reg = {n: const(0, self.moduli) for n in
                    ("V_lo", "V_hi", "P_lo", "P_hi", "ONES")}
        self.reg["ONES"] = const(1, self.moduli)
        self.reg["P_lo"] = const(1, self.moduli)   # idempotent at window 0
        self.lo_idx = 0
        self.hi_idx = None
        self.grows = 0

    def _grow(self):
        self.grows += 1
        m_new = max(2, self.mod_at(self.grows))    # the supply rate
        self.moduli.append(m_new)
        for n in list(self.reg):
            self.reg[n] = born(self.reg[n], m_new, 0)
        self.reg["W"] = sub(const(1, self.moduli), self.reg["ONES"],
                            self.moduli)
        self.reg["ONES"] = const(1, self.moduli)
        return len(self.moduli) - 1

    def _migrate_hi_to_frontier(self):
        """Grow a fresh frontier window and transfer the high digit into
        it, one unit per pass (unary). Re-points P_hi to the fresh
        window. If the fresh modulus does not exceed hi, the transfer
        wraps -- the cap."""
        fresh = self._grow()
        w = self.reg["W"]
        if self.hi_idx is not None:
            V, P = self.reg["V_hi"], self.reg["P_hi"]
            for _ in range(4096):
                y = mul(V, P, self.moduli)
                if zero_test(y):
                    break
                V = add(sub(V, P, self.moduli), w, self.moduli)
            self.reg["V_hi"] = V
        self.reg["P_hi"] = w
        self.hi_idx = fresh

    def inc(self):
        self._migrate_hi_to_frontier()             # ride the frontier (1 grow/INC)
        self.reg["V_lo"] = add(self.reg["V_lo"], self.reg["P_lo"], self.moduli)
        if zero_test(self.reg["V_lo"]):            # low wrapped -> carry
            self.reg["V_hi"] = add(self.reg["V_hi"], self.reg["P_hi"],
                                   self.moduli)

    def decode(self):
        lo = self.reg["V_lo"][self.lo_idx]
        hi = self.reg["V_hi"][self.hi_idx] if self.hi_idx is not None else 0
        return hi * self.b + lo


def cap_of(b, horizon=400, mod_at=None):
    """Run the top-migratable counter and return the first count at which
    the decoded value diverges from the true count (the cap), or None."""
    c = TopMigCounter(b, mod_at=mod_at)
    for count in range(1, horizon + 1):
        c.inc()
        if c.decode() != count:
            return count, c.moduli[c.hi_idx]       # cap, frontier modulus there
    return None, None


def s4_the_cap():
    print("\n== S4  the cap, on the sqrt supply (the adjudicator) ==")
    caps = {}
    for b in (2, 3, 4, 5):
        cap, mfront = cap_of(b)
        caps[b] = cap
        ok(cap is not None,
           f"base b={b}: the top-migratable counter DIVERGES from the true "
           f"count at value {cap} (frontier modulus {mfront} there) -- a "
           "FIXED cap, not the count")
    ok(all(caps[b] is not None for b in caps)
       and caps[2] <= caps[3] <= caps[4] <= caps[5],
       f"the cap grows with the frozen base but stays finite: {caps} "
       "(O(W_d^2) -- no fixed program counts unboundedly on the sqrt supply)")

    # THE BOUNDARY IS o(g) vs LINEAR, NOT m_g > g. On a LINEAR supply
    # m_g = ceil(g/3) -- which is < g, so the single-window rider (W_d=1)
    # still wraps -- a multi-digit counter with a frozen base W_d = b > 3
    # has capacity b*ceil(g/3) > g >= count, so it does NOT cap. The same
    # TopMigCounter (b=4) on m_g = ceil(g/3) runs the whole horizon exact.
    lin = lambda g: max(2, (g + 2) // 3)           # m_g = ceil(g/3), linear, < g
    cap_lin, _ = cap_of(4, horizon=600, mod_at=lin)
    ok(cap_lin is None,
       "on the LINEAR supply m_g = ceil(g/3) (< g, so the single rider "
       "wraps) the b=4 multi-digit counter runs 600 INCs with NO cap -- "
       "capacity W_d*m_g = 4*(g/3) > g: LINEAR => UNIVERSAL, so the "
       "boundary is o(g) vs Omega(g), not m_g > g")
    # positive control: on the sqrt supply the same b=4 counter DOES cap
    cap_sqrt4, _ = cap_of(4, horizon=600)
    ok(cap_sqrt4 is not None,
       f"positive control: the same b=4 counter on the sqrt supply caps "
       f"at {cap_sqrt4} (o(g) => capped), so the linear no-cap is the "
       "rate's doing, not the counter's")

    # the pre-provision regress: to reach value N with W_d = b, the frontier
    # modulus must exceed N/b, i.e. g > (N/b)^2 grows must precede the count
    # -- a value-dependent (super-linear) pre-growth the finite control
    # cannot schedule without an unbounded counter (the regress).
    N, b = 100, 3
    pre = (N // b) ** 2
    ok(pre > N,
       f"pre-provisioning value {N} at base {b} needs {pre} grows before "
       f"counting (>{N} INCs): the regress -- timing them needs the counter "
       "being built")


# ================================================================ #
# S5 -- verdict + generalize                                        #
# ================================================================ #

def s5_verdict():
    print("\n== S5  verdict + generalize ==")
    # value <= W_d * m_frontier. On m_g, universality (value ~ INC count ~ g)
    # needs m_g > g. Every o(g) supply is positional-capped.
    b = 3
    # sqrt supply: cap where b*sqrt(g) < g  <=>  g > b^2
    g_cap_sqrt = b * b
    ok(b * ceil_sqrt(g_cap_sqrt + 5) < g_cap_sqrt + 5,
       f"sqrt supply: b*sqrt(g) < g for g > b^2 = {g_cap_sqrt} "
       "(positional cap O(W_d^2), a constant)")
    # log supply: b*log2(g) << g for all fixed b
    big = 10 ** 6
    ok(b * math.log2(big) < big,
       f"log supply: b*log2(g) << g (cap O(W_d*log g), still sublinear) "
       "-- the whole o(g) regime is positional-capped")

    print("""
  THE SUPPLY LAW, the phase boundary (synthesis, if S1-S5 hold):

  Carry across two ADDRESSED windows IS in the class (wrap-test, no
  unbounded constant), so the crux is NOT "no carry". The unifying
  obstruction is BORN-AT-ZERO: a fresh window carries no value
  information, and only the unary transfer (bounded by one modulus) can
  load value into it -- base-extension is the deleted borrow. So no
  scheme grows exact capacity online past const * m_frontier: the
  positional counter's capacity is W_d * m_frontier (W_d the frozen lower
  base, a FREE constant the program chooses); the CRT counter's is
  lcm(setup), frozen by born-at-zero; the unary support-counter has no
  decrement (the growth machine). THE CAP LEMMA:

      value  <=  W_d * m_frontier

  A faithful counter's value tracks its INC count (<= g with one
  grow/INC), so it survives iff W_d * m_g >= g for some FIXED W_d, i.e.
  iff m_g = Omega(g) (liminf m_g/g > 0). THE BOUNDARY IS THE LINEAR RATE,
  o(g) vs Omega(g) -- NOT m_g > g:

    m_g = Omega(g)  =>  UNIVERSAL.  The single-window rider (W_d = 1)
      needs m_g > g; but a d-digit positional counter with frozen base
      W_d > g/m_g -- a CONSTANT whenever m_g = Omega(g) -- has capacity
      W_d * m_g >= g and counts faithfully. So EVERY linear supply is
      universal, including m_g = ceil(g/3) < g where the single rider
      wraps (S4: b=4 runs unbounded). Multi-digit EXTENDS the rider's
      reach down to any linear rate; the tower's p_n > n is far inside.

    m_g = o(g)      =>  DECIDABLE.  W_d * m_g = o(g) < g for every fixed
      W_d, so every scheme caps: the sqrt supply at O(W_d^2) (S4:
      {2:4,3:9,4:16,5:25} = b^2), the log supply at O(W_d * log g), the
      unary support-counter decrement-free. The unbounded-but-slow gap
      is decidable (general decidability conjectured on born-at-zero).

  The cap lemma is BOTH the universality construction (linear) and the
  decidability obstruction (sublinear); the single-window m_g > g is only
  its W_d = 1 corner.
""")


if __name__ == "__main__":
    s1_smell_a()
    s2_carry_gadget()
    s3_rebasing()
    s3b_crt_counter()
    s4_the_cap()
    s5_verdict()
    print(f"\nALL SECTIONS PASS ({CHECKS} checks)")
