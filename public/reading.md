# READING — what a digit-by-digit reader computes

The object: a **numeration**, a digit system that writes the points of a
complete metric space, the numeration's completion, as digit streams.
Its depth-t **tiles** are the sets of points sharing a t-digit prefix.
They nest, their mesh δ_t tends to 0, and their Lebesgue number ℓ_t is
the largest ℓ such that every set of diameter below ℓ lies in one tile.
A reader of a map f at lookahead c sees the input's tile at depth
t + c and commits the output's tile at depth t, and its commitments nest
into one output stream. c_min(f, t) is the least lookahead that works at
depth t. This page prices readability by the tiles' shape, sorts maps
into three classes by the Lipschitz criterion, decides the two integer
maps n ↦ mn and n ↦ ⌊n/m⌋ on every divisor chain, and shows which place
pays for a wall. The answer to the last is the archimedean place: the
absolute digit tiles of every other completion of Q or F_q(x) are balls,
on which no Lipschitz self-map of the unit ball walls, and on R's
non-redundant interval tiles some map walls until redundancy is paid
for. Below, rad(m) is the product of the primes dividing m.

```
NUMERATION            COMPLETES TO         TILES        WHAT READS
base b, trailing      the b-adic ring      balls        ⌊n/m⌋ iff
                                                         rad(m) ∣ rad(b)
divisor chain M_t     its profinite ring   balls        m M_t ∣ M_(t+c),
                                                         depth by depth
primorial chain       ∏ F_p                balls        never, from m's
                                                         least prime on
base x over F_q[x]    F_q[[x]]             balls        ⌊n/m⌋ iff m = a x^j,
                                                         a constant
base b, leading       R                    a partition  y ↦ uy (u > 0) iff
                                                         1/u ∈ Z[1/b]
1/x-adic, F_q[x]      F_q((1/x))           balls        y ↦ uy, every u ≠ 0
d-bonacci, trailing   an odometer (d = 2)  balls        ×2 and ⌊n/m⌋
                       or over a torus                    torn (no
                                                          continuous
                                                          extension) at
                                                          every
                                                          d; ×m where
                                                          1/m's word
                                                          decides
```

## The reading lemma
Tier: theorem.
Verifier: proof; reading.py::section_l.

If f is L-Lipschitz, it is read at lookahead c at depth t once
L δ_(t+c) < ℓ_t, provided the tiles chosen at successive depths nest, as
ball tiles always do, and at tiles that are the closed balls of radius
δ_t of an ultrametric once L δ_(t+c) ≤ δ_t, so where δ_(t+1) = δ_t/b the
fit costs at most max(0, ⌈log_b L⌉) digits. A partition of a connected space
into two tiles or more has ℓ_t = 0, the lemma says nothing, and
readability is a question of alignment asked map by map. A cover by
overlapping tiles, such as the closed tiles of the signed-digit cover,
can have ℓ_t > 0 from the overlap, but a Lebesgue
number alone does not make the next commitment a child of the last;
that cover's own reader is proved in the next claim.

Proof. A depth-(t + c) tile has diameter at most δ_(t+c), so its image
has diameter at most L δ_(t+c). Below ℓ_t it lies in one depth-t
tile. In an ultrametric a set of diameter at most r lies in the closed
ball of radius r about any of its points, so at ball tiles diameter
δ_t is enough. Where the tiles nest, choosing that tile at each depth
gives nested commitments, which is a reader.

At trailing base 10 the script prints c_min = 0 for 7n, 1 for ⌊n/2⌋
and 2 for ⌊n/4⌋ at depths 1 to 3, and no c ≤ 3 for ⌊n/3⌋.

## Non-redundant absolute tiles wall only at the archimedean place
Tier: theorem.
Verifier: proof; reading.py::section_b.

A numeration is **non-redundant** when its tiles at each depth partition
the space. Call a point y a **wall** of a map f when the reader that
commits at each step only what the input's tile forces commits at y a
depth that stays bounded as the input depth grows. On the unit ball of
any non-archimedean completion of Q or F_q(x) (Z_p, F_q[[x]], the ball
of F_q((1/x))), with absolute tiles, fixed in position rather than moved
with the point's valuation, the digit tiles are the closed balls of
radius δ_t, so every L-Lipschitz self-map of the ball is read at
lookahead max(0, ⌈log_g L⌉) at every depth, g the size of the residue
field, and there are no walls. On a real interval every non-redundant
numeration by interval tiles, finitely or countably many per depth, has
walls. Redundancy cures them: the signed-digit cover reads every
L-Lipschitz self-map of [−1, 1] at lookahead max(0, ⌈log₂ L⌉ + 1). So
the archimedean place charges nothing but the redundancy a wall-free
numeration of R by interval tiles must carry, which every other place
gets free, and the cover's max(0, ⌈log₂ L⌉ + 1) is at most one digit
past Z₂'s max(0, ⌈log₂ L⌉). Q_p, which carries like R, pays nothing.

