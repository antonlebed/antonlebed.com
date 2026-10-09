# ELEMENT — the walk that must stay principal

The object: a greedy growth walk under the dynamics demand in the
element world, where a move multiplies by an element and so seats the
place power it aims at together with the minimal divisor cancelling
its class, over the ring of a curve over F₂ and over an imaginary
quadratic ring. This page asks what the ring hands the walk, what the
element reading hides of a gcd and of the count of ideals by norm, which
colouring of its places is the coarsest that prices every move, what
that divisor costs and does, whether the chain of clock holders
survives it, what the walk converges to, and which of the limit's
coordinates are unbounded. Its verifiers are element.py,
element_ring.py, rider.py, sensor.py and module_law.py.

The curve rings are the functions on a curve over F₂ regular away from
one rational point at infinity, in the imaginary model y² + H(x)y = F(x)
with deg F = 2g + 1: F₂[x]; four elliptic curves h2 to h5, named by
their class numbers; and y² + y = x⁵ + x of genus 2, class number 15,
named g2. The class group is Pic⁰ of the curve and a place P of degree d
has class [P − d·∞]; a place's colour is its (degree, class), and
σ(d, c) counts the places of a colour, the table of these counts over
degree and class being the ring's **supply matrix**. λ(M) is the
exponent of the unit group of the ring mod M, and L its value at the
state. The door, the notch and the chain's words are LIMIT.md's,
degree 1 born covered: a move at an item of exponent a has door 1
when it opens a degree other than 1 that no seated degree is a
multiple of, and T + 1 − a otherwise,
T the least power of 2 at or above every exponent. A move is a
**core**, the place power at its door, plus a **rider**, the
least-degree effective divisor **MINREP**(c) of the class c that makes
the product principal; m(c) is that degree and R the largest m. A
state's **menu** is its least moves and their common price. The number
rings are the imaginary quadratic ones, Z[√−5] and the ring of integers
of Q(√−23) first, of class numbers 2 and 3, where a price is a norm and
m a least norm.

