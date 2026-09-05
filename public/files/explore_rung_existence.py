"""
THE EXISTENCE HALF OF THE RUNG LAW -- which words of the odd-residue
member monoid exist at a designed window, two base-phi conditions in
(P, r) alone, read against the census P = 4..10 and a P = 11 column
predicted before its enumeration.

THE QUESTION. At a designed window (P, A) -- partial quotients 1 at every
place but the last of each period, where a_P = A -- and an odd shift r,
a member is a legal aligned word e (the class slot j = r - 1 holding a
digit up to A, every other slot up to 1, a nonzero digit forcing the
next slot below its cap, cyclically) whose sum S = sum_j e_j theta_j
(slots j < r wrapping to theta_{j+P}) lies in (1 - eta)L, with value
lambda = S/(1 - eta). The rung law (explore_rung_law.py) fixes the class
height of every generator scanned, h F_r + s = N(lambda), and leaves two
things open: the equality is only a rule (its congruence mod F_{P-1} - 1
the theorem), and nothing says which rungs EXIST at a given (P, r) --
P = 10 lacks two rungs P = 8 and 9 carry. This file derives both.

THE HAND ATTACK (on paper before any engine code; conventions re-derived
from the engines: Cell(P, A).a has A at index P - 1, theta_k = (-p_k,
q_k) in (1, alpha) coordinates, and for k <= P - 1 the window is golden,
theta_k = (-F_k, F_{k+1}); aligned slot j >= r reads theta_j, j < r
reads theta_{j+P}; lam_of returns lambda with S = (1 - eta) lambda).

  D1  N IS A COORDINATE. N(lambda) = -(a F_{P-1} + b F_P) for lambda =
      a theta_{P-2} + b theta_{P-1} is -lambda_y, the negated
      alpha-coefficient of lambda in (1, alpha) coordinates, because
      theta_{P-2} = (-F_{P-2}, F_{P-1}) and theta_{P-1} = (-F_{P-1}, F_P).
  D2  THE EQUALITY IS A THEOREM. Write Dt_A = det(I - H_A) = 1 + (-1)^P
      - 2 F_{P-1} - A F_P and Delta_A = h F_r + s - N(lambda_A). Solving
      the member identity for Delta gives Delta_A Dt_A = -C with C
      cap-free: C = h (F_{P-r} - F_r) + sum_I (-1)^j F_{P-1-j} - s +
      (-1)^P D - sum_J F_{j+1} (d'Ocagne on the h-, near- and deep terms,
      Cassini on D; I the near set, J the deep set, D the deep units'
      theta_{P-2}-sum). Every term is a Zeckendorf-legal Fibonacci sum,
      so |C| < A F_{P-1} + F_{P+1} + F_P + 2 F_{P-1} (for a word with no
      class digit, |C| < 2 F_{P+1} + F_P). A word that is a member at
      caps A and A + 1 (A >= 2) has Dt_A | C and Dt_{A+1} | C with
      gcd(Dt_A, Dt_{A+1}) = gcd(Dt_A, F_P) <= F_P, so C is a multiple of
      (A + 1)(A F_P + 2 F_{P-1} - 2) or zero, and the bound leaves only
      zero: (A - 1)(A + 2) F_P + (A - 1) F_{P-1} - 2 (A + 1) > 0 for
      A >= 2, P >= 3. So C = 0, Delta = 0 at EVERY cap, the value's
      coordinates a = D and b = -K/(F_{P-1} - 1) are cap-free, and the
      word is a member at every cap at which it is legal: PERSISTENCE.
      The rung law's equality is the theorem, not the congruence. A
      one-cap word needs |C| >= |Dt_A|, possible only below cap
      (3 F_P + 2)/F_{P-2}, about 8.
  D3  THE GOLDEN READING. The identity S = (1 - eta) lambda is linear in
      A once lambda's (theta_{P-2}, theta_{P-1})-coordinates are fixed,
      so it holds at two caps iff it holds identically in A iff it holds
      at A = 1 (the golden window) AND its A-coefficient vanishes, which
      is the rung law (L): h F_r + sum_I F_{j+1} = N. At A = 1 define the
      Z-linear map Phi: L -> Z[phi], Phi(u + w alpha) = w + u psi with
      psi = -1/phi; it sends theta_j to phi^j for every j of the golden
      window and Phi(eta v) = phi^P Phi(v). The identity at A = 1 reads
        (G)  h phi^{P-1+r} + sum_I phi^{P+j} + sum_J phi^j = Lam (phi^P - 1),
      Lam = Phi(-lambda) = -lambda_y + lambda_x/phi -- the word read as a
      cyclic golden numeral, the near slots carried past the period. A
      cut -theta_j has Lam = phi^j, and Lam is additive.
  D4  THE INTEGER k. By (L) the phi-coefficient of h phi^r +
      sum_I phi^{j+1} - Lam phi vanishes, so that element is an integer
      -k, k = lambda_x - h F_{r-1} - sum_I F_j, and (G) becomes
        (G') sum_J phi^j = k phi^{P-1} - Lam.
  D5  THE CRITERION. A positive element of Z[phi] has exactly one
      expansion as a sum of nonconsecutive powers of phi, finite because
      phi has the finiteness property (Frougny-Solomyak), exponents
      possibly negative. So (G') FORCES the deep set: J is the support
      of the expansion of k phi^{P-1} - Lam, and the word exists iff
      that support lies in [r + 1, P - 1] (in [r, P - 1] when h = 0),
      while Lam phi - k = h phi^r + (an expansion with support in
      [1, r - 1]) forces h and I; the wrap rule P - 1 in J => 0 not in I
      is the one legality the expansions do not see. Since 0 <=
      sum_J phi^j < phi^P, k ranges over the integers in
      [Lam/phi^{P-1}, Lam/phi^{P-1} + phi): at most two. For a cut
      t(-theta_{r+m}) with n = P - 1 - r - m the deep condition is that
      the expansion of k phi^n - t has support in [1 - m, n]; at t = 1,
      k = 1: phi^n - 1 expands to {1, 3, ..., n-1} at even n and to
      {-1, 2, 4, ..., n-1} at odd n.
  D6  READ THE OTHER WAY, the criterion is a TABLE: every triple (h, I, k)
      with I Zeckendorf-legal in [0, r-2] names Lam = (h phi^r +
      sum_I phi^{j+1} + k)/phi, whose J either fits or does not. The
      member set at (P, r) is that table's fitting rows, the cap
      entering only as the first-fit threshold h + [r - 2 in I]; the
      generators are the rows no two other rows sum to digit-wise
      (explore_member_monoid.py H2 makes the pair scan over the member
      set exact). No arithmetic in the window is consulted.
  D7  HAND CHECKS, all reproducing recorded words: P = 8, r = 3: -theta_5
      has k = 1, phi^2 - 1 = phi, J = {6}; -theta_6 has k = 1, phi - 1 =
      phi^-1, J = {5}, I = {1}; 2(-theta_5) has k = 2, 2 phi^2 - 2 =
      phi^2 + phi^-1, J = {4, 7}; -theta_7 has k = 2 (k = 3 overflows),
      J = {7}, I = {1}. P = 10, r = 3: 2(-theta_5) has k = 2 and
      2 phi^4 - 2 = phi^5 + phi^-1, top 5 above n = 4, NO WORD;
      -theta_7 overflows at both k. P = 10, r = 5: -theta_7 gives
      1000400010, -theta_8 gives 1001600100, 2(-theta_7) gives
      0010801000, -theta_9 gives the pure tooth of height 11 (k = 1,
      phi^0 - 1 = 0, J empty). P = 10, r = 7: -theta_9 gives 1010004000.
      (7, 9, 3): lambda = (11, -18), k = 2, J = {5}: 0090010.
  D8  TRANSPLANTS, marked. That every P = 11 generator is a tooth word
      with a persistent value is imported from P <= 10; the criterion
      builds only such words, so a P = 11 generator outside its table
      is a miss the enumeration will show, not a prediction.

THE SLATE (frozen before the engine ran).

  Controls (red voids the run): Phi(theta_j) = phi^j for j = 0..P-1 at
  three cells; N(lambda) = -lambda_y at every recorded generator; the
  four (8, 8, 3) generators, the (8, 11, 3) height-10 word and the
  (7, 9, 3) word 0090010 each REBUILT by the criterion from its own
  lambda; Delta_A Dt_A = -C at every recorded generator; the expansion
  of phi^n - 1 as D5 states it for n = 0..12.

  P1  THE PREDICTION (printed FIRST, before any enumeration at P = 11):
      at P = 11, every odd r, the table's member words with h <= 13, the
      generators among them by pair scan, each with its first-fit cap.
      By hand at r = 3: the comb 10200101010 (h = 2, k = 1), 00401001010
      (-theta_5, h = 4, cap 4), 01600010100 (-theta_6, h = 6, cap 7) and
      NO height-8 or height-10 rung; non-cut targets are the table's.
  P2  THE CENSUS (the kill): at every (P, r), P = 4..10, odd r, and every
      cap A = 2..13, the enumeration's member set equals the table's
      rows legal at A, and the enumeration's generators equal the table's
      pair-scan generators. Print per P the words checked, the rows, the
      mismatches; ONE mismatch in either direction KILLS the criterion
      (a member the table lacks would be a one-cap word or a break in
      D3-D5; a row the enumeration lacks would be a false expansion).
  P3  THE EQUALITY'S BOUND: at every cell the maximum of |C| over all
      legal words against (A + 1)(A F_P + 2 F_{P-1} - 2); the print is
      the theorem's inequality held on the census, a control on D2.
  P4  THE P = 11 READ: the enumeration at P = 11, every odd r, caps
      2..13, against P1's printed prediction; a missing or extra
      generator kills the prediction and is P2's mismatch at one more
      period.

THE RUN. `python prime/code/memwatch.py --limit 512
prime/code/explore_rung_existence.py` from prime/code; estimate 1 minute
(the P = 11 enumeration is a few thousand words per cap), memory trivial.

THE FINDINGS (the post-run record; every number is a print of the run).

  THE CONTROLS PASSED (105 checks): Phi(theta_j) = phi^j at every j < P
  in three cells; the expansion of phi^n - 1 as D5 states it for
  n = 0..12; the six recorded words each rebuilt by the criterion from
  its own lambda with N = -lambda_y and C = 0; Delta_A Dt_A = -C at every
  generator of the (8, ., 3) column, caps 2..13.

  F1  THE CRITERION IS THE MEMBER SET (rule at the census's scope; its
      derivation D2-D5 the theorem). Over P = 4..10, odd r, caps 2..13
      the enumeration finds 490 members and the table's rows legal at
      each cap number 490, the two sets equal at every cell and their
      indecomposables equal at every cell: zero mismatches in either
      direction. Every member to P = 10 is a table row, so no one-cap
      word exists at this scope, and every table row is a member. The
      first run mis-set the first-fit cap of a word whose deep unit sits
      at slot P - 1 when r = 1 (that slot precedes the class slot, so
      it forces h <= A - 1, the same rule the near slot r - 2 obeys);
      the two cells that showed it, (4, 3, 1) and (5, 3, 1), read clean
      once the cap reads the slot before the class slot whatever r is.

  F2  THE P = 11 COLUMN, PREDICTED THEN READ (the prediction held).
      Printed before any enumeration at P = 11: r = 1 the comb
      20010101010 alone; r = 3 the comb 10200101010, 00401001010 (h = 4,
      cap 4, -theta_5) and 01600001010 (h = 6, cap 7, -theta_6), no
      height-8 and no height-10 rung; r = 5 six words at caps 2, 4, 7,
      8, 11, 14 (10102001010, 10004010010, 10016000010, 00108010100, the
      pure tooth of height 11 with a unit at slot 8, and a height-13
      word first legal at cap 14); r = 7 three words at caps 2, 4, 7
      (10101020010, 10100040100, 10100160000); r = 9 the comb 10101010200
      alone; every row has k = 1, every comb is a table row. The
      enumeration at P = 11, odd r, caps 2..13 then finds 120 members
      against 120 table rows with zero mismatching cells: every
      predicted generator legal at a cap to 13 and no other. The hand
      slate's third r = 3 string mistyped J = {7, 9} as slots 6 and 8;
      its (h, I, J) were the print's.

  F3  THE EQUALITY'S BOUND HOLDS WITH ROOM (control on D2). Over every
      legal word at P = 4..10, odd r, caps 2, 7 and 13, the largest |C|
      against the lcm floor (A + 1)(A F_P + 2 F_{P-1} - 2) is at ratio
      0.247 (P = 10, cap 2: max |C| = 121 against 528; P = 4, cap 13:
      14 against 574).

RUN RECORD. 2026-09-05, Windows 11, Python 3, `python
prime/code/memwatch.py --limit 512 prime/code/explore_rung_existence.py`
from prime/code. One process, CPython, no BLAS. 105 checks passed, 1 s
wall against a 1-minute estimate; peak working set 16.7 MB against the
512 MB ceiling.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from explore_parity_derivation import Cell                       # noqa: E402
from explore_member_monoid import (members_at, indecomposables,   # noqa: E402
                                   lam_of, theta, comb_aligned)
from explore_deep_pairs import d_of, aligned_caps, enum_legal_cyclic  # noqa: E402
from explore_odd_doubling import direct_member                   # noqa: E402

CHECKS = 0
CAPMAX = 13


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("CONTROL FAILED: " + msg)
        sys.exit(1)


def fib(n):
    """F_n for any integer n (F_{-n} = (-1)^{n+1} F_n)."""
    if n < 0:
        return (-1) ** (n + 1) * fib(-n)
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# ---- Z[phi] as pairs (u, v) meaning u + v phi -------------------------

def zsign(z):
    """Exact sign of u + v phi."""
    u, v = z
    a, b = 2 * u + v, v                      # 2(u + v phi) = a + b sqrt5
    if a >= 0 and b >= 0:
        return 1 if (a or b) else 0
    if a <= 0 and b <= 0:
        return -1
    return (1 if a > 0 else -1) if a * a > 5 * b * b else (1 if b > 0 else -1)


def zadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def zsub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def zscale(c, x):
    return (c * x[0], c * x[1])


def phipow(e):
    """phi^e = F_{e-1} + F_e phi, any integer e."""
    return (fib(e - 1), fib(e))


def expansion(z, floor=-80):
    """Support of the base-phi expansion of z >= 0 over nonconsecutive
    powers, greedy; None if z < 0 or the expansion runs past floor."""
    if zsign(z) < 0:
        return None
    out = []
    e = 100
    while zsign(z) > 0:
        while zsign(zsub(z, phipow(e))) < 0:
            e -= 1
            if e < floor:
                return None
        out.append(e)
        z = zsub(z, phipow(e))
        e -= 2
    return out


def phi_of(cell, v):
    """Phi(u + w alpha) = w + u psi = (w - u) + (-u)... as (const, phi):
    psi = 1 - phi, so w + u psi = (w + u) - u phi."""
    u, w = v
    return (w + u, -u)


# ---- the table ---------------------------------------------------------

def legal_sets(lo, hi):
    """Nonconsecutive subsets of [lo, hi] as sorted tuples."""
    out = [()]
    for j in range(lo, hi + 1):
        out = out + [s + (j,) for s in out if not s or s[-1] < j - 1]
    return out


def table(P, r, hmax=CAPMAX):
    """Every (word, lam-in-Z[phi], h, I, J, k, first cap) the criterion
    admits at (P, r) with h <= hmax; no membership test is consulted."""
    rows = []
    for h in range(0, hmax + 1):
        for I in legal_sets(0, r - 2):
            v = zscale(h, phipow(r))
            for j in I:
                v = zadd(v, phipow(j + 1))
            k = 1
            while True:
                lam_phi = zadd(v, (k, 0))                    # Lam * phi
                # Lam = lam_phi / phi = lam_phi (phi - 1): (u + v phi)(phi - 1)
                # = (v - u) + u phi
                Lam = (lam_phi[1] - lam_phi[0], lam_phi[0])
                rhs = zsub(zscale(k, phipow(P - 1)), Lam)
                if zsign(zsub(rhs, phipow(P))) >= 0:
                    break
                J = expansion(rhs)
                k += 1
                if J is None:
                    continue
                lo = r + 1 if h else r
                if J and (min(J) < lo or max(J) > P - 1):
                    continue
                if (P - 1) in J and 0 in I:
                    continue
                e = [0] * P
                e[r - 1] = h
                for j in I:
                    e[j] = 1
                for j in J:
                    e[j] = 1
                if not any(e):
                    continue
                cap = max(1, h + (1 if h and e[(r - 2) % P] else 0))
                rows.append((tuple(e), Lam, h, I, tuple(J), k - 1, cap))
    return rows


def pair_gens(words):
    return set(indecomposables(list(words)))


def word_str(e):
    return ".".join(str(d) for d in e) if max(e) > 9 else "".join(str(d) for d in e)


def dt_of(P, A):
    return 1 + (-1) ** P - 2 * fib(P - 1) - A * fib(P)


def c_of(P, r, e):
    h = e[r - 1]
    I = [j for j in range(r - 1) if e[j]]
    J = [j for j in range(r, P) if e[j]]
    s = sum(fib(j + 1) for j in I)
    D = sum((-1) ** (P - 1 - j + 1) * fib(P - 1 - j) for j in J)
    return (h * (fib(P - r) - fib(r)) + sum((-1) ** j * fib(P - 1 - j) for j in I)
            - s + (-1) ** P * D - sum(fib(j + 1) for j in J))


def n_of(lam):
    return -lam[1]


def controls():
    print("CONTROLS")
    for (P, A) in ((7, 9), (8, 4), (9, 13)):
        c = Cell(P, A)
        for j in range(P):
            ok(phi_of(c, theta(c, j)) == phipow(j), "Phi(theta_%d) at (%d,%d)" % (j, P, A))
    # phi^n - 1 expansions (D5)
    for n in range(0, 13):
        J = expansion(zsub(phipow(n), (1, 0)))
        want = list(range(n - 1, 0, -2)) if n % 2 == 0 else list(range(n - 1, 1, -2)) + [-1]
        ok(J == want, "phi^%d - 1 expands to %s not %s" % (n, J, want))
    recorded = {(8, 8, 3): [(1, 0, 1, 0, 1, 0, 1, 0), (0, 0, 4, 0, 0, 0, 1, 0),
                            (0, 1, 6, 0, 0, 1, 0, 0), (0, 0, 8, 0, 1, 0, 0, 1)],
                (8, 11, 3): [(0, 1, 10, 0, 0, 0, 0, 1)],
                (7, 9, 3): [(0, 0, 9, 0, 0, 1, 0)]}
    for (P, A, r), words in recorded.items():
        c = Cell(P, A)
        rows = {row[0]: row for row in table(P, r)}
        gens = set(indecomposables(members_at(c, r, 1)))
        for e in words:
            ok(e in gens, "recorded generator %s absent at (%d,%d,%d)" % (word_str(e), P, A, r))
            lam = lam_of(c, r, e)
            ok(e in rows, "criterion lacks %s" % word_str(e))
            ok(rows[e][1] == phi_of(c, (-lam[0], -lam[1])), "Lam of %s" % word_str(e))
            h = e[r - 1]
            s = sum(fib(j + 1) for j in range(r - 1) if e[j])
            ok(h * fib(r) + s == n_of(lam), "N = -lambda_y at %s" % word_str(e))
            ok(c_of(P, r, e) == 0, "C = 0 at %s" % word_str(e))
    # Delta Dt = -C at every generator of the (8, ., 3) column, caps 2..13
    for A in range(2, 14):
        c = Cell(8, A)
        for e in indecomposables(members_at(c, 3, 1)):
            lam = lam_of(c, 3, e)
            h = e[2]
            s = sum(fib(j + 1) for j in range(2) if e[j])
            delta = h * fib(3) + s - n_of(lam)
            ok(delta * dt_of(8, A) == -c_of(8, 3, e), "Delta Dt = -C at (8,%d,3) %s" % (A, word_str(e)))
    print("  all controls pass (%d checks)" % CHECKS)


def predict(P):
    print("\nP1  THE PREDICTION AT P = %d (no enumeration consulted)" % P)
    out = {}
    for r in range(1, P, 2):
        rows = table(P, r)
        words = {row[0]: row for row in rows}
        gens = pair_gens(words)
        comb = comb_aligned(P, CAPMAX, r)
        print("  r = %d: %d member words with h <= %d, %d generators; comb %s %s"
              % (r, len(rows), CAPMAX, len(gens), word_str(comb),
                 "in the table" if comb in words else "NOT IN THE TABLE"))
        for e in sorted(gens, key=lambda w: (words[w][6], w)):
            _, Lam, h, I, J, k, cap = words[e]
            print("    cap %2d  %s  h=%d I=%s J=%s k=%d Lam=%s" % (cap, word_str(e), h, list(I), list(J), k, Lam))
        out[r] = (words, gens)
    return out


def census(Ps, predicted=None):
    print("\nP2  THE TABLE AGAINST THE ENUMERATION (P = %s, odd r, caps 2..%d)" % (list(Ps), CAPMAX))
    t0 = time.time()
    tot_words = tot_rows = mism = 0
    for P in Ps:
        pw = pr = pm = 0
        for r in range(1, P, 2):
            if predicted and r in predicted:
                words = predicted[r][0]
            else:
                words = {row[0]: row for row in table(P, r)}
            for A in range(2, CAPMAX + 1):
                c = Cell(P, A)
                mem = set(members_at(c, r, 1))
                rows = set(e for e, row in words.items() if row[6] <= A)
                gens_e = set(indecomposables(list(mem)))
                gens_t = pair_gens(rows)
                pw += len(mem)
                pr += len(rows)
                if mem != rows or gens_e != gens_t:
                    pm += 1
                    for e in sorted(mem - rows):
                        print("    MEMBER NOT IN TABLE (%d,%d,%d): %s" % (P, A, r, word_str(e)))
                    for e in sorted(rows - mem):
                        print("    TABLE ROW NOT A MEMBER (%d,%d,%d): %s" % (P, A, r, word_str(e)))
                    for e in sorted(gens_e ^ gens_t):
                        print("    GENERATOR MISMATCH (%d,%d,%d): %s" % (P, A, r, word_str(e)))
        print("  P = %2d: %d enumerated members, %d table rows legal, %d mismatching cells, %.0f s"
              % (P, pw, pr, pm, time.time() - t0))
        tot_words += pw
        tot_rows += pr
        mism += pm
    print("  totals: %d members, %d rows, %d mismatches -> %s"
          % (tot_words, tot_rows, mism, "KILLED" if mism else "the criterion holds"))
    return mism


def bound():
    print("\nP3  THE EQUALITY'S BOUND: max |C| over legal words vs (A+1)(A F_P + 2F_{P-1} - 2)")
    worst = 0.0
    for P in range(4, 11):
        line = []
        for A in (2, 7, 13):
            m = 0
            for r in range(1, P, 2):
                caps = aligned_caps(P, A, r, 1)
                for e in enum_legal_cyclic(caps):
                    if any(e):
                        m = max(m, abs(c_of(P, r, e)))
            lcm_lo = (A + 1) * (A * fib(P) + 2 * fib(P - 1) - 2)
            worst = max(worst, m / lcm_lo)
            line.append("A=%2d max|C|=%d lcm>=%d" % (A, m, lcm_lo))
        print("  P = %2d: %s" % (P, "; ".join(line)))
    print("  worst ratio max|C| / lcm bound = %.3f (theorem needs < 1)" % worst)


def main():
    t0 = time.time()
    controls()
    pred = predict(11)
    census(range(4, 11))
    bound()
    print("\nP4  THE P = 11 READ")
    m = census([11], predicted=pred)
    print("  P = 11 verdict: " + ("a missing or extra generator: THE PERIOD IS THE LANGUAGE is killed"
                                  if m else "every predicted generator and no other: the kill misses"))
    print("\n%d checks passed, %.0f s wall" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
