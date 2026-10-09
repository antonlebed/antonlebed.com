# HEADROOM — what a probe sees of a grown state

The object: a growth state Z/M read by the demands that read λ, the
exponent of its unit group, each answering one bit per offered move m,
whether λ(Mm) = λ(M). The answers factor through one number, the
**headroom** ξ(M) = W(λ(M))/M, W(L) being the wall, the largest N with
λ(N) | L. This page asks what that number is, how it moves under a move
(what a move spends of it and what it opens), what order sits underneath
it, what it costs to tell apart two states it merges, and how many
states it merges. Its verifier, headroom.py, checks the computed
cases of every block.

The probe is the family of λ-reading demands (GROWTH.md#the-three-fates
names transparency among them), and its reading of M is ξ(M). Two
distinct states with one reading are a **blind pair**, and the states
sharing a reading, when two or more do, a **blind class**. Along a move
m the **wall gain** is Γ(M, m) = W(λ(Mm))/W(λ(M)), the **burn** is
gcd(m, ξ(M)), the **unpaid part** is u = m/gcd(m, ξ(M)), and the
**premium** is G(M, m) = Γ/u. A **door** of L is an odd prime p with
(p − 1) | L (a prime of the wall, not GROWTH.md's door, the rise of the
least move opening or deepening a place); W(L) is 2^(v₂(L)+2) at even L,
2 at odd, times p^(v_p(L)+1) over the doors
(GROWTH.md#the-wall-is-adams-number).

The answer, in one line: the reading is one number that a move spends by
truncated subtraction and reopens through the wall, at 2 and at the
doors (theorem), and the states it reads as 1 are the fixed points of
the closure M ↦ W(λ(M)), the tombstones (HEADROOM.md#the-closure);
states it merges always have different λ, are told apart exactly where
their wall gains differ (criterion) and never cheaper than the least
non-divisor of the reading (theorem); and at every even λ the reading
W(λ) is shared by a set of primes q ≡ 1 (mod λ) of positive density
(theorem).

## The headroom
Tier: property.
Verifier: headroom.py::section_h.

The moduli with λ(M) | L are closed under lcm, so each divides W(L);
since λ(M) | λ(Mm), a move m is transparent, λ(Mm) = λ(M), iff
Mm | W(λ(M)), that is iff m | ξ(M). A λ-reading demand's whole response
to a state is the indicator of the divisors of ξ(M), so the probe sees
one number. Read prime by prime off the wall: at a door l of λ,
v_l(ξ) = v_l(λ) + 1 − v_l(M); at an odd non-door both v_l(ξ) and v_l(M)
vanish; at 2, v₂(ξ) = v₂(λ) + 2 − v₂(M) at even λ and 1 − v₂(M) at odd.

Neither the reading nor the prime support determines the other: 855
and 2565 have the support {3, 5, 19} and read 161616 and 53872, while
10 and 11 read 24 on the supports {2, 5} and {11}. A demand and its
complement read identically, since a probe returns one bit per offered
move: a demand admitting exactly the moves another refuses reads the
same number.

## The ledger
Tier: theorem.
Verifier: proof; headroom.py::section_l.

Every move splits into what it spends and what it opens:

    ξ(Mm) = (ξ(M)/gcd(m, ξ(M))) · G(M, m),   G a positive integer.

Mm divides its own wall Γ·W(λ(M)) = Γ·ξ·M, so m | Γξ, and prime by prime
v_l(u) = max(0, v_l(m) − v_l(ξ)) ≤ v_l(Γ). The burn is truncated
subtraction in the exponents, so a move never destroys more headroom
than it spends, and ξ rises exactly when G > gcd(m, ξ).

Of the four parts only the wall gain is a ratio of one function of the
state taken at the two ends, so it telescopes:
Γ(M, ab) = Γ(M, a)·Γ(Ma, b), while the unpaid part, and with it the
burn and the premium, does not: from 1 the move 12 leaves 6 unpaid, but
3 then 4 leave 3 and then 1, and G(1, 3)·G(3, 4) = 4 = 2·G(1, 12).
Splitting a move m = ab gives G(M, a)·G(Ma, b) = k·G(M, ab) with k a
positive integer, so a split never undercounts the premium. With
x = v_l(ξ(M)) and a_l, b_l, g_l the exponents of a, b and G(M, a), the
reading after a is x − min(a_l, x) + g_l at l, and
min(a_l + b_l, x) ≤ min(a_l, x) + min(b_l, x − min(a_l, x) + g_l) in
both cases a_l ≥ x and a_l < x. Equality, k = 1, holds iff at every
l | b either g_l = 0 or b_l ≤ x − a_l.

## The premium in closed form
Tier: theorem.
Verifier: proof; headroom.py::section_p.

λ(Mm) is the lcm of λ(M) and λ(l^(c_l+e_l)) over the primes l | m,
with e_l = v_l(m) and c_l = v_l(M) = v_l(W(λ(M))) − v_l(ξ(M)). So

    G(M, m) = W(λ(Mm)) / ( W(λ(M)) · ∏_(l | m) l^(e_l − min(e_l, v_l(ξ))) )

is a function of λ(M), m and the reading's exponents at the primes of
m, and of nothing else; on a move prime to M it is a function of λ(M)
and m. The exponents are needed: λ(3) = λ(8) = 2, and the move 3 pays
a premium of 7 at 3, where ξ = 8, and 1 at 8, where ξ = 3.

The primes of a move interact through the lcm, at 2 and at the doors:
from 1 the moves 3, 5 and 15 pay premiums 4, 24 and 8, the wall's 2-part
taking a maximum rather than a product (a factor 4) and the door 3,
opened by 5, paid inside 15's unpaid part (a factor 3). From λ = 1 the
move 5 opens the doors 3 and 5, the move 7 opens 3 and 7, and 35 opens
3, 5, 7 and 13, since 13 − 1 = 12 takes its 4 from λ(5) and its 3 from
λ(7). So a move's premium is not assembled from its factors'. On a prime
q not dividing M the odd part of the wall gain is a product of two
parts: p^(v_p(λ′) + 1) over the **cohort**, the set of odd primes p that
are newly doors of λ′ = λ(Mq), and the bumps p^(v_p(λ′) − v_p(λ)) over
the doors already open. From the state 1 no door is open, and the cohort
of q is every odd prime p with (p − 1) | (q − 1).

## Silence lands in a blind class
Tier: theorem; rule (the share off the class, verified q < 10^5 at the
24 swept even λ > 2).
Verifier: proof; headroom.py::section_s.

A prime q not dividing M, with (q − 1) not dividing λ = λ(M), is **silent**
at M when G(M, q) = 1: λ moves and the reading does not. Then u = q, so
W(lcm(λ, q − 1)) = q·W(λ), and every door of lcm(λ, q − 1) but q is a
door of λ at the same exponent, and v₂(lcm(λ, q − 1)) = v₂(λ). Every
door p ≠ q of q − 1 is then a door of g = gcd(q − 1, λ), with
v_p(q − 1) = v_p(g), and v₂(q − 1) = v₂(g), so

    W(q − 1) = q · W(g):   a prime silent at M reads ξ(q) = W(g).

That reading is a blind class: g is even, since v₂(g) = v₂(q − 1), so by
the blind-density theorem below infinitely many primes read W(g).

At λ = 2 the silent primes are exactly the primes of the class ξ = 24
not dividing M. At odd λ none is silent: the wall's 2-part is 2 and a
prime q > 2 raises it to at least 8. Conversely a prime q ≡ 1 (mod λ)
not dividing M with ξ(q) = W(λ) is silent at M, so at even λ the silent
set holds every prime of the class ξ = W(λ) that is ≡ 1 (mod λ) and
prime to M, and has positive density by the blind-density theorem below.
It holds more. Since λ(W(λ)) = λ at λ = λ(M) (the closure below) while
λ(W(g)) divides g, a member q
with λ ∤ q − 1 reads W(g) ≠ W(λ), g a proper divisor of λ. There are
none at λ = 2, every odd q being ≡ 1 mod 2. Silence at a state that q
does not divide depends on λ alone, and below 10^5 these primes are the
majority of the primes silent at λ at each of 24 even λ chosen from 4
to 180 (headroom.py lists them): 820 of 1,262 at λ = 4 (least 23), 914
of 1,049 at 12 (least 83), the smallest share 588 of 1,066 at 6.

## The closure
Tier: theorem.
Verifier: proof; headroom.py::section_w.

M ↦ M* = W(λ(M)) is inflationary (M | M*), monotone (M | M′ gives
λ(M) | λ(M′), and W is monotone under divisibility) and idempotent
(λ(M*) = λ(M), one way by M | M* and the other by W's definition). So a
run of transparent moves is a walk in the divisor lattice between M and
M*, and the jump m = ξ lands on M* at once. The fixed points, ξ = 1, are
the **tombstones**, and every W(L) is one. Above 2 each is divisible by 24,
since λ is even from 3 up, which puts 2³ and the door 3 in the wall; 2
is the only tombstone of odd λ. The tombstones are one infinite blind
class, since W(2^j) ≥ 2^(j+2), and its infinitude needs no sieve.

## The resolution criterion
Tier: criterion (proved both ways).
Verifier: proof; headroom.py::section_r.

A blind pair always has different λ, since M = W(λ(M))/ξ(M): the probe
is injective on each λ-fibre, and blindness is a cross-λ event. A
multiplier d resolves the pair (M₁, M₂) when ξ(M₁d) ≠ ξ(M₂d), and since
ξ(M_i d) = ξ·Γ_i/d with ξ shared, d resolves iff the two wall gains
differ. A divisor of ξ moves no wall, so every resolver is a non-divisor
of the reading. On multipliers prime to M₁M₂ the wall gain depends on d
only through λ(d), so the resolving set is a union of λ-fibres there. It
is not closed upward (the watcher's guaranteed blindness below has the
witness).

## The non-divisor bound
Tier: theorem; observation (attained by a representative pair in 90 of
the 96 blind classes among the states 2..1499).
Verifier: proof; headroom.py::section_r.

The least resolver of a blind pair of reading ξ is at least κ(ξ), the
least integer ≥ 2 not dividing ξ, since a move m dividing ξ is
transparent at both states and sends both readings to ξ/m; and κ(ξ) is
a prime power: a least
non-divisor p^a·r with r > 1 prime to p has both parts dividing ξ, hence
their product. The bound is a function of the reading alone, so a probe
computes a lower bound on its own least resolver from inside its
blindness, knowing neither state. At ξ = 24 it is 5, and 10 and 11 split
at exactly 5, into 264 and 240.

## No blindness is permanent
Tier: theorem; observation (the least such prime, over one pair in each
of the 96 blind classes among the states 2..1499).
Verifier: proof; headroom.py::section_r.

For a blind pair with λ-values λ₁, λ₂, a prime q ≡ 1 (mod lcm(λ₁, λ₂))
not dividing M₁M₂, which Dirichlet's theorem provides, sends both to
λ = q − 1: the walls agree and the
readings W(q − 1)/(M_i q) cannot. This resolver exists and can be dear:
over one representative pair in each of the 96 blind classes among the
states 2..1499 the least such prime reaches 111827. The next reading is
no function of the reading and the move: 2 and 24 both read 1, and 5
sends them to 24 and 2.

## The watcher's guaranteed blindness
Tier: theorem.
Verifier: proof; headroom.py::section_r.

A watcher, handed a move m, sees the readings ξ(M_i d) at the divisors d
of m. The moves that keep a pair blind at every such reading are those
whose divisors all miss the resolvers, a divisor-closed family holding
every divisor of ξ, so at least τ(ξ) − 1 offered moves keep every blind
pair blind with certainty, τ the number of divisors, while a
**chooser**, who picks the move, need never take one of them. A move
blind at its end can be split inside it: 9 and 513 read 56, read 56
again after 57 = 3·19, and read 1064 against 56 after 3. That is a
resolver whose multiple is not one, which is the resolving set failing
to be closed upward: reading more often is a faculty of the watcher
alone, since a chooser reading after 3 has simply played 3.

## The blind-density theorem
Tier: theorem.
Verifier: proof; headroom.py::section_d.

For every even λ, the primes q ≡ 1 (mod λ) with ξ(q) = W(λ) have a
positive relative density among the primes. At λ = 2 these are the
primes with W(q − 1) = 24q, which by von Staudt–Clausen are, for q ≥ 11,
exactly the primes with denom(B_(q−1)) = 6q; 5 and 7 have that
denominator and read 48 and 72. That case is Pomerance and Wagstaff's
(The denominators of the Bernoulli numbers, Acta Arith., doi
10.4064/aa210601-16-11, arXiv:2105.13252, Theorem 3 for the denominator
6q), whose theorem gives positive density to the primes q whose
denominator is a fixed cofactor times q, for every cofactor that is
itself some Bernoulli denominator. Their condition sees only which
p − 1, p prime, divide q − 1, which pins the valuations the class needs
at λ = 2 but not in general (at λ = 4, q = 137 has denominator 30q and
reads 480, not 240), so it is theirs cut by a residue condition, and the
proof below covers every even λ.

Proof. For q ≠ λ + 1 the class condition inside the progression reads
v_p(q − 1) ≤ v_p(λ) at 2 and the doors of λ, and (p − 1) ∤ (q − 1) at
every odd prime p off them, p ≠ q: decreasing events in the vector
(v_l(q − 1))_l. Under the prime density, read on finite truncations,
where it is a residue condition, its coordinates are independent (by
Dirichlet the residue class 1 mod D has density ∏ 1/φ(l^a) over
l^a ∥ D, φ being Euler's function) and each is a chain, so Harris's
inequality gives P(E ∩ F) ≥ P(E)·P(F)
for decreasing E and F. Let δ_T be the relative density, inside the
progression, of the conditions at the doors and at the p ≤ T, a residue
condition, and ε(T) the upper density among all primes of the q with
(p − 1) | (q − 1) for some prime p > T, p ≠ q; inside the progression
that event has relative upper density at most φ(λ)ε(T). The class share
lies in [δ_T − φ(λ)ε(T), δ_T], and δ_T′ ≥ δ_T·(1 − φ(λ)ε(T)) for T′ > T,
so once ε(T) → 0 the class has density lim δ_T > 0. And ε(T) ≪
(log T)^(−c) for an absolute c > 0, since the number of such q up to x
is ≪ π(x)(log T)^(−c) uniformly in x: Luca, Pizarro-Madariaga and
Pomerance, On the counting function of irregular primes, Indag. Math. 26
(2015) 147–161, Theorem 3 with its two parameters at 1 and −1.
headroom.py's docstring re-derives it step by step from Erdős and
Wagstaff's Theorem 2 (Illinois J. Math. 24 (1980) 104–112) with
Pollack's sifted-set Shiu bound (Nonnegative multiplicative functions on
sifted sets, and the square roots of −1 modulo shifted primes, Glasgow
Math. J. 62 (2020) 187–199, Theorem 1.1), at c = η/2 ≈ 0.0066,
η = (7/6)·log(7/6) − 1/6 a Chernoff exponent of that derivation. ∎

The value of the density is not derived. At λ = 2 the verifier checks
the exact product-measure δ_T against the primes to 10⁷ (0.16108 against
0.16100 at T = 47) and one instance of Harris's inequality in exact
rationals; it checks the decreasing-event reading at every q < 10⁶,
q ≠ λ + 1, in five progressions, and, at every prime 11 ≤ q < 10⁶, that
ξ(q) = 24 exactly when the von Staudt–Clausen product of q − 1, which is
denom(B_(q−1)), is 6q. The independence product ∏(1 − 1/φ(p − 1))
tends to 0, so independence alone cannot give positivity; the tail
bound on ε is what does.

## The least resolver is unbounded
Tier: theorem.
Verifier: proof; headroom.py::section_d.

Every reading W(λ) at even λ hosts infinitely many blind pairs, two
primes of its class, by the blind-density theorem. Along
L_n = lcm(1, …, n) every odd prime r ≤ n + 1 is a door of L_n, 2 enters
through the wall's 2-part, and v_r(W(L_n)) ≥ v_r(L_n) + 1 with
r^(v_r(L_n)+1) > n, so every prime power up to n + 1 divides W(L_n) and
κ(W(L_n)) > n + 1, and by the non-divisor bound so is every least
resolver at that reading. How cheap the least resolver is cannot be bounded in
advance, though for each pair it exists.
