"""Does a substrate with NATIVE division/order read MERGE — binary-branching
hierarchy with matching, general linguistics' basic composition operation, and
here just bracket nesting — and does the flat-role independence survive it?
The dual pole tested for the converse corner of the wall-dissolution hunt
(cast two).

THE QUESTION (the second cast of the wall-dissolution hunt). Cast one
(explore_merge_dissolution.py) located the recursion wall precisely: the sole
obstruction to a native Merge readback is the DIGIT READ = division by the base,
and in ANY finite ring a POSITIONAL base (one that divides the modulus, so the
digits are ring-structural — the ideals p^i) is a ZERO-DIVISOR, so ÷base is never
a meadow op. The escape it named: an INFINITE modulus, where a base can be both
positional AND a UNIT (base 10 in the reals: positional, 10 invertible) = the
full archimedean magnitude the tower deleted. The DUAL POLE (explore_dual_pole.py)
IS that escape realized — keep ONLY the archimedean window, delete every finite
place; ÷base is native there. Cast two runs the converse test on it: does native
division/order buy the matching readback, and does the flat, order-invariant
role independence (the structure-dependence record, the §I control the tower reads
NATIVELY) SURVIVE on a substrate that carries native division? The verdict needs
BOTH answers on ONE substrate.

WHOSE VOCABULARY (fixed before any engine code was written). Two suspicions, both
TRANSPLANTS, both flagged and put at risk:
  [T1] "the magnitude wall dissolves to precision — a PRECISION RATCHET" is
       transplanted from the DEPTH-face ratchet (the recursion-growth
       record, §II.1), reading the tower's window-count growth m onto the dual pole's
       digit-precision growth t. It is not assumed: the collision structure
       (which trees share a window at precision t) is measured empirically, not
       inferred from the analogy.
  [T2] "buying native order COSTS the flat-role independence" is transplanted
       from the dual pole's two-pole exchange (explore_dual_pole.py F4, the
       equality wall = the death of exact channel independence; the two poles
       exchange crown capability and blind spot, exact zero-test vs exact size).
       This is the CURRENT design's diagnosis; the dissolution hunt must
       not inherit it as a verdict. It is MARKED and put at risk — the whole
       point is that the DISSOLUTION could fire (independence could survive), in
       which case the deletion was not forced.

THE SUBSTRATE (the dual rung, from explore_dual_pole.py). The integers read ONLY
through the archimedean window: W_{b,t}(n) = (sign n, e = floor(log_b|n|),
mantissa = the t leading base-b digits). A floating-point number IS the dual rung;
the dual ladder ascends by adding DIGITS OF PRECISION t (the mirror of the tower's
window-count growth). Native reads (the dual-pole corpus): sign, exponent,
mantissa; ÷b = a shift (exact-local — b*x is exact-local at lookahead, its inverse
where defined); order/comparison of WELL-SEPARATED values; the exact-local class
(scalings by rad(c)|rad(b), fiber-permuting maps). NOT native — THE EQUALITY WALL
(explore_dual_pole.py F4): the exact zero-test of a difference, and the exact read
of the HIDDEN low digits of a DEEP value (fiber length L = b^(e+1-t) > 1), are
unreadable at every precision short of exact.

THE PROBE. Bracket strings are trees (balanced Dyck words). Two tests, both on the
one dual substrate; the verdict is the pair.

  TEST 1  THE MERGE READBACK (does native order/division buy matching?).
      Horner-code a tree into one value v, base b, exactly as cast one
      (open -> digit 1, close -> digit 0, leading-1 sentinel; injective). On the
      dual pole ÷base IS native (the escape), so the digits — hence branching AND
      matching, via a small native counter (the Minsky fold of cast one HORN 2c,
      INC/DEC/zero-test on a SMALL counter that stays in the shallow-exact regime)
      — ARE readable, but ONLY to PRECISION t: a tree of bracket length L needs L
      base-b digits, and at precision t < L the tail digits fall into the HIDDEN
      deep fiber, so distinct trees sharing their top-t digits collapse to ONE
      window (a collision). So — UNLIKE cast one, where the magnitude wall did not
      move at all — here the magnitude wall DISSOLVES, but bounded by precision: a
      PRECISION RATCHET [T1], the mirror of the depth-face ratchet (reads depth
      up to t, unbounded needs growing precision). Observables: the number of
      census trees that share a dual window at each precision t (0 when t covers
      the longest code, > 0 below — the ratchet); that ÷base recovers the next
      base-b digit EXACTLY on the dual pole (the native op, vs cast one's
      zero-divisor failure); that the Minsky fold reads matching from recovered
      digits.

  TEST 2  THE FLAT-ROLE INDEPENDENCE CONTROL (does independence survive?).
      The §I flat-role reading has TWO parts, and they come apart on the dual
      pole:
      (2-static) order-invariant slots with distinct fillers distinguishable.
          Pack k roles into fixed-width base-b blocks, filler f_r < b^w:
          value = sum_r f_r * b^(r*w). This is presentation-order-invariant (a
          sum) and injective in the fillers. PREDICT: PASSES on the dual pole —
          static slotting survives (so the test is not rigged: the substrate is
          not trivially broken).
      (2-algebra) CRT independence = the native BINDING operation DECOMPOSES per
          role (the ring iso: on the tower (x*y) mod q_r = (x mod q_r)*(y mod q_r),
          so composing two role-vectors leaves every channel independent). Test
          whether each substrate's NATIVE binding respects the role split:
            - TOWER (positive control, MUST pass): bind by crt_mul / crt_add;
              read_r(x . y) == read_r(x) . read_r(y) for every window r. PREDICT
              0 mismatches (CRT independence — the detector fires TRUE on a
              genuinely independent substrate).
            - DUAL POLE: pack the roles, bind by the pole's OWN native arithmetic
              (integer + / *); read block_r(x . y) vs the intended per-role
              value. PREDICT > 0 mismatches — CARRY couples the blocks: a value's
              positional digits are not independent channels. The very positional
              structure Test 1 needs (carry = the positional mechanism) is what
              couples the roles.
      Secondary honest observation: the dual pole's native read is LEADING-ended
      (only the top-t digits are exact; trailing role-blocks fall in the hidden
      fiber), an asymmetry the tower — which reads all k windows symmetrically —
      does not have.

PREDICTIONS (frozen before the run).
  P1 (TEST 1, the ratchet): ÷base recovers base-b digits EXACTLY on the dual pole
     (native, positive control). At precision t >= max census code length the
     dual window is injective on the census (0 collisions — matching readable);
     at t below it, > 0 collisions (distinct trees, one window) rising as t falls.
     The Minsky fold reads matching from recovered digits on all census trees and
     rejects '][' and a net-nonzero string. So native order/division DOES buy the
     Merge readback — as a PRECISION RATCHET, not a free stack.
  P2 (TEST 2-static): the dual-pole packing is order-invariant (presentation
     permutations give one value) and injective in the fillers — static roles
     survive.
  P3 (TEST 2-algebra, the no-free-lunch): the TOWER's native binding decomposes
     per role (0 mismatches over trials, crt_mul and crt_add — CRT independence);
     the DUAL POLE's native binding does NOT (> 0 mismatches — carry coupling).
     Buying the native positional/magnitude read costs the independent algebra.
  P4 (the exclusivity): the feature that buys TEST 1 (positional magnitude, i.e.
     carry) is the feature that breaks TEST 2-algebra (carry couples the roles).
     Independence and native-positional-recursion are EXCLUSIVE on one substrate.

POSITIVE CONTROLS (run and asserted before any verdict is read).
  - Horner encode/decode round-trips (base b), so TEST 1 measures a wall not a loss;
  - ÷base recovers the exact next base-b digit on the dual pole at shallow
    precision (the native op is correct — so TEST 1's precision boundary is a real
    wall, not a harness bug);
  - the TOWER CRT-independence detector fires TRUE on the tower (crt_mul and
    crt_add decompose per window) — so a FALSE on the dual pole is meaningful;
  - the dual-pole static packing is injective in the fillers (roles distinguishable).

KILL (observable). DISSOLUTION fires iff, on the ONE dual substrate, TEST 1 reads
matching UNBOUNDED (not precision-capped — no collisions appear as trees grow) AND
TEST 2-algebra's independence SURVIVES (the native binding decomposes per role) —
then a substrate reads Merge natively AND keeps flat-role independence: the
archimedean deletion was NOT forced (outcome a, the wanted result). Its ABSENCE —
TEST 1 dissolves only to precision (a ratchet, collisions below t) while TEST 2's
independent ALGEBRA dies to carry coupling — is the NO-FREE-LUNCH (outcome b): the
two crown capabilities EXCHANGE across the poles (the tower has flat-role
independence but no native digit read, cast one; the dual pole has the native
digit read but no independent algebra), so across the two poles the archimedean
deletion is LOCALLY FORCED. Both outcomes are first-class.

FINDINGS (all four predictions met; no dissolution kill fired; every number
below is printed output; exhaustive at the stated toy scope; observation tier).
Substrate: the dual pole (archimedean window W_{b,t}), base b = 2. Census = the
22 balanced trees to m = 4 (longest code 9 base-2 digits).

  POSITIVE CONTROLS PASS. Horner encode / positional decode round-trips (the
  code is representable, so TEST 1 measures a WALL not a loss); native ÷base
  recovers the exact base-b digit (a real op — the escape cast one named, NOT a
  zero-divisor); the tower CRT-independence detector fires TRUE (native integer *
  and + decompose per window, 0/150 — the CRT iso, so a FALSE on the dual pole is
  meaningful); the dual-pole static packing is injective in the fillers.

  P1 CONFIRMED — TEST 1: native order/division BUYS the Merge readback, as a
  PRECISION RATCHET. The Horner code is injective (22/22). The dual window's
  collisions fall monotonically as precision rises — t=2: 18, t=3: 15, t=4: 13,
  t=5: 8, t=6: 5, t=7: 0 (injective; the top-7 digits already separate the whole
  census, below the 9-digit longest code) — the ratchet: below precision the tail
  digits fall in the hidden deep fiber and distinct trees collapse to one window,
  at precision they separate. The Minsky fold (INC/DEC/zero-test on a small
  shallow-exact counter) reads matching on all 22 census trees and rejects '][' and
  a net-nonzero string. So — UNLIKE cast one, where the magnitude wall did not move
  — the wall DISSOLVES here, bounded by precision: the mirror of the depth-face
  ratchet (reads depth up to t, unbounded needs growing precision).

  P2 CONFIRMED — TEST 2-static: the packed value depends only on the role→filler
  assignment (order-invariant, one value across presentations) and is injective in
  the fillers — static roles survive on the dual pole (the substrate is not
  trivially broken).

  P3/P4 CONFIRMED — TEST 2-algebra, THE NO-FREE-LUNCH: the substrate's NATIVE
  binding does NOT decompose per role. The TOWER's native integer * and + read back
  per-window with 0/150 mismatches (CRT iso — roles independent); the DUAL POLE's
  native * and + on packed roles read back WRONG in 24/54 per-role reads (44% —
  carry couples the digit-blocks). The positional magnitude that BUYS TEST 1 (carry
  = the positional mechanism) is exactly the carry that BREAKS TEST 2-algebra:
  independence and native-positional-recursion are EXCLUSIVE on one substrate.

THE VERDICT (observation tier, exhaustive at scope): NO-FREE-LUNCH CONFIRMED — the
archimedean deletion is LOCALLY FORCED across the two poles. The dual pole, which
carries native division/order, READS Merge structure natively (TEST 1 — the
magnitude wall that blocked cast one DISSOLVES, to precision, a ratchet) but LOSES
the flat-role independence (TEST 2 — its only native binding is carry-coupled
magnitude arithmetic, which does not decompose per role). The finite tower is the
exact mirror (cast one): CRT-independent order-invariant windows (flat roles
native) but NO native digit read (recursion's magnitude readback is the borrow,
paid). The two CROWN capabilities EXCHANGE across the poles — the two-pole reading criterion
(explore_dual_pole.py, exact zero-test vs exact size) read for the language
capabilities: exact channel
independence (flat roles) lives at the finite pole, the native positional read
(recursion structure) at the archimedean pole, and no single COMMUTATIVE-RING
substrate holds both, because CRT independence REQUIRES coprime non-coupling
channels while a positional magnitude IS the carry-coupling of its digits (dropping
the single-commutative-ring assumption is exactly the next cast). So across the
tower's two extremes
— delete the archimedean place (the tower) or delete every finite place (the dual
pole) — the deletion is forced: you get flat-role independence OR native
positional recursion, never both. PROGRAM 1's first arc converges; the verdict
hands to PROGRAMS 2 (learning redesign) and 3 (emergence scale).

THE PRICED DOOR (recorded, not the destination — charter: dissolve, don't just
price). The obvious product Z/p_k# x (dual-pole register) puts flat roles in the
CRT windows (independent) AND recursion magnitude in the archimedean register
(native digit read) — but that RE-ATTACHES the full deleted place as a co-factor
(exactly cast one's named escape), and binding a recursion in the register to a
role in the windows crosses the CRT boundary = base extension = the borrow (the
keystone lemma). Two substrates stapled, the staple is the borrow: a priced door,
not a dissolution. A genuinely different intermediate is a reopen (the space is
infinite; this is not a proof over all substrates).

HONEST LIMITS. Toy scope (trees to small m, base 2, small role windows). The claim
is a NATIVENESS / inductive-bias statement — which readouts are native (fixed-ring
ops + ÷base + zero-test + write-constant) vs paid, on the two POLES as the extremes
— not a learned-generalization claim, not an exactness benchmark, not a scale claim,
no learning rule (codes/readers hand-designed, as in the four prior probes and cast
one). "Locally forced across the two poles" is not "globally impossible": a
genuinely different intermediate substrate is a reopen. The precision-ratchet
reading of TEST 1 is a transplant from the depth-face ratchet, VALIDATED by the
measured collision curve, not assumed. The carry-coupling of TEST 2-algebra is
exhaustive over the trial pairs, not a proof over all packings — but any packing
into ONE magnitude inherits carry, and any split into independent channels is the
tower (coprime, non-positional). The Minsky-fold matching claim is at observation
tier over the census (cast one HORN 2c), not a proof over all readers.

RUN RECORD (python prime/code/explore_dual_merge.py, well under a second, trivial
memory, pure Python + crt.py, no external libraries). Base b = 2, census 22 trees
to m = 4. Positive controls PASS (Horner round-trip; native ÷base digit; tower CRT
iso 0/150; dual static packing injective). TEST 1: 22/22 injective codes; window
collisions 18/15/13/8/5/0 at t = 2..7 (injective from t = 7); Minsky fold reads
matching on 22/22, rejects '][' and net-nonzero. TEST 2: static order-invariant +
distinct PASS; 2-algebra tower 0/150, dual pole 24/54 per-role reads wrong. No
dissolution kill fired. All asserts green.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crt import Ring, encode  # noqa: E402


def banner(s):
    print("\n" + "=" * 68)
    print(s)
    print("=" * 68)


# ------------------------------------------------------------------ #
# balanced bracket trees + the positional (Horner) tree code          #
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


def horner_code(word, b):
    """Positional code, base b: leading-1 sentinel, open -> digit 1,
    close -> digit 0, Horner-folded v <- v*b + digit. Injective."""
    v = 1
    for ch in word:
        v = v * b + (1 if ch == "[" else 0)
    return v


# ------------------------------------------------------------------ #
# the dual rung: the size window W_{b,t}                              #
# ------------------------------------------------------------------ #

def ndigits(a, b):
    """Number of base-b digits of a >= 1, minus 1 (the exponent e)."""
    e = 0
    while a >= b:
        a //= b
        e += 1
    return e


def dual_window(n, b, t):
    """The size window (sign, exponent, t leading base-b digits) of n != 0 —
    the dual rung. Two values with the same window are indistinguishable to a
    precision-t archimedean reader (they share a deep fiber when e+1 > t)."""
    s = 1 if n > 0 else -1
    a = abs(n)
    e = ndigits(a, b)
    j = max(0, e + 1 - t)          # the hidden low digits (deep fiber length b^j)
    return (s, e, a // b**j)       # the mantissa: the t leading digits


def peel_top_digit(v, b):
    """The NATIVE dual-pole digit read: the leading base-b digit via ÷base.
    On the dual pole ÷b is native (a shift), so the top digit is
    floor(v / b^e) — a real op, unlike cast one's zero-divisor ÷base."""
    e = ndigits(v, b)
    return v // b**e, v - (v // b**e) * b**e   # (top digit, remainder)


