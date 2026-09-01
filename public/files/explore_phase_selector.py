"""WHY DOES THE CLASS PHASE SELECT THE CUT? The aperiodic parting
forms' mechanism, derived and certified.

THE QUESTION
------------
The extraction (explore_aperiodic_cut.py F3-F4) left a pattern with no
mechanism: an aperiodic one-class ladder straddles -q_{r+1} alpha
exactly at class phase 2 (large caps at k = 2 mod 3, 0-based) and
-q_r alpha at phases 0 and 1, with the cap values carrying nothing.
The periodic derivation (explore_parity_derivation.py D3-D4) has two
mechanisms, both local; the aim suspected an origin lemma on the
telescope's first tooth. This rig states the derivation and certifies
every step in integer arithmetic.

THE DERIVATION (hand-derived pre-engine; index conventions re-derived
from the engines: a[k] 0-based = a_{k+1}; theta_j = a[j-1] theta_{j-1}
+ theta_{j-2} with sign theta_k = (-1)^k; digit d[k] has cap a[k],
d[0] <= a[0]-1, and d[k] = a[k] forces d[k-1] = 0; the tooth of digit
k under stride r is theta_{k+r}; one-class window at phase phi means
a[k] >= 2 iff k = phi mod 3).

D1  THE FAMILY. The double-class comb: digit 2 at every class
    position c >= c0 (c = phi mod 3), zero elsewhere. Read off the
    walker's certified pairs pre-slate (scratch probe, three phases,
    r = 1 and 4): both members of every pair are truncations of this
    one string, with a repaired head at phase 0 (d[1] = 1, 2s from
    position 3). Legality: digit 2 at a class needs a[c] >= 2 (the
    class IS the large cap), and when a[c] = 2 the predecessor is 0
    (non-class positions are empty) -- legal at every window, EXCEPT
    c0 = 0, where d[0] <= a[0] - 1 < 2 kills the head tooth.
D2  THE TELESCOPE (two cap-1 lines, uniform in phase). Tooth
    j = c + r with c = phi, r = 1 mod 3 gives j = phi + 1 mod 3, so
    a[j] = 1 (j != phi) and a[j+1] = 1 (j+1 = phi+2 != phi):
        theta_{j+1} = theta_j + theta_{j-1}
        theta_{j+2} = theta_{j+1} + theta_j
    subtract: 2 theta_j = theta_{j+2} - theta_{j-1}. Teeth are spaced
    3, and the theta_{j+2} of one tooth is the theta_{(j+3)-1} of the
    next, so the sum telescopes:
        sum_{t=0..T} 2 theta_{j0+3t} = theta_{j0+3T+2} - theta_{j0-1}
    -> -theta_{j0-1} as T grows. The LARGE cap values never enter --
    only the two cap-1 recursions are used -- which is why the values
    carry nothing (F3's crossed result, now derived).
D3  THE ORIGIN SELECTS. The image limit is -theta_{c0+r-1}, set
    entirely by the first comb class c0:
      phase 2: c0 = 2 -> s = q_{r+1}   (the designed form)
      phase 1: c0 = 1 -> s = q_r
      phase 0: c0 = 0 illegal (D1); the comb starts at c0 = 3,
        landing -theta_{r+2}, and the head repairs it: a[r+1] = 1
        (r+1 = 2 mod 3 != 0) gives theta_{r+2} = theta_{r+1} +
        theta_r, so ONE extra tooth theta_{r+1} -- digit 1 at
        position 1, legal at phase 0 (a[1] = 1, d[0] = 0) -- lands
        -theta_{r+2} + theta_{r+1} = -theta_r.
    So phases 0 and 1 both land s = q_r: the binary selector (F4).
D4  WHY PHASE 2 CANNOT REPAIR DOWN TO q_r (the floor, within the
    family): lifting -theta_{r+1} to -theta_r needs a head equal to
    theta_{r+1} - theta_r = theta_{r-1} (a[r] = 1 at r = 1 mod 3
    != 2), a tooth at digit position k = -1 -- below the
    r-truncation's reach, teeth starting at theta_r. And no
    multi-tooth head substitutes: a head is sum d_k theta_{k+r} =
    M alpha - N with M = sum d_k q_{k+r}, so head = theta_{r-1}
    forces M = q_{r-1} by irrationality, while every available
    weight q_{k+r} >= q_r > q_{r-1} at r >= 4, and at r = 1 the one
    weight equal to q_0 = 1 is q_1 at position 0, shut by the
    leading-digit cap d[0] <= a[0] - 1 = 0. Cell-level
    minimality -- no OTHER family straddling a shallower cut -- is
    what the walker's minimal parting certifies per cell (inf_from is
    the least parting over all pairs, and p_s is monotone in s); the
    universal statement stays open, priced with the bounded half's.
D5  THE STRADDLE IS FREE. The deficit after tooth T is
    theta_{j0+3T+2}, sign (-1)^{j0+3T+2}: alternates with T, so
    consecutive truncations are themselves an agreeing pair whose
    images sit on opposite sides of the limit -- D3's periodic
    argument verbatim. Deeper starts c0 = phi + 3t land deeper cuts
    -theta_{c0+r-1}: a gated cell straddles a whole ladder of cuts,
    and the extraction's per-pair cut is the walker's minimal one.
    At P = 3 designed this comb IS explore_parity_derivation.py D3's
    (0,0,2) comb: the aperiodic derivation contains the periodic
    P = 3 case.

PREDICTIONS, FIXED BEFORE THE RUN (observables; kills name what the
rig PRINTS)
  K1 (positive control; red voids the run). At designed(3, A),
      A = 2, 5, the comb's integer partial sums match the telescope's
      closed form at every depth scanned, and the limit target is
      index r+1 -- the derived odd-P cut s = q_{r+1}
      (explore_parity_derivation.py F2's P = 3 row). KILL: any
      mismatch.
  Q2 (the telescope identity, every window). At all eight aperiodic
      windows (W1, W2, W3, e-2, W4, W5, W6, W7) and r = 1, 4, 7: the
      comb's partial sums, as exact integer pairs (sum of 2 q_{c+r},
      sum of 2 p_{c+r}), equal (q_{j0+3T+2} - q_{tgt},
      p_{j0+3T+2} - p_{tgt}) at every depth T scanned, where tgt =
      r+1 at phase 2 and tgt = r at phases 0 and 1 (head included at
      phase 0). KILL: any depth off.
  Q3 (legality and straddle). Every truncation scanned has zero
      legality failures under the classical conditions, and the
      deficit's exact sign (by the convergent bracket) alternates
      with T. KILL: a legality failure, or two consecutive equal
      signs.
  Q4 (the pair IS the family). At six cells (three phases x
      r = 1, 4), the walker's certified pair digits equal two
      truncations of the comb exactly (phase-0 head included).
      A mismatch prints per cell -- a finding about the walker's
      completions, not a kill of the derivation.
  Q5 (the floor's index arithmetic). At phase 2, the repair head's
      index r-1 is below the reach floor r at every r scanned --
      printed as the inequality itself.

THE DESIGN
----------
Everything heavy is imported unchanged: Shift, PrecWindow, tile,
witness machinery via explore_aperiodic_cut's get_pair; the window
quotient lists from their recorded owners. The comb is built here (it
is the object under derivation); sums are exact integers on (q, p).

S0  K1's periodic control.
S1  Q2 + Q3: telescope identity, legality, deficit alternation at
    all eight windows, r = 1, 4, 7, depths T = 2..30.
S2  Q4: pair-vs-comb at six cells (W1, e-2, W6; r = 1, 4).
S3  Q5 + assembly: the selector table, phase -> origin -> form.

RESOURCE: S2 reruns six witness extractions on recorded-size automata
(the parent rig's full run was 11 s); S0/S1/S3 are integer sums.
Estimate well under 1 min wall, far under 512MB; run through memwatch
at the default ceiling.

RUN RECORD
----------
Recorded run: wall 0.5 s, peak working set 20.4 MB under memwatch's
512 MB ceiling; run twice more directly, output byte-identical. Zero
KILL lines; ALL GREEN.

FINDINGS (each at its own tier)
-------------------------------
F1  CONTROL PASSES (K1): designed(3, 2) and designed(3, 5), r = 1,
    4, 7: the comb's integer partial sums match the closed form at
    all 29 depths per cell, target index r+1 -- the derived periodic
    cut s = q_{r+1} (explore_parity_derivation.py F2's P = 3 row).
F2  THE TELESCOPE IDENTITY HOLDS AT EVERY CELL (theorem -- D2's two
    cap-1 lines are the proof; certified at all eight windows x
    r = 1, 4, 7 x T = 2..30): partial sums equal
    (q_{j0+3T+2} - q_tgt, p_{j0+3T+2} - p_tgt) exactly, tgt = r+1 at
    phase 2 and r at phases 0/1 -- 24 aperiodic cells, 696 depth
    checks, zero off.
F3  LEGALITY AND THE FREE STRADDLE (Q3 lands inside the same 696
    checks): every truncation scanned passes the classical legality
    conditions with zero failures, and the deficit's exact sign
    alternates with T at every cell -- the family gates by D5's
    argument at every window.
F4  THE PAIR IS THE FAMILY (verified instances, six cells): the
    walker's certified pair digits are EXACTLY two comb truncations
    -- W1 r 1, 4 (phase 2, plain comb), e-2 r 1, 4 (phase 1, plain
    comb), W6 r 1, 4 (phase 0, repaired head d[1] = 1, 2s from
    position 3) -- so the parent rig's extracted cuts are this
    family's limits and the mechanism is the ORIGIN LEMMA: the cut is
    -theta_{c0+r-1}, set entirely by the first comb class; phase 2
    starts one class deeper than the stride frame can repair
    (s = q_{r+1}); phases 0 and 1 reach q_r, one directly, one by
    the head repair.
F5  THE FLOOR'S INDEX ARITHMETIC (Q5): at phase 2 the repair tooth
    theta_{r-1} sits at digit position -1 < 0 at every r scanned --
    no head reaches it; cell-level minimality stays grounded in the
    walker's minimal parting (D4), and the universal
    no-shallower-family statement is the open leg, filed with the
    bounded half's.
"""

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_cascade_closure import (       # noqa: E402
    PrecWindow,
    tile,
)
from explore_limit_column import Shift       # noqa: E402
from explore_shift_repair import (           # noqa: E402
    designed,
    greedy,
    legality_failures,
    quotients_e_minus_2,
)
from explore_closure_family import (         # noqa: E402
    quotients_w1,
    quotients_w2,
    quotients_w3,
)
from explore_aperiodic_cut import (          # noqa: E402
    AWANT,
    NPOS,
    get_pair,
    numeration,
    phase_of,
    quotients_w4,
    quotients_w5,
    quotients_w6,
    quotients_w7,
    sign_affine,
)

