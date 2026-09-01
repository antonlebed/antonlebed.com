"""WHICH CUT DOES AN APERIODIC LADDER STRADDLE? The certified pairs'
cuts extracted by integer arithmetic, and a designed probe for what
selects the form.

THE QUESTION
------------
The parting law (explore_parity_derivation.py) reads a straddled cut
-s*alpha off its parting position p_s = min{p : q_{p+1} >= max(s, 2)},
and the two derived periodic families give two closed forms: at odd P
the cut has s = q_{r+1} and the designed parting is the stride itself;
at even P the cut has s = q_r, parting p_{q_r}. The recorded aperiodic
parting signatures are exactly these two forms: the one-class windows'
certified ladders (W1 primes, W2 swapped, W3 Thue-Morse,
explore_closure_family.py F2-F4) part at the stride, while e-2 parts at
1, 3, 6 at strides 1, 4, 7 -- p_{q_r} on its own denominators. Nothing
recorded names which CUT an aperiodic ladder actually straddles: the
parting only pins s to one q-window, (q_p, q_{p+1}] at parting p for
s >= 2, the max(s, 2) clamp folding s = 1 into s = 2's parting. This
rig extracts the exact cut from the certified pairs by integer
arithmetic and asks what selects the form.

THE PHASE SUSPICION (marked transplant -- imported from comparing the
defining quotient lists, not from any recorded derivation). The
designed periodic windows put the large cap at the LAST position of
each period (designed(): a_{k+1} large iff k = P-1 mod P, 0-based),
and W1-W3 follow that frame: larges at k = 2 mod 3. e-2's list
[1, 2, 1, 1, 4, 1, 1, 6, ...] carries its larges at k = 1 mod 3 -- one
position EARLIER. So the two windows the parting law cannot separate
by class parity (both class period 3, odd) differ in the PHASE of the
class relative to the origin. Two designed probes make that a test:

  W4 "phase-primes"  quotients_w1 dropped by one: [1, 2, 1, 1, 3,
                     1, 1, 5, ...] -- prime cap values (W1's), larges
                     at k = 1 mod 3 (e-2's phase).
  W5 "phase-e2"      a 1 prepended to e-2: [1, 1, 2, 1, 1, 4, ...]
                     -- e-2's cap values, larges at k = 2 mod 3
                     (W1's phase).

If the phase selects the form, W4 takes e-2's cut (s = q_r) and W5
takes the designed form (s = q_{r+1}); if the cap values select, the
opposite; a mixed or third print is the finding either way.

THE EXTRACTION (all integer arithmetic). A certified pair from the
walker (witness, explore_limit_column.py) is two integers n1, n2 whose
greedy digits on the TRUE window's numeration agree to `agree`
positions while their image strings -- greedy recodings of the image
values sum(d_k q_{k+r}) -- part at `diff`. The image circle points are
the shifted stars X_i = M_i alpha - N_i with M_i = sum(d_k q_{k+r}),
N_i = sum(d_k p_{k+r}), both exact integers on the window's
convergents. The pair straddles a cut, so exactly one point
-s*alpha + t (s >= 1, integers) lies strictly between X_1 and X_2 once
the pair is deep; the rig searches s = 1..q_{r+3} and certifies strict
betweenness by the sign of (M_i + s)*alpha - (N_i + t), which is
decided exactly by evaluating the integer form at two consecutive deep
convergents bracketing alpha (same nonzero sign at both = the sign).
Candidate t per s comes from a Fraction approximation by a deep
convergent; the certificate never uses floats.

THE HAND-ATTACK (pre-engine, on paper; index conventions re-derived
from the engines: build_q_positions gives q[0] = 1, q[1] = a_1,
q[k+1] = a_{k+1} q[k] + q[k-1] with a[k] = a_{k+1} 0-based; the
numerators run p[0] = 0, p[1] = 1 on the same recursion, so
theta_0 = alpha; image value = sum d_k q_{k+r}, parting = first diff
of the greedy image strings, part_pos on the window's own q).
  Consistency of the predictions with the recorded vectors. e-2's q:
    1, 1, 3, 4, 7, 32, 39, 71, ... If s = q_r then p_s at r = 1, 4, 7
    is p_1 = 1 (q_2 = 3 >= 2), p_7 = 3 (q_4 = 7 >= 7), p_71 = 6
    (q_7 = 71 >= 71): the recorded 1, 3, 6. If s = q_{r+1} on any
    strictly increasing q then p_s = r exactly: W1-W3's recorded
    part = stride. Both forms are consistent with their recorded
    partings, so the parting alone cannot separate the forms and the
    extraction adds content: the pinned window (q_p, q_{p+1}] holds
    every s from q_p + 1 up (and s = 1 rides with s = 2 under the
    clamp), so which value in it the cut takes is the measurement.
  Uniqueness of the extracted cut. The pair's interval has width
    ~|theta| at the agreement depth (agree ~ tens to 170), while
    points -s*alpha mod 1 for s <= q_{r+3} are spaced no tighter than
    ~1/q_{r+4} by three-distance -- many orders wider. So one hit is
    expected; the rig asserts the count it PRINTS and a 0 or >= 2 is
    that cell's finding, never silently skipped.
  Precision of the bracket. alpha is bracketed by the two deepest
    convergents of a 260-quotient build (q ~ 10^100+); the affine
    forms carry M_i ~ q_180 at worst, and M_i / (q_N q_{N+1}) is
    astronomically below the candidate spacing. An INDET sign (the
    two bracket evaluations disagreeing) is asserted absent.
  Control values. designed(3, 2): q = 1, 1, 2, 5, 7, 12, 29, ... so
    at r = 1 the odd-P form predicts s = q_2 = 2, part 1; at r = 7,
    s = q_8. designed(4, 2): q = 1, 1, 2, 3, 8, 11, 19, 30, 79, ...
    even-P form s = q_1 = 1 at r = 1 (part 1), s = q_3 = 3 at r = 3
    (part 2). Every control is a cell explore_parity_derivation.py
    derived, so the extracted cut is FORCED there and any departure
    is a wiring error, not a finding.

PREDICTIONS, FIXED BEFORE THE RUN (as observables; kills name what
the rig PRINTS)
  K1 (positive control; red voids the run). At the derived periodic
      cells -- odd P: (3, 2) r = 1, 7 and (5, 3) r = 1, 3, expecting
      s = q_{r+1}; even P: (4, 2) r = 1, 3 and (6, 2) r = 1, 5,
      expecting s = q_r -- the extraction prints the derived s, one
      hit each, and part_pos(q, s) equals the observed parting. KILL:
      any control cell off -- the extractor is miswired and nothing
      below is a measurement.
  Q2 (the recorded three). At W1, W2, W3, r = 1, 4, 7, the deepest
      recorded-gated closure, turns 2 and 4: (a) exactly one cut per
      pair; (b) the cut is IDENTICAL at both turns; (c) s = q_{r+1}
      of the true window and part_pos = r = observed parting. An s
      inside the pinned window but off q_{r+1} is a THIRD form -- a
      finding, not a kill.
  Q3 (e-2). Same protocol at closures m = 12 or 15: s = q_r of e-2's
      own denominators (1, 7, 71 at r = 1, 4, 7), part_pos = 1, 3, 6.
  Q4 (the phase fork -- no direction frozen; the suspicion is a
      transplant). W4 and W5 closure ladders m = 3..18, r = 1..8
      first (the verdict vector and its stability are themselves
      observables at two new windows); then extraction at the deepest
      gated cells of r = 1, 4, 7. The fork's branches: phase selects
      = W4 prints the q_r form AND W5 prints the q_{r+1} form; values
      select = the opposite pair; anything else = neither selector
      survives, open. Whichever branch, the print stands as the
      verdict on what the parting law's "why e-2" question reduces
      to.
  Q4b (phase 0 -- an extension added AFTER the first run printed the
      phase verdict, so its slate is honest about its birth: a fork
      with no frozen direction). The class sweep has a third residue;
      W6 = e-2's values at phase 0 ([2, 1, 1, 4, 1, 1, 6, ...]) and
      W7 = primes at phase 0 ([2, 1, 1, 3, 1, 1, 5, ...]) run the
      same ladder-then-extraction protocol. Whatever form phase 0
      prints -- q_r, q_{r+1}, or a third -- is the finding.
  Q5 (extraction integrity, every cell). The rig prints the hit
      count, the strict-betweenness certificate's two signs, and the
      greedy-legality of both pair members on the true window; any
      MISS/INDET/multi-hit prints as such at its cell.

THE DESIGN
----------
Everything heavy is imported unchanged: PrecWindow, tile, verdict_of
from explore_cascade_closure; Shift, limit_column, witness from
explore_limit_column; build_q_positions, designed, greedy,
quotients_e_minus_2 from explore_shift_repair; quotients_w1/w2/w3 from
explore_closure_family (the recorded instruments -- what makes K1 a
control of this rig's wiring rather than theirs).

S0  K1's periodic control cells: witness on the designed windows
    directly (they are their own closures), extraction against the
    derived cuts.
S1  THE RECORDED FOUR: W1/W2/W3 (deepest recorded-gated closures) and
    e-2, r = 1, 4, 7, turns 2 and 4, extraction per pair.
S2  THE PHASE PROBES: W4/W5 verdict ladders m = 3..18, r = 1..8 with
    the stability print, then extraction at the deepest gated cells
    of r = 1, 4, 7.
S3  ASSEMBLY: one table -- window, class phase, cap values, per-stride
    extracted form -- and the fork read off it.

RESOURCE: the parent's full grid ran 29.7 s / 41.5 MB; this rig runs
two new windows' ladders at m <= 18 plus ~40 witness extractions on
recorded-size automata. Estimate 1-4 min wall, well under 512MB; run
through memwatch at the default ceiling; stages print as they
complete.

RUN RECORD
----------
Recorded run (with the Q4b phase-0 extension): wall 11.1 s, peak
working set 24.1 MB under memwatch's 512 MB ceiling. Zero
EXPECT-MISS, CONTROL MISS, INDET, or PART-OFF lines anywhere; every
extraction that returned a pair found exactly one cut, identical at
turns 2 and 4.

FINDINGS (each at its own tier)
-------------------------------
F1  CONTROLS PASS (K1): all eight derived periodic cells extract
    exactly the derived cut -- s = q_{r+1} at (3,2) r = 1, 7 and
    (5,3) r = 1, 3 (s = 2, 74, 2, 5); s = q_r at (4,2) r = 1, 3 and
    (6,2) r = 1, 5 (s = 1, 3, 1, 8) -- with part_pos equal to the
    observed parting at every cell, both turns.
F2  THE RECORDED FOUR'S CUTS ARE THE TWO CLOSED FORMS EXACTLY
    (verified instances; Q2 and Q3 land whole). W1/W2/W3 at
    r = 1, 4, 7 straddle s = q_{r+1} of their own numeration (W1:
    2, 12, 98; W2: 2, 16, 98; W3: 2, 12, 98), parting = r = p_s.
    e-2 straddles s = q_r (1, 7, 71), parting 1, 3, 6 = p_{q_r}. No
    third form: every extracted s is a DENOMINATOR of its own window,
    q_r or q_{r+1}, never a value between them -- and at r = 1, where
    the max(s, 2) clamp makes the partings of s = 1 and s = 2
    identical, the extraction separates what the parting cannot
    (e-2's cut is -alpha, W1's is -2alpha, same parting 1).
F3  THE CLASS PHASE SELECTS THE FORM AND THE CAP VALUES DO NOT
    (pattern, eight aperiodic windows in a crossed design; Q4's phase
    branch fires exactly). W4 -- prime caps at e-2's phase 1 -- takes
    e-2's cut s = q_r (1, 7, 57 at r = 1, 4, 7, parting 1, 3, 6);
    W5 -- e-2's caps at the designed phase 2 -- takes the designed
    cut s = q_{r+1} (2, 12, 122, parting = r). Prime values and 2n
    values each appear at both forms, so the values carry nothing;
    the 0-based residue mod 3 of the large caps decides.
F4  PHASE 0 SIDES WITH PHASE 1, WITH ITS OWN PARTING VECTOR
    (observation, two windows; Q4b's fork). W6 and W7 (2n and primes
    at phase 0) both straddle s = q_r (W6: 2, 23, 334; W7: 2, 18,
    228 at r = 1, 4, 7), parting 0, 3, 6 = p_{q_r} on their own
    denominators (part 0 at r = 1 because q_1 = 2 >= 2 there). So
    the selector is binary, not ternary: the designed form
    s = q_{r+1} appears EXACTLY at phase 2 -- the class at the last
    slot of its residue frame, the seat the designed periodic
    construction gives it -- and every other phase takes s = q_r.
F5  BOTH PROBE FAMILIES REPRODUCE THE PARITY LADDER (observation,
    beside Q4/Q4b's headline): all four designed windows' closure
    verdicts stabilize from m = 12 to G b b G b b G b -- gated
    r = 1, 4, 7 -- the recorded one-class vector, at every phase.
    The strides gated only in shallow seam-corrupted closures
    (r = 3, 5, 6, 8 at m <= 11) refuse the walker exactly as the
    recorded non-transfer signature: MISS-greedy on the true window
    or an empty bracket, at every attempt.
"""