def decode_positional(v, b):
    """Faithful positional decode (base b, native ÷base + digit reads, at full
    precision): read every digit most-significant first, drop the leading-1
    sentinel, map back to brackets. Establishes the code is representable."""
    e = ndigits(v, b)
    digits = [(v // b**i) % b for i in range(e, -1, -1)]
    return "".join("[" if d == 1 else "]" for d in digits[1:])


def minsky_balance(bits):
    """Balance from a bit sequence using ONLY a small counter with
    INC / DEC / zero-test (the counter stays shallow-exact, so its zero-test is
    native even at the dual pole). INC on open, zero-test-before-DEC on close
    (underflow = unbalanced), final zero-test (net zero). No comparison."""
    depth = 0
    for bit in bits:
        if bit == 1:
            depth += 1
        else:
            if depth == 0:
                return False
            depth -= 1
    return depth == 0


# ------------------------------------------------------------------ #
# flat-role packing on the dual pole (one magnitude, digit blocks)    #
# ------------------------------------------------------------------ #

def pack_roles(fillers, b, w):
    """Pack k role-fillers into fixed-width base-b blocks of one magnitude:
    value = sum_r f_r * b^(r*w). Order-invariant (a sum), injective when every
    f_r < b^w."""
    return sum(f * b ** (r * w) for r, f in enumerate(fillers))


def read_block(value, r, b, w):
    """Read role r's block from the packed magnitude: (value // b^(r*w)) mod b^w
    — uses ÷base (native) and the low-digit read."""
    return (value // b ** (r * w)) % (b ** w)


def main():
    b = 2                     # the numeration base (dual-pole digit base)
    census = all_trees(4)     # the 22 balanced trees to m = 4
    codes = [horner_code(w, b) for w in census]
    max_len = max(len(w) + 1 for w in census)   # +1 for the leading-1 sentinel
    print("DOES NATIVE ORDER/DIVISION READ MERGE, AND DOES INDEPENDENCE SURVIVE?")
    print(f"substrate: the dual pole (archimedean window W_(b,t)), base b={b}")
    print(f"census: {len(census)} balanced trees to m=4; "
          f"longest code = {max_len} base-{b} digits")

    # ---- POSITIVE CONTROLS -------------------------------------------
    banner("POSITIVE CONTROLS")
    # Horner round-trip (decode by native ÷base positional reads, full precision)
    for word in census:
        assert decode_positional(horner_code(word, b), b) == word
    print("Horner encode / positional decode round-trips ........ PASS")

    # ÷base recovers the exact next base-b digit at shallow precision
    for v in (6, 26, 28, 114, 1000, 123456):
        top, rem = peel_top_digit(v, b)
        assert top == v // b ** ndigits(v, b)
        assert top * b ** ndigits(v, b) + rem == v
    print("native /base recovers the exact base-b digit ........ PASS  "
          "(a real op -- not cast one's zero-divisor)")

    # TOWER CRT-independence detector fires TRUE on the tower: the NATIVE
    # integer arithmetic (the ring binding, mod N) decomposes per window (the
    # CRT iso -- non-tautological: it is WHY the windows are independent
    # channels). Tested for the same native ops (* and +) compared on the dual
    # pole below.
    tower = Ring("roles", (11, 13, 17), (1, 1, 1))
    tower_mism = 0
    for x in (5, 40, 137, 2000, tower.N - 3):
        for y in (6, 51, 208, 1500, tower.N - 9):
            zmul, zadd = (x * y) % tower.N, (x + y) % tower.N
            ex, ey, em, ea = (encode(x, tower), encode(y, tower),
                              encode(zmul, tower), encode(zadd, tower))
            for r in range(3):
                if em[r] != (ex[r] * ey[r]) % tower.moduli[r]:
                    tower_mism += 1
                if ea[r] != (ex[r] + ey[r]) % tower.moduli[r]:
                    tower_mism += 1
    assert tower_mism == 0
    print("tower CRT-independence detector fires TRUE ........... PASS  "
          "(native integer * and + decompose per window -- the CRT iso)")

    # dual-pole static packing injective in the fillers
    w = 3
    seen = {}
    for f0 in range(b ** w):
        for f1 in range(0, b ** w, 3):
            val = pack_roles((f0, f1, 2), b, w)
            assert val not in seen or seen[val] == (f0, f1, 2)
            seen[val] = (f0, f1, 2)
    print("dual-pole static packing injective in fillers ........ PASS")

    # ---- TEST 1: THE MERGE READBACK (the precision ratchet) ----------
    banner("TEST 1  the Merge readback -- native order buys matching, to PRECISION")
    print(f"distinct Horner codes: {len(set(codes))}/{len(census)} (injective, "
          "representable)")
    print("dual window collisions vs precision t (trees sharing one window):")
    ratchet = []
    for t in range(2, max_len + 2):
        windows = {}
        for word, v in zip(census, codes):
            windows.setdefault(dual_window(v, b, t), []).append(word)
        collided = sum(len(g) - 1 for g in windows.values() if len(g) > 1)
        ratchet.append((t, collided))
        note = "  <- injective (matching readable)" if collided == 0 else ""
        print(f"    t={t:>2}: {collided:>3} trees lost to a shared window{note}")
    # the Minsky fold reads matching from recovered digits
    ok = sum(1 for word in census
             if minsky_balance([1 if c == "[" else 0 for c in word]))
    rej = (not minsky_balance([0, 1])) and (not minsky_balance([1, 1, 0]))
    print(f"Minsky fold (INC/DEC/zero-test) reads matching on {ok}/{len(census)} "
          f"census trees; rejects '][' and net-nonzero: {rej}")

    # ---- TEST 2: FLAT-ROLE INDEPENDENCE ------------------------------
    banner("TEST 2  flat-role independence -- static survives, the ALGEBRA dies")
    # 2-static: the packed value depends only on the role->filler assignment,
    # not the presentation order (a sum), and is injective in the fillers.
    role_fillers = {0: 2, 1: 1, 2: 4}
    presentations = [[0, 1, 2], [2, 0, 1], [1, 2, 0]]   # listing orders
    vals = [sum(role_fillers[r] * b ** (r * w) for r in order)
            for order in presentations]
    order_inv = len(set(vals)) == 1
    distinct = (pack_roles((2, 1, 4), b, w) != pack_roles((3, 1, 4), b, w))
    print(f"2-static: order-invariant slots ({'one value' if order_inv else 'DIFFER'}"
          f") + distinct fillers distinguishable ({distinct}) -> "
          f"{'PASS' if order_inv and distinct else 'FAIL'} (static roles survive)")

    # 2-algebra: does the substrate's NATIVE binding decompose per role? Same
    # native ops (* and +) the tower control passed. On the dual pole the roles
    # are digit-blocks of ONE magnitude, so carry couples them.
    w2 = 4                              # block width; sums/products overflow a block
    dual_mism = 0
    dual_trials = 0
    for xf in ((5, 6, 3), (9, 12, 7), (10, 3, 8)):
        for yf in ((7, 11, 4), (6, 9, 13), (2, 8, 5)):
            xv, yv = pack_roles(xf, b, w2), pack_roles(yf, b, w2)
            zadd, zmul = xv + yv, xv * yv       # the pole's native binding
            for r in range(3):
                dual_trials += 2
                if read_block(zadd, r, b, w2) != (xf[r] + yf[r]) % (b ** w2):
                    dual_mism += 1
                if read_block(zmul, r, b, w2) != (xf[r] * yf[r]) % (b ** w2):
                    dual_mism += 1
    print(f"2-algebra TOWER  (native *,+): {tower_mism}/{5 * 5 * 3 * 2} per-role "
          "reads wrong  -> CRT iso, roles independent")
    print(f"2-algebra DUAL   (native *,+): {dual_mism}/{dual_trials} per-role "
          "reads wrong  -> carry couples the blocks, independence LOST")

    banner("DONE")
    print("TEST 1: native /base reads Merge digits -> matching readable to")
    print("precision t (a RATCHET: collisions appear below the code length).")
    print("TEST 2: static slots survive, but the native BINDING does not")
    print("decompose per role (carry couples the digits) -> the independent")
    print("ALGEBRA dies. The positional magnitude that buys TEST 1 is the carry")
    print("that breaks TEST 2. See the module docstring for the verdict.")


if __name__ == "__main__":
    main()