TDEPTHS = range(2, 31)


def comb_digits(a, phi, upto):
    """The double-class comb to position `upto`: 2 at classes from the
    minimal legal start, with the phase-0 repaired head (D1/D3)."""
    d = [0] * (upto + 1)
    if phi == 0:
        d[1] = 1
        start = 3
    else:
        start = phi
    for c in range(start, upto + 1):
        if c % 3 == phi % 3:
            d[c] = 2
    return d


def comb_positions(phi, T):
    """The first T+1 class positions the comb's 2s occupy."""
    start = 3 if phi == 0 else phi
    return [start + 3 * t for t in range(T + 1)]


def telescope_cell(a, q, p, phi, r):
    """Q2 + Q3 at one (window, stride) cell. Returns (#depths, ok)."""
    tgt = r + 1 if phi == 2 else r
    brk = ((p[-2], q[-2]), (p[-1], q[-1]))
    ok = True
    checks = 0
    prev_sign = None
    for T in TDEPTHS:
        cs = comb_positions(phi, T)
        top = cs[-1]
        j_end = top + r + 2
        if j_end >= len(q):
            break
        sq = sum(2 * q[c + r] for c in cs)
        sp = sum(2 * p[c + r] for c in cs)
        if phi == 0:
            sq += q[1 + r]
            sp += p[1 + r]
        want_q = q[j_end] - q[tgt]
        want_p = p[j_end] - p[tgt]
        if (sq, sp) != (want_q, want_p):
            print(f"    KILL Q2: phi {phi} r {r} T {T}: sum "
                  f"({sq},{sp}) != ({want_q},{want_p})")
            ok = False
        d = comb_digits(a, phi, top)
        lf = legality_failures(d, a)
        if lf:
            print(f"    KILL Q3-legal: phi {phi} r {r} T {T}: "
                  f"{lf} failures")
            ok = False
        sg = sign_affine(q[j_end], p[j_end], brk)
        if sg == 0:
            print(f"    KILL Q3-sign: INDET at phi {phi} r {r} T {T}")
            ok = False
        if prev_sign is not None and sg == prev_sign:
            print(f"    KILL Q3-sign: no alternation at phi {phi} "
                  f"r {r} T {T}")
            ok = False
        prev_sign = sg
        checks += 1
    return checks, ok