Proof. The first half is the reading lemma at ball tiles. For walls on
R, take a tile endpoint v inside the interval at the first depth that
splits it, a point y₀ that is no endpoint at any depth (the endpoints
are countable), and f(y) = v + λ(y − y₀) with λ > 0 small enough to map
the interval into itself. Every input tile holding y₀ holds it in its
interior, so its image holds v in its interior and lies in no tile of
v's depth: y₀ is a wall. Connectedness is why ℓ_t = 0: a positive
Lebesgue number would make every tile open, and a connected space has no
partition into two or more open sets, while the non-archimedean
completions are totally disconnected. For the cure, give [−1, 1] signed
binary digits, so a depth-t tile is [a − r, a + r] with r = 2^(−t) and
its children are [a − r, a], [a − r/2, a + r/2] and [a, a + r]. An
interval of length at most r/2 inside the tile lies in one child: in an
end child if it misses a, in the middle one if it holds a. At lookahead
c with 2^c ≥ 2L, suppose the tile committed at depth t holds the image
of the input's depth-(t + c) tile, as [−1, 1] does at t = 0 for a
self-map. The image of the input's depth-(t + 1 + c) tile lies inside
that image, so inside the committed tile, and has length at most r/2, so
it fits a child; committing that child keeps the hypothesis and the
commitments nest.

The theorem is about absolute tiles. Read with the leading degree or
exponent first, as a floating-point reader does, tiles scale with the
point, and a map cancelling leading digits reads at no bounded lookahead
at any place: y ↦ y − 1 at the input 1 + x^(−N), or 1 + 10^(−N) in R,
commits no output digit before the input's digit N places below its
lead is read. Scaling escapes this off R. At Q_p read from the valuation
up, the first j digits of uy, u a unit, are fixed by the first j of y,
multiplication by u being well defined mod p^j; at the 1/x-adic place
the leading j digits of uy are fixed by the leading j digits of y for
every u ≠ 0, since with no carries a lower term of y reaches only lower
terms of uy. Over R the leading base-b reader of y ↦ uy walls unless
1/u ∈ Z[1/b] (the wall criterion).

At the 1/x-adic numeration of F_2((1/x)) (characteristic 2, no carries)
the script finds multiplication and division by x + 1 and by x² + x + 1
fixing the leading j output digits from the leading j input digits at
every j to 12, over every input of that length. At leading base 10,
3 × 0.3…3 (k threes) is 1 − 10^(−k), so y ↦ 3y maps that tile onto
[1 − 10^(−k), 1 + 2·10^(−k)), which holds 1 in its interior at every k,
while y ↦ 2y maps the input tile [n, n + 1)·10^(−t−1) into one output
tile of depth t, since 2n + 2 ≤ 10(⌊2n/10⌋ + 1) for every integer n: it
reads at c = 1.

