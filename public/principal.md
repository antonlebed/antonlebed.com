# PRINCIPAL — where a quadratic field's first principal prime sits

The object: a quadratic field K = Q(√D), D a fundamental discriminant,
and its split primes whose places are principal. This page states how far
down the least of them can sit, which the sign of D decides, and what the
shortfall of principal primes at a finite cut is. Its engine is
principal.py.

An odd prime p with χ_D(p) = +1, χ_D the Kronecker symbol (D/·), splits
as P·P̄, and P is principal when P = (α); over a real field that is
principal as an ideal (the wide sense) unless the narrow group is named.
L₁(D) is the least odd prime with χ_D(p) = +1 and P principal; its P
is a principal rank-1 place of least odd norm, and at any principal
rank-1 place a greedy walk whose moves must be principal keeps the
carrier ladder, climbed through carriers (rank-1 and carrier as
CASCADE.md's lead defines them, the claim at
CASCADE.md#the-escape-is-a-conjunction). The principal form
of discriminant D is x² + b₀xy + c₀y², b₀ = D mod 2, c₀ = (b₀ − D)/4,
and N(x + yω) is its value at (x, y), ω = (b₀ + √D)/2. So P is principal
exactly when p or −p is a value of that form, that is when

```
4p  =  |u² − D·y²|,      u = 2x + b₀y.
```

The answer, in two lines: over an imaginary field the form is definite,
so a principal prime is at least |D|/4 and, to |D| ≤ 20000, the median
least one sits inside the floor's range over its band of |D| (an
observation), while over a real field the form is indefinite and there
is no floor at all; and over a population of fields the degree-1 primes
at a finite cut miss their classes' even shares by the prime-ideal
powers the count leaves out (a pattern): counting those powers removes
93–104% of the excess on the
classes that are neither squares nor 2-torsion over imaginary fields,
and 84–97% over real ones in the narrow class group. What still departs
over real fields sits mostly on the narrow trivial class and on the
class of principal ideals whose generators all have negative norm, and
is open.

## The floor
Tier: theorem.
Verifier: proof; principal.py::section_floor.

Over an imaginary field, L₁ ≥ |D|/4, and L₁ ≥ (|D| + 1)/4 at odd D. The
floor is met, L₁ = (|D| + 1)/4, exactly when D is odd and (|D| + 1)/4 is
an odd prime; at even D it is never met.

Proof. Let P over p be principal, so 4p = u² + |D|y². If y = 0 then
4p = u² and p is a square, which it is not; so y ≠ 0 and 4p ≥ |D|. At
odd D, u ≡ b₀y ≡ y mod 2, so a y of either parity gives 4p ≥ |D| + 1.
For equality at odd D, the form's value at (0, 1) is c₀ = (|D| + 1)/4,
and D = 1 − 4c₀ makes c₀ prime to D: an odd prime c₀ is unramified and
represented, hence split and principal, and nothing lower can be. At
D ≡ 0 mod 4, 4p = |D| forces u = 0 and |y| = 1, so p = |D|/4, which
divides D and ramifies. Conversely L₁ is an odd prime, so it meets
(|D| + 1)/4 only where that value is one.

The floor never consults the class group: it is the size of the norm
form and nothing else. Its corollary is that the imaginary fields with
L₁ ≤ B form a finite set, since none with |D| > 4B has L₁ ≤ B.
Over all 6079 imaginary fields with |D| ≤ 20000 the scan meets the
floor at 499, each at the criterion; the median L₁ runs 181, 587, 1163,
2269, 4483 over the |D| bands (0, 1000], (1000, 2500], …,
(10000, 20000], each inside the floor's range over its band, so a scan
for a principal prime costs |D|/4 before it can succeed.

## No floor over a real field
Tier: theorem.
Verifier: proof; principal.py::section_family,
principal.py::section_real.

Over a real field no lower bound on L₁ growing with D exists: L₁ = 3 at
every squarefree D > 0 of the form m² − 12 or m² + 12 with m odd and
3 ∤ m, and there are infinitely many.

Proof. With m odd, m² ≡ 1 mod 8, so D ≡ 5 mod 8 and b₀ = 1. Put
x = (m − 1)/2: then N(x + ω) = x² + x − (D − 1)/4 = (m² − D)/4 = ±3.
D ≡ m² mod 3 is a nonzero square, so χ_D(3) = +1, and x + ω generates a
place over 3. So L₁ = 3 whenever D is fundamental, that is squarefree.
Writing m = 6n ± 1, D is an irreducible quadratic in n with no fixed
square divisor: it is odd, prime to 3, and modulo ℓ² for ℓ ≥ 5 a
quadratic with unit leading coefficient 36 does not vanish at every n.
Such a quadratic takes squarefree values with positive density (Ricci,
Rend. Circ. Mat. Palermo 57, 1933; the case z² + k is Estermann's,
Math. Ann. 105, 1931).

