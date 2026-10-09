# THERMAL — the growth walks at finite temperature

The object: the demands of GROWTH.md with the least move softened
into a Boltzmann choice, an admissible m picked with probability
proportional to m^−β at inverse temperature β > 1, the greedy walk
being β = ∞. This page asks which parts of each fate survive heat, what
each demand grows at finite β, what changes over F₂[x], where a
tick sits on a log clock, and where the column locked on one place
turns critical. Its verifiers are thermal.py, floors.py and
spectrum.py.

From a state M the **thermal law** picks m in the admissible set A(M)
with probability m^−β / Ψ_M(β), where Ψ_M(β) is the sum of m^−β over
A(M); for β > 1 it is a law at every state with A(M) nonempty, since
ζ(β) bounds Ψ_M(β), and a finite nonempty A(M), as under transparency,
makes it one at every β; β → ∞ recovers the least move. σ_β(n) is the
sum of d^−β over the divisors d of n, and ξ(M) = W(λ(M))/M is the
headroom under GROWTH.md's wall W(L), the largest modulus whose λ
divides L. The answer, in one line: heat keeps what a demand's
admissible set forces by its shape and melts what only the argmin
enforced, so independence grows a random limit whose law is the zeta
function, dynamics grows all of Ẑ at every finite β > 1, transparency
dies at the same wall, and over F₂[x] a walk with its moves restricted
in degree always dies where one over Z can live.

## The zeta measure
Tier: theorem.
Verifier: proof; thermal.py::section_i.

Under independence A(M) is the integers m ≥ 2 coprime to M, so once p
divides M no later pick touches it: each prime enters once, at the depth
of that pick. At a pick with p | m write m = p^k·u with u coprime to Mp:
the weight p^−kβ·u^−β factors and the range of u does not depend on k,
so

    P(v_p(m) = k | p divides the pick) = p^−β(k−1)·(1 − p^−β)

exactly, at every state and every time, and the same factoring over
the primes of one pick makes the depths independent. The move m = p is
admissible while p ∤ M, and Ψ_M ≤ ζ(β) − 1, so p divides the pick with
probability at least p^−β/(ζ(β) − 1) at every state; by Lévy's
extension of Borel–Cantelli every prime enters almost surely. From
seed 1 the limit is the **zeta measure**, the random supernatural number
∏ p^(G_p) with G_p independent and geometric of ratio p^−β, the
exponent law of a ζ(β)-random integer given p | n. It is squarefree,
the **crystal** the greedy walk grows surely, with probability
∏ (1 − p^−β) = 1/ζ(β), the reciprocal of the zeta function, and
1/ζ(2) = 0.6079 is the squarefree density read as the fraction of worlds
that grow the primorial profile. As β → 1+, P(G_p ≥ k) → p^−(k−1), the
law of the p-adic valuation of a Haar-random p-adic integer given that p
divides it, place by place: β = 1 is at once ζ's pole and the edge of
the law.

## The hot limit is Ẑ
Tier: theorem.
Verifier: proof; thermal.py::section_z.

Under dynamics A(M) = {m ≥ 2 : λ(Mm) > λ(M)}. Since a | b gives
λ(a) | λ(b), the set is upward-closed under divisibility: m admissible
and m | m′ make m′ admissible. Its complement is
{m ≥ 2 : Mm divides W(λ(M))}, the divisors of ξ(M), finite, so
Ψ_M(β) = ζ(β) − σ_β(ξ(M)).
Multiplying by p maps A(M) into itself injectively and scales every
weight by p^−β, so

    P(p divides the pick) ≥ p^−β