import os
import sys
import time
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_cascade_closure import (       # noqa: E402
    PrecWindow,
    tile,
    verdict_of,
)
from explore_limit_column import (           # noqa: E402
    Shift,
    limit_column,
    witness,
)
from explore_shift_repair import (           # noqa: E402
    build_q_positions,
    designed,
    greedy,
    quotients_e_minus_2,
)
from explore_closure_family import (         # noqa: E402
    quotients_w1,
    quotients_w2,
    quotients_w3,
)

AWANT = 260          # quotients built per window
NPOS = 200           # numeration positions handed to the walker
EXT = 12             # extra positions for image weights q_{k+r}


# ------------------------------------------------------------- numeration

def build_p_positions(a, npos):
    """Convergent numerators on build_q_positions' recursion."""
    p = [0, 1]
    while len(p) <= npos and len(p) <= len(a):
        p.append(a[len(p) - 1] * p[-1] + p[-2])
    return p


def numeration(a, npos):
    q = build_q_positions(a, npos)
    p = build_p_positions(a, npos)
    n = min(len(q), len(p))
    return q[:n], p[:n]


# ------------------------------------------------------- exact sign tests

def sign_affine(x, y, brk):
    """Sign of x*alpha - y, alpha bracketed by consecutive convergents
    (pa/qa, pb/qb). Returns +1/-1, or 0 for INDET (never expected)."""
    (pa, qa), (pb, qb) = brk
    va = x * pa - y * qa
    vb = x * pb - y * qb
    if va > 0 and vb > 0:
        return 1
    if va < 0 and vb < 0:
        return -1
    return 0