The difference between the two signs is the sign in 4p = |u² − Dy²|: a
definite form's values grow with |D|, an indefinite one takes small
values far out. Over a quadratic field that is the unit rank, since a
finite unit group and a definite norm form are both the condition D < 0;
higher up the two come apart (a totally imaginary quartic field is
definite with unit rank 1), and which of them a floor needs there is
left open.
The class engine finds a wide-principal place over 3 at each of the 627
members below 10⁶. Over all 4865 real fields with D ≤ 16000 every one
has L₁ < 10⁴, and the median runs 7, 11, 11, 11, 11 over the D bands
(0, 1000], (1000, 2500], …, (10000, 16000]: from the second band on it
stays at 11. A complex cubic field has unit rank 1 and an indefinite norm
form, and over all 888 whose discriminant is at most 6000 in absolute
value a principal degree-1 place lies over an odd unramified prime below
250, the largest such least prime 131; to 50000 it is 823
(triple.py::section_coverage).

## Where the omitted prime powers land
Tier: property.
Verifier: proof; principal.py::section_imag.

Chebotarev in the Hilbert class field H/K, whose group is the class
group Cl of order h, speaks of the count Π_C(x) of all prime-ideal
powers P^k of K with N(P^k) < x in the class C, each weighted 1/k: its
main term is Li(x)/h for every class. The degree-1 count read on this
page is of the split places alone, so it omits three families, a
ramified prime among them though its degree is 1, and each lands on
known classes:

- an inert prime (q) has norm q² and is principal: weight 1 on the
  trivial class for each q < √x;
- the square P² of a split place has norm p² and class 2[P]: weight ½
  on a square class, twice per split p < √x;
- a ramified prime R, over the rational prime r, has R² = (r)
  principal, so [R] lies in Cl[2].

The remaining powers, each weighted 1/k at norm below x, land as
follows: even powers of a split place on squares, powers of inert and
ramified primes on the trivial class and Cl[2], and only the odd powers
k ≥ 3 of split places, p < x^(1/k) (the cubes p < 22 at x = 10⁴),
anywhere. So a class in neither 2Cl nor Cl[2] loses only that sliver of
odd-power weight, while a class in 2Cl or Cl[2] loses besides the weight
of every family and power above that lands on it. Split places below x
number about π(x), so a class holds about π(x)/h of them, and the
trivial class loses about π(√x)/2 inert primes plus, were the split
places below √x spread evenly over the classes, the share |Cl[2]|/h of
the split squares' weight π(√x)/2: to leading order under that spread, a
deficit against its Chebotarev share Li(x)/h of

```
(h + |Cl[2]|)/2 · π(√x)/π(x),
```

affine in h at a fixed |Cl[2]|. Read against the field's realised total
over h, itself short of Li(x)/h by about π(√x)/h, the trivial class
falls short by that deficit less π(√x)/π(x), to the same order. Over a
real field the
same holds in the narrow group Cl⁺, of order h⁺, since q and r are
generators of positive norm.

## The shortfall is the prime powers
Tier: pattern (imaginary fields |D| ≤ 4000 with h ≥ 2, the strata of 30
fields or more, h = 4, 6, …, 16, 20, 24, 28; real fields D ≤ 16000 with
h⁺ ≥ 2, in the narrow group; cuts 250 to 10⁴).
Verifier: principal.py::section_imag; principal.py::section_real;
principal.py::section_race.

Per field the **level** of a set of classes is its mean count per class
over the field's total divided by h. The cells are T, the trivial class;
A, the other classes of Cl[2], over a real field less one read alone
below; S, the other squares; G, the classes in
neither 2Cl nor Cl[2], which lose only the sliver of odd-power weight. Read
over a population of fields, where the explicit formula's oscillating
remainders average out and its prime-power term does not, the degree-1
levels depart from 1 by what the omitted weight predicts, to the
percentages below. Counting Π_C instead removes 93% to 104% of the G
cell's excess at every cut over imaginary fields and 84% to 97% over
real ones; over imaginary fields at 10⁴ every (class number, cell)
reading with 30 fields or more lands in 0.97 to 1.02, and over real
fields a remainder sits mostly on two classes. A field's levels average to 1
over its classes, so a cell is read against its siblings, and which
pooled cell takes a surplus depends on the fields' group shapes: a
stratum named by the class number alone hides that shape. At a prime h a
field has two cells, so the non-trivial one is fixed by the trivial one,
at level (h − η)/(h − 1) with η the level of T, and casts no vote of its
own: a fit across strata that counts it as one is testing the trivial
class twice.

Over the 1208 imaginary fields with h ≥ 2 the G cell, present at 880 of
them, reads, raw against counted in prime powers,

```
cut        250     400     630     1000    2500    10⁴
raw        1.186   1.145   1.106   1.089   1.057   1.023
Π          1.013   1.002   0.996   1.000   1.003   0.999
```