at every state, the exact value being p^−β(ζ − σ_β(ξ/p))/(ζ − σ_β(ξ)),
with σ_β(ξ/p) = 0 when p ∤ ξ. The floor ignores the state, so by Lévy's
Borel–Cantelli every prime divides infinitely many picks almost surely,
v_p(M_t) → ∞ at every p, and the limit ring lim Z/M_t is Ẑ, the whole
profinite completion, from every seed at every β > 1. The greedy walk's
lock onto one prime (GROWTH.md#the-lock-prime-law) is an artifact of
β = ∞: from seed 2 the greedy walk sits at 2^42 after 40 moves, while at
β = 2 with picks m ≤ 500 all of 100 runs have opened a second prime by
then. When v_p(λ) runs ahead of v_p(M), p's own admissible powers are
high and weigh little, yet p rides into the state on p times any
admissible move.

The proof used two facts, A(M) nonempty and upward-closed and the
weight multiplicative, so any thermal growth on the divisibility order
with those two properties reaches Ẑ almost surely. At a tombstone,
M = W(λ(M)), transparency is dead, ξ = 1 and Ψ_M = ζ(β) − 1: dynamics
there is the free zeta law on every m ≥ 2, at 24, 240 and 504.

## The closure trichotomy
Tier: theorem.
Verifier: proof; thermal.py::section_z.

Each demand's admissible set has a shape, and the shape decides how much
of the fate it forces alone. Independence avoids the support of M, and
that alone forces entry once. Dynamics is upward-closed and cofinite,
and that shape under the thermal law at finite β forces Ẑ; the greedy
walk, β = ∞, has the same admissible sets and locks onto one prime.
Transparency is the divisors ≥ 2 of ξ(M),
downward-closed and finite, and that shape alone does not force death:
A(M) = {2} at every M is downward-closed, finite, never empty, and grows
2^∞. Transparency dies because each move consumes at least one prime
factor of ξ(M), a budget: every trajectory, at every β and under any
policy at all, ends at W(λ(seed)) within Ω(W/seed) moves, Ω counting
prime factors with multiplicity. So seeds 5, 7 and 73 end at 240, 504
and 20,174,525,280, the walls the verifier computes; that every
trajectory ends there is the proof's. One fate's mark, entry once, is
authored by shape alone, one fate by shape and the finite-β weight; the
third needs shape and budget.

## What each fate needs of the ground
Tier: theorem.
Verifier: proof; floors.py.

Take the integers away one property at a time. Death needs only order:
a demand confining the walk to a finite region absorbs under every
policy within the region's height, since every move ascends strictly.
Where it dies is the demand's. Under the interval demand, every element
of the region above the state, the graves are the reachable elements
with no successor, and there is one grave iff the reachable part has a
maximum; on {1 < 2, 1 < 3} the grave is the policy's, greedy dying at
the cheaper element and the thermal law splitting the two. Transparency
is the interval case with a maximum, its fibre above a state s being
the multiples of s dividing W(λ(s)), which is why it dies at one wall.

Reaching everything needs only multiplication: on a countable
cancellative commutative monoid with a positive summable multiplicative
weight, under an up-closed nonempty demand every element almost surely
divides the state from some time on, since m ↦ am maps the admissible
set into its multiples of a injectively and gives
P(a divides the pick) ≥ w(a) at every state, for every element a and not
only the atoms. Being arithmetic rests on unique factorization:
entry-once, geometric depths and the crystal's probability
∏ (1 − w(g)) = 1/Σ w, the product over the atoms g and Σ w the weight
summed over every element, hold on a free monoid word for word, and the
last is the Euler product equalling the Dirichlet sum.

Freeness cannot be dropped. In the numerical monoid {x^n : n = 0 or n ≥ 2},
cancellative and not free since (x²)³ = (x³)², both atoms divide every
x^n with n ≥ 5, so every independence walk from the identity dies
within two moves, while under up-closed demands every element of the
same monoid eventually divides the state: two fates part inside one
world. Under the weight w(x^n) = t^n, 0 < t < 1, its Euler product
1/((1 − t²)(1 − t³)) leaves its Dirichlet sum 1 + t²/(1 − t) at t⁶,
one element with two factorizations, 1024/945 against 13/12 at
t = 1/4. And independence consumes: a move once taken
is never admissible again, so the demand owns no fixed standing move,
and a standing family for it is made of recipes
(GROWTH.md#the-standing-move-dichotomy).

## The grading and the radical
Tier: theorem.
Verifier: proof; thermal.py::section_z, thermal.py::section_i.

Heat grades each property of a fate by how much of the selection it
needs. Mortality needs none: it holds on every trajectory.
Independence's destination, every prime seated, needs only a floor,
independent of the state, on the probability that an unseated prime
divides the pick (p^−β/(ζ(β) − 1) under independence,
THERMAL.md#the-zeta-measure), and holds almost surely but never surely,
since picking odd prime squares forever is admissible. The squarefree
profile, the increasing route
(GROWTH.md#the-route-is-the-deleted-places) and the lock needed the
argmin itself and melt at every finite β: from seed 1 the first
independence pick is 2 with probability 2^−β/(ζ(β) − 1) and a power of 2
with probability 1/((2^β − 1)(ζ(β) − 1)), 0.3876 and 0.5168 at β = 2.

The limits, for a squarefree seed s:

    demand          β = ∞                    β < ∞
    transparency    W(λ(seed))               W(λ(seed))
    independence    ∏ p, the crystal         the zeta measure from s
    dynamics        one column               Ẑ

Ẑ/J = ∏ F_p, with J, the elements of Ẑ that every prime divides, the
Jacobson radical of Ẑ, so cold independence grows the quotient by the
radical and hot dynamics grows Ẑ itself: what hot dynamics holds beyond
cold independence is exactly J, while hot independence adds finite
depths and never J, entry being once. Cold independence and hot dynamics
are the two cells of the table that forget the seed: cold dynamics locks
onto a prime the seed sets, 2 from seed 2 and 7 from seed 11
(GROWTH.md#the-lock-prime-law).

## The melt over F₂[x]
Tier: theorem.
Verifier: proof; thermal.py::section_f.

Weight a monic m by |m|^−β = 2^(−β·deg m). There are 2^d monics of
degree d, so the free partition function over degree ≥ 1 is r/(1 − r)
with r = 2^(1−β), rational in 2^−β, and 1 at β = 2. The zeta measure
transfers word for word, each place g's depth geometric of ratio
|g|^−β, and the crystal probability is 1/ζ_(F₂[x])(β) = 1 − 2^(1−β),
exactly 1/2 at β = 2 against Z's 0.6079: every closed form here is
rational in 2^−β. λ is divisibility-monotone here too, so dynamics'
admissible set is upward-closed, and never empty since the wall is
finite (GROWTH.md#the-wall-over-f₂x), and |gm| = |g|·|m| gives the floor
P(g divides the pick) ≥ |g|^−β: hot dynamics reaches the full profinite
completion of F₂[x] at every β > 1. The sprawl
(GROWTH.md#the-sprawl-over-f₂x) is an artifact of β = ∞ as Z's lock is:
x + 1, starved forever by the greedy walk, opens almost surely. Hot
dynamics' limit is the same object on the whole range 1 < β < ∞, so the
only transition sits at β = ∞, and the thermal law needs no tie-break,
where the greedy walk over F₂[x] needed one.

## The two tests
Tier: criterion (proved; checked on 20 states against every monic of
degree ≤ 9, the fresh law on every Δ ⊆ {1, …, 12} at d ≤ 14).
Verifier: proof; thermal.py::section_f.

Over F₂[x], λ(g^a) = (2^d − 1)·2^⌈log₂ a⌉ at g of degree d
(GROWTH.md#the-wall-over-f₂x), so with c = v₂(λ(M)) a move m is
admissible iff it passes the **clock test**, some place of Mm at depth
above 2^c, or the **odd test**, some place of m absent from M whose
2^(deg g) − 1 does not divide λ's odd part: the 1-units are 2-groups and
the Mersenne factors are odd, so nothing else moves λ. The **fresh law**
decides the odd test: for d ≥ 2 and a set Δ of degrees, 2^d − 1 divides
the lcm of 2^d′ − 1 over d′ in Δ iff d divides some d′ in Δ. One way is
direct; the other takes a primitive prime of 2^d − 1, whose order of 2
is d (Zsigmondy's theorem), and at d = 6, where none exists, 9, whose
order of 2 is 6. So the odd test passes at most once per degree, never
at degree 1, and opening degree d′ closes it at every divisor of d′. The
two tests are the module law's split (GROWTH.md#the-module-law) read as
a list of moves.

## The mortality split
Tier: theorem.
Verifier: proof; thermal.py::section_f, thermal.py::section_b.

Restrict the moves to degree at most D. Every admissible move raises c
or passes the odd test at a degree from 2 to D not passed before, so a
trajectory of T moves has T ≤ (D − 1) + (c_T − c₀), and a clock at c
needs a depth above 2^(c−1), so 2^(c_T − 1) < deg M₀ + D·T. Together
T < D + log₂(deg M₀ + D·T) − c₀, false for large T, so T is bounded:
every restricted trajectory over F₂[x] halts, at every β and under any
policy. Over Z it need not: from 2^a with a ≥ 3 and a ≥ 2 + max
v₂(p − 1) over the odd primes p ≤ B, the move 2 stays admissible under
the restriction m ≤ B forever, since the odd part of the state can lift
λ's 2-part no higher. So every infinite trajectory over F₂[x] picks
moves of unbounded degree, since a tail inside degree D would halt. This
is the module law's rank split read as mortality: its pump prices a tick
at a constant, which a restricted walk pays forever, and the log clock
at a degree that outgrows every restriction, at every temperature. The
split has a price. Keep a halted world alive by multiplying in, at each
halt, the least-degree monic after which a move of degree ≤ D is
admissible: that bill is the least d·(2^c + 1 − ⌊D/d⌋ − v_g(M)) over
irreducibles g of degree d ≤ D, since no injection reopens an odd test.
Once a degree-1 place g leads a revival with D < 2^c, its one admissible
move is g^D, which raises the clock by one and halts the world again,
while any other place of degree d, standing at most 2^c − ⌊D/d⌋ since
the world halted at clock c, costs at least d(2^c + 1) at that next
halt: g leads forever, each revival buys exactly one move, and the bill
at every later halt, of clock c, is 2^(c−1) − D, its power-of-2 term
doubling with every move bought. Over Z the world from 2^a above needs
no revival. Heat melts what selection authored and leaves what the
module authored.

## The place spectrum
Tier: theorem; observation (the points, their order, the least below
1000).
Verifier: proof; spectrum.py::section_q.

Lock dynamics on one prime q and deepen it: the column q^a. Its
headroom is set by q's own arithmetic. At odd q,
λ(q^a) = (q − 1)·q^(a−1), and W(λ) carries q to the exponent a, exactly
the state, so q never divides the headroom: ξ(q^a) is 2^(v₂(q−1)+2)
times every odd prime p ≠ q with p − 1 dividing (q − 1)·q^(a−1), each at
the exponent v_p(q − 1) + 1. The exclusion p ≠ q is part of the formula:
q itself has q − 1 dividing λ, but its exponent a is spent by the state;
dropped, the formula is wrong at every odd column checked. At q = 2,
λ(2^a) = 2^(a−2) for a ≥ 3, the 2-part cancels, and the Fermat primes
are left. As a grows the headroom rises to a limit C_q, the same 2-part
and the same exponents over every odd prime p ≠ q of the form d·q^i + 1
with d dividing q − 1. C_q is a supernatural number, a formal product
that may hold infinitely many primes (whether 2·3^i + 1 is prime
infinitely often is open), and its divisor sum σ_β(C_q) is the
convergent product of the factors' sums. The column's normalizer falls
to Ψ_col(q) = ζ(β) − σ_β(C_q).

Each finite place q has its **critical point** β_q, the root of
Ψ_col(q) = 1. Given the depth reached by a column's walk, the set of
lower depths it passed through holds each depth a independently with
probability 1/(1 + Ψ_(q^a)), Ψ_(q^a) the normalizer there
(MEMORY.md#the-unbounded-memory-law at q = 3; the argument holds
wherever every move q^r, r ≥ 1, raises λ, at every depth of an odd
column and from depth 3 on at q = 2), so β_q is where that coin turns
fair in the deep limit. There is exactly one, and it lies in (1, β*),
β* = 1.72865 the root of ζ = 2: Ψ_col(q) is a sum of m^−β over a
fixed set of m, so strictly decreasing; the sum of 1/p over the
primes d·q^i + 1 converges, so σ_β(C_q) stays bounded as β → 1 while
ζ does not; and C_q has a divisor above 1, which puts Ψ_col(q) below
ζ − 1, and that is 1 at β*. A column whose headroom has the larger
divisor sum at every β crosses at the smaller β. The points are
β_2 = 1.60449, β_3 = 1.49595, β_5 = 1.42057, β_7 = 1.42344 and
β_11 = 1.43666, so they are not monotone in q; over the 168 primes
below 1000 the least is β_541 = 1.28150.

## The 2-adic place is the top
Tier: theorem.
Verifier: proof; spectrum.py::section_q.

β_2 > β_3 > β_q for every prime q ≥ 5. Each Ψ_col(q) decreases, so
β_q < β_r follows once σ_β(C_q) > σ_β(C_r) at every β > 1; write σ for
σ_β and b for β.

(a) At odd q ≠ 3 the headroom holds 8 and 3, so
σ(C_q) ≥ σ(8)·(1 + 3^−b). C_2 is 3 times the Fermat primes F ≥ 5, each
of the form 2^(2^n) + 1 with n ≥ 1, known or not, and the sum of 2/F
over all n ≥ 1 is below 0.5255. With Y the sum of F^−b,
Y ≤ 0.5255·2^−b ≤ 0.263 at b ≥ 1, so
∏ (1 + F^−b) − 1 ≤ Y·e^Y ≤ 0.684·2^−b, which is below σ(8) − 1. So
β_q < β_2.

(b) At q = 3, σ(C_3) ≥ 1 + 2^−b + 4^−b + 7^−b, and the same bound taken
against 5, the sum of 5/F being below 1.3137, gives
σ(C_2) ≤ 1 + 3^−b + 1.7085·(5^−b + 15^−b). Now 7^−b ≥ 1.7085·15^−b since
15/7 > 1.7085; 2^−b − 3^−b ≥ 2^−b/3; and 2^−b/3 + 4^−b > 1.7085·5^−b,
since (5/2)^b/3 + (5/4)^b ≥ 2.083 at b ≥ 1. So β_3 < β_2.

(c) At q ≥ 5, σ(C_3) = σ(8)·∏ (1 + p^−b) over the primes p = 2·3^i + 1
with i ≥ 1, and the sum of (2·3^i)^−b is at most 0.75·3^−b ≤ 0.25, so
the product is at most 1 + 0.9631·3^−b, below the factor 1 + 3^−b in
σ(C_q). So β_q < β_3.

The top place is the one whose headroom is thinnest: the 2-column
cancels its own 2-part and sees only the Fermat primes. The verifier
recomputes the three constants (0.68335, 1.70837, 0.96302) and checks
each inequality on a grid of b from 1 to 12.

## The algebraic clock over F₂[x]
Tier: theorem; observation (the points at degrees 1 to 6 and their
order).
Verifier: proof; spectrum.py::section_f.

Over F₂[x] the column is g^a at an irreducible g of degree d, and
λ(g^a) = (2^d − 1)·2^⌈log₂ a⌉ (THERMAL.md#the-two-tests). So f^j, with
f ≠ g of degree e, divides the headroom of g^a iff e divides d and
j ≤ 2^⌈log₂ a⌉: the headroom holds every place but g whose residue field
embeds in g's, F_(2^d), each at a depth that grows without bound, and g
itself to depth 2^⌈log₂ a⌉ − a. At the states a = 2^μ the headroom holds
no power of g, and the limit is the divisor sum
S_d(z) = ∏ (1 − z^e)^−(N_e − δ) over e dividing d, with z = 2^−β, N_e
the number of irreducibles of degree e, and δ = 1 at e = d and 0
otherwise, since g itself is absent. The zeta function is 1/(1 − 2z), so
the critical equation ζ − S_d = 1 clears to a polynomial in z, and every
critical point is minus log₂ of an algebraic number. Write γ_d for the
critical point of a place of degree d, read along the states a = 2^μ. At
d = 1 the polynomial is 2z² − 4z + 1: 2^−γ₁ = 1 − 1/√2 and
γ₁ = log₂(2 + √2) = 1.77155, below 2, where z = 1/4 and this ring's zeta
is 2.

Degrees 1 to 6 give 1.77155, 1.50553, 1.47652, 1.39505, 1.48768 and
1.33584. Two places of one degree share their point exactly, and
degree 5 sits above degree 3. Degree 1 is the top: for d ≥ 2 the
headroom holds both places of degree 1 at unbounded depth, so
S_d ≥ (1 − z)^−2 coefficient by coefficient, strictly above
S_1 = (1 − z)^−1 from z¹ on.

Between the states 2^μ the column breathes: at a = 2^μ + 1 the headroom
holds g itself to depth 2^μ − 1, the limit along those states is
S_d/(1 − z^d), and at d = 1 that is (1 − z)^−2 = S_2, so the degree-1
column just after a tick sits at the degree-2 point.

## The class split
Tier: theorem (the headroom reads the splitting law, and the ratio of
the normalizers tends to the class number h); observation (the
headroom's entrants and depths at P3, and the points at four columns
of Z[√−5]).
Verifier: proof; spectrum.py::section_k.

At a prime P of a number ring, of norm N over p,
λ(P^a) = (N − 1)·p^(ν(a)), with ν(a) growing without bound as a grows,
since the 1-units of the completion contain a copy of the p-adic
integers. A prime R ≠ P, over the rational prime r, enters the limit
headroom up to the largest j with λ(R^j) dividing (N − 1)·p^∞, which
depends on N, p and R's own chain and never on ν. So a column over a
number field reads the splitting law, which primes lie over which r and
with which norms, and never its own chain. In Z[√−5], at the prime P3
over 3, the headroom holds the prime P2 over 2 to depth 2, the conjugate
P3′ without bound, paid by the column's own 3-power, and both primes
over each split prime r = 2·3^i + 1: 7, 163, 487 and 39367 below 10⁶,
the range spectrum.py reads, and 2·3¹⁶ + 1 next. The primes 19 and 1459
have r − 1 dividing 2·3^∞ but are inert, of norm r², and r² − 1 is
divisible by 8, and never enter. Every entrant is nonprincipal: P2 and
P3′ hold no element of norm 2 or 3, and each split r = 2·3^i + 1 is 3
mod 4, so no x² + 5y².

The element world, whose moves must be principal, splits the point.
Its normalizer is the weight N(·)^−β summed over every principal ideal,
(1/h) times the sum of L(β, χ) over the characters χ of the class group
(ELEMENT.md#the-class-gap-between-principal-and-all-ideals), less the
same weight summed over the headroom's principal divisors, (1/h) times
the sum over χ of the headroom's divisor sum twisted by χ, as Ψ_col(q)
is ζ(β) less σ_β(C_q). At P3, where h = 2, the element
point is 1.35270 against the ideal point 1.54922. The class number is
read at the pole and not off the two points: only ζ_K has a pole at
β = 1, while the headroom's sums, plain and twisted, stay bounded
there: its entrants' norms are d·p^i + 1 with d dividing N − 1,
geometric in i, so Σ N(R)^−1 converges, and each entrant's own factor
is geometric too; so
the ratio of the ideal to the element normalizer tends to h,
and at P3 it falls through 2.0317, 2.0056 and 2.0010 at β = 1.2, 1.05
and 1.01. Four ideal points, each read at the states whose headroom
holds no power of the column's own prime, order as P2 1.70395 > P3
1.54922 > 1.45633 at a prime over 7 > 1.31983 at the inert prime over
13: the place with residue field F₂ is again on top.

## Open fronts

Whether a place with residue field F₂ tops the spectrum over every
number field that has one. It does at the four columns of Z[√−5]
computed, and the argument over Z does not carry as it stands. There
every odd column's headroom holds 8, which alone outweighs the Fermat
primes past 3, and every odd column but 3's holds 3 too; in Z[√−5] a
column whose N − 1 is 2 times an odd number holds P2 only to depth 2,
and 1 + 2^−β + 4^−β is lighter at β = 1 than the P2 column's own
headroom, both primes over 3 and the prime over 5.
