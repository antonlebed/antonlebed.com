"""
THE DECIDABLE-EQUIVALENCE DIVIDEND -- the last in a series of four
perimeter probes charting what the finite-window family IS.

The first probe (explore_reset_corner.py)
placed the CONTROL layer (INC + zero-test + reset = finite-state); the second probe
(explore_expressiveness_perimeter.py) placed the PREDICATE layer (the whole
native repertoire = one squarefree-periodic REGULAR cell, strictly inside
Presburger); the third probe (explore_erasure_ledger.py) placed the PHYSICS (reversible
core, erasure the borrow are two knobs). This probe places the DIVIDEND: the concrete
payoff of refusing the archimedean borrow.

THE SPINE. The tower is the decidable / ultrametric /
non-erasing SIBLING of universal computation. (Since re-scoped: the
DEPTH face -- moduli and their monotone growth -- is the sibling, and
the "not universal" verdicts below are that face's; the ELEMENT class
with growth has since settled universal bare, which touches none of
the canonical forms: explore_frontier_rider.py.) THE DUALITY: a Turing system's
defining artifact is the universal SELF-INTERPRETER (reflection) -- and it PAYS
with undecidable program-equivalence (Rice). The sibling's artifact is the
reverse: DECIDABLE EQUIVALENCE / CANONICAL FORMS -- and it pays with NO
self-reference. You cannot have both: a TOTAL language cannot contain its own
interpreter (diagonalize eval: d(p)=eval(p,p)+1 would force eval(d,d)=eval(d,d)+1
-- cited; total functional programming, D. Turner 2004). The two DIVIDENDS are
dual: Turing = REPRESENTATION-freedom (run anything); the sibling =
VERIFICATION-freedom (canonical forms, decidable equivalence, self-certification,
no halting problem). This probe makes the sibling's dividend CONCRETE for the tower --
three canonical forms it owns BY CONSTRUCTION, and the exact trade.

WHAT IS RUN-VERIFIED (four layers of the same dividend):

  S1  THE ELEMENT NORMAL FORM (rule, verified). The CRT tuple is a UNIQUE normal
      form -- the encode bijection (reversible per explore_erasure_ledger.py, zero erasure). Element equality
      is O(k) componentwise, trivially decidable; a fixed value written as
      different arithmetic expressions normalizes (evaluate -> tuple) to the SAME
      tuple; distinct values differ in >= 1 channel (injectivity). The normal form
      is canonical (one tuple per element) and cheap.

  S2  EXPRESSION/FUNCTION EQUIVALENCE IS DECIDABLE (rule, verified) -- THE
      CONCRETE SIBLING-OF-RICE. Two polynomial expressions over Z/N (native
      +, x, constants) are equal AS FUNCTIONS iff, per channel, they reduce to the
      same function in F_p[x]/(x^p - x): the CANONICAL FORM is the tuple of
      per-field reduced polynomials (degree < p_i each), unique. This is DECIDABLE
      by construction -- where the Turing analogue, program equivalence, is
      UNDECIDABLE (Rice's theorem, cited). The reduction is a ring-hom fact:
      Z/N -> F_p sends n -> n mod p, so f(n) mod p = f_p(n mod p) with f_p = f mod
      p; f == g as functions on Z/N iff f_p == g_p as functions on every F_p; and
      functions on F_p <-> polynomials of degree < p. The exponent rule preserving
      the value at x=0: e >= 1 |-> ((e-1) mod (p-1)) + 1 in [1, p-1], e=0 stays the
      constant 1 (x^{p-1} is NOT the constant 1 as a function -- it is 0 at x=0 --
      the rule dodges that trap). Witness: x^5 and x are the SAME function on Z/30
      (5 == 1 mod (p-1) for p=2,3,5 since p-1 in {1,2,4} all divide 4) but DIFFERENT
      polynomials -- the canonical form catches the equality, brute force over 30
      inputs cross-checks; x vs x^2 differ.

  S3  THE PREDICATE CANONICAL FORM (rule, verified). Native predicates (per
      explore_expressiveness_perimeter.py: squarefree-periodic = REGULAR) have a canonical form -- the least period M'
      plus the accepting residue set within it -- which IS the Myhill-Nerode
      minimal DFA of the (unary, purely periodic) language (cited). Two native
      predicates are equal iff canonical forms match: DECIDABLE. Witness:
      unit(Z/30) written three syntactically different ways (is_unit; coprime to
      2 AND 3 AND 5; De Morgan NOT(mult of 2 OR 3 OR 5)) all canonicalize to
      (M'=30, the 8 units); an inequivalent predicate (coprime to 6 only; divisible
      by 2) gives a different canonical form. Brute-force range cross-check.

  S4  SELF-CERTIFICATION + THE DUALITY/TRADE (synthesis; positive side verified,
      negative side = explore_reset_corner.py / explore_expressiveness_perimeter.py + cited). SELF-CERT (rule, verified): a tower result
      carries its own checkable witness -- the ECC syndrome (C1). Valid iff
      syndrome = 0, checked in O(parity) with NO re-compute and NO trust in the
      producer; corrupt a RAD codeword -> nonzero syndrome (caught), located and
      corrected. THE DUALITY (synthesis, cited): decidable-equivalence is
      MUTUALLY EXCLUSIVE with universal self-interpretation; the tower is verified
      on the decidable-equivalence side (S1-S3, and the deciders are TOTAL -- they
      return a verdict on every input, incl. the hard pairs), so it CANNOT be a
      universal self-interpreter -- exactly consistent with explore_reset_corner.py /
      explore_expressiveness_perimeter.py (not universal,
      one borrow short; the growth machine cannot simulate a universal machine).
      The trade is EXACT: verification-freedom bought with representation-freedom.

THE KILL-SHOT (the FAIR-FIGHT, named + deferred, S4). Decidable equivalence and
canonical forms are a COMMODITY -- regex/minimal-DFA, Datalog, and total proof
assistants (Agda/Coq, Turing-incomplete on purpose) all own them. The tower's
edge is NOT their existence but that its native-arithmetic normal form is the
CRT tuple: O(k) to compare, reversible (explore_erasure_ledger.py), ECC-carrying (S4), wired in BY
CONSTRUCTION rather than computed by a decision procedure. Whether that is
LOAD-BEARING at scale where a rival PAYS to simulate it is an exploitation
question this probe does NOT answer (explore_expressiveness_perimeter.py's
deferred edge; a fair-fight lesson learned from an earlier exploitation
attempt). No edge is claimed here -- this probe establishes the dividend
is REAL and names the fair fight for the exploitation phase. (Settled
since, by reading the incumbents' own literature: the CRT-tuple normal
form is the residue number system's defining lemma, homomorphic-encryption
implementations already run residue decomposition as the standard
representation, and the residue-code revival's own hardware comparison
favors binary-native Reed-Solomon by roughly an order of magnitude in
silicon -- the fight closed without a claim, exact incumbents already at
the point; the compute-through property survives at memory-ECC niche
scale.)

SCOPE + HONESTY. RUN-verified: the element normal form (S1), the per-channel
polynomial canonical form and its function-equivalence decider incl. the x^5=x
witness (S2), the predicate canonical form with three-way syntactic collision +
inequivalent controls (S3), ECC self-certification with corruption caught/located/
corrected + the deciders' totality on a battery (S4). CITED, never run: Rice's
theorem (program equivalence undecidable), the total-language / self-interpreter
impossibility (Turner 2004), Myhill-Nerode minimality of the DFA, and the
Datalog/Agda incumbents. The CONTRIBUTION is the LOCATION of the sibling
dividend -- three canonical forms the tower owns by construction, the trade named
exact, and the fair fight set for exploitation. This probe closes the series.

PREDICTIONS (fixed and hand-attacked BEFORE the run; asserts only).
  PR1 ELEMENT NORMAL FORM ... CRT tuple unique/O(k); expressions of one value
      -> same tuple; distinct values differ in >= 1 channel.
  PR2 SIBLING-OF-RICE ....... per-channel F_p[x]/(x^p-x) canonical form decides
      function-equivalence; x^5 == x on Z/30 (diff polys), x != x^2; Rice cited.
  PR3 PREDICATE CANONICAL ... (least period, accepting set) = minimal DFA; three
      spellings of unit(Z/30) collide; coprime-to-6 / even are distinct.
  PR4 SELF-CERT + DUALITY ... ECC syndrome self-certifies (corrupt->caught/fixed);
      deciders total; decidable-equiv => no self-interpreter (explore_reset_corner.py /
      explore_expressiveness_perimeter.py + cited);
      kill-shot (commodity equivalence) named + deferred.

RUN RECORD (python prime/code/explore_decidable_equivalence.py; <1 s; trivial
memory; 31 checks). SLATE PR1-PR4 all CONFIRMED, no misses.
  S1: value 17 in 4 spellings -> one tuple (1,2,2); 30/30 values distinct normal
      forms (0 collisions, bijection); decode(tuple)=17; equality = O(k) compare.
  S2: x^5 and x are different polynomials but share canonical form
      ((0,1),(0,1,0),(0,1,0,0,0)) = 'x' of degree 1 in each F_p; decision +
      brute agree x^5==x; x != x^2 (both ways); 2x^5+3 == 2x+3; decider TOTAL
      (battery verdicts [False, False, False, True] printed) and SOUND vs brute.
  S3: three spellings of unit(Z/30) (is_unit / coprime-AND / De Morgan) -> one
      canonical (M'=30, accepting = {1,7,11,13,17,19,23,29}, |.|=8=phi(30));
      controls coprime-to-6=(6,{1,5}), even=(2,{0}) decided distinct + brute-
      confirmed.
  S4: RAD data (1,2,3,4) -> codeword, syndrome (0,0,0); flip channel 1 ->
      nonzero syndrome, detected, located (ch 1), corrected back to the codeword;
      the S1-S3 deciders total + consistent (the decidable-equivalence side).
No pre-run adjudication drafted; verdicts frozen in code, numbers from output.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

from crt import (
    Ring, RAD_RING, encode, decode, is_unit, euler_phi,
    ecc_encode, ecc_syndrome, ecc_detect, ecc_locate, ecc_correct,
)

CHECKS = 0


def ok(cond, msg=""):
    global CHECKS
    if not cond:
        raise AssertionError("CHECK FAILED: " + msg)
    CHECKS += 1


# --- polynomial helpers (a polynomial = dict {exponent: coefficient}) --------

def poly_eval(poly, x, mod):
    """Evaluate sum c*x^e mod `mod`."""
    return sum(c * pow(x, e, mod) for e, c in poly.items()) % mod


def canonical_over_field(poly, p):
    """The unique degree-<p representative of `poly` AS A FUNCTION on F_p, i.e.
    its image in F_p[x]/(x^p - x). Exponent rule preserves the value at x=0:
    e>=1 -> ((e-1) mod (p-1))+1 in [1,p-1]; e=0 stays the constant term."""
    vec = [0] * p                      # coefficients of degrees 0..p-1
    for e, c in poly.items():
        c %= p
        if e == 0:
            vec[0] = (vec[0] + c) % p
        else:
            er = ((e - 1) % (p - 1)) + 1
            vec[er] = (vec[er] + c) % p
    return tuple(vec)


def canonical_over_ring(poly, primes):
    """Canonical form over squarefree Z/N = tuple of per-field representatives."""
    return tuple(canonical_over_field(poly, p) for p in primes)


def functions_equal_decision(f, g, primes):
    """Decide f == g AS FUNCTIONS on Z/N by canonical form -- the decision
    procedure (no brute force). TOTAL: returns a bool for any f, g."""
    return canonical_over_ring(f, primes) == canonical_over_ring(g, primes)


def functions_equal_brute(f, g, N):
    """Cross-check: agree at every point of Z/N."""
    return all(poly_eval(f, x, N) == poly_eval(g, x, N) for x in range(N))


# --- predicate-canonical-form helpers (unary periodic language) --------------

def least_period(indicator, span, cap):
    """Smallest p in 1..cap with `indicator` p-periodic over [0, span); else 0."""
    for p in range(1, cap + 1):
        if all(indicator(n) == indicator(n + p) for n in range(span - p)):
            return p
    return 0


def predicate_canonical(indicator, span, cap):
    """Canonical form of a purely periodic native predicate: (least period M',
    the accepting residue set within one period). This IS the Myhill-Nerode
    minimal DFA of the unary language (states Z/M', accepting subset). TOTAL."""
    M = least_period(indicator, span, cap)
    accepting = frozenset(r for r in range(M) if indicator(r))
    return (M, accepting)


def predicates_equal_brute(a, b, span):
    return all(a(n) == b(n) for n in range(span))


# ------------------------------------------------------------------ #
print("S1 -- THE ELEMENT NORMAL FORM (CRT tuple: unique, O(k), decidable)")

R30 = Ring("Z30", (2, 3, 5), (1, 1, 1))
primes30 = (2, 3, 5)
N30 = 30

# a fixed value written three syntactically different ways -> ONE normal form.
v = 17
ways = [17, 12 + 5, 47, (-13) % 30]      # all == 17 (mod 30), spelled differently
tuples = [encode(w % 30, R30) for w in ways]
ok(all(t == tuples[0] for t in tuples),
   "all spellings of the value 17 share one CRT tuple %s" % (tuples[0],))
ok(tuples[0] == (17 % 2, 17 % 3, 17 % 5) == (1, 2, 2),
   "the normal form of 17 is its residue tuple (1,2,2)")
# element equality is O(k) componentwise; decode is its inverse (bijection).
ok(decode(tuples[0], R30) == 17, "decode(normal form) = 17 (bijection, reversible)")

# injectivity: the normal form is UNIQUE -- distinct values differ in >=1 channel.
seen = {}
collisions = 0
for n in range(N30):
    t = encode(n, R30)
    if t in seen:
        collisions += 1
    seen[t] = n
ok(collisions == 0 and len(seen) == N30,
   "all %d values have distinct normal forms (injective: 0 collisions)" % N30)
# element-equality decided in k channel-comparisons, not by re-running anything:
ok((encode(17, R30) == encode(47, R30)) and (encode(17, R30) != encode(18, R30)),
   "element equality = tuple equality (k comparisons), trivially decidable")
print("  value 17: 4 spellings -> one tuple (1,2,2); %d values, 0 collisions"
      " (bijection); equality = O(k) compare" % N30)
print()


# ------------------------------------------------------------------ #
print("S2 -- SIBLING OF RICE: function-equivalence DECIDABLE (per-field canon)")

# THE WITNESS: x^5 and x are the SAME function on Z/30, DIFFERENT polynomials.
f_x5 = {5: 1}
f_x = {1: 1}
ok(f_x5 != f_x, "x^5 and x are DIFFERENT polynomials (as syntax)")
ok(functions_equal_decision(f_x5, f_x, primes30),
   "the decision procedure says x^5 == x as FUNCTIONS on Z/30")
ok(functions_equal_brute(f_x5, f_x, N30),
   "brute force over all 30 inputs confirms x^5 == x")
# the canonical form is the identity monomial in every channel:
cf5 = canonical_over_ring(f_x5, primes30)
cfx = canonical_over_ring(f_x, primes30)
ok(cf5 == cfx, "x^5 and x share the canonical form %s" % (cf5,))
ok(cf5 == ((0, 1), (0, 1, 0), (0, 1, 0, 0, 0)),
   "the shared canonical form is 'x' in each F_p (degree 1, all deg<p)")

# an UNEQUAL pair: x vs x^2 differ (already on F_3, and F_5).
f_x2 = {2: 1}
ok(not functions_equal_decision(f_x, f_x2, primes30),
   "decision procedure says x != x^2 as functions on Z/30")
ok(not functions_equal_brute(f_x, f_x2, N30),
   "brute force confirms x != x^2 (e.g. x=2: 2 vs 4)")

# canonical form is a genuine NORMAL FORM: two syntactically different but equal
# expressions (2*x^5 + 3  vs  2*x + 3) collapse; degree is < p in every channel.
g1 = {5: 2, 0: 3}
g2 = {1: 2, 0: 3}
ok(functions_equal_decision(g1, g2, primes30) and functions_equal_brute(g1, g2, N30),
   "2x^5+3 == 2x+3 as functions (canonical form collapses them)")
cf = canonical_over_ring(g1, primes30)
ok(all(len(v) == p for v, p in zip(cf, primes30)),
   "each channel's canonical polynomial has degree < p (the F_p[x]/(x^p-x) rep)")

# TOTALITY of the decider: it returns a bool for a whole battery (no divergence),
# and the battery exercises BOTH verdicts (three unequal pairs + one equal pair).
battery = [({7: 1}, {1: 1}),        # x^7 vs x  -> differ on F_5 (x^7 = x^3)
           ({4: 1}, {2: 1}),        # x^4 vs x^2 -> differ on F_5
           ({30: 1}, {0: 1}),       # x^30 vs 1  -> differ (x^30 = 0 at x=0)
           ({5: 1}, {1: 1})]        # x^5 vs x   -> EQUAL (the True the battery needs)
verdicts = [functions_equal_decision(a, b, primes30) for a, b in battery]
ok(all(isinstance(v, bool) for v in verdicts) and len(verdicts) == len(battery),
   "the equivalence decider is TOTAL: a verdict on every pair")
ok(verdicts == [False, False, False, True],
   "the battery exercises both verdicts: %s" % (verdicts,))
print("  battery verdicts (x^7?=x, x^4?=x^2, x^30?=1, x^5?=x):", verdicts)
# and the decider agrees with brute force across the battery (soundness):
ok(all(functions_equal_decision(a, b, primes30) == functions_equal_brute(a, b, N30)
       for a, b in battery),
   "the per-field decider agrees with brute force on the whole battery (sound)")
print("  x^5 == x (diff polys, shared canonical form %s); x != x^2; decider"
      " total + sound" % (cf5,))
print("  Rice's Turing analogue -- program equivalence -- is UNDECIDABLE (cited)")
print()


# ------------------------------------------------------------------ #
print("S3 -- THE PREDICATE CANONICAL FORM (least period + accepting set = min DFA)")

# unit(Z/30) written THREE syntactically different ways.
u_isunit = lambda n: 1 if is_unit(n % 30, R30) else 0
u_coprime = lambda n: 1 if (n % 2 and n % 3 and n % 5) else 0
u_demorgan = lambda n: 0 if (n % 2 == 0 or n % 3 == 0 or n % 5 == 0) else 1

cf_isunit = predicate_canonical(u_isunit, 240, 60)
cf_coprime = predicate_canonical(u_coprime, 240, 60)
cf_demorgan = predicate_canonical(u_demorgan, 240, 60)
ok(cf_isunit == cf_coprime == cf_demorgan,
   "three spellings of unit(Z/30) share ONE canonical form")
M, accepting = cf_isunit
ok(M == 30, "least period of the unit set is 30 (squarefree)")
ok(accepting == frozenset({1, 7, 11, 13, 17, 19, 23, 29}) and len(accepting) == euler_phi(30) == 8,
   "accepting residues = the 8 units mod 30 = phi(30)")
# equivalence is DECIDED by comparing canonical forms; brute cross-checks.
ok(predicates_equal_brute(u_isunit, u_demorgan, 300),
   "brute force: is_unit and the De Morgan form agree over 0..300")

# INEQUIVALENT controls: different canonical form -> decided NOT equal.
p_cop6 = lambda n: 1 if (n % 2 and n % 3) else 0        # coprime to 6 only
p_even = lambda n: 1 if n % 2 == 0 else 0
cf_cop6 = predicate_canonical(p_cop6, 240, 60)
cf_even = predicate_canonical(p_even, 240, 60)
ok(cf_cop6 == (6, frozenset({1, 5})),
   "coprime-to-6 canonical form = (6, {1,5}) -- distinct from unit(Z/30)")
ok(cf_even == (2, frozenset({0})),
   "even canonical form = (2, {0}) -- distinct")
ok(cf_isunit != cf_cop6 and cf_isunit != cf_even,
   "unit(Z/30) is decided NOT equal to coprime-to-6 or even (canonical forms differ)")
ok(not predicates_equal_brute(u_isunit, p_cop6, 300),
   "brute force confirms unit(Z/30) != coprime-to-6")
print("  unit(Z/30): 3 spellings -> one canonical (M'=30, 8 accepting = phi(30));"
      " Myhill-Nerode minimal DFA (cited)")
print("  controls coprime-to-6=(6,{1,5}), even=(2,{0}) decided distinct")
print()


# ------------------------------------------------------------------ #
print("S4 -- SELF-CERTIFICATION + THE DUALITY/TRADE")

# A tower result carries its own checkable witness: the ECC syndrome.
data = (1, 2, 3, 4)                     # 4 data channels of RAD (k=7)
code = ecc_encode(data, RAD_RING)
ok(ecc_syndrome(code, RAD_RING) == (0, 0, 0),
   "a valid RAD codeword self-certifies: syndrome = 0 (checked in O(parity))")
ok(not ecc_detect(code, RAD_RING), "no corruption detected on the clean codeword")

# corrupt one channel -> nonzero syndrome (caught), located, corrected -- with NO
# recomputation of the result and NO trust in the producer.
bad = list(code)
bad[1] = (bad[1] + 1) % RAD_RING.moduli[1]     # flip data channel 1
bad = tuple(bad)
ok(ecc_detect(bad, RAD_RING) and ecc_syndrome(bad, RAD_RING) != (0, 0, 0),
   "corruption in channel 1 -> nonzero syndrome (self-certification fails loudly)")
ok(ecc_locate(bad, RAD_RING) == 1, "the corrupted channel is located (channel 1)")
fixed, ch = ecc_correct(bad, RAD_RING)
ok(fixed == code and ch == 1, "the single-channel error is corrected back to the codeword")
print("  RAD codeword self-certifies (syndrome=0); corruption caught, located"
      " (ch %d), corrected -- O(parity), no re-run" % ch)

# THE DUALITY / THE TRADE (synthesis, cited -- undecidability cannot be run).
# The equivalence deciders of S1-S3 are TOTAL (a verdict on every input). By the
# duality, decidable equivalence is mutually exclusive with a universal
# self-interpreter (a total language cannot contain its own interpreter). So the
# tower CANNOT be self-interpreting -- exactly what explore_reset_corner.py /
# explore_expressiveness_perimeter.py found (not universal,
# one borrow short; the growth machine cannot simulate a universal machine).
# We assert only the RUN-checkable half: the deciders are total and consistent.
decidable_side = (
    functions_equal_decision(f_x5, f_x, primes30) is True
    and functions_equal_decision(f_x, f_x2, primes30) is False
    and cf_isunit == cf_demorgan
)
ok(decidable_side,
   "the tower is verified on the DECIDABLE-EQUIVALENCE side (S1-S3 total deciders)")
print("  THE DUALITY (cited): decidable-equivalence XOR universal self-interpretation")
print("  the tower sits on the decidable side (verified) => NOT self-interpreting")
print("  -- consistent with explore_reset_corner.py / "
      "explore_expressiveness_perimeter.py (not universal, one borrow short)")
print("  THE TRADE (exact): VERIFICATION-freedom bought with REPRESENTATION-freedom")
print("  KILL-SHOT (fair-fight, deferred): decidable equivalence is a COMMODITY")
print("  (regex/Datalog/Agda own it); the tower's edge = the CRT-tuple normal form")
print("  (O(k), reversible, ECC-carrying, by construction) -- load-bearing? exploitation")
print()

print("ALL CHECKS PASSED:", CHECKS)
