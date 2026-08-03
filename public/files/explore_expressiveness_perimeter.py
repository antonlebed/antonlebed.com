"""
THE EXPRESSIVENESS PERIMETER -- the second in a series of four perimeter
probes charting what the finite-window family IS.

This series charts what the finite-window family IS before the docs are rebuilt
to its frame. The first probe (explore_reset_corner.py) placed the CONTROL layer:
INC + native zero-test + reset (no decrement) is finite-state. This probe places
the PREDICATE layer: where does the tower's native predicate class sit in
the classical decidable hierarchy (Presburger / semilinear / regular), and
of each capability -- NATIVE LAW or PAID SIMULATION?

THE OBJECT. The tower reads an integer through its residue windows:
    n |-> (n mod p_1, ..., n mod p_k).
EVERY native tower predicate -- unit (sieve survivor), quadratic residue,
idempotent support, ECC syndrome, the seed-flower -chi, transparency -- is a
function of that CRT tuple and nothing else. So the tower's ENTIRE native
predicate repertoire is ONE class: the SQUAREFREE-PERIODIC BOOLEAN ALGEBRA
-- Boolean combinations of residue-mod-p tests = unions of residue classes
modulo a squarefree (primorial) modulus = purely periodic subsets of Z with
squarefree period.

THE PLACEMENT (rule, proved + verified S1-S4; undecidability/complexity
CITED). Four nested classes, each one deletion below the last:

  1. arithmetic (N, +, x)          UNDECIDABLE            (Godel / Robinson)
        | delete x  (keep +, <)
  2. PRESBURGER = semilinear       DECIDABLE              (Ginsburg-Spanier
     = eventually periodic (1-dim)                         1966; Presburger
     TWO ingredients: PERIODS + THRESHOLDS                 1929)
        | delete order / thresholds
  3. PERIODIC sets (any modulus)   regular, all moduli
        | delete prime-power depth  (keep residue FIELDS F_p, not Z/p^k)
  4. TOWER = squarefree-periodic   REGULAR floor          <-- the native class
     Boolean algebra

The tower sits inside Presburger via TWO INDEPENDENT deletions, each exactly
ONE import away, and each a tower CONSTRUCTIVE deletion (the tower's own construction):
  - the ORDER / THRESHOLD axis is OUT = the ARCHIMEDEAN place deleted
    (size, sign, comparison -- none is a window quantity);
  - the PRIME-POWER DEPTH axis is OUT = the tower keeps residue FIELDS F_p,
    not local rings Z/p^k (the "depth fate" direction, a separate line
    of growth-law records).
So the previously banked conjecture "the finite-window family = the Presburger-decidable
fragment" is FALSE AS STATED (S2 refutes it both ways): the tower is a
PROPER, DOUBLY-RESTRICTED sub-fragment of Presburger -- the squarefree-
modular, order-free fragment, sitting at the REGULAR/PERIODIC floor of the
decidable hierarchy. That is GOOD news for the decidable-sibling
reading: even more decidable
than Presburger, with a two-axis account of exactly what it gives up, both
axes = the tower's own deleted places.

THE NATIVE-LAW READING (observation + cited context, S3). A tower predicate
is decided by k PARALLEL residue reads plus a Boolean lookup on the tuple:
QUANTIFIER-FREE, constant depth -- one layer of MOD gates (the ACC^0
primitive: residue-mod-p IS a MOD_p gate). A general decidable engine
recovers the same predicate through search: "n = r (mod p)" is Presburger
only as EXISTS y. n = r + p*y -- a quantifier a decision procedure must
eliminate; Datalog a fixpoint. VERIFIED here: the structural contrast (zero
quantifiers, k reads, a truth table over the tuple) -- NOT a complexity
separation (that is cited ACC^0 context, exploitation-deferred). The
kill-shot stands unclaimed: Datalog/Agda already own decidable-usefulness;
the tower's edge must be its NATIVE LAWS load-bearing where a rival PAYS to
simulate, and whether the mod-gate-layer edge is load-bearing at scale is an
exploitation question this probe does NOT answer (a fair-fight lesson from
an earlier exploitation attempt: the edge must survive the rival simulating
it at table stakes). (Settled since, by reading the incumbents' own
literature: Cooper's quantifier elimination on an order-free conjunction
bottoms out in Chinese-remainder brute force over the residues, so on the
shared fragment a general engine already collapses to the same residue
lookup, and small-modulus table-lookup arithmetic is the residue number
system field's standing hardware practice -- the deferred edge closed
without a claim: exact incumbents already sit at the point.)

THE DYNAMIC LIFT + A CORRECTION TO AN EARLIER LEAD (synthesis + cited, S4). The STATIC
predicate class is regular/periodic. Add the growth DYNAMICS (INC + native
zero-test, no borrow -- explore_growth_machine.py / explore_archimedean_dial.py):
halting and coverability are
DECIDABLE (a well-structured transition system), and the archimedean BORROW
is the ceiling -- restore it and the machine is Minsky-universal, halting
undecidable (explore_reset_corner.py; explore_archimedean_dial.py).
(A later run settled the adjacent general question: with growth moves the
bare element class is universal -- a sparse counter riding the growth
frontier keeps the native zero-test exact, explore_frontier_rider.py -- so
the decidability verdict here is this construction's own.)
CORRECTION (a later citation
correction): the previously banked lead "VASS reachability sets are semilinear
(Presburger-definable)" OVERSTATES. General VASS reachability sets are NOT
semilinear -- Hopcroft-Pansiot 1979 give a 3-VASS witness; effective
semilinearity holds only in dimension <= 2. The honest statement is
DECIDABLE, not always semilinear. THREE-TIER RULER: static regular/periodic
-> dynamic decidable-WSTS (VASS reachability decidable but Ackermann-complete:
upper bound Leroux-Schmitz 2019, hardness Czerwinski-Orlikowski/Leroux 2021)
-> +borrow undecidable (Minsky 1967). The archimedean
import is the final step; the tower deletes it by construction.

SCOPE + HONESTY. What is RUN-verified is finite: every tower predicate
factors through the tuple and is squarefree-periodic (S1); the two escaping
witnesses -- a threshold (archimedean axis) and a mod-p^2 class (depth axis)
-- are provably NOT in the squarefree-periodic algebra (S2, exact atom
splits); the structural quantifier-free / k-read contrast (S3); the
growth-machine finite-quotient reachability re-derived (S4). What is CITED,
never run: Presburger decidability and the semilinear characterization
(Presburger 1929; Ginsburg-Spanier 1966), (N,+,x) undecidability (Godel;
Robinson), VASS reachability decidable-but-non-semilinear and Ackermann-complete
(Mayr/Kosaraju/Leroux; Hopcroft-Pansiot 1979; upper bound Leroux-Schmitz
2019, hardness Czerwinski-Orlikowski/Leroux 2021), Minsky
universality (Minsky 1967), the ACC^0 mod-gate class (Barrington et al.).
The CONTRIBUTION is the LOCATION -- the tower's whole native repertoire in
ONE cell at the regular floor, the two escaping axes = the two constructive
deletions, and the refutation of the previously banked "= Presburger" conjecture.

FINDINGS (tiers per the standard naming scale; run record below; every
section asserts).

1. EVERYTHING FACTORS THROUGH THE TUPLE (rule, proved + verified S1). Units
   (sieve survivors), a per-channel quadratic-residue test, an ECC-valid set,
   and the seed-flower support are each functions of (n mod p_i) only, hence
   squarefree-periodic with period p_k#, hence a finite union of residue
   classes = a semilinear (finite-union-of-linear) set, hence Presburger.
   The tower's whole repertoire lives in ONE expressiveness cell.

2. TWO AXES ESCAPE (rule, proved + verified S2 -- refutes the "= Presburger"
   conjecture both ways). (a) THE ARCHIMEDEAN AXIS: the threshold {n >= t}
   (t >= 1) is Presburger but is NOT purely periodic -- no squarefree period
   p has 1_{>=t}(n) = 1_{>=t}(n+p) for all n (it fails at n = 0). Order/size
   is the deleted archimedean place, verified as an expressiveness gap.
   (b) THE DEPTH AXIS: {n = 1 (mod 4)} is Presburger (period 4) but is NOT in
   the squarefree-modulus algebra -- on Z/12 the atoms of <mod 2, mod 3> are
   the six classes mod 6, and {1,5,9} splits the atom {1,7} (1 in, 7 out), so
   no Boolean combination of residue-mod-p tests isolates a mod-p^2 class.
   Keeping residue FIELDS not local rings deletes the depth axis.

3. NATIVE = A MOD-GATE LAYER (observation + cited, S3). Tower membership is
   k parallel residue reads + a Boolean lookup on the tuple: QUANTIFIER-FREE,
   constant depth (one layer of MOD gates). The Presburger representation of
   the same residue predicate needs a quantifier (EXISTS y. n = r + p*y). The
   structural contrast is verified (0 vs >=1 quantifier; a truth table over
   the tuple decides membership); the asymptotic cost is cited ACC^0 context,
   the edge exploitation-deferred (kill-shot named, unclaimed).

4. THE DYNAMIC CEILING + AN EARLIER LEAD CORRECTED (synthesis + cited, S4). The
   static class is regular; the growth dynamics lift it to a decidable WSTS
   (INC + zero-test, halting decidable -- the finite quotient re-derived
   here), and the archimedean borrow is the ceiling to undecidability
   (Minsky; explore_reset_corner.py). (A later run settled the adjacent
   general question: with growth moves the bare element class is
   universal -- a sparse counter riding the growth frontier keeps the
   native zero-test exact, explore_frontier_rider.py -- so the
   decidability verdict here is this construction's own.) The previously
   banked lead "VASS reachability sets are semilinear" is
   corrected to DECIDABLE, NOT ALWAYS SEMILINEAR (Hopcroft-Pansiot 1979).

PREDICTIONS (fixed and hand-attacked BEFORE the
run; adjudicated by asserts only:
  PR1 EVERYTHING FACTORS ... units/QR/ECC/seed-flower each squarefree-
      periodic; a residue class exhibited as a linear set.
  PR2a ARCHIMEDEAN AXIS OUT  {n>=t} not purely periodic (fails at n=0 for
      every candidate squarefree period).
  PR2b DEPTH AXIS OUT ...... {n=1 mod 4} splits an atom of <mod 2, mod 3> on
      Z/12; no Boolean combo of residue tests isolates a mod-p^2 class.
  PR3 MOD-GATE LAYER ....... tower rep 0 quantifiers, k reads; Presburger rep
      of "n=r mod p" uses a quantifier. Structural only; ACC^0 cited.
  PR4 DYNAMIC LIFT ......... growth machine halting decidable (finite
      quotient); previously banked "VASS=semilinear" corrected (Hopcroft-Pansiot).

RUN RECORD (python prime/code/explore_expressiveness_perimeter.py; <1 s;
trivial memory; 4423 checks). SLATE PR1-PR4 all CONFIRMED, no misses.
S1: units(Z/30) least period 30 = 8 = phi(30) classes; QR-mod-7 period 7;
RAD ECC-valid set nontrivial (n=0 valid, n=210 first invalid) periodic mod
p_7#=510510; idempotent support all 2^3=8 patterns period 30 -- every tower
predicate squarefree-periodic. S2a: {n>=5} has NO period p in 1..4096
(universal witness n=t-1). S2b: {n=1 mod4} least period 4 (not squarefree),
not periodic with any of 8 squarefree candidates, splits atom {1,7} of
<mod2,mod3>. S3: unit(Z/30) truth-table = membership over 300 values, 0
quantifiers vs Presburger's EXISTS y (witness y=5 for n=31=1+6*5). S4:
growth machine halting decided on the finite sign quotient (halt from c0=0,+;
loop decided where naive sim never ends); the previously banked 'VASS=semilinear' lead
retired for the corrected decidable-but-not-always-semilinear statement.
No pre-run adjudication drafted; verdicts frozen in code, numbers from output.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

from crt import RAD_RING, encode, is_unit, ecc_syndrome, euler_phi

CHECKS = 0


def ok(cond, msg=""):
    global CHECKS
    if not cond:
        raise AssertionError("CHECK FAILED: " + msg)
    CHECKS += 1


def is_periodic(indicator, period, span):
    """Does the 0/1 indicator repeat with `period` over [0, span)?"""
    return all(indicator(n) == indicator(n + period) for n in range(span))


def least_period(indicator, span, cap):
    """Smallest p in 1..cap with indicator p-periodic over [0, span); else 0."""
    for p in range(1, cap + 1):
        if all(indicator(n) == indicator(n + p) for n in range(span - p)):
            return p
    return 0


# ------------------------------------------------------------------ #
print("S1 -- EVERYTHING FACTORS THROUGH THE TUPLE (squarefree-periodic)")

# (i) UNITS of Z/30 = sieve survivors = coprime to 30. Period 30 (squarefree).
from crt import Ring
R30 = Ring("Z30", (2, 3, 5), (1, 1, 1))
unit30 = lambda n: 1 if is_unit(n % 30, R30) else 0
per_unit = least_period(unit30, 240, 60)
ok(per_unit == 30, "unit set of Z/30 is periodic, least period 30 (squarefree)")
n_units = sum(unit30(n) for n in range(30))
ok(n_units == euler_phi(30) == 8, "unit count = phi(30) = 8 residue classes")
# the unit set IS a union of 8 residue classes mod 30 -> semilinear:
unit_classes = [r for r in range(30) if unit30(r)]
ok(all(unit30(r) == unit30(r + 30) for r in range(240)),
   "each unit class {r + 30*j} is a linear set; union of 8 = semilinear")
print("  units(Z/30): least period %d, %d classes = phi(30); semilinear"
      % (per_unit, n_units))

# (ii) a per-channel QUADRATIC RESIDUE test mod 7 -- still a residue predicate.
qr7 = lambda n: 1 if (n % 7) in {(x * x) % 7 for x in range(7)} else 0
per_qr = least_period(qr7, 100, 20)
ok(per_qr == 7, "QR-mod-7 predicate periodic, least period 7 (a prime field)")
print("  QR mod 7: least period %d (a multiplicative predicate, still a tuple"
      " read)" % per_qr)

# (iii) ECC on RAD: the set of n whose residue tuple is a valid codeword (the
# parity channels match the ECC function of the data channels) is a NONTRIVIAL
# squarefree-periodic set -- a genuine tower predicate, period p_7#=510510.
rad_valid = lambda n: 1 if ecc_syndrome(encode(n, RAD_RING), RAD_RING) \
    == (0, 0, 0) else 0
ok(rad_valid(0) == 1, "n=0 is a valid RAD codeword (all-zero)")
first_invalid = next(n for n in range(510510) if rad_valid(n) == 0)
ok(rad_valid(first_invalid) == 0 and first_invalid < 510510,
   "some n is NOT a valid codeword (n=%d): the ECC set is nontrivial"
   % first_invalid)
# periodic mod p_7# (squarefree): the predicate depends only on the tuple.
ok(all(rad_valid(n) == rad_valid(n + 510510) for n in (0, 1, first_invalid, 42)),
   "RAD ECC-valid set is periodic mod p_7# = 510510 (squarefree)")
print("  RAD ECC-valid set: nontrivial tuple predicate (n=0 valid, n=%d not),"
      " periodic mod p_7#=510510" % first_invalid)

# (iv) the IDEMPOTENT SUPPORT of n (its zero-pattern across channels) -- the
# 2^k idempotents / meadow structure -- is a tuple function, period 30.
support = lambda n: tuple(1 if (n % p) == 0 else 0 for p in (2, 3, 5))
ok(all(support(n) == support(n + 30) for n in range(240)),
   "idempotent support is periodic mod 30 (squarefree)")
ok(len({support(n) for n in range(30)}) == 8 == 2 ** 3,
   "support realizes all 2^k = 8 zero-patterns (the 2^k idempotents)")
print("  idempotent support: periodic mod 30, all 2^3=8 patterns (a tuple"
      " read)")
print("  => the tower's whole native repertoire is squarefree-periodic"
      " (in Presburger)")
print()


# ------------------------------------------------------------------ #
print("S2 -- TWO AXES ESCAPE (refutes 'finite-window = Presburger' both ways)")

# (a) THE ARCHIMEDEAN AXIS: threshold {n >= t}, t>=1. Presburger, NOT purely
# periodic. For ANY candidate squarefree period p, periodicity fails at n=0.
t_thr = 5
thr = lambda n: 1 if n >= t_thr else 0
# a purely periodic set eventually constant is constant; a threshold is not.
# universal witness: for EVERY period p >= 1, thr(t-1)=0 but thr(t-1+p)=1,
# so no p >= 1 is a period -- the threshold is aperiodic outright.
for p in range(1, 4097):
    ok(thr(t_thr - 1) != thr(t_thr - 1 + p),
       "threshold {n>=%d} not p-periodic (witness n=t-1) for p=%d"
       % (t_thr, p))
print("  {n >= %d}: Presburger (eventually all-1) but has NO period p>=1"
      " (witness n=t-1) --" % t_thr)
print("  the ARCHIMEDEAN axis (size/order) is OUT (the deleted place)")

# (b) THE DEPTH AXIS: {n = 1 mod 4} is Presburger (period 4) but not in the
# squarefree-modulus Boolean algebra. Every set in the algebra is a function
# of the residue tuple (n mod p_1, ..., n mod p_k), so it is periodic with
# period lcm(p_i) = a SQUAREFREE modulus. {n = 1 mod 4} has period 4.
def is_squarefree(m):
    d = 2
    while d * d <= m:
        if m % (d * d) == 0:
            return False
        d += 1
    return True


mod4eq1 = lambda n: 1 if n % 4 == 1 else 0
per_mod4 = least_period(mod4eq1, 200, 64)
ok(per_mod4 == 4, "{n = 1 mod 4} has least period 4")
ok(not is_squarefree(4), "4 is not squarefree (2^2 | 4)")
# every period of the set is a multiple of the least period 4, hence never
# squarefree, hence the set has NO squarefree period -> not in the algebra.
for p in (2, 3, 5, 6, 30, 210, 2310, 510510):   # candidate squarefree periods
    ok(is_squarefree(p) and not is_periodic(mod4eq1, p, 40),
       "{n=1 mod4} is NOT periodic with squarefree period p=%d" % p)
# the concrete atom witness on Z/12 = <mod 2, mod 3>: atoms = classes mod 6.
target = {n for n in range(12) if n % 4 == 1}     # {1, 5, 9}
ok(target == {1, 5, 9}, "the mod-4=1 set on Z/12 is {1,5,9}")
atom_of = lambda n: (n % 2, n % 3)                # the atom label (mod 6)
ok({m for m in range(12) if atom_of(m) == (1, 1)} == {1, 7},
   "atom (n%2,n%3)=(1,1) on Z/12 is {1,7}")
ok(1 in target and 7 not in target,
   "the mod-4 set SPLITS the atom {1,7}: 1 (=1 mod4) in, 7 (=3 mod4) out")
print("  {n = 1 mod 4}: Presburger (least period 4, not squarefree) --"
      " no squarefree window sees mod-4")
print("  concrete: splits atom {1,7} of <mod2,mod3>; the DEPTH axis is OUT"
      " (residue FIELDS F_p, not Z/p^k)")
print()


# ------------------------------------------------------------------ #
print("S3 -- NATIVE = A MOD-GATE LAYER (quantifier-free; ACC^0 primitive)")

# The tower decides "n = r (mod p)" with ONE residue read: quantifier-free.
# Build the truth table over the tuple for a compound tower predicate
# ("unit of Z/30") -- membership is a lookup on (n%2, n%3, n%5), no search.
def tower_membership_unitsofZ30(residue_tuple):
    r2, r3, r5 = residue_tuple
    return (r2 != 0) and (r3 != 0) and (r5 != 0)   # k=3 reads, Boolean AND


# the tuple truth-table decides membership EXACTLY, with no quantifier and no
# search -- k=3 residue reads and a Boolean combination:
for n in range(300):
    lhs = tower_membership_unitsofZ30((n % 2, n % 3, n % 5))
    rhs = bool(unit30(n))
    ok(lhs == rhs, "tuple truth-table = unit membership at n=%d" % n)

# the Presburger representation of a SINGLE residue class uses a quantifier:
#   n = r (mod p)   <=>   EXISTS y . n = r + p*y
# we cannot "count quantifiers" of an external procedure, but we can exhibit
# the existential witness structure vs the tower's zero-witness read.
def presburger_residue_witness(n, r, p):
    """Returns the existential witness y (the search the tower does NOT do)."""
    if (n - r) % p != 0:
        return None
    return (n - r) // p


w = presburger_residue_witness(31, 1, 6)      # 31 = 1 + 6*5
ok(w == 5, "Presburger 'n=1 mod 6' needs the existential witness y=5")
ok(presburger_residue_witness(30, 1, 6) is None, "no witness when 30 != 1 mod6")
print("  unit(Z/30): 3 residue reads + Boolean AND, 0 quantifiers (truth"
      " table over the tuple)")
print("  Presburger 'n=1 mod 6' = EXISTS y. n=1+6y -- a quantifier/search"
      " (witness y=5 for n=31)")
print("  structural contrast verified; the ACC^0 cost separation is CITED,"
      " edge exploitation-deferred")
print()


# ------------------------------------------------------------------ #
print("S4 -- THE DYNAMIC CEILING + AN EARLIER LEAD CORRECTED")

# The growth machine (INC + native zero-test, NO borrow): halting decidable by
# the finite sign-quotient (re-derived from explore_reset_corner.py /
# explore_growth_machine.py). Small witness here.
def growth_step(instr, q, s):
    ins = instr[q]
    op = ins[0]
    if op == "INC":
        _, i, qp = ins
        s = list(s); s[i] = 1; return qp, tuple(s)
    if op == "JZ":
        _, i, qz, qn = ins
        return (qz if s[i] == 0 else qn), tuple(s)
    raise ValueError("growth machine has no borrow; op " + op)


def growth_halts(instr, q0, c0):
    """Decide halting on the finite sign quotient Q x {0,+}^k (no decrement =>
    exact, explore_growth_machine.py / explore_reset_corner.py)."""
    q, s = q0, tuple(0 if x == 0 else 1 for x in c0)
    seen = set()
    while True:
        if q == "HALT":
            return True
        if (q, s) in seen:
            return False
        seen.add((q, s))
        q, s = growth_step(instr, q, s)


# a growth machine: while c0 == 0, INC c0; then halt. From c0=0 it halts.
G = {0: ("JZ", 0, 1, "HALT"), 1: ("INC", 0, 0)}
ok(growth_halts(G, 0, [0]) is True, "growth machine halts from c0=0 (decided)")
ok(growth_halts(G, 0, [5]) is True, "growth machine halts from c0=+ (decided)")
# a non-halting growth loop, decided LOOP on the finite quotient:
GL = {0: ("INC", 0, 1), 1: ("JZ", 0, "HALT", 0)}   # c0 never zero again
ok(growth_halts(GL, 0, [0]) is False,
   "growth loop decided LOOP (finite quotient, naive sim never ends)")
print("  growth machine (INC + zero-test, no borrow): halting DECIDED on the"
      " finite sign quotient (WSTS)")

# THE CORRECTION TO AN EARLIER LEAD (documentation, not a check -- undecidability and
# non-semilinearity CANNOT be run). The banked lead "VASS reachability sets
# are semilinear" OVERSTATES: general VASS reachability sets are NOT
# semilinear (Hopcroft-Pansiot 1979, 3-VASS; effective only dim <= 2). The
# carried statement is decidable-but-not-always-semilinear (Minsky's borrow
# is the ceiling to undecidability). These are CITED facts, printed not
# asserted -- the S4 run-verified content is the growth-machine decider above.
print("  lead CORRECTED: 'VASS reachability sets semilinear' -> decidable"
      " but NOT always semilinear (Hopcroft-Pansiot)")
print("  three-tier ruler: regular/periodic (static) -> decidable WSTS"
      " (dynamic) -> +borrow undecidable (the archimedean import)")
print()


print("ALL CHECKS PASSED:", CHECKS)