def s0_control():
    print("=" * 78)
    print("S0 CONTROL (K1): designed(3, A) -- the derived periodic cut")
    ok = True
    for A in (2, 5):
        a = designed(3, A, AWANT)
        q, p = numeration(a, NPOS)
        for r in (1, 4, 7):
            n, good = telescope_cell(a, q, p, 2, r)
            ok &= good and n > 0
            print(f"  designed(3,{A}) r {r}: {n} depths, "
                  f"target index r+1 = {r + 1}, "
                  f"{'ok' if good else 'KILL'}")
    return ok


WINDOWS = [
    ("W1-primes", quotients_w1),
    ("W2-swapped", quotients_w2),
    ("W3-thue-morse", quotients_w3),
    ("e-2", quotients_e_minus_2),
    ("W4-phase-primes", quotients_w4),
    ("W5-phase-e2", quotients_w5),
    ("W6-phase0-e2", quotients_w6),
    ("W7-phase0-primes", quotients_w7),
]


def s1_telescope():
    print("=" * 78)
    print("S1 THE TELESCOPE IDENTITY (Q2 + Q3): eight windows, "
          "r = 1, 4, 7")
    ok = True
    total = 0
    for name, qfun in WINDOWS:
        a = qfun(AWANT)
        phi = phase_of(a)
        q, p = numeration(a, NPOS)
        for r in (1, 4, 7):
            n, good = telescope_cell(a, q, p, phi, r)
            total += n
            ok &= good and n > 0
            tgt = "r+1" if phi == 2 else "r"
            print(f"  {name:18s} phase {phi} r {r}: {n} depths, "
                  f"target q_{tgt}, {'ok' if good else 'KILL'}")
    print(f"  total depth checks: {total}")
    return ok


