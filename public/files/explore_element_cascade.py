"""THE CASCADE LADDER IN THE ELEMENT WORLD -- re-walking the pinned-cap
sweep at the loosened cap an element move pays for, and measuring the
constant that loosens it rather than bounding it.

THE QUESTION. explore_module_law.py C proves the cascade reduction --
non-lock forces an infinite carrier ladder at every rank-1
characteristic -- and names the world it holds in: THE IDEAL WORLD. An
element move is not single-place, so the three steps fare differently.
This rig acts on what that leaves.

  (a) Step (2)'s door survives with a constant attached. The cheapest
      PRINCIPAL ideal of P-valuation v+2 is P^(v+2)*B with B in the
      inverse class, so the door costs at most tau_K * p^(v+2) where
      tau_K is the largest, over ideal classes, of the least norm in the
      class. The cap on the carrier multiplier loosens from m <= p-1 to
      m < tau_K * p, and the sweep that closed 167 characteristics is
      the same walk with that one constant moved.
  (b) tau_K has been BOUNDED (Minkowski) and never measured. For an
      imaginary quadratic field it is exactly computable: ideal classes
      correspond to reduced binary quadratic forms (a,b,c) of the
      discriminant, and the least norm in a class is that form's leading
      coefficient a -- so tau_K = max a over reduced forms, with no
      slack at all.
  (c) Step (1) -- cost divergence -- runs on the single-place lemma,
      which is exactly what dies in the element world. It is
      re-established by hand below; the sweep is worth running only
      because it is.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) COST DIVERGENCE, RE-ESTABLISHED. K a number field of degree n and
      class number h, O its ring of integers, greedy = cold D-DYN (the
      least-norm lambda-growing move), LOCK = bounded-cost tail. Suppose
      infinitely many moves cost <= B.
        (1a) THE PIGEONHOLE MOVES FROM PLACES TO IDEALS. Each multiplier
        is a principal ideal of norm <= B, and a number field has
        finitely many ideals of norm <= B, so ONE ideal A = (alpha0) of
        norm <= B is the multiplier at infinitely many times. Every place
        of A is therefore deepened infinitely often. This is the whole
        repair: the ideal world pigeonholes over PLACES of bounded norm,
        the element world over IDEALS of bounded norm, and both sets are
        finite for the same reason.
        (1b) SOME PLACE OF A TICKS AND OWNS INFINITELY OFTEN. Greedy only
        makes lambda-growing moves, so each application of A grows
        lambda; lambda is the lcm of the columns, so the growth is a tick
        at some place of A owning its characteristic's valuation at that
        moment. A has finitely many places, so one place P | A, of
        residue characteristic p, ticks-and-owns infinitely often.
        (1c) THE ALWAYS-AVAILABLE MOVE SURVIVES PRINCIPALITY. P's depth
        goes to infinity, hence past theorem A's local threshold
        b > e_P/(p-1), past which each e_P of further depth is exactly
        one lambda_p-tick. So A^(e_P) is a legal element move at EVERY step,
        at the constant cost C = N(A)^(e_P), raising P's column p-part by
        one: whenever P owns v_p(lambda), it is lambda-growing and greedy
        pays at most C. The ideal world got this from P^e alone; here the
        constant-price always-available move is a power of the recurrent
        BUNDLE.
        (1d) OWNERSHIP IS NOT TAKEN BACK CHEAPLY, AND GREEDY NEVER PAYS
        DEARLY TO TAKE IT. Fix n0 late enough that P is past threshold
        and p^(v+1) > C, v = v_p(lambda) at n0; just after A is applied
        at n0, P owns v_p. Ownership can pass only three ways, and NONE
        of them escapes a bounded price. To a carrier Q not over p
        already held: its p-part is frozen at opening (lambda(Q^b) =
        lcm(N(Q)-1, E_Q(b)) with E_Q a power of Q's own residue
        characteristic, so only N(Q)-1 carries p), and P's own p-part
        passes it in finitely many A-applications. To a FRESH carrier off
        p: owning v_p there demands p^(v+1) | N(Q)-1, hence a norm above
        p^(v+1) > C, and greedy never buys that while a C-priced growing
        move is live. To another place P' OVER p -- the one transfer that
        can actually happen, and it needs no argument about how P' got
        there, since a place over p offers its own lambda-growing move at
        a CONSTANT price: the class-order power N(P')^m <= p^(n*h), the
        element world's reading of theorem B's recurrent p^rank. So the
        owner of v_p is, from n0 on, always one of the finitely many
        places over p, each of them selling a growing move at a fixed
        price, and every move costs at most max(C, p^(n*h)): a
        bounded-cost tail, i.e. a LOCK, contradicting non-lock. Hence
        cost_n -> infinity along a non-locking element trajectory. The
        repair costs ONE constant, and it is a field constant rather than
        a p-dependent one.
  (2) THE DOOR CONSTANT, DEFINED EXACTLY. tau_K = max over ideal classes
      c of min{N(a) : a in c}. Then the element door is at most
      tau_K * p^(v+2); tau_K = 1 iff h = 1 (a class of least norm 1 is
      the principal class); and tau_K is at most the Minkowski bound,
      which is where a bound rather than a value comes from.
  (3) THE LOOSENED CAP. A carrier Q is affordable when its element cost
      undercuts the door. Its element cost is at least N(Q) -- it may
      itself pay a principalization tax the door has already paid -- so
      the LOOSEST reading, and hence an upper bound on the supply, is
      N(Q) < tau_K * p^(v+2). With N(Q) = m*p^(V+1)+1 that gives
      m < tau_K * p, against the ideal world's m <= p-1. The supply at
      rung V is therefore

          supply(p, V, tau) = {m*p^(V+1) + 1 : 1 <= m <= tau*p - 1}

      exactly, for integer tau. Multipliers divisible by p are kept: they
      deliver a valuation rise of 2 or more rather than 1, which
      over-delivers on the rung's demand, and dropping them would tighten
      a supply this rig wants loose.
  (4) PARITY STILL HALVES IT. For odd p, p^(V+1) is odd, so
      m*p^(V+1)+1 is even exactly when m is odd, and an even prime power
      is a power of 2. So the effective supply is the floor(tau*p/2)-ish
      even multipliers plus a thin exceptional set, whatever tau is --
      the loosening buys the ladder tau times the candidates and the same
      one-half discount.
  (5) tau_K FOR AN IMAGINARY QUADRATIC FIELD, WITH NO SLACK. The classes
      of the maximal order of discriminant D < 0 correspond to reduced
      forms (a,b,c), b^2-4ac = D, |b| <= a <= c (b >= 0 when |b| = a or
      a = c), and the least norm represented in a class is the reduced
      form's a. So tau_K = max a over reduced forms, and a <= sqrt(|D|/3)
      is the reduction bound. At D = -23 the reduced forms are (1,1,6)
      and (2,+-1,3), so h = 3 and tau_K = 2 -- against a Minkowski bound
      of 3.05. RESIST reading that 2 into the element census's 4/move
      against an ideal price of 2: those agree by COINCIDENCE at this
      field. The census's factor is the tail's VEHICLE menu, the rational
      (p) at norm p^min(fm,n) = p^n = 4 (explore_module_law.py finding 4),
      a lock price; tau_K is the padding on a DOOR at a rank-1 place. Two
      quantities, two mechanisms, equal here and not in general.

PREDICTIONS (fixed before any engine code beyond the timing probe noted
under HOW THIS RIG GOT HERE, which is where E5's standing comes from).

  E1 (POSITIVE CONTROL, the test). The prime-power test agrees with a
     brute trial-division test on every integer below AGREE_LIMIT, and
     decides a hand-built large specimen q^2 that trial division over the
     wheel cannot certify. KILL: any disagreement below AGREE_LIMIT -- a
     false death would report the boundary closed where it is open, which
     is the failure mode this rig has to fear most.
  E2 (POSITIVE CONTROL, the tau = 1 walk). At tau = 1 this rig reproduces
     explore_cascade_chars.py's published deaths exactly: D(3) = 2,
     D(5) = 3, D(19) = D(23) = 1, D(17) = 2, D(29) = 8, D(101) = 10,
     D(151) = 12, D(751) = 33, D(997) = 45, D(719) = 62 = max D, and no
     odd prime below 1000 still climbing. KILL: any published death
     moves -- the loosened walk would then not be the same walk.
  E3 (POSITIVE CONTROL, the class-group instrument). Reduced-form
     enumeration gives h(-4) = 1, h(-15) = 2, h(-20) = 2, h(-23) = 3,
     h(-163) = 1; tau_K(-23) = 2; and across the whole discriminant sweep
     tau_K = 1 exactly at h = 1 (a theorem, so a control and not a
     finding). KILL: any of these.
  E4 (THE QUESTION; rule in range if it holds). At tau = 2, 3 and 4,
     every odd prime p below that tau's sweep bound has a certified death
     rung below RUNG_CAP. OBSERVABLE: the printed count of primes still
     climbing at the cap, per tau. KILL: that count is nonzero at any
     tau -- the deaths stop being generic under the loosening, the
     element-world statement would not be the ideal-world one with a
     constant attached, and the /growth/fields sweep block would owe an
     explicit statement of which world it lives in.
  E5 (THE MARGIN, and it carries no verdict AND no evidential weight).
     D_tau(p)/D_1(p) is near tau, within [tau/2, 2*tau] for every p.
     OBSERVABLE: the violation count and the extreme ratios. This
     prediction was formed AFTER the timing probe printed max-D at
     P <= 400, so it is scored and never counted; see HOW THIS RIG GOT
     HERE.
  E6 (THE PARITY LAW AT EVERY tau). Every accepted odd-multiplier carrier
     is a power of 2, at tau = 1, 2, 3 and 4. OBSERVABLE: the printed
     accepts with their splittings. KILL: an accepted odd-m carrier that
     is not a power of 2 -- hand-derivation (4) would be wrong.
  E7 (THE FIELD CENSUS; observation, no kill). Over the fundamental
     discriminants down to -D_MAX, the fraction of fields with
     tau_K <= 4 says how much of the imaginary quadratic world the
     sweep's tau range actually reaches, and the fraction with h = 1 says
     how much of it the ideal-world walk already covered.

WHAT A CLEAN RUN BUYS. Hand-derivation (1) carries the reduction's step
(1) into the element world, (2)-(3) carry step (2) and loosen step (3),
and a clean E4 walks the loosened ladder to its death at every odd
characteristic below that tau's own bound. Together those close the
cascade boundary in the ELEMENT world of a char-0 ring holding a rank-1
characteristic below the bound BELONGING TO ITS OWN tau -- 1000 at
tau_K <= 2, 700 at 3, 500 at 4, the bound falling exactly where the ring
needs it most -- against an ideal-world close that reached the element
world only at h = 1. Reading tau_K there is the safe direction, tau_P at
the place being at most it. What it does not buy: the ladder's death is
still certified per rung by arithmetic rather than proved
(explore_cascade_chars.py hand-derivation (4) is unchanged by the
loosening), each sweep is an initial segment, and tau_K > 4 is
untouched.

FINDINGS (run record at bottom; all sections assert; copied from run
output only).

  1. THE DEATHS SURVIVE THE LOOSENING, AND THE KILL-SHAPE MISSED (rule in
     range; E4 clean at every tau). At tau = 2 all 167 odd primes below
     1000 still reach a certified death rung -- the ideal world's close,
     bound for bound. At tau = 3 all 124 below 700; at tau = 4 all 94
     below 500. The ladder is not saved by the loosening: it is DELAYED
     by it, the death rung deepening by roughly a factor of tau (mean
     D_tau/D_1 = 1.97, 2.82, 3.61 at tau = 2, 3, 4) and always arriving.
     Each of those means is taken over its OWN tau's swept range, so they
     summarise three walks and are not a controlled series in tau; the
     probe's equal-range clock, 1.5 / 12.6 / 48.0 / 88.9 s at p <= 400,
     is the one measurement here that does hold the range fixed.
     The maxima move with it: 62 at p = 719 (tau = 1) becomes 116 at
     p = 859 (tau = 2), and 137 at p = 499 (tau = 4). So the element
     world's statement IS the ideal world's with a constant attached,
     over the range swept.

  2. tau_K MEASURED RATHER THAN BOUNDED, AND AT K23 IT IS 2 (rule; the
     reduced-form instrument, controlled at five known class numbers).
     Q(sqrt(-23)) has reduced forms (1,1,6) and (2,+-1,3), so h = 3 and
     tau_K = 2 exactly, against a Minkowski bound of 3.05. The working
     constant is the measurement, not the bound, and a smaller tau is
     directly a stronger close. It is NOT the element census's 4/move
     against an ideal 2, however nearly that reads: that factor is the
     tail's vehicle menu (the rational (p) at p^min(fm,n) = p^n = 4,
     explore_module_law.py finding 4), a lock price rather than a door's
     padding. The two agree at this field and have no reason to in
     general -- p^(n-ef) is a splitting fact and tau_K a class-group
     one.

  3. BUT tau_K GROWS LIKE THE DISCRIMINANT'S ROOT, so a wider sweep is
     the wrong instrument for the rest (observation; 305 fundamental
     discriminants down to -1000). Mean tau_K = 9.58, largest 17 at
     D = -935 (h = 28), and the fraction of fields the swept range
     reaches is small and falling: tau_K <= 2 at 6.2% of them, <= 4 at
     11.8%. The reduction bound tau_K <= sqrt(|D|/3) is the shape of it.
     And Minkowski is NOT the slack: tau_K/Minkowski averages 0.705 and
     reaches 0.907, so the bound tracks the value to within about 40%
     and the constant genuinely grows. Raising tau buys a shrinking
     fraction of fields per unit of a cost that grows like tau cubed.

  4. THE COVERAGE MEASURE IS PER-PLACE, AND IT COLLAPSES AT A PRINCIPAL
     ONE -- so finding 3 measures the wrong thing (rule, proved by hand;
     derived AFTER the slate froze, so it predicted nothing and the run
     tests it nowhere). The door at characteristic p pads P^(v+2) by an
     ideal of class [P]^-(v+2), so the constant that actually applies
     there is tau_P = max over k of the least norm in [P]^-k, which is at
     most tau_K and is 1 exactly when P is PRINCIPAL. At a principal
     rank-1 place the door costs p^(v+2) on the nose and the ideal
     world's cap m <= p-1 holds verbatim. Since ONE characteristic closes
     a ring (the conjunction), the tau = 1 walk already closes the ELEMENT
     world of every char-0 ring holding a principal rank-1 place below
     1000 -- strictly more rings than the PIDs the ideal-world scope
     reached, and reached without any loosening at all. Principal
     degree-1 places are those splitting completely in the Hilbert class
     field, so they carry POSITIVE density in every number field, and
     1/(h*n) exactly when K/Q is Galois -- H/Q is Galois only then, so
     the clean constant is the quadratic case's and not the general one.
     The only question left is how far down the first one sits. That is the
     quantity a coverage census should have measured, and it is not this
     rig's.

  5. THE PARITY LAW IS INDEPENDENT OF tau (E6). Across every rung of
     every ladder at all four tau, the accepted odd-multiplier carriers
     number TWO, and they are the same number twice: 64 = 2^6 at p = 3,
     V = 1, m = 7, once at tau = 3 and once at tau = 4. So the loosening
     hands the ladder tau times the candidates and the same one-half
     discount, and the effective supply stays the even multipliers.

RUN RECORD. 27/27 checks pass. Peak working set 13.5 MB against the
512 MB ceiling, wall 1064.9 s under memwatch.py (E1's brute control and
E3/E7's 305-field census are seconds; the sweep is 40.7 s at tau = 1,
391.9 s at tau = 2, 340.4 s at tau = 3, 291.8 s at tau = 4 -- the per-tau
bounds doing exactly the job they were set for). AGREE_LIMIT = 50,000,
RUNG_CAP = 500, D_MAX = 1000, TAU_PMAX = {1: 1000, 2: 1000, 3: 700,
4: 500}.

HOW THIS RIG GOT HERE. Three things, none visible in the code, and the
first two bear on how much E4 is worth.

  THE SWEEP BOUNDS WERE SET BY WALL-CLOCK, AND E4 HAD ALREADY BEEN SEEN
  BELOW THEM. A timing probe ran before the slate froze -- the walk's
  cost had to be sized before any bound could be chosen -- and it printed
  the alive-count as well as the clock, at every tau for p <= 400 and, on
  a second timing pass, at tau <= 3 for p <= 700. So E4's content is
  ALREADY OBSERVED there, and what this rig's bounds genuinely add is
  400 < p <= 1000 at tau = 2, 400 < p <= 700 at tau = 3, and
  400 < p <= 500 at tau = 4. E5, formed after those probes printed their
  max death rungs, is a description and not a prediction, which is why it
  is scored and never counted. What the bounds cannot be is
  verdict-selected: they were fixed from the clock BEFORE this run, and no
  probe at any bound ever produced a survivor, so there was never an
  unsettled prime for a bound to be drawn around. Note which way the
  probed regions sit -- a SUBSET of the bound at tau = 2 and tau = 4,
  coinciding with it at tau = 3 -- so at two of the three the stretch the
  bound genuinely adds was settled by this run and by nothing earlier.

  A FLAT BOUND WAS TRIED FIRST AND COST TWO HOURS FOR NOTHING. The first
  attempt swept every tau to 1000 and ran 6833 s (peak working set
  14.4 MB, so the ceiling was never in question) -- and its stdout was
  lost to a pipe, so the run bought no numbers at all. The lesson that
  survives is about the cost law rather than the plumbing: the walk grows
  like the cube-and-a-half of the sweep bound and roughly the cube of
  tau, so a bound flat in tau spends nearly all of its time on the tau = 4
  tail. Hence TAU_PMAX.

  THE EXPONENT CAP IS SOUND AND IT IS NOT WHAT MADE THE RIG AFFORDABLE.
  Diagnosing that first run, the perfect-power loop looked like the cost:
  it sweeps exponents to bit_length, ~2500 integer roots per candidate at
  these depths, where the wheel already bounds the exponent by
  bit_length/9. Capping it changed the clock by nothing measurable --
  for large exponents the root is 1 or 2 and Newton converges at once, so
  those iterations were already free. The cap stays because it is correct
  and tight, and it is recorded here because the diagnosis it came from
  was WRONG: the cost is Miller-Rabin on candidates that reach 500 digits,
  and no rearrangement of the roots touches it.
"""

