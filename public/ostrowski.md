# OSTROWSKI — the circle a trailing numeration reads

The object: the trailing Ostrowski numeration at an irrational α in
(0, 1), α = [0; a₁, a₂, …], with denominators q₀ = 1, q_(k+1) = a_(k+1)
q_k + q_(k−1) (q₋₁ = 0), numerators p_k, and remainders θ_k = q_k
α − p_k (θ₋₁ = −1), which alternate in sign and shrink. Every n ≥ 0 has
one greedy string n = Σ d_k q_k with d₀ ≤ a₁ − 1, d_k ≤ a_(k+1), and
d_(k−1) = 0 wherever d_k = a_(k+1). Its depth-t tile is the integers
sharing d₀ … d_(t−1), and a reader at lookahead c sees the input's
depth-(t + c) tile and commits the output's depth-t tile, as in
READING.md. Zeckendorf is α = 1/φ, φ the golden ratio; there q₀ = q₁ = 1
and d₀ is always 0, so digit k here is digit k − 1 of READING.md's
Zeckendorf, and depth t here is depth t − 1 there. This page shows
that the numeration is the circle R/Z tiled by arcs, the integers
sitting at nα mod 1, and decides every affine map n ↦ mn + ω (m ≥ 1)
and every floor division at every α. An affine map the circle carries
reads exactly where READING.md's wall criterion says, with the cut
points −jα as its tile endpoints B. READING.md sorts maps into three
classes: LIPSCHITZ (bounded lookahead), MIDDLE (finite lookahead at
every depth, unbounded) and DISCONTINUOUS (no lookahead at some
depth). Of the affine maps only n + ω (ω ≥ 0), the successor's powers,
is LIPSCHITZ, and the successor
reads at lookahead 1 at every depth with two tiles or more. Floor
division ⌊n/m⌋, m ≥ 2, is carried by no continuous map of the circle: a
tile confines nα mod 1 to an arc and fixes nothing of n mod m, and
from that the proof below finds integers of two output arcs in every
tile about some point. So it reads at no lookahead from the first depth
with two tiles or more, at every α, and no α puts it in MIDDLE.

Which place pays for the walls. The **odometer**, this numeration's
completion, is totally disconnected, and its tiles are the balls of the
agreement ultrametric, under which two strings are close when they share
a long prefix. On such tiles, by READING.md#the-reading-lemma, a map
Lipschitz for that metric reads at bounded lookahead and has no wall.
The affine maps that fail here fail because their arithmetic lives on
the circle, not on the odometer. The map n ↦ nα mod 1, extended to the
odometer, folds it onto R/Z, two to one over the cuts. An affine circle
map with a cut preimage that is not a cut has a wall there, since every
input arc about that point maps across a cut (the containment criterion
below), and it is DISCONTINUOUS
on the odometer, READING.md's three classes carrying over to a compact
completion with finitely many tiles per depth. ×m is such a map. Floor
division is not: it is no continuous circle map at all, so its walls
come from the map, not from the folding, and like those of ×m they
stand at every α. Reading from the least significant digit, whose
completion is ultrametric, does not make the arithmetic it reads
non-archimedean: it reads n through nα mod 1, a point of the connected
circle R/Z.

```
MAP             ON THE CIRCLE      PREIMAGE OF A CUT       CLASS
n + ω, ω ≥ 0    x ↦ x + ωα         a cut                   LIPSCHITZ,
                                                             c ≤ 1 eventually
n + ω, ω ≤ −1   x ↦ x + ωα         of −α: −(ω + 1)α,       DISCONTINUOUS
                                     never a cut
mn + ω, m ≥ 2   x ↦ mx + ωα        (h − (j + ω)α)/m,       DISCONTINUOUS
                                     never a cut at h ≠ 0
⌊n/m⌋, m ≥ 2    none               —                       DISCONTINUOUS
```

In the table h = 0, …, m − 1 indexes the m preimages of the cut −jα.
The three DISCONTINUOUS rows read at no lookahead from t₀, the first
depth with q_t ≥ 2 (t₀ = 1 when a₁ ≥ 2, t₀ = 2 when a₁ = 1), and
every map reads at 0 at the depths before it.