Two other prices of Z belong to the characteristic rather than the
place: the carries (SIZE.md#the-f₂x-control) and a bundle's capacity
(BINDING.md#the-characteristic-cap). This one belongs to the place, as
the connectedness that makes a partition's Lebesgue number 0.

## The wall criterion
Tier: criterion.
Verifier: proof; reading.py::section_w.

Take a partition cover of a real interval whose tile endpoints B stay
endpoints at every deeper depth, tiles half-open on the right, f
continuous and strictly increasing, and y ∉ B. If f(y) ∉ B, the reader
at y emits without bound. If f(y) ∈ B, emission freezes at a constant.
So the walls of f are exactly f⁻¹(B) \ B. A decreasing f turns each
half-open tile around, so an endpoint can wall too: when B = −B,
negation maps a tile [v, v + h) of width h onto (−v − h, −v], meeting
the tiles on both sides of the endpoint −v at every depth past −v's own,
so it walls at every endpoint v.

Proof. y lies inside its tile at every depth. If f(y) ∉ B, then f(y)
lies inside its output tile at every depth, and by continuity a fine
enough input tile maps into it. If f(y) ∈ B, every input tile about y
maps onto an interval with f(y) in its interior, and a tile of depth
past the endpoint's own never holds both sides of it. At y ∈ B an
increasing f maps [y, y + h) onto [f(y), f(y + h)), which fits one
half-open tile, so the endpoints themselves never wall.

At leading base 10, B = Z[1/10] and y ↦ uy (u > 0) has walls B/u \ B, empty
iff 1/u ∈ Z[1/10]. Conversely, if 1/u = k/10^c, the preimage of a
depth-t tile endpoint is an endpoint at depth t + c, so no input tile
of that depth maps across one, and lookahead c reads everywhere. So
×2 reads and ×3 walls at 1/3. For y ↦ y² the script prints emission
frozen at 0 at √0.2 and √0.5, at −1 (not even the units digit) at
√2 and √3, and growing as 19, 59, 119, 199 at input depths 20, 60,
120, 200 at √(1/3), and as 19, 59, 119, 200 at √(1/7).

## The Lipschitz criterion
Tier: criterion.
Verifier: proof; reading.py::section_m.

On a trailing numeration at base b, f is read at lookahead c iff it is
b^c-Lipschitz in the agreement ultrametric
dist(y, z) = b^−(agreement depth). It is read at bounded lookahead iff
it extends to a Lipschitz self-map of the completion. Continuity is
weaker, and it splits the maps into three classes: **LIPSCHITZ**
(bounded lookahead), **MIDDLE** (a continuous extension to the
completion, with a lookahead finite at every depth and unbounded) and
**DISCONTINUOUS** (no continuous extension: no lookahead at some depth).
Continuity on the integers alone decides nothing, since they are
discrete in the value metric and dense only in the agreement one. MIDDLE
is inhabited: the decimation D(n) = Σ_(j≥0) n_(2j) 2^j at base 2, n_j
the digit of n at position j, has c_min(D, t) = t − 1 exactly.

Proof. "Agreement to depth t + c forces image agreement to depth t" is
dist(fy, fz) ≤ b^c dist(y, z), and a Lipschitz map on a dense subset of a
complete space extends to it with the same constant. On a completion
with finitely many tiles per depth, which is compact, continuity gives
a modulus: image agreement to t from input agreement to s(t).
Conversely a lookahead finite at every depth is such a modulus on the
dense subset, so f is uniformly continuous there and extends
continuously to the completion. Nothing forces s(t) ≤ t + c. D's output
digits 0..t − 1 are input digits
0, 2, …, 2t − 2, so depth 2t − 1 suffices and depth 2t − 2 does not.

Metric, not topological: a map can be readable at every depth and still
not at any bounded lookahead. Related: for rational word functions
Choffrut's theorem (1977) makes co-sequential the same as Lipschitz for
the suffix distance (Frougny–Sakarovitch, Combinatorics, Automata and
Number Theory, 2010, Thm 2.6.13); that distance counts unmatched
letters, not agreement depth. The script prints c_min(D, t) = 0, 1, …, 9
at t = 1..10.

## The division criterion
Tier: criterion.
Verifier: proof; reading.py::section_r.

Let a trailing numeration's depth-t tiles be the classes n mod M_t of
a divisor chain M_1 ∣ M_2 ∣ ⋯. Multiplication by m is 1-Lipschitz in
the chain's agreement metric, since it keeps every agreement mod M_t.
At a depth t with M_t ≥ 2, ⌊n/m⌋ is read at lookahead c iff
m M_t ∣ M_(t+c).

Proof. If m M_t ∣ M_(t+c), n mod m is fixed by n mod M_(t+c), so
inputs agreeing there have quotients differing by a multiple of
M_(t+c)/m, which M_t divides. Conversely, inputs agreeing at depth
t + c differ by a multiple of M = M_(t+c), so the one-step pairs
(r, r + M) decide. As r runs over 0..m − 1 the difference
⌊(r + M)/m⌋ − ⌊r/m⌋ takes the value ⌊M/m⌋ and, when m ∤ M, also
⌊M/m⌋ + 1. Two consecutive integers are not both divisible by
M_t ≥ 2, so m ∣ M is forced, and then the difference is M/m.

Three chains. At base b the condition is m ∣ b^c, and it holds at a
bounded c at every depth iff rad(m) ∣ rad(b). At the factorial chain
M_t = (t + 1)! it holds at every depth, at the least c with
m ∣ (t + 2)⋯(t + c + 1), a lookahead that moves with the depth but
never passes m, since m consecutive integers have a product divisible
by m!: every floor division is LIPSCHITZ there (proved; the script does
not scan this chain). At the primorial
chain M_t = p_t#, the product of the first t primes p_1, …, p_t, the
condition m p_t# ∣ p_(t+c)# holds iff m is squarefree with every prime
in (p_t, p_(t+c)], so every m ≥ 2 fails at every depth from its least
prime's index on. On
the primorial completion, ∏ F_p (TOWER.md), every ⌊n/m⌋ with m ≥ 2 is
DISCONTINUOUS: at depths 1 to 5, ⌊n/3⌋ reads only at depth 1, ⌊n/5⌋ at
depths 1 and 2, and ⌊n/4⌋ at none. The script's brute search agrees with
the divisibility at all 1142 (chain, m, t, c) it scans at bases 10 and
12 and the primorial chain. It runs the one-step reduction the proof
uses, so it checks the floor arithmetic and not the reduction.

## The division trichotomy
Tier: theorem.
Verifier: proof; reading.py::section_x.

On a divisor chain, ⌊n/m⌋ is LIPSCHITZ iff the least c with m
M_t ∣ M_(t+c) is bounded over t, MIDDLE iff it is finite at every t and
unbounded, and DISCONTINUOUS iff some depth has none. All three occur on
one chain. So that ⌊n/m⌋ never falls in MIDDLE is a fact about
fixed-radix chains, not about rings.

Proof. The division criterion, depth by depth, with the three classes of
the Lipschitz criterion, whose compactness argument holds on the
completion of any divisor chain, finitely many tiles per depth. For the
example, take radix 2 at the depths that are powers of two and radix 3
elsewhere. Then M_(t+c)/M_t is the product of the radices at depths
t + 1..t + c. For m = 2 the least c reaches the next power of two,
c = 2^(⌊log₂ t⌋ + 1) − t, finite and unbounded. For m = 3 it is at most
2, since two consecutive depths from 2 on are never both powers of two.
For m = 5 it never exists.

The script prints c_min(⌊n/2⌋, t) = 1, 2, 1, 4, 3, 2, 1, 8, 7, 6 at
t = 1..10, with the largest value 32 over t ≤ 40. For ⌊n/4⌋ it prints
finite values up to 96, for ⌊n/3⌋ at most 2, and ⌊n/5⌋ unread at all 40
depths. At a fixed base b the least c is constant in t, so a
fixed-base numeration shows only two classes.

## Division over F_q[x]
Tier: criterion.
Verifier: proof; reading.py::section_r.

The same statement holds with polynomial division, for a chain with deg
M_1 ≥ 1, where the integer proof takes M_t ≥ 2: ⌊n/m⌋, the quotient of n
by m, is read at lookahead c at depth t iff m M_t ∣ M_(t+c). At base x
it is read at bounded lookahead iff m is a constant times a power of x.
The sufficiency proof above transfers, since the remainder has degree
below deg m and so is fixed by n mod m. The necessity proof over Z does
not, since the pairs (n, n + kM) are not chains of one-steps, but
linearity replaces it. Division by m is F_q-linear, so with M = M_(t+c)
the condition is that ⌊kM/m⌋ ∈ (M_t) for every polynomial k. If m ∤ M,
write M = hm + s with s ≠ 0 of degree below deg m, and take
k = x^(deg m − deg s): then ks has degree deg m, and ⌊kM/m⌋ = kh + a for
a nonzero constant a. With h ∈ (M_t), from k = 1, a would lie in (M_t),
which has no nonzero constants. So m ∣ M, the quotient of kM is kM/m,
and k = 1 asks M_t ∣ M/m. The script's brute search, every pair below a
degree bound over F₂[x] at bases x and x(x + 1) with m of degree 1 to 3,
agrees at 168 of 168 cases. The division criterion therefore reads the
same over Z and over F_q[x], and so does its fixed-base form
rad(m) ∣ rad(base).

## The comb
Tier: theorem.
Verifier: proof; reading.py::section_c.

Take the trailing d-bonacci numeration, whose positional weights are
q_k = q_(k−1) + ⋯ + q_(k−d), with q_j = 2^j for j < d, and whose
greedy digits are exactly the strings with no d consecutive ones. At
every d ≥ 2 the completion carries no continuous addition extending
the integers', so it is not a topological ring extending them; d = 2
is Zeckendorf. Doubling walks a carry down:
2q_k = q_(k+1) + q_(k−d) for k ≥ d. So the comb
T_K = q_d + q_(2d+1) + ⋯ + q_K, which steps by d + 1, doubles to a comb
that steps by d, and the bottom of that comb cycles through d phases
with period d(d + 1) in K. T_K and T_(K+d+1) agree to depth exactly
K + d + 1, while their doubles differ at a digit ≤ d − 2, so ×2 has no
continuous extension. At Zeckendorf the scan finds adding 1 read where
doubling is not: the successor n + 1 has c_min = 1 at depths 1 to 8.

Proof. A string with no d consecutive ones sums below the next place,
one of its top d indices being absent, so it is its value's greedy
expansion; conversely d ones at j, …, j − d + 1 sum to q_(j+1), so a
greedy expansion has none. Write K = d + (d + 1)i′ and i = i′ mod d. The
digits of 2T_K are the bottom {0, …, i} and the teeth j ≡ i + 1 mod d
from d + 1 + i to K + 1 when i ≤ d − 2, and the teeth j ≡ 0 mod d from d
to K + 1 when i = d − 1. The base is 2T_d = q_(d+1) + q_0. The step adds
2q_(K+d+1) = q_(K+d+2) + q_(K+1): the q_(K+1) doubles the top tooth,
each doubled tooth j leaves q_(j+1) and doubles the tooth d below, so
every tooth moves up one. At the bottom tooth the carry moves q_(i+1)
down onto the bottom; at i = d − 2 the full bottom sums to q_d, a tooth,
and at i = d − 1 the tooth d splits to q_(d+1) + q_0. Each result has
its teeth d apart and a bottom run shorter than d below a gap, so it is
canonical, and the d bottoms differ pairwise at a digit ≤ d − 2.

The script prints d patterns and period d(d + 1) at every d = 2..6, with
the doubles of T_K and T_(K+d+1) first apart at a digit ≤ d − 2, the
largest such digit d − 2 at each d, and reads the proof's phase sets off
112 doubles at d = 2..8, all matching. At Zeckendorf, 2n reads at no
c ≤ 6 at depths 1 to 3, a check that the scan detects a discontinuity.
Known on the completion's other side: the d-bonacci system is measurably
conjugate to a translation of the (d − 1)-torus (at d = 3, Rauzy, Bull.
Soc. Math. France 110, 1982, who proves the coding by the three pieces
of the Rauzy fractal and states as Remarque 6.3 the conjugacy with the
d = 3 completion; for every substitutive Arnoux–Rauzy sequence,
Berthé, Jolivet and Siegel, Uniform Distribution Theory 7, 2012). The
completion itself is totally disconnected and maps onto that torus: at d
= 2 it is the Zeckendorf odometer (OSTROWSKI.md) over a circle rotation,
and each d ≥ 3 sits over a torus translation, none of them a topological
ring extending the integers'. The group extending the integers' that the
completion lacks exists in a coarser topology:
Carton, Sudbery and Yassawi (arXiv:2606.30496, 2026) build the U-adic
integers of every zero-preserving Pisot numeration U, U its sequence of
positional weights, set the agreement topology aside, and project them
onto a
torus, isomorphically at Zeckendorf (Rittaud and Vivier had the
Zeckendorf case, 2012, as they report); they find a ring "difficult" and
prove no obstruction. The comb is the obstruction in the topology they
set aside. That addition has no continuous extension at Zeckendorf is
older: Barat, Berthé, Liardet and Thuswaldner (Ann. Inst. Fourier 56,
2006, Example 5.5) add (01)^∞ and (10)^∞ along two integer
approximations and get two cluster points, saying the same holds for
every Ostrowski numeration. The comb is sharper, one argument added to
itself.

## Floor division on the d-bonacci completion
Tier: theorem.
Verifier: proof; bonacci.py::section_f.

At every d ≥ 2 and m ≥ 2, ⌊n/m⌋ has no continuous extension to the
d-bonacci completion. The proof reads the torus the completion sits
over; β is the largest root of x^d − x^(d−1) − ⋯ − 1, a Pisot number,
its other roots inside the unit circle (Brauer, Math. Nachr. 4,
1950). With α = (β⁻¹, …, β⁻⁽ᵈ⁻¹⁾) and
ν_k = (q_(k−1), …, q_(k−d+1)), the recurrence run backward giving
q_(−1) = 1 and q_j = 0 for −d < j ≤ −2, θ_k = q_k α − ν_k shrinks
geometrically: each coordinate solves the recurrence and its β-part
cancels. So φ(y) = Σ y_k θ_k mod Z^(d−1) is continuous on the
completion, and φ(n) = nα. The inputs q_K tend to 0, and
⌊q_K/m⌋α = (θ_K + ν_K − r_K α)/m with r_K = q_K mod m. The state
(q_K, …, q_(K−d+1)) mod m is purely periodic and not constant, since it
holds 2 beside 1 at K = d − 1. On a class γ of its period every cluster
point of ⌊q_K/m⌋ maps to (ν_γ − r_γ α)/m, ν_γ and r_γ being the values
of ν_K mod m and of r_K on γ, and two classes with different states give
different points because β is irrational. So ⌊n/m⌋ has at
least two cluster values over the input 0. The circle case d = 2 is
OSTROWSKI.md#floor-division-is-never-middle-here.

## The scaling certificate
Tier: rule (proved per pair at 47 pairs, d ≤ 10, m ≤ 12).
Verifier: bonacci.py::section_w; bonacci.py::section_x.

The comb's move does not reach ×3, since 3q_k = q_(k+1) + q_k + q_(k−d)
keeps a copy at k. 1/m's expansion in base β reaches it pair by pair.
Let W be a purely periodic word with period π and no d consecutive ones,
read cyclically, and let A_K = Σ_(1≤i≤K) w_i q_(K−i) be W written
downward from position K − 1. Its string is greedy, and on a class K ≡ γ
mod π its low digits do not move, so A_K converges. With
Δ(z) = 1 − z − ⋯ − z^d and R(z) = Σ_(i≤π) w_i z^i, the error
e_K = q_K − mA_K has generating function
(1 + z + ⋯ + z^(d−1))(1 − z^π − mR)/(Δ(1 − z^π)). When Δ divides
1 − z^π − mR, which says that Σ w_i β^(−i) = 1/m, e_K is purely periodic
with period π, with one value e_γ on each class K ≡ γ mod π. The
string of q_K − r (r ≥ 1) has its zeros exactly at the positions
≡ K mod d down to the least such J with q_J ≥ r, and q_J − r's greedy
string below that. So it has d limits, one per residue of K. If a class
has e_γ ≥ 1 and meets two residues mod d, A_K converges there while mA_K
= q_K − e_γ does not, and ×m has no continuous extension. The
divisibility is a finite check, so each pair it passes is proved.

At m = 2 the word is 0 1^(d−1) 0 at every d, since (1 + z)Δ = 1 −
z^(d+1) − 2(z² + ⋯ + z^d). So e = 1, 2, …, 2, 1 over period d + 1,
and every class decides: a second proof that ×2 is torn at every d,
independent of the comb. At m = 3 the word is certified and decides
at d = 3, 4, 5, 6, 9; at d = 3 it is 0100010110000. At d = 7 and 8
it is certified with period 364 and 80, which d divides, so each class
sits in one residue and nothing is decided. At d = 10 no word with
period below 1200 was found. ×3 is open at d = 7, 8 and 10,
and unscanned past 10. The certificate aims only at the d limits of
q_K − r, the codings of −r; any other point of the torus with several
codings, such as the
comb's limits, could serve as the target instead.
Over d = 2..10 and m = 2..12 the certificate tears 47 of the 99 pairs;
23 are certified and undecided, and 29 have no word found. At m = 1 it
decides nothing, as it must. The word's period equals the state's
period mod m at all 70 certificates. That the state's period divides
it is proved, since e_K ≡ q_K mod m; the converse is observed.

## Open fronts

Which class ×m falls in on a d-bonacci completion. Floor division and ×2
are DISCONTINUOUS at every d, and the scaling certificate tears ×m pair
by pair. At d = 2 every ×m, m ≥ 2, is DISCONTINUOUS
(OSTROWSKI.md#the-affine-maps). Open, at d ≥ 3: the pairs the
certificate leaves undecided or for which no word was found, ×3 at
d = 7, 8 and 10 among them, and every pair with m ≥ 3 outside d ≤ 10,
m ≤ 12. The comb's move does not carry over to ×3. Routes that could
decide a whole degree: a certificate aimed at another point with several
codings, such as the comb's limits, or an argument over the set of torus
points with several codings. A longer word search decides pairs one at a
time.