The answer, in one line: the ring hands the walk its class group, over a
curve a supply matrix whose colours no coarser colouring can replace,
over a number ring a ladder per place, and over each of these curves
every class summons exactly one minimal rider. Over a curve, past a
finite transient (the walk to its last opening that pays a rider,
ELEMENT.md#greed-pays-no-avoidable-rider) and a finite notch the riders
arrive too slowly to break the chain, so the walk keeps exactly one
runaway, with a few rider-fed coordinates beside it that a recursion on
(Z/n)², n the order of the runaway's class, sorts into unbounded and
stopped, the unbounded ones growing at most like the logarithm of the
runaway's exponent. Over a number ring the ideal walk's lid
(CLOCK.md#a-lidded-block-locks-the-walk-for-good) has a twin in the
element world, priced with riders, so a walk reaches a lidded block
exactly when its prices are bounded infinitely often
(ELEMENT.md#the-element-lid); a lock repeating one vehicle
(ELEMENT.md#the-bare-door) carries its rider at the core's own rate
(ELEMENT.md#the-lock-carries-its-rider, a rule at two rings, Z[√−5]'s
lock riderless), and over an imaginary quadratic ring that rider lies
over the core's own prime.

## The ring is a supply matrix
Tier: rule (verified at six rings: every colour to degree 9 against a
brute count of places, the counts to degree 400 by an exact
recursion); theorem for the finiteness of the principal-free degrees.
Verifier: element.py::cells, element.py::section_c,
element.py::section_g.

In the group ring Z[Pic⁰], Φ(z) = ∏_P (1 − [cls P] z^(deg P))⁻¹ over the
projective curve counts effective divisors by class, and Riemann–Roch
gives every class 2^(n + 1 − g) − 1 effective divisors of degree
n ≥ 2g − 1. So E = Φ·(1 − z)(1 − 2z) is a polynomial of degree 2g, read
off the places of degree ≤ 2g − 2 (none below genus 2), and the
logarithmic derivative gives Σ_(d | n) d·A_d^(n/d) = w_n + (1 + 2ⁿ)[0],
with A_d the sum of the classes of the degree-d places, A^(k) pushed
forward by multiplication by k, and w the coefficients of zE′/E.
Division by n comes out whole at every degree, and with ∞ dropped from
degree 1 the counts equal a count by root finding over
F₂[x]/(ϖ), ϖ running over the irreducibles of F₂[x], an inert place
counted at class 0. The class numbers are 1, 2, 3, 4, 5 and 15 by
Cantor's enumeration, each the zeta numerator at 1.

A supplied degree with no place of class 0 is **principal-free**. To
degree 400 they are none, {1, 4}, {1, 3}, {1, 2, 4}, {1, 5} and
{1, 2, 4, 5, 7}, and every supplied degree above them to 400 holds at
least two principal places (at least one at F₂[x], where every place is
principal). They are finitely many on every such curve: the places of
class 0 are those splitting completely in the Hilbert class field, a
curve over F₂ in which ∞ splits, and the Weil bound on that field counts
about 2^d/(d·h) of them at degree d, h the ring's class number, so every
large degree holds one. At the trivial
group the walker is LIMIT.md's: 608 menus and states equal to limit.py's
corner walk over F₂[x].

## The element reading sees only classes
Tier: criterion (proved in any Dedekind domain with finite class
group; brute force at three rings).
Verifier: proof; sensor.py::section_c; sensor.py::section_s.

Two nonzero non-units α and θ are **element-coprime** when no non-unit
element divides both, **ideal-coprime** when (α) + (θ) is the whole
ring. They are element-coprime iff the classes of the primes of
G = (α) + (θ), taken with multiplicity, form a zero-sum-free sequence in
the class group: no nonempty part of it sums to 0. So the two tests
agree on every pair iff h = 1, h the class number, and a
**hidden gcd**, one the element test cannot see, carries at most
D(Cl) − 1 primes, D the Davenport constant and Cl the class group.

Proof. A common non-unit divisor δ gives a principal ideal (δ) dividing
G, and a principal divisor (δ) of G gives δ dividing both; a divisor of
G is a part of its prime sequence, principal iff its classes sum to 0.
If h = 1 every nonempty sequence sums to 0. If h > 1, take a
nonprincipal prime P and integral I₁, I₂ in the class of P⁻¹ with I₁, I₂
and P pairwise coprime, which every class allows; then PI₁ = (α) and
PI₂ = (θ) meet in G = P, one nonzero class. A zero-sum-free sequence is
at most D(Cl) − 1 long by the definition of D, and for a cyclic class
group D(Z/h) = h.

So the element reading of a gcd is a reading of its class sequence and
nothing finer: it sees a common prime only through a part of the
sequence that closes up to a principal ideal. Over Z[√−5] (h = 2),
taking the non-unit elements of norm at most 120 up to units, 904 of
their 3240 unordered pairs are hidden, each gcd one nonprincipal
prime, the norm-least being 2 against 1 ± √−5. Over the ring of
Q(√−23) (h = 3), hidden gcds of one prime and of two occur and none
longer, so the bound D(Z/3) − 1 = 2 is attained; over Z[i] none is
hidden. The script checks a brute search for common divisors against
the criterion at every pair of non-unit elements of norm at most 120,
up to units, at each ring, after checking the class map against every
element of norm at most 3000.

## The class gap between principal and all ideals
Tier: theorem (the identity, by character orthogonality); rule (the
genus form at Z[√−5], verified n ≤ 10⁴).
Verifier: proof; sensor.py::section_g.

Counting elements up to units counts principal ideals, which is the
count of all ideals over h plus the class group's nontrivial
L-functions over h. A principal ideal's indicator is (1/h) Σ_χ
χ(I) over the characters of Cl, so

```
Σ_(I principal) N(I)^(−s)  =  (1/h) Σ_χ L(s, χ),
```

the trivial character giving the ring's Dedekind zeta function. At
Z[√−5] genus theory names the one
nontrivial L-function as L(s, χ₋₄)L(s, χ₅), with χ₋₄, χ₅ and χ₋₂₀ the
Kronecker symbols (−4/·), (5/·) and (−20/·): the principal ideals of
norm n number (φ_n + ψ_n)/2, with φ_n = Σ_(d | n) χ₋₂₀(d) and
ψ_n = Σ_(d | n) χ₋₄(d)χ₅(n/d), at every n ≤ 10⁴, and with ψ_n dropped
the count fails.

## The coarsest colouring
Tier: theorem (the witnesses built at six rings for every pair of
colours of degree ≤ 6).
Verifier: proof; element.py::section_k.

No coarser colouring than (degree, class) tells every state, an
assignment of exponents that is principal, from a non-principal one and
prices every menu. A coarsening merging colours (d₁, c₁) and (d₂, c₂)
identifies two assignments that exchange the exponents of an item X₁ of
the first and an item X₂ of the second. A witness is such an exchange
where one side is principal and the other is not, or where both are
principal and their least costs differ. Neither reads a colour, so a
witness stands against every coarsening that merges its pair, and every
proper coarsening merges one: pairs suffice. Every class holds an affine
effective divisor avoiding X₁ and X₂, a pad: of its 2^(n + 1 − g) − 1
effective divisors of a large degree n on the projective curve, at most
2^(n − d₁ + 1 − g) − 1 contain X₁ and 2^(n − d₂ + 1 − g) − 1 contain X₂,
and one containing neither is a pad once its multiple of ∞ is dropped.
If the classes differ, X₁ one above X₂ beside a pad making the
assignment principal gives an exchange moving the class sum by
c₂ − c₁ ≠ 0. If they agree, at c, with d₁ < d₂, fix a pad for every
class and let k be their largest exponent; take T a power of 2 above
d₂ + R + k + 1, seat the pad of class −Tc, X₁ alone or X₂ alone at T,
and principal places outside the pair and the pad, at exponent 1,
covering every supplied degree to d₂ + R (the context; a principal-free
degree is covered through a multiple holding a principal place, which
the finiteness of the principal-free degrees provides). The notch is T
on both sides and the core at T has door 1; every other seated item's
clock costs at least T + 1 − k, an unseated item of a covered degree
more, and an opening more than d₂ + R. So the least costs are d₁ + m(−c)
against d₂ + m(−c). The verifier builds the witnesses with MINREP(−Tc)
as the pad, doubling T until it avoids the pair: over the six rings 531
cross-class and 118 same-class pairs carry them, and without the context
28 of the 118 price alike. So a ring reaches the dynamics through two
numbers per place and a count.

## The minimal rider is unique
Tier: theorem.
Verifier: proof; element.py::section_m.

Every class of Pic⁰ of an imaginary hyperelliptic curve has exactly one
reduced representative (Mumford's representation; Cantor, Math. Comp.
48, 1987, for y² = F(x) in odd characteristic, and Koblitz, J.
Cryptology 1, 1989, for y² + H(x)y = F(x) in every characteristic): a
pair (u, v) with u of degree ≤ g dividing v² + Hv + F, standing for an
effective affine divisor of degree deg u. Let Δ attain m(c). Its degree
is at most g, the reduced representative's; it holds no inert place, no
place with its conjugate beside it and no ramified place twice, since
each is the divisor of a polynomial in x and removing it lowers the
degree. So Δ is reduced, and Δ is the reduced representative: every
class has one minimal rider, m(c) = deg u ≤ g. A place in MINREP(c) is
the only place of its colour, since a second would give a second minimal
rider; and m is a shortest path in the class group, m(c) = min over
colours (d, c′) of d + m(c − c′) at c ≠ 0, with m(0) = 0, read off σ
alone, with no further reference to the curve. At all six rings the
shortest path meets the reduced divisor in degree and in support at
every class, and R = g: 0, 1, 1, 1, 1, 2.

## The bare door
Tier: theorem.
Verifier: proof; element.py::menu.

A principal effective divisor V raising λ carries some place Q of colour
(d, c) at least to Q's door r, say to v ≥ r. V − vQ is effective of
class −vc, so deg V ≥ d·v + m(−vc), and MINREP(−vc) plus v − r copies of
Q is effective of class −rc, so that is at least d·r + m(−rc). At
equality V − vQ is MINREP(−vc) and (v − r)Q + MINREP(−vc) is
MINREP(−rc), the minimal rider being unique
(ELEMENT.md#the-minimal-rider-is-unique). So the least moves are exactly
r·Q + MINREP(−rc), costing d·r + m(−rc) at the door r, and a longer core
never wins: 13.7 million longer cores offered, up to g + 1 past the
door, none cheaper. The cost is a price of the core's colour and door;
the effect is not a price: the move raises places outside its core,
which no one-item move does. Two cores can summon one divisor, so the
menu is read by **vehicle**, the whole divisor a move multiplies in,
core plus rider.

## Greed pays no avoidable rider
Tier: theorem.
Verifier: proof; element.py::analyse.

An opening at an uncovered degree d costs d with a principal core and
d + m(−c) > d otherwise, and every item of an uncovered degree is
unseated. So an opening pays a rider only at a principal-free degree,
each opened at most once, and the **transient** — the walk up to the
last opening that pays a rider — is finite whenever the principal-free
degrees are. Past it, only clock moves summon riders, at most R units
each. Over every walk at the five curves h2 to h5 and g2 the transient
ends at step 4 to 9 of 300 (steps counted from 0), and
over the six rings, F₂[x] with them, none of 43,503 openings paid an
avoidable rider, an opening in the stretch counted once per branch.

## The margin step
Tier: theorem.
Verifier: proof; element.py::chain_step.

LIMIT.md's chain step fails twice here: a rider lifts a rival with no
door paid, and d·r + m(−rc) is not increasing in the door across
classes. What survives is a **margin**, R below the holder's notch: a
place standing that low, lifted as the move's core, takes over only by
falling in degree. Let the holder Z's last clock move meet notch t, so
Z stands at t + 1 or above, and let the next clock move
lift a place Y ≠ Z, standing at a_Y, past the notch T′ as the move's core,
at door T′ + 1 − a_Y. Z's door is at most T′ − t, so its cost is at most
d_Z(T′ − t) + R. If d_Y ≥ d_Z, Y's cost is at least

    d_Z(T′ + 1 − a_Y) = d_Z(T′ − t) + d_Z(t + 1 − a_Y),

which exceeds Z's once a_Y ≤ t − R, and greed would have moved Z. So a
change of holder to a place standing at most t − R, lifted as the move's
core, falls in degree. At the price d·r, LIMIT.md's chain is the case
R = 0, where every rival stands at most t and the premise always holds.

## The eventual chain
Tier: theorem (the principal-free degrees being finitely many, by the
Weil bound in the supply matrix's section above).
Verifier: proof; element.py::analyse.

Past the transient every clock move at least doubles the notch and
brings at most R rider units. Fix a notch t₀ past the transient. An item
no clock move has lifted past the notch since t₀ stands at its exponent
then plus R per clock move, O(log t), below t − R at a large notch t. A
strand made past that notch stands at most t + j, j = O(log t) its rider
units, so its door is at least T′ − t + 1 − j; it left the chain above
the later holders' degrees, so its cost is at least
(d_Z + 1)(T′ − t + 1 − j), above the holder Z's d_Z(T′ − t) + R
(ELEMENT.md#the-margin-step) once
T′ − t > R + (d_Z + 1)(j − 1), which T′ ≥ 2t and
t > R + (d_Z + 1)(j − 1) ensure. No
rider lifts an item past T′ ≥ 2t then either, every non-holder standing
below T′ + 1 − R. So past the transient and a finite notch every
crossing is made by a move's core and every change of holder falls: the
changes are finitely many. A walk clocks forever, an opening costing
at least its degree and each degree opening once while a clock move's
price stands still between clock moves, so it has exactly one runaway.
The rider-fed coordinates beside it can still grow; the orbit law below
sorts them.

## Where the chain changes hands
Tier: rule (verified over every branch of six rings, an 8-move stretch
continued to 300 moves: 2, 2, 2, 4, 20 and 120 branches).
Verifier: element.py::analyse, element.py::section_w, element.py::apply.

A branch is a distinct state, notch and seating, that the ties reach in
the 8-move stretch, walked on canonically to 300 moves; paths reaching
one state keep the first, so the changes of holder below are read on one
history per state. Eleven changes of holder stood under the margin
step's premise, one at h2 and ten at g2, and all fell; seventy-eight
more fell without it, all at g2. Fifty-two did not fall, all at g2 and
within the transient, and every one is a hand-off to the conjugate place
at the holder's own exponent: same degree, negated class. There, with P
the holder and ι(P) its conjugate, the image of P under the curve's
involution (x, y) ↦ (x, y + H(x)), the vehicle P^r·ι(P)^r is the r-th
power of a polynomial in x, which lifts both places alike, so which of
the two holds is a naming, and the step's premise fails by construction.
No change of holder comes after step 9 or notch 8 at any branch of any
ring, but 53 come after the transient (one at h2, 52 at g2, all
falling), so the **change range**, the steps up to the last change of
holder, is not the transient. No rider crosses the notch alone on any
branch's history, and in all 28 crossings a rider joins, counted once
per move applied (merged successors included, so not on one history per
state), the core crosses and every crossing place lands at the core's
exponent, and the core's place holds.

## The orbit law and the rider recursion
Tier: theorem (past the change range; verified over every branch of
six rings, an 8-move stretch continued to 300 moves).
Verifier: proof; element.py::analyse, element.py::verdict.

Past the transient and the last change of holder, the only rider source
is the runaway C's own move, and an **era** runs from one of C's clock
moves to the next. At notch T its door r = T + 1 − a_C summons
MINREP(−rγ), γ the runaway's class, of which ρ units land on C; C stands
at T + 1 + ρ ≤ 2T since ρ ≤ R < T, so

    T′ = 2T,   r′ = T − ρ,   ρ read off r mod n, n = ord γ.

The steady state is the self-map (T, r) ↦ (2T, T − ρ(r)) of (Z/n)²,
eventually periodic within n² steps. A colour some MINREP(−rγ) uses at
an r in the cycle gains units forever and is unbounded; one used only in
the pre-period stops at a finite exponent. The verdict reads the state
at the change range's end, which only a walk provides. Every door and
every rider of the 895 eras past the change range is the recursion's.

## The element limit
Tier: rule (verified over every branch of six rings, an 8-move stretch
continued to 300 moves).
Verifier: element.py::section_w.

The limit is ∞ at the runaway, the cycle's colours unbounded, the
pre-period's and the transient's leftovers at finite exponents, and one
place at exponent 1 at each opened degree. At F₂[x] and h3 it is the
ideal limit (LIMIT.md#the-ideal-limit): γ = 0, the runaway of degree 1
or 2 at F₂[x] and the principal degree-2 place at h3, nothing beside
it. At h2 and h4 γ has
order 2 and the cycle feeds nothing beside the runaway: at h2 the
cycle's doors are even and summon nothing, ρ = 0 absorbing, and at h4
they are odd and the one rider they summon is the runaway itself,
ρ = 1 every era. Either way the runaway alone is unbounded, beside at
most one other place above exponent 1. At h5 and g2 the runaway
is a rational place of a nonzero class, γ of order 5 and 15, and a
cycle of length 4 feeds two rational places forever: three unbounded
coordinates at every branch, the two beside the runaway gaining at
most R units an era against a notch that doubles. A pre-period of
length 1 leaves one more colour at a finite exponent at 23 of g2's 120
branches, and with the transient's leftovers g2 ends with two to five
places above exponent 1 beside the runaway.

## The number rings price in (min, ×)
Tier: rule (verified at Z[√−5] and Q(√−23): the classes against
principality over the places of norm ≤ 50, m against every ideal of
norm ≤ 200, the menu at 3,180 states over 53 seeds).
Verifier: element_ring.py::section_classes,
element_ring.py::section_rider, element_ring.py::section_walks.

A place's class is its reduced binary quadratic form. m(c), the least
norm of an ideal in class c, is a shortest path in the class group with
each class's edge weighted by the least norm of a place in it, taken in
(min, ×): a least ideal keeps its class when a place is swapped for a
least place of the same class, so the curve's (min, +) holds after
logarithms. The bare door's proof holds over any Dedekind ring with
finite class group, norms multiplying where degrees added: a principal V
raising λ carries some place J of class c to a depth v at least J's door
r; V·J^(−v) is integral of class −vc, so
N(V) ≥ N(J)^v·m(−vc) ≥ N(J)^r·m(−rc), since J^(v−r) times a least ideal
of class −vc lies in class −rc; and at equality V is J^r times a least
ideal of class −rc, so the least moves are the cores at their doors
times least ideals of class −rc, which need not be unique there.
What the matrix cannot carry is the door
itself, which reads each place's own ladder λ_P, λ_P(b) = λ(P^b),
against L: over F₂ every place shares the notch, and a number ring
hands the walker a ladder per place, not per norm
(CLOCK.md#a-norm-does-not-fix-a-column). At both rings each
class's minimum is attained once, m is (1, 2) and (1, 2, 2), and the
menu read from the matrix and the ladders equals the ring's least
raising elements at every state, where 1,528 of its 3,196 vehicles are
compound, their support more than one place.
None of 36,078 longer cores, up to 3 past the door, is cheaper.

## The lock carries its rider
Tier: rule (verified at the 53 seeds, the void and every principal
ideal of norm ≤ 40, the last 20 of 60 moves; each lock's permanence
proved).
Verifier: element_ring.py::section_walks, module_law.py::section_e.

Every seed ends on one vehicle repeated over its last 20 moves: (2), the
ramified place over 2 squared, at all 26 of Z[√−5]; (2) = P₂P₂′ at 24 of
Q(√−23)'s 27, and the inert (5) at 3. Each ride is permanent: at both
rings 4 is the least norm of a non-unit and 2 the only element of norm 4
up to sign, and (2) raises L at every move once the deeper place over 2
gives the whole 2-part of L and is past its head
(CLOCK.md#the-ladder-is-ψs-orbit-save-a-head-at-the-bend), where its
column count
(CLOCK.md#a-rings-door-is-one-valuation-and-its-clock-a-count) rises by
one every e units of depth, e its ramification index, deepening the one
place over 2 of Z[√−5] by its e = 2 and the deeper of Q(√−23)'s two by
its e = 1; the (5) lock
holds because every cheaper element misses the place it deepens
(GROWTH.md#the-lock-over-a-number-ring). A lock is V = P^r times a least
ideal of class −rc at a constant door r, so every place X of V gains
v_X(V) units a move and the rider grows at the core's rate: at Q(√−23)
both places over 2
gain one a move with a constant gap, the deeper set by the seed; at
Z[√−5] the door is 2 against a class of order 2, so −2c = 0 and the lock
has no rider. The margin step does not port: over a curve a clock move
brings at most R rider units while the door doubles, so the rider share
of the runaway's growth falls to zero; at a number ring's constant door
the share is fixed, and the limit's unbounded places are the lock
vehicle's support.

## The element lid
Tier: theorem (the lid and the four statements over any number ring;
the lock's one prime over an imaginary quadratic field).
Verifier: proof; rider.py::section_lid, rider.py::section_seeds,
rider.py::section_table, rider.py::section_bite.

A place Y's price at door k is π_Y(k) = N(Y)^k·m(−k·c_Y), nondecreasing
in k by the bare door, and its tail price is Λ_Y = π_Y(e_Y), e_Y
the ramification index of Y over the rational prime below it. The
bare door bound holds for every place of a vehicle, not only its core:
a principal ideal in which Y has valuation k has norm at least π_Y(k).
A **block holder** over p is a seated place at count exactly V = v_p(L)
(CLOCK.md#a-rings-door-is-one-valuation-and-its-clock-a-count), V being
in this section the block's count and no longer a move's divisor; past
its tail index its door is at most e_Y, so its next move costs at most
Λ_Y. A **creeper** over p is a place Y over p some least ideal holds at
least once and fewer than e_Y times, so that a rider can move it fewer
than e_Y depths, less than one tail gap (CLOCK.md#the-two-numbers). The block
is **lidded** when it has a block holder, V is past the tail index of
every place over p, and p^(V+1) ≥ B, the largest Λ over its block
holders and the creepers over p; its **lid** is the largest Λ over its
block holders. These
are the element world's own terms, priced with riders, not CLOCK.md's
lid for the ideal walk.

A lidded block stays lidded, and every later price is at most its lid,
which never exceeds B and, with no creeper over p, never rises. A jump
of the count (CLOCK.md#a-rings-block-keeps-one-runaway-in-counts)
needs a newly seated place of norm ≡ 1 mod p^(V+1), and any vehicle
holding it costs more than B. A place a move leaves at the top count
after k depths has Λ at most the price paid when k ≥ e_Y, by the bound
read at it; with k < e_Y it is either the place of the move's core, a
block holder already, having crossed from count V at its door, or a
creeper riding. So the four statements of
CLOCK.md#a-lidded-block-locks-the-walk-for-good stay one when moves must
be principal: a walk reaches a lidded block, clocks some block
infinitely often, makes finitely many openings, and has its prices
bounded infinitely often, together or not at all. Past a lidded block
every price is at most B and an opening costs at least its core's norm,
the riders being finitely many places, so finitely many openings follow.
Finitely many openings leave finitely many seated places, one of them a
core's place infinitely often; prices bounded infinitely often bring cores of
bounded norm, each opened once. Either way some block's count rises by
a core's crossing infinitely often, so V passes every tail index over p
and p^(V+1) every Λ over p, and after such a rise the crossing core's place
is a block holder: the block is lidded. What does not carry is one vehicle
forever, whose ideal proof reads single
places.

Over an imaginary quadratic field the places over one prime share Λ, a
split pair being conjugate with inverse classes and m(−c) = m(c):
p·m(c) at a split place of class c, p² at a ramified or inert one. So
a block's lid is constant once lidded, and it exceeds the ideal lid
N(Y)^(e_Y) only at a split non-principal place, by a factor, the leading
coefficient of its class's reduced form: at Z[√−5] the pair over 3
lids at 6. And a lock's rider lies over its core's prime. Let
W = S^r·U repeat forever, S over p and U its rider. S's conjugate, or
S itself when ramified, gives an ideal of class −r·c_S at norm p^r, and
an inert S is principal, so N(U) ≤ p^r. If U held a place over q ≠ p,
W's places over q would grow
without bound, and at each rise of the q-count one of them, Y, is a
block holder, past the tails once the count is, pending at most
Λ_Y ≤ q²; but N(W) ≥ p^r·N(Y) > q², since q ≤ N(U) ≤ p^r and p^r ≠ q.
Then W is not a least move. The quadratic field enters twice: in the
bound N(U) ≤ p^r, and in Λ_Y ≤ q², which in a field of degree n reads
only q^n.

Over the 122 fields Q(√−f), f squarefree and at most 200, of class
numbers 1 to 20, the void walked 40 moves with every tie
branched gives 207 ends and 7762 prices after a block is lidded: no
lid lost or risen, no price over it, no jump on a lidded block, every
end with a lidded block by move 4, and 3567 prices over the ideal lid at
13 fields. The 1206 principal seeds of norm ≤ 40, walked one path each,
keep the lid: no lid lost or risen, no price over it, no jump on a
lidded block. Of 4062 seeds built on a split non-principal place of norm
≤ 60 whose least rider lies over another prime, 100 take that two-prime
vehicle and every one leaves it; no lock read lies over two primes. At
Q(√−15) the class of the places over 2 has order 2 and holds both, so it
has two least ideals, and P₂² and P₂P₂′ tie at 4 at every move: a number
ring's minimal rider need not be unique, and the walk repeats a price
rather than a vehicle.

## Open fronts

Whether a lock's rider can sit over another prime than its core in a
field of higher degree; whether a walk with finitely many openings
always settles on one vehicle up to ties; and an explicit notch bound
for the curve's eventual chain.