## The circle numeration
Tier: theorem.
Verifier: proof; ostrowski.py::section_cuts.

The depth-t tiles match the q_t arcs into which the cuts −α, −2α, …,
−q_t α divide the circle R/Z: n lies in a tile iff nα mod 1 lies in
its arc. The prefix of value r (0 ≤ r < q_t) has the arc r α + J,
with J the open interval between −θ_t and −θ_(t−1) when r < q_(t−1)
(so d_(t−1) = 0) and between −θ_t and −θ_(t−1) − θ_t otherwise.
The arcs have at most two lengths, |θ_(t−1)| + |θ_t| and |θ_(t−1)|. The
open arcs of a depth are disjoint and nest in their parents', so a
point off the cuts has one infinite coding, and the cut −jα has
exactly two. They part at digit t − 1 for the least t with q_t ≥
max(j, 2).

Proof. The **star** of a digit string is Σ d_k θ_k, and the **cap** at position
k is the largest digit allowed there, a_(k+1), or a₁ − 1 at position 0. Write
S = Σ_(k≥t) d_k θ_k for the star of a legal tail. Because
a_(k+1) θ_k = θ_(k+1) − θ_(k−1), the cap-filling on one parity, every position
of that parity at its cap and the rest 0, telescopes:
(a_(t+1), 0, a_(t+3), 0, …) has star −θ_(t−1) and
(0, a_(t+2), 0, a_(t+4), …) has star −θ_t. The θ_k alternate in sign, so
S is largest when every position of positive θ sits at its cap and every
other position is 0. That string is legal, and one of the two
cap-fillings is exactly it, so every finite tail lies strictly inside
the interval between −θ_t and −θ_(t−1). When d_(t−1) ≠ 0 the cap at
position t is barred, and the cap-filling that uses it becomes
(a_(t+1) − 1, 0, a_(t+3), …), with star −θ_(t−1) − θ_t. Position 0
always has this second form, its cap being a₁ − 1. Now n = r + (tail)
gives nα ≡ Σ d_k θ_k, and so the arc.

Its endpoints are r α − θ_t ≡ −(q_t − r)α and r α − θ_(t−1) ≡
−(q_(t−1) − r)α, or −(q_(t−1) + q_t − r)α in the second form. Each is
−jα with 1 ≤ j ≤ q_t. The q_(t−1) prefixes below q_(t−1) take the
longer arc, and the lengths sum to q_t |θ_(t−1)| + q_(t−1) |θ_t| =
|q_t p_(t−1) − q_(t−1) p_t| = 1. The union of the closed arcs holds
the dense set of nα, so it is the circle, and total length 1 makes the
interiors disjoint. A child's tail stars are a subset of its parent's,
so the arcs nest. q_t arcs tiling a circle have q_t endpoints, all
among the q_t points −jα, so they are those points. A point interior
to an arc at every depth has one nested chain of tiles. A cut −jα,
from the first depth where it is an endpoint of two different arcs,
has two chains, left and right.

Over seven α — golden, silver and bronze (every quotient 1, 2 and 3
respectively), √3 − 1, then e − 2 from its quotient pattern, ∛2 − 1 from
certified quotients, and a seeded random α with quotients in 1..4 — the
script (ostrowski.py --full) checks 185,523 tiles at every depth with
q_t ≤ 20000. It finds every endpoint a −jα, each j twice, the arcs
abutting in circular order, the lengths summing to 1 exactly, and every
n < 20000 strictly inside its own prefix's arc. The arithmetic is exact,
with α replaced by a convergent of denominator past 10⁶⁰, and the least
arc clears the approximation error by a factor of 10²⁰ (asserted; the
margins of the comparisons that place each n are not).

## The two codings of −α
Tier: theorem.
Verifier: proof; ostrowski.py::section_codings.