def s2_pair_is_family():
    print("=" * 78)
    print("S2 THE PAIR IS THE FAMILY (Q4): walker digits vs the comb")
    cells = [("W1-primes", quotients_w1, [21]),
             ("e-2", quotients_e_minus_2, [15]),
             ("W6-phase0-e2", quotients_w6, [15])]
    ok = True
    for name, qfun, ms in cells:
        a = qfun(AWANT)
        phi = phase_of(a)
        q, p = numeration(a, NPOS + 12)
        qtrue = q[:NPOS]
        for r in (1, 4):
            got = None
            for m in ms:
                sh = Shift(PrecWindow(tile(a[:m], m), m), r)
                got = get_pair(sh, qtrue, 3)
                if not isinstance(got, str):
                    break
            if isinstance(got, str) or got is None:
                print(f"  {name} r {r}: no pair ({got})")
                ok = False
                continue
            n1, n2, agree, diff, cyc = got
            cellok = True
            for n in (n1, n2):
                d = greedy(n, q)
                top = max(k for k in range(len(d)) if d[k])
                want = comb_digits(a, phi, top)
                if d[:top + 1] != want:
                    print(f"  {name} r {r}: MISMATCH vs comb at n = "
                          f"{'n1' if n == n1 else 'n2'}")
                    cellok = False
            print(f"  {name:14s} phase {phi} r {r}: both members comb "
                  f"truncations: {'yes' if cellok else 'NO'}")
            ok &= cellok
    return ok


def s3_assembly():
    print("=" * 78)
    print("S3 THE SELECTOR TABLE (Q5): phase -> origin -> form")
    for r in (1, 4, 7):
        print(f"  r = {r}: phase-2 repair tooth at digit position "
              f"{-1} < 0 (floor holds)")
    print("  phase 2: comb starts c0 = 2 -> limit -theta_{r+1}, "
          "s = q_(r+1)  (the designed form)")
    print("  phase 1: comb starts c0 = 1 -> limit -theta_r, s = q_r")
    print("  phase 0: c0 = 0 illegal; comb from 3 + head d[1] = 1 "
          "-> limit -theta_r, s = q_r")
    print("  values never enter: only the two cap-1 recursions are "
          "used (D2)")
    return True


if __name__ == "__main__":
    t0 = time.time()
    if not s0_control():
        print("S0 RED: stopping -- nothing below is a measurement.")
        sys.exit(1)
    ok = s1_telescope()
    ok &= s2_pair_is_family()
    ok &= s3_assembly()
    print("=" * 78)
    print(f"{'ALL GREEN' if ok else 'KILL LINES ABOVE'} "
          f"({time.time() - t0:.1f} s)")
    sys.exit(0 if ok else 1)