at 42 standard errors or more above 1 raw, with 93% to 104% of the
excess removed. The raw excess falls by a factor of 8.0 from cut 250 to
10⁴; in the same level units the term's leading piece π(√x)/π(x) falls
by 5.6 and the whole prime-power weight absorbs the rest, where a fixed
count of primes would fall by π(10⁴)/π(250) = 23 and a constant level
by 1. At 10⁴ all 39 (class number, cell) readings with 30 fields or more
read 0.97 to 1.02 counted in prime powers, while the raw trivial class
runs from 0.95 at h = 4 down to 0.75 at h = 28. Averaged over all 1208
fields at 10⁴, its raw deficit 1 − η is 0.208, and the level's deficit
the section above predicts field by field, the renormalisation taken
off, averages 0.204, a ratio of 1.02.
Below x ≈ |D|/4 the trivial class is empty by the floor, so η at small
cuts is read, never predicted.

Over the 4107 real fields with h⁺ ≥ 2, the G cell present at 1069 of
them, the same count removes 84% of the G excess at cut 250 and 97% at
10⁴ (1.0255 raw, 1.0009 counted). What it leaves is not spread evenly:
counted in prime powers, the trivial class reads 1.07 at cut 250 and
1.005 at 10⁴, and k₀, the narrow class of a principal ideal whose
generators all have negative norm, 0.82 and 0.99; the other cells lie
within 0.035 of 1 at cut 250 and 0.005 at 10⁴. That remainder is
open (PRINCIPAL.md#open-fronts). The classical instance is the control:
over the 77 odd prime moduli below 400 at x = 10⁶ the non-residue lead,
the count of primes below x that are non-residues less the count that
are residues, over the two counts' mean, reads 0.00180 ± 0.00031
against π(√x)/π(x) = 0.00214, and
−0.00042 ± 0.00031 counted in prime powers.

In the character basis, a weight spread evenly over 2Cl, which is the
split squares' weight in the mean over fields, transforms onto the
characters trivial on 2Cl, the genus characters, since the indicator of
a subgroup transforms onto the characters trivial on it.

## The bias against principal primes
Tier: known.
Source: M. Aoki and S. Koyama, Chebyshev's bias against splitting and
principal primes in global fields, J. Number Theory 245 (2023), 233–262,
Corollary 3.5 and Example 3.7.

Assume **DRH**(A), the deep Riemann hypothesis in Aoki and Koyama's form
(A): the convergence of the Euler products of Gal(H/K)'s L-functions at
s = ½, none vanishing there. Then over the prime ideals P of K with
N(P) ≤ x,

```
Σ_{P non-principal} 1/√N(P)  −  (h − 1)·Σ_{P principal} 1/√N(P)
    =  (|Cl/2Cl| − 1)/2 · log(log x)  +  c  +  o(1),
```

a bias against principal primes whenever h is even; over an imaginary
field |Cl/2Cl| = 2^(t − 1), t the number of primes dividing D (genus
theory). Aoki and Koyama's race is weighted and asymptotic; the unweighted
count of degree-1 primes at a finite cut, class by class, is the
accounting above.

## Open fronts

What the prime-power count leaves over real fields sits on the trivial
class and on k₀, and k₀ is the class the archimedean place names. It
exists when the fundamental unit has norm +1, so that h⁺ = 2h, and then
complex conjugation, which fixes the real field K, moves its narrow
class field H⁺: its image in Gal(H⁺/K) = Cl⁺ is k₀. The two real places
give the same image, since their classes differ by that of (α) for a
totally negative α, and (α) = (−α) has the totally positive generator
−α. So a character χ of Cl⁺ with χ(k₀) = −1 is odd at both real places:
its L-function carries the gamma factor Γ_R(s + 1)² and does not vanish
at s = 0. One with χ(k₀) = +1 carries Γ_R(s)², and a double zero at
s = 0 if it is nontrivial; ζ_K has a simple one. Let ψ(x, χ) be the sum
of χ(P^j)·log N(P) over the prime ideal powers P^j of norm at most x. In
the explicit formula a zero of order m at s = 0 puts −m·log x into
ψ(x, χ), and averaging over the characters against χ̄(C) gives
−(1 − 1/h⁺)·log x at C = 1 and at C = k₀ and +(1/h⁺)·log x at every
other class. The archimedean place alone sets the two classes 1 and k₀
one log x below the rest in ψ; when the fundamental unit has norm −1
there is no k₀, every character is even, and the term is −(2 − 1/h)·log
x on the trivial class alone, two log x below the rest. Whether that
term is the whole of k₀'s deficit at the cuts read, what it becomes in a
count of primes rather than in ψ, and why the trivial class reads high
where k₀ reads low, is not derived. Nothing further is claimed of
what the prime-power count leaves.
