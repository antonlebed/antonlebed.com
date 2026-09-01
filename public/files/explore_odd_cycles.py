"""The odd-residue cycle chart: what the interior cycles at the gated
cells ARE — the one uncharted leg of the cycle classification.

THE QUESTION
------------
The deficit-graph criterion (explore_bounded_half.py) decides the
bounded half per cell and CLASSIFIES the even-residue cycles: telescope
combs only, zero interior. At the odd residues — the gated cells —
interior cycles exist (the derivation's comb families land ON cuts) and
nothing beyond the combs is classified: (2, 3, 1) prints the integer
multiples k(1 - alpha), k = 1..3, and (6, 4, 3) an 11-state branching
SCC. This rig charts the odd-residue cycle sets over the full grid,
reads them against the comb orbits and a multiples law, and asks where
the even-residue four-step theorem chain breaks at odd r.

THE HAND-ATTACK (pre-engine, on paper; index conventions re-derived
from the engines: digit caps A at k = P-1 mod P, aligned caps A at
j = r-1 mod P, d_of(e, r)_k = e_{(k+r) mod n}; theta_k = q_k alpha
- p_k; w = sum e_j q_j; phi = w* - w with w* the mirrored signed sum;
N_m = p_{mP-1} + q_{mP} - 2; chain semantics need mP even)
----------------------------------------------------------------------
H1  WHAT A CYCLE IS. By the criterion rig's D6, unrolled: a cycle IS
    a periodic legal pattern whose tail value V = S_m/(1 - eta^m)
    lands in L, its states the suffix-value orbit; conjugate
    positivity is free. So the odd-residue chart is exactly: which
    legal periodic patterns land lattice tail values at odd r.
H2  THE DERIVED COMBS MUST APPEAR. At odd P and EVERY odd r the
    gating comb (1 at even in-period positions 2..P-3, 2 at the
    class) has lambda = Psi/(1 - eta) in L
    (explore_parity_derivation.py s3); at even P and every odd r the
    comb of 1s at odd positions telescopes to -theta_r
    (explore_parity_derivation.py s4). Both are period-P legal
    patterns with lattice values: their deficit orbits are subsets of
    the cycle sets — the positive control tying this rig to the
    derivation.
H3  THE MULTIPLES MECHANISM. S is linear in the digits, so if d is a
    member and k*d is legal (digit-wise scaling), k*d is a member
    with value kV. Scaling preserves legality only where d's support
    sits at class slots with headroom (a supported cap-1 slot pins
    k = 1). At (2, 3, 1) the comb is [0, 1], support the class slot
    alone, scalings k <= A = 3 — exactly the recorded k(1 - alpha),
    k = 1..3. TRANSPLANT, flagged: whether "value set = the legal
    multiples of one generator" survives at cells whose combs touch
    cap-1 slots, and at the branching cells, is the run's question,
    not an expectation.
H4  BRANCHING IS A SUBSHIFT. A branching SCC (a cycle state with two
    in-SCC successors) certifies infinitely many distinct periodic
    patterns landing lattice values — qualitatively beyond any comb
    list. Where the box holds several lattice points whose mutual
    differences are reachable by digit swaps, loops can interleave.
    No closed shape frozen: the chart prints SCC sizes and branching
    counts as data.
H5  THE CHAIN AT ODD r. The even-residue theorem chain: (1) member
    => Phi == 0 mod N_m, and |Phi| <= Dmax < N_m forces Phi = 0;
    (2) on Phi = 0, membership <=> q_{mP-1} | w, w = t q_{mP-1};
    (3) w* <= q_{mP-1} - 1 (odd P) forces t = 0; (4) t = 0 census
    forces the zero pattern. At odd r nonzero members EXIST, so some
    step dies. The layer (1) is an identity in the lattice frame
    whose proof consumes det H^m = +1 (mP even) and never r, so the
    expectation (TRANSPLANT from the even-r chain, flagged) is that
    members sit at Phi = 0 with q_{mP-1} | w and t >= 1 — the
    W*-BOUND step (3) is the one that dies, the class cap landing on
    slots the mirrored-caps telescope cannot cover. Hand-check at
    (2, 3, 1), m = 1: q_{n-1} = 1, member [0, k] has w = t = k >= 1
    and max legal w = 3 > q_{n-1} - 1 = 0. The kill-shape observable
    is a member row printing Phi % N != 0 — the layer itself dying.

FINDINGS (all stages green; final form run twice byte-identical,
464 lines; record at the end)
----------------------------------------------------------------------
F1  CONTROLS PASS (N1): (2, 3, 1) prints 6 cycle states — 4
    interior, 2 endpoint — carrying exactly the 3 values k(1 -
    alpha), k = 1..3 (the criterion rig's F6 counts loops BY VALUE:
    three 2-loops); (6, 4, 3) the 11-state single branching SCC; the
    derived comb orbit is contained in the cycle set at ALL 48
    odd-residue cells (P = 2..8, A = 2..4), zero misses; the even-r
    chain controls land (zero members at the odd-P even-r cells, the
    even-P even-r comb at t = 1).
F2  THE COMB IS ALMOST ALWAYS EVERYTHING (N2 + N3): at 42 of 48
    cells the cycle set EQUALS the union of legal scaled comb orbits
    — one P-state SCC (the comb loop) at P >= 4, the scaled family
    k = 1..A at P = 2 and k <= A/2 at P = 3 (class-slot support
    scales; a supported cap-1 slot pins k = 1). All interior at
    P >= 3; at P = 2 the top scaling k = A sits at the endpoint.
    The six exceptions are ALL at A = 4 — (4, 4, 1), (5, 4, 1),
    (6, 4, 3), (7, 4, 3), (8, 4, 3), (8, 4, 5) — where a SECOND
    member family joins: fused into one branching SCC of 11-13
    states at the r = 3, 5 cells, a second P-loop with a bridging
    branch state at the r = 1 cells. At the FUSED cells branching
    = a subshift: at m = 2 the two period-P members concatenate
    freely (all four mixed words are members, e.g. 004000101010 at
    (6, 4, 3)); at the r = 1 cells they do not (two members at
    m = 2, each loop its own square).
F3  THE VALUE LAW (observation, every member printed at the 48-cell
    grid, m <= 2): every member value is a landed CUT — v = -theta_j
    exactly, or t(-theta_j) for the scaled families — with the comb
    carrying j = r at even P and j = r + 1 at odd P (the gated
    derivation's own cuts -q_r alpha and s = q_{r+1}), and EVERY
    second family carrying j = r + 2, both parities: the deeper cut
    one index down, e.g. comb v = 2 - 3a = -theta_3 and tooth
    v = 5 - 8a = -theta_5 at (6, 4, 3). The suffix values (the
    other cycle states) are the orbit's deficits, not cuts; the
    multiples reading of (2, 3, 1) is the class-slot-support
    special case (P <= 3), NOT the general law — the (4, 4, 1) and
    (5, 4, 1) t = 2 members land -theta_{r+2}, not twice the comb
    value.
F4  WHICH CHAIN STEP DIES AT ODD r (N4): at every odd-residue
    instance swept (48 cells, m in {1, 2} even-P / {2} odd-P, mP
    even): the congruence layer HOLDS — every member has Phi = 0
    exactly (not merely 0 mod N_m); the census divisibility HOLDS —
    q_{mP-1} | w at every member, t >= 1; the MASS bound
    Dmax < N_m HOLDS at every instance (the mass theorem's
    inequality is r-parity-blind at scanned scope); and the ONE
    step that dies is the extremal w* bound: max legal
    w* = sum e_j (-1)^j q_{mP-2-j} exceeds q_{mP-1} - 1 at EVERY
    odd-residue instance (against <= q_{mP-1} - 1 at odd-P even-r
    and = q_{mP-1} at even-P even-r), exactly the transport
    reading — the class cap lands where the mirrored-caps telescope
    needs cap 1, and the overflow admits t >= 1.
F5  THE TOOTH CRITERION (N5, s3 all pass): the single class-slot
    tooth of height h is a member iff h0 | h, where h0 is the order
    of theta_{P-1+r}'s class in L/(1 - eta)L (h0 divides the index
    |det(I - H)|, computed exactly per cell); the pure-tooth cycle
    exists iff h0 <= A — on the grid exactly P <= 3 (h0 = 1, 2) and
    (6, 4, 3) (h0 = 4 = A, index 40). Elsewhere h0 sits at 4..87,
    mostly AT the full index: the tooth's rarity is the class
    order's size. The other five A = 4 second families are NOT pure
    teeth (tooth-plus-unit-digit words, e.g. 00400010 at
    (8, 4, 3)); their values still land -theta_{r+2} (F3).
F6  THE PARITY CONTRAST, completed: even residues carry only
    extremal-pinned cycles (endpoint, the telescope combs) and odd
    residues carry interior cycles landing genuine cuts — with the
    deficit criterion this is the WHOLE bounded/gated split read
    off one graph invariant: cycles at endpoints cannot straddle
    (touch without crossing), interior cycles produce the two-sided
    straddle. The odd-residue census is now CHARTED at scanned
    scope: comb cuts everywhere, one deeper-cut family exactly
    where the cap A = 4 admits it.

PREDICTIONS (frozen before the run; observables)
  N1 (controls; red voids the run): (a) (2, 3, 1) prints 3 cycle
      states — 2 interior, 1 endpoint — with values k(1 - alpha),
      k = 1..3; (6, 4, 3) prints an 11-state single SCC with
      branching. (b) The derived comb orbit is a SUBSET of the cycle
      set at every odd-residue grid cell (P = 2..8, A = 2..4).
      (c) The chain stage's even-r controls: zero nonzero members at
      the odd-P even-r cells, and the even-P even-r comb prints
      t = 1.
  N2 (the chart): per-cell counts print — box, cycle states,
      interior/endpoint, SCC sizes, branching states, distinct
      values, value rank. No shape frozen: this is the uncharted
      leg.
  N3 (the readings): per cell, whether the value set equals
      {k * v0 : k = 1..K} for a single generator v0, and whether the
      cycle set equals the union of the legal scaled comb orbits;
      exceptions print with witnesses.
  N4 (the chain): per member, whether Phi == 0 mod N, whether
      Phi == 0, whether q_{mP-1} | w, and t = w / q_{mP-1}; per
      cell, max legal w vs q_{mP-1} and Dmax vs N_m. Kill-shape
      observable: a member with Phi % N != 0.

THE DESIGN
----------
Exact end to end; every engine imported from the shipped rigs, not
re-implemented: Rig, comb_orbit (explore_bounded_half), odd_comb,
alt_comb, Cell (explore_parity_derivation), aligned_caps,
enum_legal_cyclic, d_of, phi_of, w_of, dp_max, gvec
(explore_deep_pairs), n_m (explore_congruence_kill), direct_member
(explore_odd_doubling — no norm assumption, so m = 1 at odd P is
testable where used). Stages:
  s0  N1(a)+(b): the two anchor cells against their recorded data;
      comb-orbit containment at all 48 odd-residue cells.
  s1  N2+N3: the chart — per cell the SCC decomposition of the
      cycle-set subgraph, values, rank, the multiples reading, and
      the scaled-comb-orbit comparison.
  s2  N4+N1(c): the chain quantities per member — enumeration at
      mP even (odd P: m = 2; even P: m = 1, 2), membership by
      direct_member, per-member (Phi mod N, Phi, w mod q, t, and the
      value v = S/(1 - eta^m) read off the sublattice solve), per
      cell the max legal MIRRORED sum w* (the step-3 quantity,
      weights (-1)^j q_{n-2-j}) and Dmax; the even-r control cells
      through the same code path; every member's deficit orbit
      asserted a subset of the cell's cycle set (ties s2 to s1
      through H1).
  s3  N5: the tooth criterion — the second family seen at A = 4 is
      the single tooth at the digit class slot (height h, value
      h theta_{P-1+r}/(1 - eta)); per cell probe the minimal member
      height h0 (h = 1..60) and read the tooth cycle as h0 <= A.
One command runs all; wall-clock estimate ~2 min; memory trivial.

N5 (frozen before s3's first run; the six A = 4 second-family
cells are the transplant source): per cell the admitting heights
print; membership h theta in (1 - eta)L is linear in h WITHIN a
cell, so the admitting set must be the multiples of its minimum h0
(asserted); the cycle-vs-no-cycle chart of s1 must reproduce as
h0 <= A vs h0 > A at every cell where the beyond-comb family was
the tooth. Kill-shape observable: an admitting set that is not the
multiples of its minimum.

FIRST-RUN CORRECTIONS (the record of the slate's own errors, kept
beside the findings they graded):
  * N1(a) as first frozen said (2, 3, 1) prints 3 cycle states —
    a misreading of the criterion rig's F6, which counts LOOPS BY
    VALUE ("the multiples k(1 - alpha), each its own 2-loop"): a
    2-loop is two states, so the state count is 6 (4 interior, 2
    endpoint at k = 3), which is what the machine printed on the
    unchanged data. The control now asserts the corrected counts.
  * The first draft's step-3 line computed max legal w = sum e_j q_j
    where the chain's step-3 quantity is the MIRRORED sum
    w* = sum e_j (-1)^j q_{n-2-j}; the even-r control contradicting
    the shipped theorem (printed 19 > 12 at (3, 2, 2) where
    explore_odd_m2_bound F3 proves w* <= q_{n-1} - 1) was the tell.
    Repaired to the mirrored weights; no verdict had been read off
    the wrong line.
  * s3's first probe capped heights at 60 and read "multiples of
    the minimum" across a range with None rows; the exact form
    (h0 = least admitting divisor of |det(I - H)|) replaced it,
    with the 1..60 sweep kept as the multiples control. The first
    exact draft asserted h0 | N_1 = tr H - 2 and the machine killed
    it at (5, 2, 1) (h0 = 8, N_1 = 14, index 16): N_1 is the index
    only at even P (det H = +1); at odd P the index is |tr H|. The
    shipped
    form computes |det(I - H)| directly and is parity-free.

RUN RECORD: python explore_odd_cycles.py — s0..s3, ~53 s wall,
memory trivial, exit 0; final form run twice byte-identical
(464 lines), s0 GREEN s3 GREEN, every member orbit asserted inside
its cell's cycle set.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_parity_derivation import Cell, odd_comb, alt_comb  # noqa: E402
from explore_bounded_half import Rig, comb_orbit                # noqa: E402
from explore_deep_pairs import (                                # noqa: E402
    aligned_caps, enum_legal_cyclic, d_of, phi_of, w_of, dp_max, gvec)
from explore_congruence_kill import n_m                         # noqa: E402
from explore_odd_doubling import direct_member                  # noqa: E402


def odd_res_cells():
    return [(P, A, r) for P in range(2, 9) for A in (2, 3, 4)
            for r in range(1, P, 2)]


def derived_comb(P, A):
    """The gating comb in digit coordinates (H2)."""
    return odd_comb(P, A, 1) if P % 2 == 1 else alt_comb(P, P)


def sccs_of(graph, nodes):
    """SCC partition of the induced subgraph on `nodes` (iterative
    Tarjan); returns SCCs of size > 1 plus self-loops."""
    sub = {n: [x for x in graph[n] if x in nodes] for n in nodes}
    index, low, on, stk = {}, {}, {}, []
    result, counter = [], [0]
    for start in sub:
        if start in index:
            continue
        work = [(start, iter(sub[start]))]
        index[start] = low[start] = counter[0]
        counter[0] += 1
        stk.append(start)
        on[start] = True
        while work:
            v, it = work[-1]
            advanced = False
            for nxt in it:
                if nxt not in index:
                    index[nxt] = low[nxt] = counter[0]
                    counter[0] += 1
                    stk.append(nxt)
                    on[nxt] = True
                    work.append((nxt, iter(sub[nxt])))
                    advanced = True
                    break
                elif on.get(nxt):
                    low[v] = min(low[v], index[nxt])
            if advanced:
                continue
            work.pop()
            if work:
                pv = work[-1][0]
                low[pv] = min(low[pv], low[v])
            if low[v] == index[v]:
                scc = []
                while True:
                    n = stk.pop()
                    on[n] = False
                    scc.append(n)
                    if n == v:
                        break
                result.append(scc)
    keep = []
    for scc in result:
        if len(scc) > 1 or scc[0] in sub[scc[0]]:
            keep.append(sorted(scc))
    return keep, sub


def legal_digit_cyclic(d, caps):
    """Cyclic legality in digit coordinates: cap per position, cap-1
    after a nonzero, wrap included."""
    n = len(d)
    P = len(caps)
    for j in range(n):
        top = caps[j % P] - (1 if d[(j - 1) % n] > 0 else 0)
        if d[j] < 0 or d[j] > top:
            return False
    return True


def multiples_read(vals):
    """Is the value set {k*v0 : k in K} for one generator? Returns
    (v0, sorted ks) or None."""
    for v0 in sorted(vals, key=lambda v: (abs(v[0]) + abs(v[1]), v)):
        ks = set()
        ok = True
        for v in vals:
            if v0[0] * v[1] != v0[1] * v[0]:
                ok = False
                break
            k = v[0] // v0[0] if v0[0] != 0 else v[1] // v0[1]
            if k < 1 or (k * v0[0], k * v0[1]) != v:
                ok = False
                break
            ks.add(k)
        if ok:
            return v0, sorted(ks)
    return None


def value_rank(vals):
    vals = list(vals)
    if not vals:
        return 0
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            if vals[i][0] * vals[j][1] != vals[i][1] * vals[j][0]:
                return 2
    return 1


def el(u, w):
    return f"{u}{w:+d}a"


def cell_data(P, A, r):
    """Rig + cycle set + SCC decomposition + graph, once per cell."""
    rig = Rig(P, A, r)
    n, cyc, endp, inter = rig.verdict()
    graph = {nd: rig.edges_from(nd, {x: True for x in cyc})
             for nd in cyc}
    sccs, sub = sccs_of(graph, set(cyc))
    branch = sum(1 for nd in sub if len(set(sub[nd])) > 1)
    return rig, n, set(cyc), endp, inter, sccs, branch


def s0():
    print("=" * 74)
    print("S0 CONTROLS: the two anchor cells; comb-orbit containment"
          " at all odd-residue cells")
    bad = 0
    rig, n, cyc, endp, inter, sccs, branch = cell_data(2, 3, 1)
    vals = {(u, w) for (_, _, u, w) in cyc}
    ok = (len(cyc) == 6 and len(inter) == 4 and len(endp) == 2
          and vals == {(1, -1), (2, -2), (3, -3)})
    print(f"  (2,3,1): cyc={len(cyc)} int={len(inter)} "
          f"end={len(endp)} vals={sorted(vals)} "
          f"{'ok' if ok else '<-- OFF THE RECORD'}")
    bad += 0 if ok else 1
    rig, n, cyc, endp, inter, sccs, branch = cell_data(6, 4, 3)
    ok = (len(cyc) == 11 and len(sccs) == 1 and branch > 0)
    print(f"  (6,4,3): cyc={len(cyc)} sccs={[len(s) for s in sccs]} "
          f"branching={branch} {'ok' if ok else '<-- OFF THE RECORD'}")
    bad += 0 if ok else 1
    miss = 0
    for (P, A, r) in odd_res_cells():
        rig = Rig(P, A, r)
        _, cyc, _, _ = rig.verdict()
        orb = comb_orbit(rig, derived_comb(P, A))
        if not orb <= set(cyc):
            miss += 1
            print(f"  P={P} A={A} r={r}: comb orbit NOT contained "
                  f"({len(orb - set(cyc))} states outside)")
    print(f"  comb-orbit containment: {len(odd_res_cells())} cells, "
          f"{miss} misses")
    bad += miss
    print(f"  {'PASS' if bad == 0 else 'FAIL'}")
    return bad == 0


def s1():
    print("=" * 74)
    print("S1 THE CHART + READINGS: per odd-residue cell")
    for (P, A, r) in odd_res_cells():
        rig, n, cyc, endp, inter, sccs, branch = cell_data(P, A, r)
        vals = {(u, w) for (_, _, u, w) in cyc}
        rk = value_rank(vals)
        mr = multiples_read(vals)
        mstr = (f"v0={el(*mr[0])} ks={mr[1]}" if mr else "NOT multiples")
        # scaled-comb-orbit union
        comb = derived_comb(P, A)
        union = set()
        notes = []
        k = 1
        while True:
            kd = [k * x for x in comb]
            if not legal_digit_cyclic(kd, rig.caps):
                break
            if direct_member(rig.cell, r, kd, 1):
                union |= comb_orbit(rig, kd)
            else:
                notes.append(f"k={k} legal non-member")
            k += 1
        eq = "EQ" if union == cyc else \
            f"excess={len(cyc - union)} missing={len(union - cyc)}"
        print(f"  P={P} A={A} r={r}: box={n} cyc={len(cyc)} "
              f"int={len(inter)} end={len(endp)} "
              f"sccs={[len(s) for s in sccs]} branch={branch} "
              f"vals={len(vals)} rank={rk}")
        print(f"      {mstr}; combs(k<={k - 1}): {eq}"
              f"{'; ' + '; '.join(notes) if notes else ''}")
        if union != cyc and len(cyc - union) <= 6:
            for nd in sorted(cyc - union):
                print(f"      beyond-comb state (phi={nd[0]},z={nd[1]})"
                      f" eps={el(nd[2], nd[3])}")
    return True


def member_value(cell, r, d, m):
    """v = S/(1 - eta^m) in (1, alpha) coordinates: S = nu b0 + nw b1
    with b_i = (1 - eta^m) theta_i, so v = nu theta_0 + nw theta_1."""
    from explore_congruence_kill import s_xy
    P = cell.P
    x, y = s_xy(cell, r, d)
    t0, tmp = (-cell.p[0], cell.q[0]), (-cell.p[m * P], cell.q[m * P])
    t1, tmp1 = (-cell.p[1], cell.q[1]), \
        (-cell.p[m * P + 1], cell.q[m * P + 1])
    b0 = (t0[0] - tmp[0], t0[1] - tmp[1])
    b1 = (t1[0] - tmp1[0], t1[1] - tmp1[1])
    det = b0[0] * b1[1] - b0[1] * b1[0]
    nu = x * b1[1] - y * b1[0]
    nw = b0[0] * y - b0[1] * x
    assert nu % det == 0 and nw % det == 0
    nu, nw = nu // det, nw // det
    return (nu * t0[0] + nw * t1[0], nu * t0[1] + nw * t1[1])


def chain_rows(P, A, r, m, rig=None, show=6):
    """Members at (P, A, r, m) with their chain quantities; returns
    n_members."""
    cell = Cell(P, A)
    n = m * P
    caps = aligned_caps(P, A, r, m)
    q1 = cell.q[n - 1]
    N = n_m(cell, m)
    g = gvec(cell, m)
    dmax = dp_max(g, caps)[0]
    mirror = [(cell.q[n - 2 - j] if n - 2 - j >= 0 else 0)
              * (1 if j % 2 == 0 else -1) for j in range(n)]
    wsmax = dp_max(mirror, caps)[0]
    members = []
    for e in enum_legal_cyclic(caps):
        if not any(e):
            continue
        d = d_of(e, r)
        if direct_member(cell, r, d, m):
            members.append((e, d))
    lay = phz = div = 0
    ts = {}
    for (e, d) in members:
        phi, w = phi_of(e, cell), w_of(e, cell)
        if phi % N == 0:
            lay += 1
        if phi == 0:
            phz += 1
        if w % q1 == 0:
            div += 1
            t = w // q1
            ts[t] = ts.get(t, 0) + 1
        if rig is not None:
            orb = comb_orbit(rig, d)
            assert orb <= rig._cyc, "member orbit escapes cycle set"
    tag = (f"members={len(members)} Phi==0modN:{lay} Phi==0:{phz} "
           f"q|w:{div} t-hist={dict(sorted(ts.items()))}")
    print(f"  P={P} A={A} r={r} m={m}: {tag}")
    print(f"      w*max={wsmax} q_(n-1)={q1} "
          f"{'step-3 kill holds' if wsmax <= q1 - 1 else 'step-3 kill FAILS'}; "
          f"Dmax={dmax} N={N} "
          f"{'mass DIES' if dmax >= N else 'mass holds'}")
    shown = 0
    for (e, d) in members:
        if shown >= show:
            break
        phi, w = phi_of(e, cell), w_of(e, cell)
        v = member_value(cell, r, d, m)
        print(f"      e={''.join(map(str, e))} Phi={phi} w={w} "
              f"t={w // q1 if w % q1 == 0 else 'q!|w'} v={el(*v)}")
        shown += 1
    return len(members)


def s2():
    print("=" * 74)
    print("S2 THE CHAIN AT ODD r: which step dies (controls first)")
    print("  -- even-r controls (the theorem: zero members; "
          "even-P comb t = 1):")
    z = chain_rows(3, 2, 2, 2)
    z += chain_rows(5, 3, 2, 2)
    ok_zero = (z == 0)
    nc = chain_rows(4, 2, 2, 1)
    print(f"  controls: odd-P even-r members={z} "
          f"{'ok' if ok_zero else '<-- THEOREM VIOLATED'}; "
          f"even-P even-r members={nc} (comb expected)")
    print("  -- the odd-residue cells:")
    for (P, A, r) in odd_res_cells():
        rig, n, cyc, endp, inter, sccs, branch = cell_data(P, A, r)
        rig._cyc = cyc
        ms = (2,) if P % 2 == 1 else (1, 2)
        for m in ms:
            if m * P > 16:
                continue
            chain_rows(P, A, r, m, rig=rig)
    return True


def s3():
    print("=" * 74)
    print("S3 THE TOOTH CRITERION: minimal height h0 with h*delta at"
          " the digit class slot a member (m = 1), per cell; the"
          " tooth cycle exists iff h0 <= A")
    bad = 0
    for (P, A, r) in odd_res_cells():
        cell = Cell(P, A)

        def is_mem(h):
            d = [0] * P
            d[P - 1] = h
            return direct_member(cell, r, d, 1)

        # h0 divides |L/(1-eta)L| = |det(I - H)| (exponent divides
        # order), so the exact h0 is the least admitting divisor.
        h = cell.H
        idx = abs((1 - h[0]) * (1 - h[3]) - h[1] * h[2])
        h0 = min(h for h in range(1, idx + 1)
                 if idx % h == 0 and is_mem(h))
        hits = [h for h in range(1, 61) if is_mem(h)]
        if hits != [h for h in range(1, 61) if h % h0 == 0]:
            bad += 1
            law = f"h0={h0} NOT the generator of the admitting set"
        else:
            law = f"h0={h0}"
        print(f"  P={P} A={A} r={r}: {law} (idx={idx}) "
              f"tooth-cycle={'YES' if h0 <= A else 'no'}")
    print(f"  {'PASS' if bad == 0 else 'FAIL'}: admitting heights = "
          f"the multiples of h0 (a divisor of the index) at every cell")
    return bad == 0


if __name__ == "__main__":
    ok = s0()
    s1()
    s2()
    ok3 = s3()
    print("=" * 74)
    print("ALL STAGES RAN; s0 " + ("GREEN" if ok else "RED")
          + "; s3 " + ("GREEN" if ok3 else "RED"))