def extract_cut(stars, r, q, p, brk, s_max):
    """All cuts -s*alpha + t strictly between the two image stars.

    stars = [(M1, N1), (M2, N2)] with X_i = M_i alpha - N_i. Returns
    (hits, lo_sign_ok) where hits is a list of (s, t)."""
    (M1, N1), (M2, N2) = stars
    order = sign_affine(M1 - M2, N1 - N2, brk)
    if order == 0:
        return None, "INDET-order"
    if order > 0:
        (Mlo, Nlo), (Mhi, Nhi) = (M2, N2), (M1, N1)
    else:
        (Mlo, Nlo), (Mhi, Nhi) = (M1, N1), (M2, N2)
    (pa, qa), (pb, qb) = brk
    af = Fraction(pb, qb)
    xlo = Mlo * af - Nlo
    xhi = Mhi * af - Nhi
    hits = []
    for s in range(1, s_max + 1):
        tlo = s * af + xlo
        thi = s * af + xhi
        t0 = tlo.numerator // tlo.denominator   # floor
        for t in (t0, t0 + 1, t0 + 2):
            if not (tlo < t < thi):
                continue
            s1 = sign_affine(Mlo + s, Nlo + t, brk)
            s2 = sign_affine(Mhi + s, Nhi + t, brk)
            if s1 == 0 or s2 == 0:
                return None, "INDET-cut"
            if s1 < 0 < s2:
                hits.append((s, t))
    return hits, "ok"


