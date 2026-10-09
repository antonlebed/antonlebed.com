# FORGET — when a state provably no longer holds a datum

The object: a **history space** H with a positive weight π or a family
π_β of them, β > 0; a **datum** X, any function of history to be
forgotten; and a **state map** Φ, the still-working present. The datum's
posterior at a state s is π conditioned on the fiber Φ⁻¹(s) and pushed
to X. The question is when a state provably no longer holds X, what buys
that at every weight, how the answer moves when X is coarsened, and what
is left of it when the state must keep computing a function of history.
A **grown world** gives the weights by THERMAL.md's thermal law with its
admissible set replaced by a **menu**, the moves offered at each step,
possibly depending on the route so far where MEMORY.md's depends on the
state alone, each move m multiplying the state by m and drawn with
probability m^−β / Ψ, Ψ the sum of n^−β over the moves n offered, a
history being the route of moves from the state 1. There a state does
two jobs, the integer a route reaches and a value of Φ, and Φ is the
dated state, that integer with its move count, unless a section takes
another. Its verifiers are forget.py and quarantine.py.

The thesis: in a grown world, hiding the route at every temperature
from the dated state, or from any refinement of it, costs prime
recycling (FORGET.md#the-quarantine-theorem). Forgetting is
graded fiber by fiber, from readable through spread and tuned to robust
(FORGET.md#the-four-grades). A structural **witness**, a factoring of
the history with the datum's slot uniformly weighted or a symmetry of
the normalizers, buys the robust grade, flat at every weight, but is not
needed: a world recycling its primes can be robust for the route with
none, while a world that never recycles
(FORGET.md#the-quarantine-theorem) is robust for the route on no
**dated fiber**, the histories sharing a state and a move count, their
**age**, written (state, age), holding two routes, at any age. No grade
passes from a datum to its functions except readability: a state flat
for the route can leak the first move. A state that must keep computing
a function g can forget X across a g-fiber only by cutting that fiber
into blocks each spread and flat, a cure
(FORGET.md#the-working-clause): two classes never cure by refinement,
and at equal weights a cure exists iff no class holds a majority.
Keeping less of g can leave its fibers with no cure.

## The four grades
Tier: property; observation (the breadth world's 363 fibers).
Verifier: proof; forget.py::section_grades.

A fiber is **readable** when it meets one class of X, and the state then
reads X. It is spread when it meets two or more, and then flat at a
weight when the classes it meets carry equal mass there. A spread fiber
flat at some members of the family but not every one is **tuned**, and
one flat at every member is **robust**. So a fiber has one of four
grades: readable, spread and flat at no member, tuned, or robust.
Flatness is uniformity behind what the state pins, not
posterior = prior: a grown world's state is its present, which always
informs its past.

A world is given by its menus, a state with none listed offering no
move. Spread does not bring flat. The **breadth world**, the squarefree
moves 2 to 30 coprime to the state, holds each route's moves
distinct and in every order at every multi-route fiber, and none of
the 363 to age 3 is flat at β = 1. The
**tuned world**, menu(1) = {2, 3}, menu(2) = {3, 5, 15},
menu(3) = {2, 10}, is flat for the route at fiber (6, 2) at β = 1, where
Ψ(2) = Ψ(3) = 3/5, with normalizers that differ as functions of β, and
its odds are 117/70 at β = 2. One world hides different parts of the
route at β = 1 at different fibers: (6, 2) holds one move set in two
orders, (30, 2) two sets, {2, 15} against {3, 10}, one order each, and
both are flat for the route.

## Two witnesses buy the robust grade
Tier: theorem.
Verifier: proof; forget.py::section_factoring,
forget.py::section_grades.

Factoring. Let H = 𝒳 × R, π_β(x, r) = μ(x) ν_β(r) and Φ(x, r) = h(r).
Then the posterior of X, the 𝒳 slot, is μ at every state and every β, so
every fiber is robust when μ is uniform on two or more values.
Conversely, posterior = prior under every product weight holds only when
Φ ignores the 𝒳 slot. Normalizer symmetry. On a dated fiber of a grown
world holding two routes or more, if the multisets of the normalizers
each route passes before its endpoint agree, as functions of β, the
fiber is robust for the route.

Proof. The fiber of s is 𝒳 × h⁻¹(s), on which X is distributed as μ.
Conversely, on a fiber F with sections F_x = {r : (x, r) ∈ F} the
posterior is proportional to μ(x) ν(F_x), so it is μ for every μ iff
ν(F_x) is the same for every x; a ν with generic values separates
distinct subsets, so the sections coincide and F = 𝒳 × F_x. For the
symmetry, the route-weight cancellation
(MEMORY.md#the-route-weight-cancellation) makes the route posterior
proportional to the product of 1/Ψ over the states it passes before its
endpoint, and equal multisets have equal products.

The **depth column**, the constant menu {2, 3}, has one normalizer, so
every dated fiber holding two routes is robust for the route.

## The quarantine theorem
Tier: theorem.
Verifier: proof; quarantine.py::section_arms,
quarantine.py::section_last.

A grown world **recycles** when some menu offers a move sharing a prime
with the integer it is offered at, and is coprime otherwise: every menu
is coprime to that integer. In a coprime world no two distinct routes
of a dated fiber carry equal posteriors at every β, at any age. So no
dated fiber holding two routes is robust for the route, and no state
map refining (state, age) cuts a dated fiber holding two routes into
blocks each spread and flat for the route at every β. The menus may
depend on the whole route so far, not only on the state.

Proof. A route's posterior is proportional to 1/D, D the product of the
normalizers it passes (MEMORY.md#the-route-weight-cancellation); each Ψ
is a Dirichlet polynomial with coefficient 1 at each menu element, and a
tie at every β is equality of the D as formal Dirichlet polynomials.
Induct on the age, for two routes from any shared start state; a
route of age 1 is its endpoint over the start. Cancel the shared factor of
the start state, the formal Dirichlet polynomials being a domain. The
coefficients are nonnegative, so the support of the rest is the set of
products of one element per later menu, and both routes' later menus use
one set of primes S. Every later state is divisible by the first move,
and coprime menus avoid its primes, so each route's first move is prime
to S, while every later move is drawn from a later menu and lies over S.
The first move is then the part of the endpoint prime to S, the same for
both routes: the routes share their first state and its menu, whatever
the menu reads, and the induction runs on from there.

The theorem needs coprimality to the whole state. A world whose menus,
indexed here by route, avoid only the last move's primes escapes:
menu() = {2, 3}, menu(2) = {3, 5}, menu(3) = {2, 5},
menu(2, 3) = {2, 5}, menu(3, 2) = {3, 5} holds the fiber (30, 3) at the
routes 2,3,5 and 3,2,5 with equal normalizer multisets. The scan agrees
at every draw: no tie in 141,216 fibers of age 2 and 3 over all 87,885
coprime tables of state menus on the moves 2 to 6 with every allowed
menu nonempty, fibers counted table by table, or
in 3,183 fibers of random coprime worlds with state or route menus to
age 4, while the same scan finds ties once coprimality is dropped. Since
flatness passes in neither direction under coarsening
(FORGET.md#readability-descends-spread-ascends-flatness-neither), the
theorem says nothing of a coarser datum. Measured only, no coprime fiber
of the scan with at most eight routes hides its first move at every β, 0
of 120,386; whether a proof exists is open.

So exact amnesia of the route comes three ways. Normalizer symmetry and
a witness-free design (the rogue world,
FORGET.md#recycled-worlds-need-no-witness) hide it at every β and
both recycle, the depth column repeating its moves; tuning hides it at
finitely many β, the two routes' D differing by a nonzero finite sum of
exponentials, and is the only way open to a coprime world, the tuned
world being one.

## Recycled worlds need no witness
Tier: property.
Verifier: proof; quarantine.py::section_rogue,
quarantine.py::section_coarse.

The **rogue world**, menu(1) = {2, 32}, menu(2) = {2, 4, 8},
menu(16) = {2, 16}, menu(32) = {2, 4}, menu(128) = {2, 8, 32}, holds the
dated fiber (256, 3) at exactly 2,8,16 and 32,4,2, robust for the route
with normalizer multisets that differ. Three is the least age this
takes, a fiber of age 1 holding one route. The **coarse world**, every
move a power of 2, holds a witness-free tie beside a symmetric one and
so buys a cure (FORGET.md#the-working-clause) flat at every β, where the
dated state, the state with its age, is flat at one β only (a strict
cure at every β but that one,
FORGET.md#a-strict-cure-needs-three-classes):
menu(1) = {2, 4, 8, 16}, menu(2) = menu(4) = {4, 8}, menu(8) = {8},
menu(16) = {8, 16}, menu(64) = {2, 4}, menu(128) = {2} hold (256, 3) at
P = 2,8,16, Q = 4,4,16, A = 8,8,4 and B = 16,8,2, the dated state leaks
the route at every β but log₂ of the golden ratio (1 + √5)/2, and the
blocks {P, Q} and {A, B} are spread and flat at every β.

Proof. With x = 2^−β the rogue products are (x + x² + x³)(x + x⁴) and
(x + x²)(x + x³ + x⁵), both x² + x³ + ⋯ + x⁷: the two pairings of
(1 + x)(1 + x + x²)(1 − x + x²), whose last factor has a negative
coefficient and so stands in no menu alone. At age 2 each route passes
one state after the start, so a tie is one Ψ equal to another, one menu,
the witness. In the coarse world Ψ(2) = Ψ(4) ties P and Q,
x³(x + x²) = (x³ + x⁴)x ties A and B, and P's product is A's times
x(1 + x), which is 1 only at x = (√5 − 1)/2. Which ties a recycling
world can hold at all is
COLLIDE.md#a-witness-free-tie-is-a-regrouping-or-passes-a-seed.

## Readability descends, spread ascends, flatness neither
Tier: theorem.
Verifier: proof; forget.py::section_coarsening.

Let f be a function of X's values. A fiber readable for X is readable
for f(X), and a fiber spread for f(X) is spread for X. Flatness passes
in neither direction. In the depth column at the dated fiber
(2^a 3^b, a + b), a, b ≥ 1, the first move is 2 with posterior a/(a + b)
at every β: the **count leak** a/(a + b) − ½, zero only at a = b, in a fiber
robust for the route that meets both classes of the first move, so leaks
it without reading it.

Proof. A fiber meeting one class of X meets one of f(X), and one
meeting two classes of f(X) meets two of X. Down: a flat posterior
pushed through f gives each class of f(X) mass in proportion to the
number of X-classes it holds. Up: a class of a flat f(X) may split
unevenly, as X's classes of masses ⅓, ⅙ and ½ do when f merges the
first two. In the depth column the routes of the fiber are the
C(a + b, a) arrangements, equally weighted, and C(a + b − 1, a − 1)
of them open with 2.

So a certificate for a datum does not certify its functions, and each
coarsening owes its own flatness. The exact readout of
LEARNER.md#exact-readout-reads-the-subdominant is not this leak in
another form: it reads which classes a component meets and never how
many, so it follows readability downward and never sees a count.

## The working clause
Tier: property.
Verifier: proof; forget.py::section_working.

A state that must retain a function g of history computes it iff Φ
refines g, so the admissible state maps are the interval from g to the
discrete partition, and a choice inside one g-fiber constrains no other.
A g-fiber is **cured** at a weight when it can be cut into blocks each
spread and flat there, and its price is the fewest blocks. A g-fiber
meeting one class of X is readable under every admissible Φ. The
two-class law and, at equal weights, the no-majority criterion below
read the classes' masses and counts and nothing else: no menu, prime or
temperature. They are facts about a finite weighted partition lattice,
and a grown world enters only by supplying the weights; under unequal
weights a cure reads the histories' masses, not only the classes'.

## Two classes never cure by refinement
Tier: theorem.
Verifier: proof; forget.py::section_working.

A g-fiber meeting exactly two classes of X, of masses w₁ and w₂, is
cured iff w₁ = w₂, that is, iff Φ = g is already flat there. In the
depth column with the dated state retained, the first move leaks at
every dated fiber (2^a 3^b, a + b) with a, b ≥ 1 and a ≠ b, and no
state design stops it.

Proof. Every spread block holds both classes and a flat one holds
them at equal mass; summing over the blocks, w₁ = w₂. The converse is
the one-block cut.

## The no-majority criterion
Tier: criterion.
Verifier: proof; forget.py::section_working.

On a g-fiber of N equally weighted histories whose classes have counts
c₁ ≥ c₂ ≥ … ≥ c_ℓ, a cure exists iff c₁ ≤ N − c₁. Under unequal
weights a cure needs the largest class mass to be at most half the
fiber's, and that is not enough: exact cuts are subset-mass matching,
and the fibers passing the mass test with no cure are the **matching
gap**.

Proof. A block takes t ≥ 1 from class 1 and, being flat and spread, at
least t from the others; summing gives necessity, by count or by mass.
At even N, list the histories by class and pair the i-th with the
(i + N/2)-th: no class fills more than half the list, so every pair
holds two classes. At odd N two classes would force c₁ = c₂ and N even,
so ℓ ≥ 3; a triple from the three largest classes leaves N − 3 histories
whose largest count, c₁ − 1 or c₄, is at most (N − 3)/2 (c₄ ≤ N/4 ≤
(N − 3)/2 once N ≥ 7, and c₄ = 1 at N = 5), and the even case
finishes.

The search agrees at every count vector of 2 ≤ N ≤ 8, and on 400 drawn
weighted fibers 47 of the 86 passing the mass test have no cure.

## Retaining less can leave no cure
Tier: theorem.
Verifier: proof; forget.py::section_retention.

In the depth column, retain the age alone. The first move is then 2 with
posterior 3^β/(2^β + 3^β) > 1/2 at every β > 0, a strict majority, so no
cut of the age fiber cures it, while retaining the dated state leaves
every dated fiber (2^a 3^b, a + b) with a = b ≥ 1 flat at every β.
Every state map admissible before stays admissible, the dated state
among them; what is lost is the cure, graded on the coarser g-fiber.

Proof. The first move is drawn once from the constant menu and nothing
later depends on it, so on the age fiber its posterior is the first
step's, 2^−β/(2^−β + 3^−β). A strict mass majority fails the necessity
of the no-majority criterion in every partition. On a dated fiber the
numerators cancel, which is what the age alone does not do.

## A strict cure needs three classes
Tier: theorem.
Verifier: proof; forget.py::section_retention.

A cure the coarsest state map Φ = g lacks, a **strict cure**, needs a
g-fiber meeting three classes of X or more, and one exists. In the depth
column, retain the dated state and, on the dated fiber (24, 4), forget
the first two moves: the routes 3222, 2322, 2232 and 2223 give counts
(2, 1, 1) and Φ = g gives the classes (½, ¼, ¼), while the blocks
{3222, 2232} and {2322, 2223} are spread and flat at every β, price 2.

Proof. One class is readable, and two classes cure only when already
flat. In the example the dated fiber's routes are equally weighted,
and each block holds one route of the doubled class and one singleton.

Partition design alone buys a robust certificate Φ = g lacks.

## Open fronts

Whether some coprime fiber hides its first move at every β, which asks
for an identity between sums of route weights rather than a collision
of products; where the quarantine's boundary lies past the one escape
stated, for menus that read the state at mixed ages; and whether the
recycled side holds a witness-free fiber of three or more routes flat
at every β.
