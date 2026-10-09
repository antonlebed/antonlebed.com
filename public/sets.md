# SETS — set-valued prediction against its exact optimum

The object: an observable with atoms r of mass w_r, each carrying an
exact posterior p(y | r) over k labels, and a **set rule** choosing a
set of labels at every atom. A pair (r, y) costs w_r and covers w_r
p(y | r); a rule's cost is its expected set size and its coverage the
mass its sets hold. The marginal optimum **OPT** is the least cost
covering T = 1 − α, α the miscoverage allowed. The **operative level** t*
is the largest posterior value whose pairs {p ≥ t*} cover T; A is the
pairs strictly above it, the **tied block** the b pairs at it, and the
**coverage deficit** δ = T − cov(A). Two rules and a bound bracket OPT:
the threshold form **THR**, every pair at or above t*; the certificate
**CERT**, A plus the least-cost tied subset covering δ, whose cost is
its fill; and the bound L = cost(A) + δ/t*, the value of the relaxation
that may buy a fraction of a pair. The **surplus** D is CERT's coverage
minus T. The specimen is RULER.md's magnitude class ⌊kx/N⌋ read through
x mod M under the tilt θ^x (the set-valued reading in
RULER.md#one-live-arc-the-magnitude-parent), at four cells: **TILT-3**
(N = 105, M = 15, k = 3, θ = 24/25), **FLAT-3** (the same untilted),
**DEAD-7** (N = 105, M = 15, k = 7, untilted) and **TILT-4-WIDE**
(N = 1155, M = 105, k = 4, θ = 199/200), each read at T = 7/10.
Frequencies are read on a sweep at the same T and k = 3, every row a
posterior in tenths: 400 equal-mass cells of three or four atoms and
3,000 unequal three-atom cells with masses in twentieths
(sets.py::sweep), joined in the fate and exchange blocks by 1,500
unequal four-atom cells with masses in tenths (fates.py::four_arm). The
verifiers are sets.py, fates.py, swaps.py and gaplaw.py.

The thesis: once the posterior is exact, the least set size is a
computation, and it grades what the literature can only bound. A marginal
coverage guarantee cannot tell two rules apart that differ by everything
at one atom. The thresholded posterior, the form a published theorem
makes optimal, pays at every tie wider than the deficit needs; the
certificate that repairs it is the optimum wherever every pair costs the
same, and off equal weights it can overstate. What it overstates by is
bounded by its surplus divided by the operative level, and three gaps,
each sufficient, turn that bound into a proof of exactness wherever one
fires: the weight lattice's, the box its own sizes anchor, and the least
nonzero absolute reduced cost. Where none fires, fixing by reduced cost
and a two-halved frontier search find the optimum exactly, and the same
solver reaches cells no enumeration does. Along a geometric walk of step
1/n, for every n ≥ 1451, the anchored gap
(SETS.md#three-tests-can-prove-the-certificate-exact) is one product of
factors z^d − 1 read at a point, falling as n⁻⁴, while the certificate's
overstatement falls as 1/n. The optimum hands some atoms the empty set,
and an atom's **fate** is whether the optima serve it, abandon it or
differ on it. At equal masses the operative level forbids the two wrong
forced fates
(SETS.md#at-equal-masses-the-operative-level-forbids-the-wrong-forced-fates),
and an atom abandoned can be outnumbered rather than rare; off equal
masses no test on the atom's own numbers decides it, and what does is
the rest of the cell's integer price at the k + 1 remainders the atom
can leave. An optimum abandoning an atom turns into one serving it
only by an exchange whose masses balance exactly, so the rescue is
arithmetic before it is coverage. Nothing here needs the ring: it
supplies placement and an exact truth, and the failures are the forms'.

## A marginal coverage guarantee cannot rank two set predictors
Tier: observation (the four ring cells, samples of 2,000, 8,000 and
32,000, 20 trials each, every coverage exact).
Verifier: sets.py::section_coverage.

Split conformal thresholds one global quantile of an estimated
posterior; Mondrian conformal takes the quantile within each atom, so
its guarantee is per atom. The impossibility of conditional coverage
(Barber, Candès, Ramdas and Tibshirani, Inf. Inference 2021; Vovk,
"Conditional validity of inductive conformal predictors", 2012,
Proposition 4) is stated for a marginal without atoms, and Vovk notes
that at an atom a predictor keeping only that object's examples is
conditionally valid. The observable x mod M has M atoms, so per-atom
coverage is attainable here and scoring it is legitimate; and since the
truth is exact, every set's coverage is computed with no test sample.
Split conformal holds its marginal guarantee at every cell and sample
size (mean 0.704 to 0.726 against 0.70), and at both tilted cells its
worst atom receives a set of exact coverage 0 in 19 or 20 of every 20
trials at every size, while its mean size sits within 0.04 of OPT.
Mondrian on the same draws keeps its worst atom, averaged over trials,
at 0.716 (TILT-3) and 0.653 (TILT-4-WIDE) at 32,000 samples: its
guarantee holds per atom in expectation over draws, and the worst of
TILT-4-WIDE's 105 atoms in one trial sits below it. At TILT-3 its size
excess over the per-atom oracle, the least sets covering T at each atom,
falls as the sample grows. Two predictors the advertised guarantee cannot
separate differ by everything at one atom, and more data does not move
split's zero. At the untilted cells split's mean size sits within 0.04
of OPT (2 and 74/15) and below THR (3 and 7): sampling noise breaks the
ties the threshold form is sunk by, so the threshold form's penalty
falls on the form and not on the practice.

## The certificate brackets the optimum
Tier: property (proved; read at 3,404 cells, the sweep's and the four
ring cells, the certificate's sizes costing CERT and covering T + D).
Verifier: proof; sets.py::section_certificate.

δ > 0: if A alone covered T, the next posterior value up would be
operative. With rc_i = w_i(1 − p_i/t*), the reduced cost at price
1/t*, every rule R covering T satisfies

    cost(R) = Σ_{i∈R} rc_i + cov(R)/t* ≥ Σ_{rc<0} rc_i + T/t* = L,

and the pairs of negative reduced cost are exactly A; so
L ≤ OPT ≤ CERT ≤ THR. Every tied pair covers t* times its cost, so
CERT's coverage is cov(A) + t*·fill and

    CERT − L = fill − δ/t* = D/t*

exactly, for any fill: the certificate's whole room over the
relaxation is its surplus divided by the operative level. Read rule
by rule, with the excess of a pair w|p − t*|, e(X) the excess of the
pairs of A a rule R drops and f(Y) that of the pairs below t* it buys,
the same display is

    t*·(cost(R) − CERT) = e(X) + f(Y) + D_R − D,

D_R the rule's own overshoot: R beats the certificate iff what it
drops above, buys below and overshoots by together fall under D. ∎ The
display is complementary slackness and the argument is standard; what
it settles is how far the certificate can overstate, and by which
trades.

## At equal weights the certificate is the optimum
Tier: property (proved; exact at 402 equal-weight cells, two of them
ring cells, the form paying at 117).
Verifier: proof; sets.py::section_equal.

When every pair costs w, OPT is w times the least count of pairs whose
posteriors, taken largest first, cover T, and those are A followed by
tied pairs, since t* is operative; so CERT = OPT, the greedy by
posterior, and

    THR − OPT = w (b − ⌈δ/(w t*)⌉).

The thresholded form (Sadinle, Lei and Wasserman, JASA 2019, Theorem
1, whose optimality argument needs a posterior without ties) pays
exactly when the operative level is tied past what the deficit needs,
and never at b = 1: a tie fact, not an atomicity one. At FLAT-3 every
atom carries {3/7, 2/7, 2/7}, no threshold makes a set of size 2, and
THR is 3 against OPT 2; at DEAD-7, 7 against 74/15. And since the fill
stops at the first tied pair that closes δ, D < w t*, so D/t* < w. ∎

## Off equal weights the certificate can overstate
Tier: property (proved by two exhibited cells; how often, an
observation on a sampled sweep).
Verifier: proof; sets.py::section_unequal, sets.py::section_controls.

Three atoms of weights 3/10, 3/10, 2/5, each with posteriors
(2/5, 2/5, 1/5), at T = 7/10: t* = 2/5 with nothing above it, the fill
needs tied cost 7/4, and the least sum of four 3/10s and two 2/5s
reaching it is 2, so CERT = THR = 2 with coverage 4/5; the sizes
(2, 3, 1) cost 19/10 and cover exactly 7/10. An optimum drops a heavy
tied pair and tops up with a light pair below the operative level,
spending the surplus the fill overshot by. The zero half of the
equal-weight law fails too: at weights 1/10, 9/20, 9/20 and posteriors
(1, 0, 0), (1, 0, 0), (4/5, 1/5, 0), b = 1 and THR = CERT = 1, while
dropping the light atom's above-level pair costs 9/10 and still covers
0.81. ∎ The certificate overstates at over a third of a sampled
unequal-weight sweep, b = 1 included, and is exact at the rest, so off
equal weights it is an upper bound and not in general a value.

## Three tests can prove the certificate exact
Tier: property (proved; the three tests read at the 3,400 sweep cells
and the four ring cells, the anchored gap at every ring cell but
TILT-4-WIDE, whose 105 atoms are not searched).
Verifier: proof; sets.py::section_criteria.

CERT − OPT lies in [0, D/t*] by the room identity, so a floor under the
positive values CERT − OPT can take that exceeds D/t* proves CERT = OPT.
Two such floors hold, and a third test reads the prices. The
**lattice gap** g, the least positive integer combination of the
weights: CERT − OPT is one; by the equal-weight law
this test decides every equal-weight cell. The **anchored gap** ĝ, the
least positive Σ c_r w_r over the box c_r ∈ [s_r − k, s_r], s the
certificate's sizes: CERT − OPT = Σ (s_r − s′_r) w_r for an optimum's
sizes s′_r ∈ [0, k], and ĝ ≥ g since the box sits in the lattice. The
**price gap** ρ, the least nonzero |rc_i|, is no such floor, but by the
bracketing display a rule leaving out a pair of A or holding a pair
below t* costs at least
L + |rc_i|, so D/t* < ρ confines every optimum to A plus tied pairs,
whose best is the fill; per pair, t*ρ is the least single-pair excess. ∎
The tests reach different cells:

| cell | D/t* | g | ĝ | ρ | exact |
|------|------|---|-----|---|-------|
| TILT-3 | 2.79e-2 | 2.3e-21 | 1.8e-9 | 1.41e-2 | no |
| FLAT-3 | 5.00e-2 | 6.67e-2 | 6.67e-2 | 3.33e-2 | yes, g and ĝ |
| DEAD-7 | 3.33e-2 | 6.67e-2 | 6.67e-2 | none | yes, g and ĝ |
| TILT-4-WIDE | 4.35e-6 | 6.0e-242 | not searched | 1.81e-3 | yes, ρ |

Geometric weights drive the lattice gap toward zero, so on the tilted
cells the lattice gap does not fire; at TILT-3, where the certificate
overstates, no test can, and at TILT-4-WIDE the price gap fires.

## On the geometric walk's tail the anchored gap is one product
Tier: rule (proved for every real n ≥ 1451).
Verifier: gaplaw.py::section_profile, gaplaw.py::section_box,
gaplaw.py::section_argmin, gaplaw.py::section_optimum,
gaplaw.py::section_tail_proof.

The walk W-n is the ring cell N = 105, M = 15, k = 3 at
θ = (n − 1)/n; TILT-3 is W-25. Its weights are geometric,
w_r = θ^r κ with κ = (1 − θ)/(1 − θ¹⁵), so a box vector c is a
polynomial P_c(z) = Σ c_r z^r with Σ c_r w_r = κ P_c(θ), and since
θ − 1 = −1/n its expansion at 1 is a series in 1/n,
P_c(θ) = Σ_j m_j (−1/n)^j over its binomial moments
m_j = Σ_r C(r, j) c_r: the anchored gap is
FLATTEN.md's object read at one point
(FLATTEN.md#flattening-is-annihilation).

For every real n ≥ 1451 the certificate's sizes are 111112222233333, and
at n = 1450 they are not. Eight signs decide the profile: six
comparisons of posteriors with the operative level
(q² − q⁴)/(1 − q⁷), q = θ¹⁵, the level's coverage, and the fill test
that the four heaviest tied pairs fall short. Each is an integer
polynomial in θ of degree at most 120, and exact root isolation finds
all eight root-free on [θ₁₄₅₁, 1), θ_n = (n − 1)/n; the fill test's one
root past n = 1400 sits at n = 1450.31. On that box the anchored gap is,
exactly,

    ĝ = κ·θ(θ − 1)(θ² − 1)(θ³ − 1)²
        = θ(1 + θ)(1 + θ + θ²)² / ((1 + θ + ⋯ + θ¹⁴)·n⁴),

which tends to (6/5)·n⁻⁴. A vector is flattened to J when its first J
moments m_0, …, m_{J−1} vanish, its flattening is the largest such J,
and h(15, J) is the least height of a nonzero integer vector of length
15 so flattened (FLATTEN.md#the-least-height-is-a-lattice-minimum).
The box holds no nonzero vector flattened past 4: a free box of height 3
reaches 6 but not 7 (h(15, 6) = 3, h(15, 7) = 4), and the anchoring
denies 5 and 6. At flattening J ≤ 3, n^J·|P_c(θ)| ≥ |m_J| − E_J, E_J
bounded by the box's own largest |m_{J+1}| and a coordinatewise tail,
and the margin over what beating 18·n⁻⁴ needs is at least 0.39 at
n = 1451 and grows with n. At flattening 4, m_4 ≤ −1 leaves P_c negative
and m_4 ≥ 19 leaves it above 18·n⁻⁴. The least positive m_4 is 18, and
one vector attains it: z(z − 1)(z² − 1)(z³ − 1)², the one shift of that
product the box's ranges admit. ∎ The box's 4¹⁵ vectors are searched
exactly, by meet-in-the-middle on their moments.

So on the walk's tail the anchored test fails for every large n: its gap
falls as n⁻⁴ while the room tends to 1/20, since in the limit the
certificate covers 5/7 against T = 7/10 at the operative level, near
2/7; at the tail's values of n computed the room exceeds the gap by
eleven orders or more. It is right not to fire: on the whole tail the
certificate overstates. The optimum's sizes are 011111133333333 for
every real n ≥ 1451, and it abandons atom 0, the heaviest. At θ = 1 a
heavy pair covers 3/105 and a light one 2/105, so a rule of S slots
serving σ atoms covers (2S + σ)/105 against T = 73.5/105: no rule of 29
slots covers, and every rule of 30 serving at least 14 atoms covers at
the same cost. The tilt then costs a rule κ(S − Σ r·s_r/n + O(n⁻²)), so
the tied rule with the largest first moment wins, and that is
011111133333333, at 273 against a runner-up 272. On the tail it is
exact: the second-order terms of any two 30-slot rules differ by at most
1365/n², below the 1/n a unit of first moment buys once n > 1365, and
fifteen integer polynomials in θ, root-free on [θ₁₄₅₁, 1), show that the
optimum covers T while no rule of 29 slots does and no other 30-slot
rule of moment at least 273 does; a rule of 31 or more slots costs more,
since 31θ¹⁴κ > 30κ for every n ≥ 434. For one set of served atoms, the
one abandoning atoms 13 and 14, the coverage bound does not settle
whether it covers T, but its rules reach moment 218 at most, below 273,
so none of them wins. The difference of the two size vectors is a box
vector with m_0 = 0 and m_1 = −13, so CERT − OPT = κ(13/n − 60/n² + ⋯),
and (CERT − OPT)·n reads 0.8681 at n = 1451 and 0.8667 at 10⁷, toward
13/15: the overstatement sits at flattening 1, three powers of n above
the least difference the box allows.

## An exact solver for the marginal optimum
Tier: property (proved; with and without the fixing equal to
enumeration at 3,400 sweep cells, and at TILT-3 the unfixed search equal
to the fixed, both in sets.py::section_controls).
Verifier: sets.py::solve, sets.py::section_solver,
sets.py::section_controls.

Minimizing set size under marginal coverage is a multiple-choice
knapsack: atom r takes a size s ∈ [0, k] at cost w_r s and coverage
w_r times its s largest posteriors. The bracketing display fixes every
pair with |rc_i| > CERT − L, in if rc_i < 0 and out if rc_i > 0, since
flipping it costs more than the certificate. Each atom keeps a range
of sizes; the atoms split into two halves, each folded to its Pareto
frontier of cost against coverage, and the halves join on the coverage
axis. The answer is exact with or without the fixing, which only
shrinks the frontiers. The four ring cells, costs in expected labels:

| cell | L | OPT | CERT | THR |
|------|---|-----|------|-----|
| TILT-3 | 0.9008338 | 0.9194957 | 0.9287750 | 1 |
| FLAT-3 | 1.95 | 2 | 2 | 3 |
| DEAD-7 | 4.9 | 74/15 | 74/15 | 7 |
| TILT-4-WIDE | 0.8966969 | 0.8967012 | 0.8967012 | 1 |

At TILT-4-WIDE the fixing leaves only the 26 atoms holding the tied
block's pairs free, 8,192 frontier points a half; enumerating its 5^105
size vectors is out of reach.

## At equal masses the operative level forbids the wrong forced fates
Tier: property (proved; the condition exact at 400 equal-weight cells,
the eight-atom optimum by enumeration, its conformal reading 20 trials
at each sample size).
Verifier: proof; fates.py::section_equal, fates.py::section_straddle.

An atom is **forced-abandoned** when every optimum gives it the empty
set and **forced-served** when none does. The **abandonment condition**:
no atom carrying a label above t* is forced-abandoned, and no atom whose
whole row sits below t* is forced-served. At equal masses the
certificate is an optimum, and it serves every atom above the operative
level and abandons every atom below it, so the condition holds. ∎ Other
optima may differ where the surplus covers a swap: 28 above-level atoms
of the sweep's equal-mass cells are each abandoned by some optimum, none
of them forced. The atom abandoned need not be light, rare or
adversarial. Eight atoms of mass 1/8, seven peaked at 0.86, 0.85, ...,
0.80 and one at (0.40, 0.32, 0.28), against a bar of 0.70: the seven
tops cover 0.72625, so t* = 4/5 and the one optimum is seven singletons
and the empty set at the eighth, OPT = 7/8. The eighth atom is
outnumbered. Split conformal, run on it, leaves its least-covered atom
at exact coverage 0 in every trial at sample sizes 2,000, 8,000 and 32,000 with
marginal coverage 0.7262, while the optimum too covers one atom, its
eighth, at 0; the complaint an auditor has is with the marginal
constraint, not with the method meeting it.

## Off equal masses the condition fails both ways
Tier: property (proved by two exhibited cells, each with one optimum).
Verifier: proof; fates.py::section_witnesses.

Above: masses (1/10, 9/20, 9/20), rows (1, 0, 0), (1, 0, 0),
(4/5, 1/5, 0), T = 7/10. Here t* = 4/5. Below cost 9/10 at most one
heavy label is bought and coverage is at most 0.55; cost 9/10 forces
s₀ = 0 and s₁ + s₂ = 2, and only (0, 1, 1) covers (0.81): the atom of
mass 1/10, certain of its label, p = 1 > t*, is forced-abandoned,
because the two heavy atoms clear the bar without it. Below: masses
(17/20, 1/10, 1/20), rows (4/5, 1/5, 0), (4/5, 1/5, 0), (3/5, 2/5, 0).
Level 4/5 covers 0.76, so t* = 4/5, and the certificate (1, 1, 0)
costs 19/20; (1, 0, 1) costs 9/10 and covers 0.68 + 0.03 = 0.71, and
nothing cheaper reaches the bar. The light atom, whose best label 3/5
sits below the operative level, is forced-served, because it tops up the
heavy atom's shortfall
at half the price of the tied pair. ∎

## No test on one atom's own numbers decides its fate
Tier: property (proved by an exhibited pair).
Verifier: proof; fates.py::section_dead.

A test an auditor runs on one subpopulation reads its mass, its row and
the operative level, a function of (w, sorted row, t*). The atom of mass
1/10 with row (1, 0, 0) at t* = 1/2 is forced-abandoned in the cell of
masses (11/20, 7/20, 1/10) with rows (7/10, 3/10, 0), (1/2, 1/2, 0),
(1, 0, 0), whose one optimum (1, 2, 0) costs 5/4, and forced-served in
the cell of masses (3/5, 3/10, 1/10) with rows (1/2, 1/2, 0),
(1/2, 2/5, 1/10), (1, 0, 0), whose one optimum (2, 0, 1) costs 13/10
while every rule without it costs at least 3/2. Every such test fails on
one of the two. ∎ Over the sweep, 276 of the 1,255 distinct
(w, sorted row, t*) that carry a forced fate carry both: min-cost
covering stops being pointwise once the purchases are lumpy.

## The rest's integer price decides the fate
Tier: property (proved; the fractional key's collisions counted on the
sweep).
Verifier: proof; fates.py::section_rest.

An atom's rule of size s is no better than its top-s prefix, covering
w·P_s, w the atom's mass and P_s the sum of its s largest posteriors,
and the rest of the cell is bought independently; with Λ(v) the least
cost at which the other atoms cover v,

    OPT = min_s [ s·w + Λ(T − w·P_s) ],   s = 0, …, k.

The atom is forced-abandoned iff the s = 0 term is strictly least,
forced-served iff some s ≥ 1 term is strictly below it, and open on a
tie. ∎ So the atom's mass, its row and the rest's integer price at the
k + 1 remainders T − w·P_s its prefixes leave decide the fate, and
that tuple is its rest key; the k + 1 sums s·w + Λ(T − w·P_s)
already do. The same separable minimum,
OPT = min_o [cost(o) + Λ(T − cov(o))] over an atom's options o, each
with its cost and coverage, holds for any finite menu of options,
nested or not; the equal cost of an atom's labels is what shrinks its
menu of label sets to the k + 1 nested prefixes. The rest's fractional
price at the same remainders, its pairs bought by posterior with the
last in part, does not decide it: 115 keys built on it carry both
forced fates. The lumps of the rest's purchases do the deciding.

## Two mass bounds cap an abandoned atom and one wholly below the operative level
Tier: property (proved; both attained exactly on the sweep).
Verifier: proof; swaps.py::section_mass_bounds.

A rule abandoning r covers T from the other atoms, of mass 1 − w_r, so
any atom any feasible rule abandons has w_r ≤ 1 − T. Let ψ_u be the
posterior mass atom u holds at or above t*, and ψ_max the largest ψ_u
over all the atoms. An atom r wholly below t* holds none of the pairs
{p ≥ t*}, which cover T, so T ≤ (1 − w_r)·ψ_max and w_r ≤ 1 − T/ψ_max,
a bound on those atoms only: an atom with a label at or above the
operative level can be abandoned and still exceed it, as 18 atoms of
the sweep are.

## A rescue is an exchange whose masses balance
Tier: property (proved; on the sweep the swap and the full partner
build 991 and 123 rescues, each an optimum, and an atom rescued only by
gain is printed).
Verifier: proof; swaps.py::section_exchange.

Let R abandon r and R′ serve it at size s, both optima. Where R′ is
lower on a partner it drops d_i labels, where higher it gains a_j, and
since both cost OPT,

    Σ_drops w_i·d_i − Σ_gains w_j·a_j = s·w_r   exactly.

So every rescue is a mass-balanced exchange, and one that only drops
(a dominated rescue) exists only if some drop-set within R weighs
exactly s·w_r for some s ≤ k: the rescue is arithmetic before it is
coverage. Two conditions each give a dominated rescue. The swap: if R's
lowest label on a partner r′, of posterior p, has s·w_r ≤ w_r′ and
w_r′·p ≤ w_r·P_s + D_R (P_s the sum of r's s largest posteriors), the
trade is an optimum serving r, and then s·w_r = w_r′. The full partner:
if R serves a partner i fully and w_i·d = s·w_r, dropping i's lowest d
labels loses at most w_i·d/k while r's top s gain at least s·w_r/k, so
the trade is an optimum with no coverage condition. ∎ Where no drop-set
balances, every rescue gains somewhere. At masses (1/20, 1/2, 9/20) and
rows (4/5, 1/10, 1/10), (3/5, 2/5, 0), (3/5, 1/5, 1/5), t* = 2/5, the
atom of mass 1/20, above the operative level, is abandoned by the
optimum (0, 2, 1) and served only by (1, 1, 2): one label of mass 1/2
dropped, one of 9/20 gained, and no drop-set of (0, 2, 1) weighs 1/20,
1/10 or 3/20.

## Open fronts

At slack 1 − w_min − T ≥ 0, which weight vectors leave no atom above the
operative level forced-abandoned whatever the rows, and how is that set
graded by the slack? Below zero no atom is ever abandoned, and equal
weights qualify. The swap gives a dominated rescue by dropping one
label of a partner, the full partner by dropping d labels of a partner
served fully; what condition gives one when d ≥ 2 labels are dropped
from a partner served only in part? At unrestricted masses, is deciding
an atom's fate as hard as the rest's knapsack, and for masses on a fixed
grid, is there a statistic of the rest cheaper than its integer price at
the k + 1 remainders that still decides it?