# ------------------------------------------------------------ the walker

def get_pair(sh, qtrue, turns):
    """A certified pair at `turns` cycle turns, or a string tag."""
    lc = limit_column(sh)
    if verdict_of(lc) != "GATED":
        return "not-gated"
    t = lc["inf_from"]
    for tt in range(t, t + 7):
        try:
            got = witness(sh, tt, turns, qtrue)
        except AssertionError:
            return "MISS-greedy"
        if got is not None:
            return got
    return "no-pair"


def form_name(s, q, r):
    if r < len(q) and s == q[r]:
        return "q_r"
    if r + 1 < len(q) and s == q[r + 1]:
        return "q_{r+1}"
    return "OTHER"


def part_pos(q, s):
    s = max(s, 2)
    pp = 0
    while q[pp + 1] < s:
        pp += 1
    return pp


def run_cell(tag, sh, a, r, expect=None):
    """Extract the cut at one (window, stride) cell, both turns.
    Returns the set of (s, t, form) seen, or None."""
    q, p = numeration(a, NPOS + EXT)
    qtrue = q[:NPOS]
    brk = ((p[-2], q[-2]), (p[-1], q[-1]))
    s_max = q[min(r + 3, len(q) - 1)]
    seen = []
    for turns in (2, 4):
        got = get_pair(sh, qtrue, turns)
        if isinstance(got, str):
            print(f"  {tag} r {r} turns {turns}: {got}")
            continue
        n1, n2, agree, diff, cyc = got
        d1, d2 = greedy(n1, q), greedy(n2, q)
        stars = []
        for d in (d1, d2):
            assert all(d[k] == 0 for k in range(len(d) - r, len(d))), \
                "digit above the image range -- raise NPOS/EXT"
            M = sum(d[k] * q[k + r] for k in range(len(d) - r) if d[k])
            N = sum(d[k] * p[k + r] for k in range(len(d) - r) if d[k])
            stars.append((M, N))
        hits, status = extract_cut(stars, r, q, p, brk, s_max)
        if hits is None:
            print(f"  {tag} r {r} turns {turns}: {status}")
            continue
        if len(hits) != 1:
            print(f"  {tag} r {r} turns {turns}: {len(hits)} hits "
                  f"{hits} -- NOT UNIQUE")
            continue
        s, t = hits[0]
        fm = form_name(s, q, r)
        pp = part_pos(q, s)
        qr = q[r] if r < len(q) else None
        qr1 = q[r + 1] if r + 1 < len(q) else None
        ok_part = "ok" if pp == diff else "PART-OFF"
        exp = ""
        if expect is not None:
            exp = ("  expect ok" if s == expect
                   else f"  EXPECT-MISS (want {expect})")
        print(f"  {tag} r {r} turns {turns}: agree {agree} part {diff}"
              f" cut s = {s} (q_r {qr}, q_r+1 {qr1}) form {fm}"
              f" p_s {pp} {ok_part} cycle {cyc}{exp}")
        seen.append((s, t, fm))
    return seen


