"""The two lattice-avoidance lemmas' candidate census: is route (A)
parametric — box lattice points uniformly few in a, dying locally?

THE QUESTION
------------
The bounded half's universal statement is reduced (transport + aligned
theorem + coding dichotomy, D1-D4 below) to excluding, at
every even-residue cell (P, A, r), every box lattice point other than
the shared max-comb orbit. The certified scan (explore_bounded_half.py)
covers A = 2, 3, 4. Route (A) of the proof plan enumerates the box
lattice points as closed forms in A and kills each family by hand. This
probe reads whether that route is viable: how the candidate census
grows with A, whether the verdicts stay on the parity law beyond the
certified caps, and whether non-cycle candidates die LOCALLY (bounded
peeling depth), which is what a bounded-step parametric argument needs.

Also carried: the exact transport control. The reduction rests on
theta_{k+r} = mu * ttheta_k with mu = -theta_{r-1} and L = mu * L_r
(unimodular pair theta_{r-1}, theta_r); a slate this load-bearing gets
a machine check before anything leans on it.

THE HAND-ATTACK (pre-engine, on paper; the reduction package this
probe serves — frame as in explore_bounded_half.py)
----------------------------------------------------------------------
D1  THE TRANSPORT (theorem). For 0 < r < P set mu = -theta_{r-1} and
    let alpha_r be the r-rotated window [0; bar(a_{r+1},...,a_{r+P})]
    with theta-sequence ttheta and lattice L_r = Z + Z alpha_r. Then
    theta_{k+r} = mu * ttheta_k for all k >= -1 (bases: ttheta_{-1} =
    -1 by definition of mu; theta_r = mu * alpha_r from alpha =
    (p_r x' + p_{r-1})/(q_r x' + q_{r-1}) with x' the complete
    quotient; induction via the shared recurrence), and L = mu * L_r,
    because (theta_{r-1}, theta_r) is a basis of L: its determinant is
    p_{r-1} q_r - p_r q_{r-1} = (-1)^r. So V(d) = mu * Vt(d) with
    Vt(d) = sum d_k ttheta_k, and V(d) in L <=> Vt(d) in L_r; the
    factor's conjugate mu' = -theta'_{r-1} > 0 preserves the box
    positivity, and ttheta_{k+P} = eta ttheta_k — the SAME unit. The
    residue-r problem IS the rotated window's ALIGNED problem with
    FOREIGN caps: digits keep cap(k) = a_{(k mod P)+1} (class at
    phase P-1) while the rotated window's own caps put the class at
    phase P-1-r.
D2  THE ALIGNED THEOREM (r = 0, EVERY purely periodic window). The
    purely periodic own-caps-admissible patterns with value in the
    window's lattice are exactly the zero pattern and the two
    full-cap extremal telescopes. Proof: (i) the stride-P shift is
    the bare coordinate map — admissibility is phase-local and its
    first-position rule only weakens on suffixes, so shift^P maps
    admissible strings to admissible strings with the correctly
    renormalized value: delay 0, no gate — at EVERY purely periodic
    window; (ii) explore_bounded_half.py's criterion arguments D1-D3
    are window-generic (they use only theta' < 0, |theta'| increasing,
    eta' > 1, finite caps), so an interior cycle would force a gate:
    there is none; (iii) a periodic pattern with lattice value has all
    suffix values in the box forming a cycle, hence every suffix AT an
    interval endpoint; (iv) a value has at most two admissible codings
    — greedy, and a terminating twin exactly at finite-string values
    (the 0.999... doubling) — and the extreme's greedy coding is the
    full-cap comb, while a nonzero periodic pattern has infinitely
    many nonzero digits and cannot be the terminating twin: one
    endpoint suffix pins the whole pattern to the telescope. QED.
    This turns the certified r = 0 column classification into a
    THEOREM at all (P, a) and all rotations.
D3  THE CODING DICHOTOMY. x in L_r in coding range: its greedy rotated
    coding either terminates or is eventually a full-cap comb (the
    deficit walk stays in L_r, enters the finite box unless it
    terminates, and its periodic tail is classified by D2). And a
    NONZERO periodic pattern's value has positive conjugate while a
    finite star's is <= 0, so for the lemmas' objects the coding is
    eventually a COMB: both lemmas now read "no lattice point with an
    eventually-comb aligned coding also has a purely periodic
    foreign-caps representation, except the shared max comb".
D4  THE CAP-FIT MECHANISM (the parity law explained; position parity
    has period 2 while caps have period P, so at odd P the class slot
    wanders both parities once per 2P). Even P, even r: both class
    phases (P-1 and P-1-r) are odd, the two cap vectors agree on the
    even (max) side, the max combs COINCIDE — C1 is the shared
    survivor; the min combs differ, which removes the comb route to a
    lattice tmin — consistent with tmin certifying as a non-lattice
    point (explore_bounded_half.py D7), which nothing here derives.
    Odd P, even r: neither extremal comb fits the
    foreign caps — nothing survives (acyclicity, F4 of
    explore_bounded_half.py). Even P, odd r: the rotated max comb
    needs its class cap on a slot the original caps at 1 — those are
    the gated cells, the derived comb families of
    explore_parity_derivation.py.

PREDICTIONS, FIXED BEFORE THE RUN (observables)
  N1 (control; red voids the run): the transport identity holds
      exactly — mu * ttheta_k = theta_{k+r} for k = -1..30 at every
      probed cell, and |p_{r-1} q_r - p_r q_{r-1}| = 1.
  N2 (the census): node counts per cell printed for A = 2..12. The
      slate is honestly open here: bounded-in-A supports route (A);
      linear growth without few-family structure kills it.
  N3 (scope extension): at every swept cell the cycle verdict stays on
      the parity law — even residues carry no interior cycle at
      A = 5..12 either. Any cell off is a FINDING against the law.
  N4 (local death): peeling the box graph (repeatedly deleting nodes
      with no successor, then nodes with no predecessor) leaves only
      the cycle states within a bounded number of rounds; prediction:
      the round count stays bounded as A grows (guess: <= 2P + 2).
  N5 (the deep core; frozen before s4 ran, after s1-s3 printed): the
      set of nodes surviving the last THREE peel rounds (the hard core
      a parametric proof must kill by exact closed forms) STABILIZES
      in A — its size becomes constant and its (u, w) coordinates move
      along at most finitely many A-linear families. Observable: core
      sizes per cell for A = 2..12, and the core lists at (4, 2) and
      (6, 4) across A.

FINDINGS (run record at the end; every stage green, exact arithmetic)
----------------------------------------------------------------------
F1  THE TRANSPORT IS EXACT (N1): mu * ttheta_k = theta_{k+r} for
    k = -1..30 and |p_{r-1} q_r - p_r q_{r-1}| = 1 at all 22 probed
    cells (every (P, r), A = 2 and 7). The reduction's load-bearing
    identity is machine-checked.
F2  THE PARITY LAW EXTENDS TO A = 12 (N3): at all 121 swept cells
    (11 (P, r) pairs x A = 2..12) the box graph carries NO interior
    cycle, and the cycle-state count is exactly P at even-P cells
    (the comb orbit) and 0 at odd-P cells — constant in A.
F3  THE RAW CENSUS GROWS ~A^2 (N2): e.g. (4, 2): 78 nodes at A = 2,
    720 at A = 12; (8, 2): 648 -> 8443. Naive box enumeration is NOT
    a parametric route; the kill must be structural (the deep core
    plus a coarse argument for the generic mass).
F4  LOCAL DEATH IS BOUNDED (N4): the alternating no-successor /
    no-predecessor peel empties every non-cycle node, never sticking,
    in <= 27 rounds at every cell, the depth stabilizing in A (e.g.
    (5, 2): 7 rounds at every A; (8, 4): 23 from A = 5 on).
F5  THE EVEN-P DEEP CORE IS FINITE AND A-LINEAR (N5, even P): the
    survivors of the last three peel rounds stabilize at 7-9 nodes
    per even-P cell, their (u, w) coordinates moving on A-linear
    families concentrated at the CLASS phase P-1 — at (4, 2),
    A >= 4: the nine are (0,0,2,-3), (0,1,2,-3), (1,1,2,-3) fixed
    and, at phase 3, (u, w) = (2A+1, -(3A+2)) and (2A+3, -(3A+5))
    at z = 1, and (4A+4, -(6A+7)) and (6A+7, -(9A+12)) each at
    both z. These families were the concrete targets a
    parametric even-P proof was expected to kill by closed form
    (settled another way: explore_deep_pairs.py's odd-support
    theorem closes every P <= 12 strip pair without touching them). At ODD P the
    observable is CONFOUNDED and reads nothing: the graph is acyclic,
    so the "last three rounds" are just the final tranche of a peel
    of everything, and scale with the graph (e.g. (5, 2): 71 -> 799);
    the odd-P attack stays acyclicity-shaped, not core-shaped.

RUN RECORD: python explore_lattice_avoidance.py — s0..s4, 194 s wall,
memory trivial, ALL STAGES GREEN (two captured runs diffed: s0-s3
byte-identical, s4's counts and core lists matching row for row).

THE DESIGN
----------
Reuses explore_bounded_half.Rig (box enumeration, edges, Tarjan) and
explore_parity_derivation.Cell exactly as certified; everything exact
(Fraction / integer). s0 transport control at 22 cells (every (P, r),
A = 2 and 7); s1 census + verdict sweep, P in {4,...,8}, even nonzero
r, A = 2..12; s2 node coordinate dump at (P, r) = (4, 2), (6, 2),
(5, 2) at A = 2, 3, 5, 8 to read closed forms; s3 peeling depth per
cell; s4 the deep-peel core (last three rounds' survivors) per cell.
One command runs all; wall-clock estimate: a few minutes; memory
trivial.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_bounded_half import Rig                    # noqa: E402


# ----------------------------------------------------------- transport

def transport_control(P, A, r, upto=30):
    """Check mu * ttheta_k == theta_{k+r} exactly, k = -1..upto, and
    the unimodularity of (theta_{r-1}, theta_r). Returns True/False."""
    rig = Rig(P, A, r)
    c, F = rig.cell, rig.F
    # unimodularity
    det = c.p[r - 1] * c.q[r] - c.p[r] * c.q[r - 1]
    if abs(det) != 1:
        return False
    mu = (Fraction(c.p[r - 1]), Fraction(-c.q[r - 1]))    # -theta_{r-1}
    # rotated quotients: atilde_k = a_{r+k} (a list is 1-indexed by CF
    # convention: cell.a[j] = a_{j+1})
    atil = [c.a[(r + j) % P] for j in range(0, 300)]
    # rotated convergents
    qt = [0, 1]     # qtilde_{-1}, qtilde_0
    pt = [1, 0]     # ptilde_{-1}, ptilde_0
    for k in range(1, upto + 3):
        qt.append(atil[k - 1] * qt[-1] + qt[-2])
        pt.append(atil[k - 1] * pt[-1] + pt[-2])
    # alpha_r = -theta_r/theta_{r-1} as an element of Q(alpha)
    th_r = (Fraction(-c.p[r]), Fraction(c.q[r]))
    th_rm1 = (Fraction(-c.p[r - 1]), Fraction(c.q[r - 1]))
    alpha_r = F.mul((-th_r[0], -th_r[1]), F.inv(th_rm1))
    for k in range(-1, upto + 1):
        # ttheta_k = qtilde_k * alpha_r - ptilde_k  (index shift: list
        # position k+1 holds index k)
        tt = F.sub(F.scale(alpha_r, qt[k + 1]),
                   (Fraction(pt[k + 1]), Fraction(0)))
        lhs = F.mul(mu, tt)
        rhs = (Fraction(-c.p[k + r]), Fraction(c.q[k + r]))
        if lhs != rhs:
            return False
    return True


# ------------------------------------------------------------- peeling

def peel_depth(graph, cyc):
    """Rounds of alternating no-successor / no-predecessor deletion
    until only cyc remains: the maximum death round (0 if graph == cyc
    already), or -1 if the peel sticks."""
    death = death_rounds(graph, cyc)
    if death is None:
        return -1
    return max(death.values()) if death else 0


# ------------------------------------------------------------- driver

def even_residues(P):
    return [r for r in range(2, P, 2)]


def main():
    print("s0: transport control")
    cells = [(P, A, r) for P in (4, 5, 6, 7, 8)
             for r in even_residues(P) for A in (2, 7)]
    ok = all(transport_control(P, A, r) for (P, A, r) in cells)
    print("  transport exact at %d cells: %s"
          % (len(cells), "PASS" if ok else "FAIL"))
    assert ok

    print("s1: census + verdict sweep, A = 2..12")
    bad = []
    counts = {}
    for P in (4, 5, 6, 7, 8):
        for r in even_residues(P):
            row = []
            for A in range(2, 13):
                rig = Rig(P, A, r)
                nodes = rig.enumerate_box()
                graph = {n: rig.edges_from(n, nodes) for n in nodes}
                from explore_bounded_half import cycle_states
                cyc = cycle_states(graph)
                interior = [n for n in cyc
                            if rig.classify(n) == "interior"]
                if interior:
                    bad.append((P, A, r, len(interior)))
                row.append((A, len(nodes), len(cyc)))
                counts[(P, r, A)] = (nodes, graph, cyc, rig)
            print("  P=%d r=%d: " % (P, r)
                  + "  ".join("A=%d:%d/%d" % t for t in row)
                  + "   (nodes/cycle-states)")
    print("  interior cycles at even residues: %s"
          % ("NONE (parity law holds to A=12)" if not bad else bad))

    print("s2: node coordinates (phi,z,u,w) — closed-form reading")
    for (P, r) in ((4, 2), (6, 2), (5, 2)):
        print("  (P,r)=(%d,%d):" % (P, r))
        for A in (2, 3, 5, 8):
            nodes = sorted(counts[(P, r, A)][0])
            print("    A=%d n=%d: %s" % (A, len(nodes), nodes))

    print("s3: peeling depth per cell (rounds; negative = stuck)")
    for P in (4, 5, 6, 7, 8):
        for r in even_residues(P):
            row = []
            for A in range(2, 13):
                nodes, graph, cyc, rig = counts[(P, r, A)]
                row.append((A, peel_depth(graph, cyc)))
            print("  P=%d r=%d: " % (P, r)
                  + "  ".join("A=%d:%d" % t for t in row))

    print("s4: the deep-peel core (survivors of the last 3 rounds)")
    for P in (4, 5, 6, 7, 8):
        for r in even_residues(P):
            row = []
            cores = {}
            for A in range(2, 13):
                nodes, graph, cyc, rig = counts[(P, r, A)]
                death = death_rounds(graph, cyc)
                if death is None:
                    row.append((A, -1))
                    continue
                last = max(death.values()) if death else 0
                core = sorted(n for n, rd in death.items()
                              if rd > last - 3)
                cores[A] = core
                row.append((A, len(core)))
            print("  P=%d r=%d: " % (P, r)
                  + "  ".join("A=%d:%d" % t for t in row))
            if (P, r) in ((4, 2), (6, 4)):
                for A in (2, 3, 5, 8, 12):
                    print("    core A=%d: %s" % (A, cores[A]))

    print("ALL STAGES DONE")


def death_rounds(graph, cyc):
    """Round at which each non-cycle node dies under the alternating
    peel; None if stuck."""
    alive = set(graph)
    death = {}
    rounds = 0
    while alive - cyc:
        rounds += 1
        drop = {n for n in alive - cyc
                if not any(m in alive for m in graph[n])}
        if not drop:
            preds = {n: 0 for n in alive}
            for n in alive:
                for m in graph[n]:
                    if m in alive:
                        preds[m] += 1
            drop = {n for n in alive - cyc if preds[n] == 0}
        if not drop:
            return None
        for n in drop:
            death[n] = rounds
        alive -= drop
    return death


if __name__ == "__main__":
    main()