q_K − 1 is the cap-filling on one parity: (0, a₂, 0, a₄, …, a_K) at even
K and (a₁ − 1, 0, a₃, 0, …, a_K) at odd K. The first has star −α + θ_K
and the second 1 − α + θ_K, so as K grows the two converge to the two
codings of −α. They part at position t₀ − 1, the lowest position a
nonzero digit can take. So n ↦ n − 1 carries the inputs q_K, which
converge to 0 in the odometer, to images that converge, alternately, to
two distinct points of the completion. At golden the two strings and the
two points of the odometer that the successor sends to 0 are Barat,
Berthé, Liardet and Thuswaldner's (Ann. Inst. Fourier 56, 2006, Example
5.5), who say every Ostrowski numeration behaves alike; the closed form
at every α is not stated there.

Proof. At K = 1 the string is q₁ − 1 = a₁ − 1 itself. At K ≥ 2,
q_K − 1 = a_K q_(K−1) + (q_(K−2) − 1), with 0 ≤ q_(K−2) − 1 <
q_(K−1), so the greedy digit at position K − 1 is the cap a_K. Then
position K − 2 is 0, and the recursion goes down in steps of two to
q₀ − 1 = 0 or q₁ − 1 = a₁ − 1. The stars are the telescoped sums of
the previous proof, cut at K. At position 0 the two strings read 0 and
a₁ − 1, and at position 1 they read a₂ and 0, so they part at 0 when
a₁ ≥ 2 and at 1 when a₁ = 1.

The script finds the closed form at every K = 1..60 at all seven α,
and the star exactly −α + θ_K or 1 − α + θ_K at every one. The
parities part at position 1 at golden, √3 − 1 and e − 2 and at
position 0 at the others.

## The containment criterion
Tier: criterion.
Verifier: proof; ostrowski.py::section_successors;
ostrowski.py::section_tears.

Let f(n) = mn + ω with m ≥ 1, on the n where it is ≥ 0, so that
f(n)α ≡ g(nα) with g(x) = mx + ωα. At a depth t with q_t ≥ 2, f reads
at lookahead c iff every g-preimage of every cut −jα, j ≤ q_t, is a cut
−iα with i ≤ q_(t+c). At q_t = 1 every map reads at 0. So the points
where f's emission freezes at a finite depth, its walls on the circle,
are g⁻¹(B) \ B with B the cuts: READING.md#the-wall-criterion's set,
on a connected space.

Proof. Take an input arc I at depth t + c. If no preimage lies in
its interior, g(interior I) is connected and misses every depth-t
cut. (Were it to wrap past the whole circle, it would meet one.) So it
lies in one output arc, and the integers of I are never at its
endpoints. If a preimage y lies inside I, the integers of I sit dense
on both sides of y, and g, a local homeomorphism, puts their images
on both sides of the cut g(y). Those are two different arcs once
q_t ≥ 2.

## The affine maps
Tier: theorem.
Verifier: proof; ostrowski.py::section_successors;
ostrowski.py::section_tears.

n + ω with ω ≥ 0 reads at c_min(t) = min{c : q_(t+c) ≥ q_t + ω}
wherever q_t ≥ 2. At ω ≥ 1 that is 1 at every depth where q_t ≥ 2
and q_(t−1) ≥ ω, so the map is LIPSCHITZ, and the successor reads at
lookahead 1 from t₀ on. n + ω (ω ≤ −1) and mn + ω (m ≥ 2, any ω) read
at no lookahead at any depth t ≥ t₀: DISCONTINUOUS, at every
irrational α.

Proof. The preimages of −jα under x ↦ mx + ωα are (h − (j + ω)α)/m,
h = 0..m − 1. Such a point is −iα mod 1 only if (mi − j − ω)α is an
integer ≡ −h mod m, which for irrational α forces mi = j + ω and h = 0.
At m = 1, ω ≥ 0 every preimage −(j + ω)α is a cut, at depth t + c iff
q_t + ω ≤ q_(t+c), and q_(t+1) ≥ q_t + q_(t−1) gives the 1. At
m = 1, ω ≤ −1 the preimage of −α under x ↦ x + ωα is −(ω + 1)α, which is
−iα for no i ≥ 1. At m ≥ 2 the preimages with h ≠ 0 are never cuts.
Take −α, a cut at every depth, and apply the containment criterion.
So 2n has walls at (1 − α)/2 and at −α/2 (the preimage at h = 0,
where 2i = 1 has no solution), among others.

