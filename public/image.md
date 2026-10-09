# IMAGE — the set of limits a greedy walk reaches

The object: a greedy growth walk under the dynamics demand, every tie
followed, over Z, over an imaginary quadratic ring and over the ring of
a curve over F₂, in the ideal and the element world. Its **greedy image**
is the set of limits of all its branches. This page asks how big that
set is, what the walk must be run for and what the ring's supply
decides without a run, which of a ring's features reach the count, and
whether a lock that carries its rider adds a limit or removes one, and
what the image becomes when every policy is free. Its verifiers are
image.py and free_image.py, with race.py for the widest tie a cubic
ring stages.

A place's **colour** is what the dynamics reads of it: over a curve its
degree in the ideal world and its (degree, class) in the element world,
as in ELEMENT.md; over a number ring its norm and local kind, the (e, f)
and width that fix its ladder (CLOCK.md), with its class in the element
world. The **supply** σ(ω) counts the places of colour ω, LIMIT.md's
count of items per degree read by colour. A limit gives every place an
exponent or ∞; a walk that locks repeats one vehicle forever, sending
that vehicle's support to ∞ and freezing the rest. The shape of a state or a
limit forgets which place of a
colour carries which exponent, keeping per colour the multiset of
exponents. The **rider reach** is the union of the supports of the least
divisors of every class, the minimal riders MINREP(c), c a class.

The answer, in one line: the image is a sum over the limit shapes a walk
reaches of products of multinomials over the supply, so a walk is run
only to find its shapes; over Z that is one point, over an imaginary
quadratic ring, on every seed run, where the walk locks, a finite
number, 2^t in the ideal world, t the ties a trajectory meets, and over
a curve with a rational place besides the one removed, at LIMIT.md's
corner, in the ideal world, the continuum; and the lock that carries its
rider removes a limit, the one choice it can reach, at the two seeds of
Q(√−23) whose tie lies in its support. Free every policy in the ideal
world and the ring drops out: the image is one of five forms fixed by
the demand and the seed, and the ring reaches it only through the wall.

## The colour count
Tier: theorem.
Verifier: proof; image.py::section_o.

Every permutation π of the places that preserves colour and fixes the
seed maps branches to branches. λ of a state, the exponent of its unit
group (GROWTH.md, the dynamics demand), is an lcm of place
contributions read off (degree, exponent), or (norm, kind, exponent)
over a number ring; a door is the least r with λ_P(a + r) not dividing
L, where a is P's exponent, λ_P(b) is λ(P^b) and L is the state's λ; a
price is d·r over a curve, d the place's degree, or N^r over a number
ring, N the place's norm, joined in the element world by the least rider of
class −r·c, c the place's class, its degree m(−r·c) added over a curve
and its norm multiplied over a number ring; and a rider is a least
divisor of class −r·c, which π, keeping degree or norm and class, sends
to a least divisor of the same class. With every least vehicle on the
menu, π carries menus to menus (over the curves one least divisor per
class, ELEMENT.md#the-minimal-rider-is-unique, and at the two quadratic
rings walked; over Q(√−15) two, which π may swap), and the limit map
commutes with π, and the image Im(s) of the seed s is a union of
orbits. The orbit of a limit X is counted by the supply alone:

    |Im(s)| = Σ over the limit shapes reached of
              ∏ over colours ω of σ(ω)! / ∏_k n(ω, k)!,

a colour refined by the seed's exponent, σ(ω) then counting the places
of the refined colour, and n(ω, k) the places of ω at exponent k in X,
the places at 0 included. The walk is run to find the
shapes, and the supply prices each. The product of tie multiplicities
over a trajectory's openings is the case of one shape whose opened
colours carry one place at exponent 1 each, and a tie between two
colours separates limits wherever its branches reach different shapes.
A count of trajectories is not a count of limits: a limit forgets the
order of seating and the finite exponents at the places it sends to ∞.