import os
import sys
import time
from math import gcd, isqrt, log, sqrt

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_bridge_reach as BR

PASS = []


def ok(cond, label):
    PASS.append(bool(cond))
    print(f"    [{'PASS' if cond else 'FAIL'}] {label}")


# ---------------------------------------------------------------- primitives

def integer_root(n, a):
    """Largest r with r^a <= n. EXACT and float-free: the carriers here
    run past 10^60, where float(n) is lossy or an OverflowError, so the
    seed comes from the bit length and the refinement is integer Newton."""
    if a == 1:
        return n
    if a == 2:
        return isqrt(n)
    r = 1 << (n.bit_length() // a + 1)
    while True:
        nxt = ((a - 1) * r + n // r ** (a - 1)) // a
        if nxt >= r:
            break
        r = nxt
    while r ** a > n:
        r -= 1
    while (r + 1) ** a <= n:
        r += 1
    return r


# One gcd against this primorial replaces hundreds of trial divisions. It
# cannot reject a prime power whose base is inside the wheel, so the wheel
# primes are re-checked as bases before a candidate is discarded.
WHEEL = [q for q in range(3, 1000) if BR.is_primeZ(q)]
WHEEL_PRODUCT = 1
for _q in WHEEL:
    WHEEL_PRODUCT *= _q


def _power_of(n, q):
    """-> a if n = q^a exactly (a >= 1), else None."""
    a = 0
    while n % q == 0:
        n //= q
        a += 1
    return a if n == 1 else None


def is_prime_power(n):
    """-> (True, 'q^a') if n = q^a with q prime and a >= 1, else
    (False, None). Primality plus exact integer roots plus a small-prime
    wheel; never a full factorization, so it is sound at any size.

    WHY THE DEATH CERTIFICATE IS A PROOF AND SURVIVAL IS NOT, which is
    the direction this rig needs: BR.is_primeZ is Miller-Rabin over fixed
    bases, so a COMPOSITE verdict exhibits a witness and is a proof while
    a PRIME verdict is probable-prime only. A death rung is a conjunction
    of composite verdicts plus exact not-a-perfect-power, hence certified;
    a surviving rung rests on a probable prime, which can only make a
    ladder look LONGER. Both errors point away from a false death."""
    if n < 2:
        return False, None
    if n % 2 == 0:
        a = _power_of(n, 2)
        return (True, f"2^{a}") if a else (False, None)
    g = gcd(n, WHEEL_PRODUCT)
    if g > 1:
        q = next(q for q in WHEEL if g % q == 0)
        a = _power_of(n, q)
        return (True, f"{q}^{a}" if a > 1 else str(q)) if a else (False, None)
    if BR.is_primeZ(n):
        return True, str(n)
    # THE EXPONENT IS BOUNDED BY THE WHEEL, and this is the whole cost of
    # the rig. Reaching here means n is coprime to every prime below 1000,
    # so any prime factor exceeds 2^9; q^a <= n therefore forces
    # a <= bit_length(n)/9. Sweeping a to bit_length instead -- which is
    # what a test written without the wheel in view does -- takes ~250x
    # the integer-Newton roots per candidate at the depths this sweep
    # reaches, and the roots are where the time goes.
    for a in range(2, n.bit_length() // 9 + 2):
        r = integer_root(n, a)
        if r < 2:
            break
        if r ** a == n and BR.is_primeZ(r):
            return True, f"{r}^{a}"
    return False, None


def brute_prime_power(n):
    """Independent decision by full trial division. Small n only; the E1
    control's job is to be slow and obviously right."""
    if n < 2:
        return False
    q = 2
    while q * q <= n:
        if n % q == 0:
            while n % q == 0:
                n //= q
            return n == 1
        q += 1
    return True


def supply(p, V, tau):
    """The affordable carriers at rung V under a door loosened by tau."""
    base = p ** (V + 1)
    return [m * base + 1 for m in range(1, tau * p)]


def death_rung(p, tau, rung_cap):
    """First rung V >= 1 at which every candidate in supply(p, V, tau) is
    a certified non-prime-power. -> (V, misses, odd_hits), or
    (None, None, odd_hits) if still climbing at rung_cap.

    Odd p only: the budget inequality pins the rise at one, so the
    valuation and the rung index coincide and the walk is a scan. EVERY
    candidate at every rung is tested, not only up to the first hit --
    E6 needs the odd-multiplier accepts, and stopping early would make
    that list a function of multiplier ORDER rather than of the supply.
    The death verdict is unaffected: an all-miss is an all-miss."""
    odd_hits = []
    for V in range(1, rung_cap + 1):
        base = p ** (V + 1)
        hit = False
        for m in range(1, tau * p):
            n = m * base + 1
            pp, split = is_prime_power(n)
            if pp:
                hit = True
                if m % 2 == 1:
                    odd_hits.append((p, V, m, n, split))
        if not hit:
            return V, supply(p, V, tau), odd_hits
    return None, None, odd_hits


# ------------------------------------------------- the class-group instrument

def reduced_forms(D):
    """Every reduced primitive positive-definite form (a,b,c) of
    discriminant D < 0: b^2 - 4ac = D, |b| <= a <= c, and b >= 0 when
    |b| = a or a = c. The list IS the class group of the order, one form
    per class, and a is the least norm represented in that class."""
    out = []
    a = 1
    while 3 * a * a <= -D:
        for b in range(-a, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a:
                continue
            if gcd(gcd(a, b), c) != 1:
                continue
            if (abs(b) == a or a == c) and b < 0:
                continue
            out.append((a, b, c))
        a += 1
    return out


def is_fundamental(D):
    """D < 0 is a fundamental discriminant: D = 1 mod 4 squarefree, or
    D = 4m with m = 2,3 mod 4 squarefree."""
    if D >= 0:
        return False
    if D % 4 == 1:
        return squarefree(-D)
    if D % 4 == 0:
        m = D // 4
        return m % 4 in (2, 3) and squarefree(-m)
    return False


def squarefree(n):
    q = 2
    while q * q <= n:
        if n % (q * q) == 0:
            return False
        q += 1
    return True


def minkowski_bound(D):
    """(2/pi)*sqrt(|D|) for an imaginary quadratic field: n = 2, s = 1,
    (4/pi)^s * (n!/n^n) * sqrt(|D|)."""
    return (4 / 3.141592653589793) * 0.5 * sqrt(-D)


# ------------------------------------------------------------------ constants

AGREE_LIMIT = 50000
RUNG_CAP = 500
# The sweep bound is PER TAU and it is set by wall-clock, not by verdict:
# the walk's cost grows like the cube-and-a-half of the bound and roughly
# the cube of tau (the supply is tau times wider and the death rung
# roughly tau times deeper, and the candidates carry that depth in their
# digits), so a bound that is flat in tau spends hours on the tau = 4 tail
# and minutes on everything else. See HOW THIS RIG GOT HERE for what fixed
# these four numbers and for the bounds at which E4 was already observed.
TAU_PMAX = {1: 1000, 2: 1000, 3: 700, 4: 500}
TAUS = tuple(sorted(TAU_PMAX))
D_MAX = 1000
PUBLISHED = {3: 2, 5: 3, 17: 2, 19: 1, 23: 1, 29: 8, 101: 10, 151: 12,
             719: 62, 751: 33, 997: 45}

print("=" * 72)
print("E1 THE TEST: rebuilt prime-power decision against brute trial division")
print("=" * 72)

disagree = [n for n in range(2, AGREE_LIMIT)
            if is_prime_power(n)[0] != brute_prime_power(n)]
ok(not disagree,
   f"E1: agrees with brute trial division below {AGREE_LIMIT} "
   f"({len(disagree)} disagreements)")

BIG = 10 ** 60 + 7
while not BR.is_primeZ(BIG):
    BIG += 2
BIGPP = BIG ** 2
mine = is_prime_power(BIGPP)
print(f"    large specimen q^2, q = {BIG}: {len(str(BIGPP))} digits")
print(f"      decided: {mine[0]} ({mine[1][:24]}...)")
ok(mine[0] and mine[1] == f"{BIG}^2",
   "E1: the large specimen is decided exactly, with no factorization")

# The exponent cap is the one place a speedup could manufacture a false
# death, so it gets a control of its own: the smallest wheel-coprime
# prime raised to every exponent the cap is supposed to admit, plus the
# neighbours of each such power, which must all be refused.
CAPQ = 1009
capfail = [a for a in range(2, 41)
           if is_prime_power(CAPQ ** a) != (True, f"{CAPQ}^{a}")
           or is_prime_power(CAPQ ** a - 2)[1] == f"{CAPQ}^{a}"]
ok(not capfail,
   f"E1: the exponent cap admits {CAPQ}^a for every a <= 40 and refuses "
   f"its neighbours ({len(capfail)} failures)")

print()
print("=" * 72)
print(f"E3 THE CLASS-GROUP INSTRUMENT: tau_K = max a over reduced forms")
print("=" * 72)

for D, h_want in ((-4, 1), (-15, 2), (-20, 2), (-23, 3), (-163, 1)):
    forms = reduced_forms(D)
    tk = max(a for a, _, _ in forms)
    ok(len(forms) == h_want,
       f"E3: h({D}) = {h_want} (got {len(forms)}), tau_K = {tk}, "
       f"Minkowski {minkowski_bound(D):.2f}, forms {forms}")

fields = []
for D in range(-3, -D_MAX - 1, -1):
    if not is_fundamental(D):
        continue
    forms = reduced_forms(D)
    fields.append((D, len(forms), max(a for a, _, _ in forms)))

ok(all((tk == 1) == (h == 1) for _, h, tk in fields),
   f"E3: tau_K = 1 exactly at h = 1 across {len(fields)} fields")
ok(all(tk <= sqrt(-D / 3) + 1e-9 for D, _, tk in fields),
   "E3: tau_K <= sqrt(|D|/3), the reduction bound")
ok(all(tk <= minkowski_bound(D) for D, _, tk in fields),
   "E3: tau_K <= the Minkowski bound at every field (the bound is sound)")

print()
print("=" * 72)
print(f"E7 THE FIELD CENSUS: imaginary quadratic fields, |D| <= {D_MAX}")
print("=" * 72)
for t in (1, 2, 3, 4, 5):
    n_le = sum(1 for _, _, tk in fields if tk <= t)
    print(f"    tau_K <= {t}: {n_le:>4} of {len(fields)} fields "
          f"({100.0 * n_le / len(fields):5.1f}%)")
worst = max(fields, key=lambda r: r[2])
print(f"    largest tau_K in range: {worst[2]} at D = {worst[0]} "
      f"(h = {worst[1]}); mean tau_K = "
      f"{sum(tk for _, _, tk in fields) / len(fields):.2f}")
_ratios = [tk / minkowski_bound(D) for D, _, tk in fields]
print(f"    ratio tau_K / Minkowski, mean "
      f"{sum(_ratios) / len(_ratios):.3f}, worst {max(_ratios):.3f}")

print()
print("=" * 72)
print(f"E2/E4/E6 THE SWEEP: odd primes at tau -> bound {TAU_PMAX}")
print("=" * 72)

ALL_PRIMES = [p for p in range(3, max(TAU_PMAX.values()) + 1)
              if BR.is_primeZ(p)]
D_of = {}
odd_m_hits = []
for tau in TAUS:
    t0 = time.time()
    odd_primes = [p for p in ALL_PRIMES if p <= TAU_PMAX[tau]]
    deaths, alive = {}, []
    for p in odd_primes:
        D, _, odd_hits = death_rung(p, tau, RUNG_CAP)
        deaths[p] = D
        odd_m_hits.extend((tau,) + h for h in odd_hits)
        if D is None:
            alive.append(p)
    D_of[tau] = deaths
    settled = [p for p in odd_primes if deaths[p] is not None]
    mx = max(settled, key=lambda q: deaths[q]) if settled else None
    print(f"    tau = {tau}: {len(settled)}/{len(odd_primes)} settled "
          f"(p <= {TAU_PMAX[tau]}), max D = {deaths[mx] if mx else '-'} "
          f"at p = {mx}, {time.time() - t0:.1f}s")
    print("      " + ", ".join(f"D({p})={deaths[p]}"
                               for p in (3, 5, 17, 19, 29, 101, 151, 499)))
    if tau == 1:
        for p, want in PUBLISHED.items():
            ok(deaths[p] == want,
               f"E2: tau=1 reproduces D({p}) = {want} (got {deaths[p]})")
        ok(not alive, f"E2: tau=1 has no prime still climbing ({len(alive)})")
    else:
        ok(not alive,
           f"E4: tau={tau} -- every odd prime <= {TAU_PMAX[tau]} has a "
           f"certified death rung ({len(alive)} still climbing at "
           f"V={RUNG_CAP}: {alive[:10]})")

print()
print("=" * 72)
print("E5 THE MARGIN (scored, no verdict, formed after the timing probe)")
print("=" * 72)
for tau in TAUS[1:]:
    rats = [D_of[tau][p] / D_of[1][p] for p in ALL_PRIMES
            if p <= TAU_PMAX[tau] and D_of[tau][p] and D_of[1][p]]
    viol = [r for r in rats if not (tau / 2 <= r <= 2 * tau)]
    print(f"    tau = {tau}: mean ratio {sum(rats) / len(rats):.2f}, "
          f"range [{min(rats):.2f}, {max(rats):.2f}], "
          f"{len(viol)} outside [{tau / 2:.1f}, {2 * tau}]")

print()
print("=" * 72)
print("E6 THE PARITY EXCEPTIONS: accepted odd-multiplier carriers")
print("=" * 72)
print(f"    {len(odd_m_hits)} accepted odd-m carriers below the death rungs, "
      f"over all tau")
for tau, p, V, m, n, split in odd_m_hits[:20]:
    print(f"      tau={tau} p={p} V={V} m={m}: {str(n)[:40]} = {split}")
ok(all(split.startswith("2^") or split == "2"
       for _, _, _, _, _, split in odd_m_hits),
   "E6: every accepted odd-multiplier carrier is a power of 2, at every tau")

print()
print("=" * 72)
print(f"{sum(PASS)}/{len(PASS)} checks pass")
print("=" * 72)