The successor's finite-state side is C. Frougny's (On the
sequentiality of the successor function, Inform. Comput. 139 (1997)
17–38). Her right-to-left reading, least significant digit first, is
the one here. A function is right subsequential when a deterministic
finite transducer reading right to left computes it, and her Theorem 3
takes a scale that is a linear recurrence with a dominant root β: the
successor is right subsequential iff the greedy expansion of 1 in base
β is finite and the recurrence is the one its digits write.
Among Ostrowski scales it reaches those whose partial quotients are
eventually a constant a, where q_(k+1) = a·q_k + q_(k−1) from some k
on (the theorem lets the first terms be any), that expansion is
the two digits a, 1, and the successor is right subsequential, in
agreement with its lookahead 1 above. Otherwise q_(k+1)/q_k = [a_(k+1); a_k, …,
a₁] has no finite limit, so the scale is no recurrence with a dominant
root and the theorem does not apply; at partial quotients of period 2
the ratio alternates between two limits.

The script's exhaustive check over n < 20000 agrees with the formula for
n + ω, ω = 0..5, at every depth it can decide at all seven α. n + 5
reads 0, 0, 3, 2, 2 and then 1 at golden, the bumps where
q_(t+1) − q_t < 5. For n − 1, n − 2, 2n, 2n + 1, 3n, 3n + 1, 4n and
4n + 1 at N = 10⁴ and 10⁵, the least lookahead the check finds at t₀
over n < N is c_N − 1, c_N or c_N + 1, where c_N is the largest c with
q_(t₀+c) ≤ N (one depth deeper, a tile holds at most one integer below
N). So the check succeeds only where the input tiles hold a few integers
below N, an artifact of the finite N: at golden, lookahead 17 or 18 at
N = 10⁴ (c_N = 17) and 22 or 23 at N = 10⁵ (c_N = 22).

## Floor division is never MIDDLE here
Tier: theorem.
Verifier: proof; ostrowski.py::section_residues;
ostrowski.py::section_tears.

Every tile, at every depth and every α, holds integers of every pair
(n mod m, ⌊nα⌋ mod m), and ⌊n/m⌋ (m ≥ 2) reads at no lookahead at any
depth t ≥ t₀, at every irrational α: DISCONTINUOUS, never MIDDLE.
READING.md#the-division-trichotomy puts floor division in MIDDLE on
a sparse divisor chain. That works because a chain's tiles are residue
classes, which fix n mod m once m divides the modulus. An Ostrowski
tile is the integers of an arc and fixes n mod m at no depth. Nothing
about α, not a growing, bounded or periodic continued fraction, changes
that.

Proof. The rotation by (1, α) on Z/m × R/mZ is minimal. Its forward
orbit's closure is a closed subgroup, since in a compact group the
closure of a semigroup is a group. It holds m(1, α) = (0, mα), whose
multiples are dense in R/mZ because α is irrational, and adding (1, α)
gives the rest. So the integers whose nα mod 1 lies in an arc realize
every pair. Write n = mu + s with u = ⌊n/m⌋ and s = n mod m,
0 ≤ s < m. Then uα = (nα − sα)/m, so fix s. The images of an input
tile about a non-cut x then come arbitrarily close to all m points
(x − sα + P)/m, P = 0..m − 1, which are 1/m apart. As x moves, these
points rotate. At the moment one of them crosses a cut, no other sits on
a cut, since cut differences are irrational. So the crossing point and
some other point lie in different depth-t arcs just before or just after
the crossing. At a non-cut x there, every input tile about x holds
integers of both.

The script's --full run finds all m² pairs in each of 11,169 (tile, m)
tests, a tile holding at least 40m² integers below 10⁵, for m = 2..5
over the seven α. The exhaustive check reads ⌊n/2⌋, ⌊n/3⌋ and ⌊n/4⌋ at
t₀ only at c_N + 1, at both N and all seven α.