# --------------------------------------------------------------- windows

def quotients_w4(want):
    """W1's primes dropped by one: larges at k = 1 mod 3."""
    return quotients_w1(want + 1)[1:]


def quotients_w5(want):
    """A 1 prepended to e-2: e-2's values, larges at k = 2 mod 3."""
    return [1] + quotients_e_minus_2(want)[:want - 1]


def quotients_w6(want):
    """e-2's values at phase 0: larges at k = 0 mod 3."""
    return [2 * (k // 3 + 1) if k % 3 == 0 else 1 for k in range(want)]


def quotients_w7(want):
    """Primes at phase 0: larges at k = 0 mod 3."""
    return quotients_w1(want + 2)[2:]


def phase_of(a):
    """0-based residue mod 3 of the first cap above 1."""
    for k, c in enumerate(a):
        if c > 1:
            return k % 3
    return None


# ---------------------------------------------------------------- stages

def s0_controls():
    print("=" * 78)
    print("S0 CONTROLS: extraction against the derived periodic cuts (K1)")
    ok = True
    cells = [(3, 2, (1, 7), "odd"), (5, 3, (1, 3), "odd"),
             (4, 2, (1, 3), "even"), (6, 2, (1, 5), "even")]
    for P, A, rs, par in cells:
        a = designed(P, A, AWANT)
        caps = designed(P, A, 70)
        q, _p = numeration(a, NPOS + EXT)
        for r in rs:
            expect = q[r + 1] if par == "odd" else q[r]
            sh = Shift(PrecWindow(caps, P), r)
            seen = run_cell(f"designed({P},{A})", sh, a, r, expect)
            good = (len(seen) == 2
                    and len({x[:2] for x in seen}) == 1
                    and seen[0][0] == expect)
            ok &= good
            if not good:
                print(f"    designed({P},{A}) r {r}: CONTROL MISS")
    return ok


def s1_recorded_four():
    print("=" * 78)
    print("S1 THE RECORDED FOUR: W1/W2/W3 + e-2, r = 1, 4, 7 (Q2, Q3)")
    runs = [("W1-primes", quotients_w1(AWANT), [24, 21, 18]),
            ("W2-swapped", quotients_w2(AWANT), [21, 18, 15]),
            ("W3-thue-morse", quotients_w3(AWANT), [21, 18, 15]),
            ("e-2", quotients_e_minus_2(AWANT), [15, 12, 18])]
    forms = {}
    for name, a, ms in runs:
        for r in (1, 4, 7):
            seen = []
            for m in ms:
                sh = Shift(PrecWindow(tile(a[:m], m), m), r)
                seen = run_cell(f"{name} m {m}", sh, a, r)
                if seen:
                    break
            forms[(name, r)] = seen
    return forms


def s2_phase_probes():
    print("=" * 78)
    print("S2 THE PHASE PROBES: W4/W5 ladders, then extraction (Q4)")
    forms = {}
    for name, a in (("W4-phase-primes", quotients_w4(AWANT)),
                    ("W5-phase-e2", quotients_w5(AWANT)),
                    ("W6-phase0-e2", quotients_w6(AWANT)),
                    ("W7-phase0-primes", quotients_w7(AWANT))):
        print(f"  {name} (larges at k = {phase_of(a)} mod 3):"
              f" closure verdicts m = 3..18, r = 1..8")
        gated = {}
        for m in range(3, 19):
            vec = ""
            for r in range(1, 9):
                v = verdict_of(limit_column(
                    Shift(PrecWindow(tile(a[:m], m), m), r)))
                vec += {"GATED": "G", "delay-0": "0", "bounded": "b"}[v]
                if v == "GATED":
                    gated.setdefault(r, []).append(m)
            print(f"    m {m:2d}: {vec}")
        for r in sorted(gated):
            ms = gated.get(r, [])
            seen = []
            for m in reversed(ms[-3:]):
                sh = Shift(PrecWindow(tile(a[:m], m), m), r)
                seen = run_cell(f"{name} m {m}", sh, a, r)
                if seen:
                    break
            forms[(name, r)] = seen
    return forms


def s3_assembly(forms):
    print("=" * 78)
    print("S3 ASSEMBLY: window, phase, values, extracted form per stride")
    rows = [("W1-primes", 2, "primes"), ("W2-swapped", 2, "primes-swap"),
            ("W3-thue-morse", 2, "2/3 TM"), ("e-2", 1, "2n"),
            ("W4-phase-primes", 1, "primes"), ("W5-phase-e2", 2, "2n"),
            ("W6-phase0-e2", 0, "2n"), ("W7-phase0-primes", 0, "primes")]
    for name, phase, vals in rows:
        cells = []
        for r in (1, 4, 7):
            seen = forms.get((name, r), [])
            fs = {x[2] for x in seen}
            cells.append(f"r{r} {'/'.join(sorted(fs)) if fs else '-'}")
        print(f"  {name:18s} phase {phase} values {vals:12s} "
              + "  ".join(cells))


if __name__ == "__main__":
    t0 = time.time()
    if not s0_controls():
        print("S0 RED: stopping -- nothing below is a measurement.")
        sys.exit(1)
    forms = s1_recorded_four()
    forms.update(s2_phase_probes())
    s3_assembly(forms)
    print(f"wall {time.time() - t0:.1f} s")
