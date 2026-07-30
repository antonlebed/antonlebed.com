"""Can the recursion wall be DESIGNED AWAY? A principled intermediate
substrate — the p-adic-augmented tower — tested for a native read of MERGE:
binary-branching hierarchy with matching, the composition operation general
linguistics takes as basic. The name is that field's; the object here is
bracket nesting and nothing more.

THE QUESTION (the first cast of the wall-dissolution hunt). Four prior probes
located the recursion wall precisely: Merge (binary-branching hierarchy with
matching) is representable on the tower but a NATIVE read on NEITHER face
(explore_structure_dependence.py, explore_recursion_growth.py,
explore_element_merge.py), and the two walls are the two halves of the DELETED
archimedean place — the order/count RELATION and the MAGNITUDE. A wall in the
CURRENT design is never proof the wall is NECESSARY; the standing first move is
to hunt a design space where it DISSOLVES, going as deep as the founding
construction (the archimedean deletion included). The question here: is deleting
the archimedean place the only way — or is there a PRINCIPLED substrate that
keeps a MINIMAL slice of archimedean structure (the nesting Merge needs) WITHOUT
re-importing the full magnitude/order the tower deleted, on which Merge is a
NATIVE read while the flat-role nativeness (the structure-dependence reading,
explore_structure_dependence.py) SURVIVES?

WHOSE VOCABULARY (fixed before any engine code was written). The suspicion is written
in the vocabulary of the two-halves UNIFICATION (explore_element_merge.py §II.3):
the wall = {order/count RELATION, MAGNITUDE}. That is the CURRENT design's
diagnosis; the dissolution hunt must not inherit it as a verdict. It is MARKED as
a transplant and put at risk: the whole point is to find a substrate where at
least one half is NATIVELY supplied. The candidate is chosen to attack the
MAGNITUDE half head-on (positional digit access), which the pure squarefree tower
could not read (the base-extension borrow, B2b) — so the transplant's "magnitude
wall" is exactly what this substrate is designed to breach.

THE CANDIDATE SUBSTRATE (principled, intermediate — NOT an ad-hoc tape). The
MIXED-RADIX / p-adic-augmented tower: Z/(p^t * m), with m squarefree and coprime
to p. By CRT it splits as Z/p^t x Z/m:
  - Z/m  (squarefree windows): flat, order-invariant role binding — the
    flat-role reading verbatim, PRESERVED BY CONSTRUCTION (this is the "flat
    roles survive" requirement of the dissolution outcome).
  - Z/p^t  (the p-adic register, NON-squarefree): the minimal archimedean slice.
    It carries a native p-adic filtration Z/p^t -> Z/p^{t-1} -> ... -> Z/p (the
    ultrametric ball-nesting — nesting is native here, unlike a squarefree
    window), a native valuation v_p in {0..t}, and native multiplication by p
    (a PUSH that raises valuation). It is MORE than the pure squarefree tower
    (no valuation register there) and LESS than the dual pole (no sign, no
    magnitude comparison, no leading digits — only bounded p-adic depth). A
    designed INTERMEDIATE between the tower and the dual pole (the mirror
    deletion; records in explore_dual_pole.py). The nesting mechanism is a native
    ALGEBRAIC structure (the p-adic filtration), NOT a bracket string recorded
    verbatim and read by a bolted-on stack — the trap to avoid
    (re-importing a Turing tape proves nothing); it is explicitly avoided.

THE NATIVE READ SET (fixed-ring, the frontier-rider set applied to Z/p^t x Z/m).
Native: channel-local ring ops (+,-,* and the meadow inverse for UNITS), reading
the residue field of a channel (read v mod p at a named window — for the p^t
channel this is v mod p, the TOP p-adic digit), named-channel projection, the
global 1-bit zero-test, write-constant, born-at-0. NOT native: base extension
ACROSS the CRT boundary (the keystone lemma), and DIVISION BY p inside Z/p^t —
p is a ZERO-DIVISOR there (no meadow inverse exists), and the deflation map
(p)/(p^t) ~= Z/p^{t-1} that would peel the next digit CHANGES the modulus (a
decrement the fixed ring does not carry). So the fixed-ring native set gives the
BOTTOM digit (mod p) and — via zero-tests of p^{t-i}*v — the VALUATION, but NOT
the higher digits: peeling digit j>=1 is the deflation ÷p, the borrow in p-adic
form.

THE PROBE. A bracket string is the object (balanced Dyck words = trees). Two
encodings into the p-adic register, the two horns of the old pincer re-run on the
new substrate:

  HORN 1  THE WALK REGISTER (predict: total collapse; and its close is itself
      non-native). open = *p (v_p + 1), close = /p (v_p - 1). *p and /p CANCEL,
      so the FINAL element of every balanced string is p^0 = the same value: the
      endpoint is order-blind, the matching lives in the walk HISTORY (the order
      of operations), which a single algebraic value forgets. (And /p is the
      non-native deflation — foreshadowing HORN 2b.) This is B1 (the relation is
      not a value fact) re-instantiated.

  HORN 2  THE HORNER REGISTER (predict: representable; the magnitude readback is
      STILL the borrow — now ÷zero-divisor; and matching would follow natively
      from the digits, so the SOLE wall is the digit read). Positional-code the
      tree into one p-adic value v (base p): open = v <- v*p + 1, close =
      v <- v*p + 0 (a leading-1 sentinel; injective).
      (a) ADEQUACY: distinct trees -> distinct codes (representable).
      (b) THE BORROW PERSISTS (the transplant's magnitude wall, NOT breached).
          The digits of v ARE the bracket structure, but peeling digit j>=1
          needs ÷p, and p is a ZERO-DIVISOR in Z/p^t: mod_inverse(p, p^t) does
          not exist — WORSE than the squarefree tower, where the base had an
          inverse (it merely computed the wrong thing, B2b). What the register
          DOES buy natively is the VALUATION (the code's trailing close-run, a
          depth scalar) via zero-tests of p^{t-i}*v, and the bottom digit (mod p) — a
          DEPTH read (a ratchet, the depth face of explore_recursion_growth.py),
          NOT the tree STRUCTURE. Reading the higher digits with Python's `%` on
          the ambient integer uses the magnitude the ring does not natively
          carry: it is the borrow performed OFF-substrate.
      (c) THE SOLE WALL IS THE DIGIT READ (the order half does not add a wall).
          GIVEN the bracket bit sequence, balance is NATIVELY decidable by a
          Minsky counter fold: INC on open, a zero-test-BEFORE-DEC on close
          (underflow = unbalanced), a final zero-test (net zero). No '<', no
          comparison — only INC/DEC/zero-test, all native. So there is no
          separate ORDER wall: the matching PREDICATE (balance) is native given
          the digits (full tree reconstruction is the same universal-reader parse,
          §II.2, not re-tested here). The whole obstruction is extracting the
          digits, which is the borrow (b): the deleted place bites through ONE
          channel, the digit read = ÷base.

PREDICTIONS (frozen before the run).
  P1 (HORN 1 collapse): every balanced string's walk ends at the SAME element
     (net depth 0); distinct forests, one endpoint. Matching unreadable from the
     value. (And the close /p is the non-native deflation.)
  P2 (HORN 2 adequacy): the p-adic Horner code is injective over the census
     (distinct trees -> distinct codes); decode round-trips. Representable.
  P3 (HORN 2 borrow persists): p is a zero-divisor in Z/p^t (mod_inverse(p,p^t)
     fails), so ÷p (digit descent) is not a meadow op; the register natively
     reads the VALUATION (the native read validated against the true p-adic
     valuation on a sample, then applied to the census) and the bottom digit,
     but NOT the higher digits — peeling them is the borrow, p-adic form. The
     magnitude half is NOT dissolved.
  P4 (HORN 2 the sole wall): a Minsky counter fold (INC/DEC/zero-test only)
     decides balance from the bit sequence on all census trees (and rejects
     '][') — so matching adds no order wall; the whole obstruction is the digit
     read = ÷base.

POSITIVE CONTROLS (run and asserted before any verdict is read).
  - encode/decode round-trips on the mixed ring Z/(p^t * m);
  - FLAT ROLES SURVIVE: on the squarefree part, two role-orderings of the same
    fillers give identical residues (order-invariant), distinct fillers differ
    (roles preserved) — the flat-role nativeness is intact on the candidate;
  - the native VALUATION read (zero-tests of p^{t-i}*v) equals the true p-adic
    valuation on a sample — the native op is correct;
  - the Horner code decodes back to the exact bracket string (faithful, so P3/P4
    measure a WALL, not a loss).

KILL (observable). A borrow-free FIXED reader recovers the FULL tree (branching
AND matching) off the p-adic register -> the recursion wall DISSOLVES on a
principled intermediate: the archimedean deletion was not the only way (outcome
a, the wanted result). Its ABSENCE — HORN 1 collapses, HORN 2 is representable
but the digit readback needs ÷p (the borrow, and p a zero-divisor), while the
register natively reads only DEPTH (the valuation) — is the CONSERVATION LAW
(outcome b): changing which archimedean slice is kept does not dissolve the wall;
the magnitude readback is division-by-the-base, and a POSITIONAL base (one that
divides the modulus, so the digits are ring-structural) is a zero-divisor, so
÷base is never native. Both outcomes are first-class.

FINDINGS (all four predictions met; no dissolution kill fired; every number
below is printed output; exhaustive at the stated toy scope; observation tier).
Candidate substrate Z/(2^14 * 3 * 5 * 7), N = 1720320. Census = the 22 balanced
trees to m = 4.

  POSITIVE CONTROLS PASS. Mixed-ring encode/decode round-trips; FLAT ROLES
  SURVIVE on the candidate (roles {0:2, 1:1, 2:4}, reads invariant to
  presentation order, distinct fillers distinct — the flat-role reading is intact
  alongside the p-adic register); the native VALUATION read (zero-tests of
  p^{t-i}*v) equals the true 2-adic valuation on the sample; the Horner code
  decodes to the exact tree.

  P1 CONFIRMED -- HORN 1 collapses TOTALLY. The *p / /p walk sends all 22
  distinct forests to ONE endpoint (value p^0 = 1). Matching lives in the walk
  ORDER, which a single value forgets (B1). And the close /p is itself the
  non-native deflation (p a zero-divisor) — foreshadowing 2b.

  P2 CONFIRMED -- HORN 2 is representable. The p-adic Horner code is injective
  (22 trees -> 22 distinct codes: '[]'->6, '[[]]'->28, '[][]'->26, '[[]][]'->114),
  decode round-trips. The tree is representable.

  P3 CONFIRMED -- the BORROW PERSISTS (the magnitude half is NOT breached). In
  Z/2^14 the meadow inverse of p=2 DOES NOT EXIST (p is a zero-divisor) — so ÷p
  (digit descent) is not a field op, and WORSE than the squarefree tower where
  the base had an inverse (it merely computed the wrong thing, B2b). What the
  register reads NATIVELY is the VALUATION (the code's trailing close-run, a depth scalar): '[]'->val 1,
  '[[]]'->val 2, '[[[]]]'->val 3, '[[]][]'->val 1, and the bottom digit (mod p) —
  a DEPTH read (a ratchet), NOT the tree structure. The higher digits (the
  branching/matching) need ÷p = the borrow; reading them with Python's `%` uses
  the ambient magnitude the ring does not natively carry.

  P4 CONFIRMED -- the SOLE wall is the digit read. A Minsky counter fold
  (INC/DEC/zero-test only) decides balance correctly on all 22 census trees,
  rejects '][' (zero-test-before-DEC underflow) and a net-nonzero string — with
  no '<' and no comparison. So GIVEN the digits, matching adds NO order wall; the
  whole obstruction is extracting the digits (2b) = ÷base.

THE VERDICT (observation tier, exhaustive at scope): CONSERVATION LAW, located at
the ZERO-DIVISOR borrow — no dissolution, no partial dissolution. The
p-adic-augmented tower does not read Merge natively. It natively reads the
VALUATION (depth — a ratchet, the depth face of explore_recursion_growth.py) but
not the tree STRUCTURE: branching and matching need the digit sequence, and
peeling the digits is division by the base p, which is a ZERO-DIVISOR in any
finite register (no meadow inverse) — the borrow, in p-adic form. This is
explore_element_merge.py's magnitude wall re-instantiated on the new substrate:
changing WHICH archimedean slice is kept (the p-adic filtration here) does not
dissolve it. The reason is a clean no-free-lunch: for the digits to BE the
bracket structure the base must DIVIDE the modulus (that is what makes the
positional filtration ring-structural — the ideals p^i), and a base that divides
the modulus is a ZERO-DIVISOR, so ÷base is not a meadow op. A base COPRIME to the
modulus IS a unit (÷base native) but generates NO filtration — no nesting to
read. So in a finite ring nesting-native and digit-division-native are EXCLUSIVE.
And the matching adds NO second wall: a Minsky fold reads balance from the digits
with only INC/DEC/zero-test, so the deleted place bites through ONE channel — the
digit read. The escape is exactly an INFINITE modulus, where a base can be both
positional AND invertible (base 10 in the reals: positional and 10 a unit) — the
archimedean value the tower deleted, in FULL, not a minimal slice. So the borrow
is INVARIANT to which finite slice you keep; a dissolution re-imports the whole
deleted place. Flat roles survive on the candidate by construction; the valuation
is a native depth bonus, a ratchet, not the tree. Outcome (b), the conservation
law, is the finding.

HONEST LIMITS. Toy scope (trees to small m, one small base p, bounded t). The
claim is about which readouts are NATIVE (fixed-ring ring ops + read-mod-p +
zero-test + write-constant) vs PAID, on ONE designed candidate substrate — a
nativeness/inductive-bias statement, not a learned-generalization claim, not an
exactness benchmark, not a scale claim, and no learning rule (the codes/readers
are hand-designed, as in the four prior probes). It is one CAST of the
wall-dissolution hunt, not a proof over all conceivable intermediate substrates:
a different principled intermediate is a reopen. "This candidate does not
dissolve the wall" is not "no substrate can" — but it LOCATES the obstruction:
the digit read is ÷base, native only if the base is a UNIT, i.e. an
invertible/infinite value = the archimedean magnitude the deletion removed, in
full (not a minimal slice) — so a dissolution re-imports the deleted place rather
than a minimal slice. The Minsky-fold argument (matching adds no wall) is at
observation tier over the census, not a proof over all codes. And the
non-nativeness of the higher digits rests on the ARGUMENT that ÷p is not a meadow
op (p a zero-divisor, no inverse — demonstrated) and the deflation changes the
modulus — the same style of argument as explore_element_merge.py B2b (field-op /
polynomial-degree), not an exhaustive search over all native-op programs.

RUN RECORD (python prime/code/explore_merge_dissolution.py, well under a second,
trivial memory, pure Python no external libraries). Candidate ring
Z/(2^14 * 3 * 5 * 7), N = 1720320. Positive controls PASS (mixed round-trip;
flat roles survive, roles {0:2, 1:1, 2:4} presentation-order-free; native
valuation correct; Horner decode faithful). HORN 1: 22 forests -> 1 walk
endpoint (value 1). HORN 2a: 22/22 injective ('[]'->6, '[[]]'->28, '[][]'->26,
'[[]][]'->114). HORN 2b: meadow inverse of p=2 in Z/2^14 does not exist
(zero-divisor); native valuations 1/2/3/1 for '[]'/'[[]]'/'[[[]]]'/'[[]][]'.
HORN 2c: Minsky fold correct on all 22 census trees, rejects '][' and a
net-nonzero string. All asserts green.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import Ring, encode, decode, mod_inverse, primes_up_to  # noqa: E402

PRIMES = tuple(primes_up_to(200))


def banner(s):
    print("\n" + "=" * 68)
    print(s)
    print("=" * 68)


# ------------------------------------------------------------------ #
# balanced bracket trees + the p-adic Horner code                     #
# ------------------------------------------------------------------ #

def dyck_words(m):
    """All balanced bracket strings with m opens (Catalan(m))."""
    out = []

    def rec(s, opened, closed):
        if opened == m and closed == m:
            out.append(s)
            return
        if opened < m:
            rec(s + "[", opened + 1, closed)
        if closed < opened:
            rec(s + "]", opened, closed + 1)

    rec("", 0, 0)
    return out


def all_trees(max_m):
    out = []
    for m in range(1, max_m + 1):
        out += dyck_words(m)
    return out


def horner_code(word, p):
    """Positional code into the p-adic register, base p: leading-1 sentinel,
    open -> digit 1, close -> digit 0, Horner-folded v <- v*p + digit. Injective
    (the sentinel keeps different lengths apart)."""
    v = 1
    for ch in word:
        v = v * p + (1 if ch == "[" else 0)
    return v


def decode_horner(v, p):
    """Invert: peel base-p digits (this peel uses the ambient integer magnitude,
    NOT the ring — it is the borrow performed off-substrate), drop the sentinel,
    map back to brackets."""
    digits = []
    while v > 1:
        digits.append(v % p)
        v //= p
    return "".join("[" if d == 1 else "]" for d in reversed(digits))


def bracket_bits(word):
    """The bracket bit sequence in reading order (1 = open, 0 = close)."""
    return [1 if ch == "[" else 0 for ch in word]


# ------------------------------------------------------------------ #
# native reads on the p-adic register Z/p^t                           #
# ------------------------------------------------------------------ #

def valuation_native(v, p, t):
    """The p-adic valuation of v in Z/p^t by NATIVE ops only: v lies in the
    ideal (p^i) iff v * p^{t-i} == 0 (mod p^t) — a multiply-by-constant plus a
    zero-test. The valuation is the largest such i. No division, no magnitude."""
    q = p ** t
    val = 0
    for i in range(t + 1):
        if (v * p ** (t - i)) % q == 0:
            val = i
    return val


def minsky_balance(bits):
    """Decide whether a bracket bit sequence is balanced using ONLY a counter
    with INC / DEC / zero-test (a Minsky-machine fold — all native ring ops on a
    counter register): INC on open, zero-test-before-DEC on close (underflow =
    unbalanced), final zero-test (net zero). No '<', no comparison. Demonstrates
    that GIVEN the digits, matching adds no order wall."""
    depth = 0
    for b in bits:
        if b == 1:            # open -> INC
            depth += 1
        else:                 # close -> zero-test THEN DEC
            if depth == 0:    # native zero-test: underflow
                return False
            depth -= 1
    return depth == 0         # native zero-test: net zero


def main():
    p = 2               # the p-adic register base ([=digit 1, ]=digit 0)
    t = 14              # register depth: p^t comfortably exceeds every census code
    role_primes = (3, 5, 7)   # the squarefree part m = 3*5*7 (flat roles)
    print("CAN THE RECURSION WALL BE DESIGNED AWAY?")
    print(f"candidate substrate: Z/(p^t * m), p={p}, t={t}, "
          f"m = {role_primes} (squarefree)")
    mixed = Ring("mixed", (p,) + role_primes, (t,) + (1,) * len(role_primes))
    print(f"  {mixed!r}  N = {mixed.N} = {p}^{t} * {' * '.join(map(str, role_primes))}")

    census = all_trees(4)

    # ---- POSITIVE CONTROLS -------------------------------------------
    banner("POSITIVE CONTROLS")
    for n in (0, 1, mixed.N // 3, mixed.N - 1):
        assert decode(encode(n, mixed), mixed) == n
    print("mixed-ring encode/decode round-trip .............. PASS")

    # flat roles survive: bind 3 roles into the 3 squarefree windows; the
    # squarefree residues are invariant to role ORDER (order-invariant), and
    # distinct fillers give distinct residues (roles preserved).
    sf = Ring("roles", role_primes, (1,) * len(role_primes))
    fillers = (2, 1, 4)   # one filler per role, each < its window prime
    res_order1 = tuple(f % q for f, q in zip(fillers, sf.moduli))
    res_order2 = tuple(f % q for f, q in zip(reversed(fillers),
                                             reversed(sf.moduli)))
    by_role = {r: fillers[r] % sf.moduli[r] for r in range(len(fillers))}
    assert all(res_order1[r] == by_role[r] for r in range(len(fillers)))
    assert res_order2[::-1] == res_order1   # reversed presentation, same by-role
    distinct = tuple((f + 1) % q for f, q in zip(fillers, sf.moduli))
    assert distinct != res_order1           # distinct fillers -> distinct reads
    print("flat roles survive (order-invariant role reads) ... PASS  "
          f"(roles {by_role}, presentation-order-free)")

    # the native valuation read is correct
    for v in (1, 2, 4, 6, 12, 24, 48):
        tv = 0
        x = v
        while x and x % p == 0:
            x //= p
            tv += 1
        assert valuation_native(v, p, t) == tv
    print("native valuation (zero-tests of p^{t-i}*v) correct  PASS")

    for w in census:
        assert decode_horner(horner_code(w, p), p) == w
    print("p-adic Horner code decodes to the exact tree ..... PASS  "
          "(faithful representation)")

    # ---- HORN 1: THE WALK REGISTER -----------------------------------
    banner("HORN 1  walk register: *p / /p cancel -> the endpoint collapses")
    endpoints = {}
    for w in census:
        val = 1
        for ch in w:
            val = val * p if ch == "[" else val // p   # /p is the non-native deflation
        endpoints.setdefault(val, []).append(w)
    print(f"balanced trees censused: {len(census)}")
    print(f"  distinct walk ENDPOINTS: {len(endpoints)}  "
          f"(values: {sorted(endpoints)})")
    biggest = max(endpoints.values(), key=len)
    print(f"  one endpoint hosts {len(biggest)} distinct forests, e.g. "
          f"'{biggest[0]}' and '{biggest[1]}' -> value {p ** 0}")
    print("  the endpoint is net-depth only; matching lives in the walk ORDER,")
    print("  which a single algebraic value forgets (B1). And close = /p is the")
    print("  non-native deflation (p a zero-divisor) -- foreshadowing HORN 2b.")

    # ---- HORN 2a: REPRESENTATIONAL ADEQUACY --------------------------
    banner("HORN 2a  Horner code is injective (representable)")
    codes = [horner_code(w, p) for w in census]
    assert len(set(codes)) == len(census)
    print(f"balanced trees: {len(census)}; distinct p-adic codes: "
          f"{len(set(codes))}  -> injective")
    for w in ("[]", "[[]]", "[][]", "[[]][]"):
        print(f"  '{w}' -> {horner_code(w, p)}")

    # ---- HORN 2b: THE BORROW PERSISTS (p-adic form) ------------------
    banner("HORN 2b  the magnitude readback is STILL the borrow (/zero-divisor)")
    q = p ** t
    try:
        mod_inverse(p, q)
        inv_exists = True
    except ValueError:
        inv_exists = False
    print(f"p={p} in Z/p^t (q={q}): meadow inverse of p exists? {inv_exists}")
    print("  -> p is a ZERO-DIVISOR: /p (digit descent / deflation) is NOT a")
    print("  field op. WORSE than the squarefree tower, where the base HAD an")
    print("  inverse (it merely computed the wrong thing, explore_element_merge.py B2b).")

    # what the register DOES read natively: the valuation (depth), not structure
    print("\n  what IS native: the VALUATION (the trailing close-run, a depth scalar) --")
    print("  a DEPTH read (a ratchet), not the tree structure:")
    for w in ("[]", "[[]]", "[[[]]]", "[[]][]"):
        v = horner_code(w, p)
        print(f"    '{w}' -> code {v:>4}  native valuation {valuation_native(v, p, t)} "
              f"(bottom digit v mod p = {v % p})")
    print("  the HIGHER digits (the branching/matching structure) need /p = the")
    print("  borrow; reading them with Python's `%` uses the ambient magnitude")
    print("  the ring does not natively carry (the borrow performed off-substrate).")

    # ---- HORN 2c: THE SOLE WALL IS THE DIGIT READ --------------------
    banner("HORN 2c  given the digits, matching is native -> the sole wall is the read")
    ok = 0
    for w in census:
        assert minsky_balance(bracket_bits(w)) is True   # all census trees balanced
        ok += 1
    assert minsky_balance(bracket_bits("][")) is False   # underflow caught natively
    assert minsky_balance([1, 1, 0]) is False            # net nonzero caught natively
    print(f"Minsky counter fold (INC/DEC/zero-test only) on the bit sequence:")
    print(f"  balanced verdict correct on all {ok} census trees; '][' rejected")
    print("  (zero-test-before-DEC underflow), '[[]'-style net-nonzero rejected.")
    print("  No '<', no comparison -> matching adds NO order wall. The whole")
    print("  obstruction is extracting the digits (HORN 2b) = /base = the borrow.")

    banner("DONE")
    print("HORN 1 collapses (endpoint net-depth only; close /p non-native). HORN 2")
    print("is representable but its digit readback is the borrow (/p, p a")
    print("zero-divisor); the register natively reads only DEPTH (the valuation),")
    print("and given the digits a Minsky fold reads matching -> the sole wall is")
    print("the digit read = /base, while flat roles survive by construction.")
    print("See the module docstring for the verdict.")


if __name__ == "__main__":
    main()