The verifier checks it by brute force from the void, to a finite
depth. An engine over every place of degree ≤ 9, λ read as an
integer, reaches exactly the shapes of the
walker that reads colours alone (limit.py's corner, element.py's element
world) at every depth, and every shape's labelled states number exactly
its product: F₂[x] and ELEMENT.md's curves h2 and g2 in the ideal world
to depth 9, 9 and 8 (6,480, 12,096 and 4,608 states at the last), h2, h3
and g2 in the element world to depth 11. In the element world the
(degree, class) colouring is the coarsest that prices every menu
(ELEMENT.md#the-coarsest-colouring), and the one coarsening run on the
count fails it: grouped by degree alone the element world's states sit
off the degree multinomial at every depth of all three rings. A price
reading one place's label breaks the count at every depth of F₂[x].

## A quadratic ring's ideal image is 2^t
Tier: rule (the tie shape and the conjugate never seated proved; the
count verified at Z[√−5] and Q(√−23) over the void and every ideal of
norm ≤ 40; the bound on a tie's width attained at one cubic ring).
Verifier: image.py::section_q, race.py::section_width.

A least move P^r costs N(P)^r, a power of P's rational prime, so two of
equal cost lie over one prime, and a prime carries two places only when
it splits: every tie is a conjugate pair, one colour with σ = 2.
Conjugates share a ladder, so if K is the least depth whose λ does not
divide L, a seated P at depth a ≥ 1 has door K − a and its unseated
conjugate door K: the conjugate is dearer by a factor of at least
N(P)^a at every later state, its **starvation**, and is never seated; a
conjugate seated shallower, at b < a, stands dearer by a factor
N(P)^(a−b) and never moves. The walk locks on every seed run
(GROWTH.md#the-lock-over-a-number-ring), and where it locks a
trajectory makes finitely many ties t, the same t on every branch by the
colour count, and the two members of each stand at different exponents
in every limit. The image is one shape, of 2^t
limits. Its symmetry is a swap at each split prime separately, so it is
a single Galois orbit only when t ≤ 1, and then only at a Galois-stable
seed. Over a field of degree n every tie still lies over one rational
prime, which carries at most n places, so a tie is at most n wide, and
the bound is reached: at x³ − x + 3, discriminant −239, 3 splits
completely, its three places each complete to Q₃ and share a ladder, and
they tie at the void; the winner runs at price 3 and its partners, their
doors raised by the shared unit, are never seated, one shape of
3!/(1!·2!) = 3 limits.

At Z[√−5] t is 0, 1 and 2 at 35, 15 and 2 of 52 seeds, and at Q(√−23) 0
and 1 at 65 and 14 of 79: every seed's branches share one t, its limits
number 2^t in one shape, and the starvation held at every state visited,
4,028 checks of strict dearness.

## The lock's rider erases a choice
Tier: rule (verified at the void and every principal ideal of norm ≤
40: 26 seeds at Z[√−5] and 27 at Q(√−23)).
Verifier: image.py::section_q, element_ring.py::section_walks.

In the element world conjugates carry inverse classes, so a conjugate
pair is one colour where its class is its own inverse and two colours
where it is not. At Z[√−5], of class number h = 2, the ten seeds with a
tie reach two
limits each in one shape. At Q(√−23), h = 3, four seeds reach two limits
in two shapes, and two reach two lock-time states and one limit. Those
two are the seeds (2) and (2)², and their two states differ at the two
places over 2 and nowhere else. The lock vehicle is (2) = P₂P₂′, a core
at door 1 and its rider (ELEMENT.md#the-lock-carries-its-rider), which
sends both places to ∞: which of the two stands deeper is a finite gap
the state keeps forever and the limit forgets. So the rider adds no
limit and erases one, and at these two rings the count is 2^(t − ε), ε
the ties whose two members both lie in a rider-carrying lock's support.
Z[√−5]'s lock (2) is the ramified place squared with no rider, and
Q(√−23)'s inert lock (5), at 3 of its 27 seeds on the single walk,
carries one place:
neither erases anything. Each of the 1,599 element menus the branched
walks read (image.py, every branch followed, a count apart from the
3,180 states of the single walks of
ELEMENT.md#the-number-rings-price-in-min-) equals the ring's own least
raising elements.

## A curve's image is the continuum
Tier: rule (proved from LIMIT.md's ideal limit at the corner and
ELEMENT.md's element world, both rules; the element half at every ring
whose principal places number two or more at infinitely many degrees,
which six rings meet at every degree above 2 opened past the transient
in 300 moves, the hypothesis read only at the degrees the run opens).
Verifier: image.py::section_c, image.py::section_e.

In the ideal world at the corner, over a curve holding a rational place
besides the one removed (all six the verifier runs), every branch's
limit is ∞ at one runaway C of degree 1 or 2 and one place at exponent 1
at each other opened degree, every supplied degree above 1 opening
(LIMIT.md#the-ideal-limit). So the shapes are at most two, and

    |Im| = σ(1) ∏_(d ≥ 2) σ(d)  +  σ(2) ∏_(d ≥ 3) σ(d),

each product over the supplied degrees, σ(d) > 0, the second present
exactly when σ(2) > 0, as the void menu then ties. Each product has
infinitely many factors of 2 or more, so each shape's orbit is the
continuum and its points are choice functions on the degrees: the
runaway, then one place per degree. The runaway degrees over every
branch followed, every tie branched over the first 10 moves, are {1, 2}
at the five rings with a degree-2 place and {1} at h5, which has none;
the runaway and the first ten openings of the degree-1 shape already
offer 10^11.6 at F₂[x] and 10^11.6 to 10^17.0 over the curves. No lock
is needed for a coordinate to be decided: every coordinate of this limit
is written down.

In the element world, past the transient, the walk to its last opening
that pays a rider, an opening at degree d takes a principal core and
pays no rider (ELEMENT.md#greed-pays-no-avoidable-rider), so it chooses
one of σ(d, 0) places. A declined one is never seated later: as a core
it is raised by a clock move (LIMIT.md), T the notch, at d(T + 1)
against its seated sibling's d·T at most, neither paying a rider, and
as a rider it cannot come, a rider's place being alone in its colour.
The recurrent price doubles while an opening costs its degree, so the
openings never stop, and every limit carries each
opened colour outside the rider reach as one place at a positive
exponent and the rest at 0: a factor σ(d, 0) per degree opened past
the transient. Over
every branch followed at the six rings, every opening past the transient
chose from two or more principal places but F₂[x]'s one of degree 2, and
every opened colour outside the reach ended with one seated place. The
reach is finite, since the class group is and each class has finitely
many least divisors: h − 1 rational places over an elliptic curve and
six places over g2.

## The gap
Tier: rule (the point proved, the continuum as the curve section's
rule, the finite count verified at the two quadratic rings on the seeds
run).
Verifier: growth.py::section_c, image.py::section_q.

Over Z least moves at distinct primes are powers of distinct primes and
never tie (GROWTH.md#the-lock-prime-law), so every branch is the one walk and
the image is a point. Over an imaginary quadratic ring it is a finite
number wherever the walk locks, as on every seed run, and over a curve
with a rational place besides the one removed, at LIMIT.md's corner, the
continuum; neither is countably infinite. Over the curve, however many
choices the walk loses to erasure, a limit forgetting the order of
seating and the finite history of a place it sends to ∞, one shape's
orbit is already the continuum, so the count cannot fall to the
countable.

## The free image has five forms
Tier: theorem.
Verifier: proof; free_image.py::section_k1, free_image.py::section_k2,
free_image.py::section_k3.

Let a policy take any move its demand admits, the demand one of the five
named below: transparency, independence, new idempotents and dynamics as
GROWTH.md defines them, and semisimplicity, which asks that the new
modulus be squarefree. The **free image** of a demand and a seed s is
the set of limits of every maximal run from s. In the ideal world, a
move multiplying the state by any proper ideal, several places at once
allowed, over every ring this page walks and any Dedekind ring with
finite residue fields, finitely many places of each norm and infinitely
many places (the rings of integers away from finitely many places of any
global field), it takes one of five forms, W(L) the wall, for any L the
maximum of the states whose λ divides L (shown below). A limit is
finite when its support is finite and every exponent finite, that
is when it is a state, and X ≥ s means every exponent of X is at least
the seed's:

    transparency     the one finite point W(λ(s));
    semisimplicity   s·∏_{P∈S} P, S infinite and off supp(s), at a
                     squarefree seed; the point s at any other;
    independence     s·∏_{P∈S} P^(a_P), S infinite and off supp(s),
                     every a_P finite;
    new idempotents  every X ≥ s of infinite support;
    dynamics         every X ≥ s that is not finite.

Closure: a coprime move carries no seated place, so the seed's and each
seated exponent are final, and a coprime move always exists, the places
being infinitely many, so S is infinite; a squarefree product admits no second
copy; a new idempotent needs a new place, so the support is infinite;
and a dynamics run never halts, a place P off the current state M
with λ_P(1) > λ(M) always existing since finitely many places have
bounded size, while infinitely many non-unit moves cannot converge to a
finite limit.
λ(lcm) = lcm(λ) and λ is monotone under divisibility, so {M : λ(M) | L}
is closed under lcm, and finite, since finitely many places have
N(P) − 1 dividing L and each ladder is unbounded
(GROWTH.md#the-module-law); its maximum is W(L)
(GROWTH.md#the-three-fates over Z, GROWTH.md#the-wall-over-f₂x over
F₂[x]); a transparent run from s stays among the multiples of s dividing
W(λ(s)), and any smaller state admits a place of the quotient, so every
run ends at W. Reach, the places listed by norm and ties in a fixed order:
seat the least unseated support place each step at
its target exponent (1 where the target is ∞), bring one seated place
short of its finite target up to it (seed places included), raise every
seated place bound for ∞ by one, several places making one move, and
under dynamics add a pad when λ has not risen: an unseated support place
Q with λ_Q(1) not dividing λ, seated at its target exponent (1 where the
target is ∞), which exists when the support is infinite; or else the
least place bound for ∞, seated or not, pushed up its unbounded ladder
until λ rises, which exists since a target of finite support in the
image is not finite. The least
unseated place rises strictly, so every support place is seated at a
finite step, and from then rises at every step or reaches its finite
target within finitely many. At a squarefree seed the last four nest
strictly, witnessed by exponents 1, 2, 3 on an infinite support, one
infinite exponent on an infinite support whose other exponents are 1,
and s·P^∞, one infinite exponent on a finite support; the transparency
point lies in none.

The verifier runs the closure over Z and F₂[x] on a battery of 14
states and 12 states against every move to a cap, 8,634 state-move
pairs: the three blind demands' zeros there are their definitions read
back, and its content is that every battery state has a dynamics move.
It runs the transparent reach from four seeds per ring, 2, 6, 12, 30
and 1, x, x², x² + x + 1, exact at all eight; and the reach construction
from the void and a squarefree seed: 56 constructions clean for 12
steps, every step admissible (the construction builds each below its
target and rising), every place off the seed at ∞ and, from the
squarefree seed, its places raised to 3 among them, 3,124 dynamics
targets of finite support, each with an infinite exponent, run 12
steps, every place bound for ∞ rising at every step after its seating,
and each of eight out-of-image targets stalling, its step and reason
printed.

## The free image forgets the ring
Tier: theorem.
Verifier: proof; free_image.py::section_k4.

Every image but transparency's is described by conditions on the seed's
places and, off them, on the multiset of exponents alone, every place
taken as one colour. So each is a union of orbits of G_s, the
permutations of all places fixing the seed's exponents: the colour
count's symmetry with the coarsest colouring there is, every place
alike, whose supply is infinite, so the orbit is no number to count; and
each of these four holds a continuum orbit, but semisimplicity's at a
seed that is not squarefree, the point s. An image can have more
symmetry than its demand. Dynamics reads λ_P, so a permutation breaking
the ring's colouring changes which moves it admits, at 161 of the
(state, move) pairs tested over Z and 96 over F₂[x], and a
degree-preserving one over F₂[x] at none; yet every dynamics target with
such a pair exchanged is reached, dynamics' image being a union of
orbits of G_s, and the verifier runs the construction toward six such
targets from two seeds per ring, one exchanged pair each, three of the
six moved by the exchange, every run clean for 12 steps. The one image
that reads the ring is transparency's point, the wall, where the ring's
arithmetic sits: Adams' number over Z
(GROWTH.md#the-wall-is-adams-number), a product of whole degree classes
of irreducibles over F₂[x] (GROWTH.md#the-wall-over-f₂x). The ring
reaches the greedy image through its colours and the free image through
the wall, and nowhere else.

## The fates are the image's extremes
Tier: property.
Verifier: proof; free_image.py::section_k5.

A limit in a free image has two coordinates, the support and the
exponents. BREADTH is the support every place and DEPTH an exponent
infinite, each a face, extreme in one coordinate with the other free;
MORTALITY, a finite limit, is where both bottom out. Every move at least
doubles the size, so a run from a seed dies exactly when its limit is
finite. Breadth and depth hold together at 2^∞ times every odd prime; a
member missing infinitely many places with every exponent finite holds
no fate; and new idempotents and dynamics hold the same fates as
different images, so fates do not determine an image. A finite reachable
set puts a demand at MORTALITY, since no run can repeat a state; a ban
on depth does not: **fresh dynamics**, which admits only a new place
lifting λ, never deepens and never dies, such a place always existing.
The verifier runs it 20 steps from four seeds, every place it seats at
exponent 1, and over F₂[x] no two of them of one degree.

## Greed's point
Tier: rule (resting on GROWTH.md's lock rules, this page's curve rule and
the five forms; the places at ∞ read at the 27 principal seeds of norm
≤ 40 of Q(√−23)).
Verifier: free_image.py::section_c, free_image.py::section_k3,
image.py::section_c, image.py::section_q,
element_ring.py::section_walks.

Where a greedy walk locks, over Z and over an imaginary quadratic ring
on the seeds run (GROWTH.md#the-lock-prime-law,
GROWTH.md#the-lock-over-a-number-ring), its limit has a finite support
and its lock vehicle's places at infinity, one place over Z, and at
Q(√−23) in the element world both places over 2 at 24 of 27 seeds on
the single walk with one tie-break, an element-world run being an
ideal-world run whose moves are principal: a member of the dynamics
image, finite support with an infinite exponent,
that no smaller image holds. Over Z greedy dynamics runs from the void
to 3^∞, while a free policy reaches 2^∞ by refusing the least move, 4
lifting λ where 2 does not: that the walk never sends 2 to ∞ is greed's
choice, not the demand's. Where the walk sprawls, over a curve over F₂,
its limit keeps the infinite exponent and seats one place per opened
colour outside a finite rider reach (the curve section above), a support
infinite and missing infinitely many places, interior in its coordinate.
Both hold the depth fate alone; only the support separates them. Over Z
the walk is deterministic only because least moves at distinct primes
never tie; a tie-break is needed wherever moves share a cost, and the
greedy image prices it, nothing over Z, a factor of two per surviving
tie over the two quadratic rings walked, the continuum over F₂[x].

## Open fronts

Whether a Dedekind ring with an infinite class group, where the rider
reach need not be finite, can lose endlessly many choices and land
between the finite and the continuum, is open.

Two policy questions stay open. Whether a walk's fate is set by the
clock whatever the policy, or some policy between greed and freedom
changes it. And how the classes of policies between those two order by
the images they reach: this page computes the image only at the ends,
the greedy walk's and the free one's, and a class strictly between them
with its image computed would open that order.
