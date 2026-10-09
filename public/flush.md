# FLUSH — what a redundant reader of the circle computes

The object: the trailing Ostrowski numeration at an irrational α
(OSTROWSKI.md) read by a bottom-up reader into a redundant output.
Position t may carry any digit up to a_(t+1) + s and position 0 any
digit up to a₁ − 1 + s₀, for slacks s and s₀ ≤ s + 1, and the condition
that a digit equal to a_(t+1) sits over a zero is dropped, so an integer
has many output strings. The input stays greedy. The slack (s, s₀) buys
an excess E = s₀α + s S₁, S_t = Σ_(k≥t) |θ_k|, by which the output's
level-0 range, the real stars of its strings read from position 0 (its
**level** t is position t), is longer than 1. A reader at lookahead c
writes e_t having seen d₀ … d_(t+c). The **completion reader** writes,
for each point of the odometer, an infinite string whose star is mx + M,
x being the input's star and M an integer. The **integer reader** of
n ↦ mn + ω writes, for each n, a finite string equal to mn + ω; where no
ω is named it is ×m's, ω = 0. The notation (q_k, θ_k, the star Σ e_k θ_k
of a string, tiles, cuts, the odometer, t₀) is OSTROWSKI.md's. This page
shows that redundancy with positive excess cures n ↦ mn (m ≥ 2) on the
completion and never floor division, for the reasons OSTROWSKI.md gives
for their walls. It shows that at a purely periodic α the integers cost
the completion reader's lookahead plus the **flush**, the duty to end,
and nothing else, and that there an integer reader of ×m reads at 0 or
at no lookahead below 2, never at 1.

Which price is which. The walls of ×m were the coding's, since x ↦ mx is
continuous on R/Z. Overlapping output tiles cure them, and the cure is
READING.md's signed-digit cover moved onto the circle. At E = 0 the tear
survives, because dropping that condition alone buys no overlap at the
top level. Floor division is no continuous circle map: an input tile
hides n mod m, and no output slack shows it. Between the completion and
the integers two things differ. For ×m the lift is the output's real
star less m times the input's, an integer. The integer reader carries
the set of lifts still possible, and those are the fibre of R over R/Z,
not residues mod m. At a purely periodic α tracking them costs nothing:
the completion reader's least lookahead is that of the same game with
the flush dropped. The flush is what is left. An integer's string ends,
so a capped input digit at a deep enough position k leaves a residual
the reader must write from where it stands. When (m − 1)a_(k+1) > s and
m a_(k+1) < q_(k−1), that residual's only string needs a digit above
a_(k+1) + s for a reader at lookahead 0 or 1; on most cells of the grid
below a deeper reader pays nothing for it.

```
MAP         LEGAL OUTPUT      REDUNDANT, E = 0    REDUNDANT, E > 0
n ↦ n + 1   c = 1             c = 0               c = 0
n ↦ mn      DISCONTINUOUS     torn from t₀        completion: ≤ c_ov
                                                  integers: 0 or ≥ 2
                                                  (purely periodic α)
⌊n/m⌋       DISCONTINUOUS     walled from t*      walled from t*
```

The script's grid: the six purely periodic α golden [1], silver [2],
bronze [3], √3 − 1 = [1, 2], [1, 1, 1, 2] and [2, 1, 3, 1], where
[a₁, …, a_p] is the α whose quotients repeat that block; the maps ×2 …
×5; and the six slacks (s, s₀) = (0, 0), (0, 1), (1, 0), (1, 1), (2, 2),
(3, 3). On this page a periodic α is a purely periodic one. In the table
c_ov is the overlap reader's lookahead and t* the depth from which floor
division walls, both fixed in their sections below.

## The tear at E = 0
Tier: theorem.
Verifier: proof; flush.py::section_tear; flush.py::section_grid.

At s = s₀ = 0, with the condition dropped, no reader of n ↦ mn
(m ≥ 2) at any lookahead commits an output tile of depth t₀ or more
about (1 − α)/m, t₀ the first depth with q_t ≥ 2, at every irrational
α. The successor reads at lookahead 0 there, and so at every slack,
since slack only widens the output digits; the legal output needs
lookahead 1 (OSTROWSKI.md#the-affine-maps).

Proof. At s = s₀ = 0 the level-0 range is exactly [−α, 1 − α], so a
string of N has as real star the representative of Nα mod 1 in
(−α, 1 − α); no N ≥ 0 sits on an end, since (N + 1)α is not an integer.
The least string (0, a₂, 0, a₄, …) has star −α by the telescoping
a_(k+1) θ_k = θ_(k+1) − θ_(k−1), and the greatest (a₁ − 1, 0, a₃, 0, …)
has star 1 − α. A string's star minus −α is Σ (e_k − e_k^min) θ_k, a sum
of non-negative terms, so a string within η of −α agrees with the least
string at every position with |θ_k| > η, and likewise at the top. The
two extremes part at position t₀ − 1. The non-cut y = (1 − α)/m is
carried to the cut −α by x ↦ mx
(OSTROWSKI.md#the-containment-criterion). The integers of every input
tile about y have images mnα on both sides of −α and arbitrarily near
it, so their output strings agree low down with the least string on one
side and with the greatest on the other, whatever the reader chooses,
and no output tile of depth t₀ holds both. The successor writes
e₀ = d₀ + 1, or e₀ = 0 and e₁ = d₁ + 1 when d₀ = a₁ − 1, which is legal
with the condition dropped because d₁ = a₂ forces d₀ = 0. At a₁ = 1 the
same happens one position up.

The script enumerates all 8,321 strings of every N < 300 at s = s₀ = 0
over seven α (the grid's six and the fractional part of Euler's number,
quotients 1, 2, 1, 1, 4, 1, 1, 6, …) and finds every star the
representative, and every string near an end in agreement with that
end's extreme. Its game reads ×2 … ×5 at no c ≤ 3 at each of the
grid's six α, and the successor at 0.

## The overlap reader
Tier: theorem.
Verifier: proof; flush.py::section_completion.

At E > 0, ×m has a completion reader at every irrational α at lookahead
c_ov, the least c with
w_t = m(|θ_(t+c)| + |θ_(t+c+1)|) ≤ ov_t = |θ_(t+1)| + s S_(t+1) at every
level t and w₀ ≤ E. c_ov bounds the completion reader's least lookahead
and need not equal it: golden ×2 at (s, s₀) = (0, 1) has c_ov = 4, and
the safety game below reads it at 3. c_ov is finite, since
|θ_(k+2)| < |θ_k|/2. This is READING.md's signed-digit cure
(READING.md#non-redundant-absolute-tiles-wall-only-at-the-archimedean-place):
the children of a tile overlap by a positive amount, so an interval
shorter than the overlap lies in one child.

Proof. The tails from level t have stars filling the interval T_t
between −Σ cap_k |θ_k| over the k ≥ t with θ_k < 0 and Σ cap_k θ_k over
those with θ_k > 0, cap_k being the **output cap** at k, the largest
output digit allowed there: a_(k+1) + s, or a₁ − 1 + s₀ at k = 0 (the
input cap is a_(k+1), or a₁ − 1 at k = 0). By the telescoping its length
is |θ_(t−1)| + |θ_t| + s S_t, and 1 + E at t = 0. Its members e
θ_t + T_(t+1), e = 0 … cap_t, cover it, and consecutive members overlap
by ov_t. The legal input tails from position j have stars in the closed
interval I_j between −θ_j and −θ_(j−1)
(OSTROWSKI.md#the-circle-numeration), and those opening with a digit d
lie in d θ_j + I_(j+1), which is inside I_j. So once d₀ … d_(t+c) are
seen and e₀ … e_(t−1) written, the star still owed, at a lift M, lies in
J_t = M + m(Σ_(k≤t+c) d_k θ_k + I_(t+c+1)) − Σ_(k<t) e_k θ_k, an
interval of width w_t, and J_(t+1) lies inside J_t − e_t θ_t. Some lift
M puts J₀ inside T₀ when w₀ ≤ E, and a member holds J_t when w_t ≤ ov_t.
Committing that member keeps J_t inside T_t at every depth. The length
of T_t tends to 0, so the output codes mx + M.

The script runs this reader 36,000 times to depth 40 over nine α (the
grid's six, the fractional part of Euler's number, [4] and [5]), ×2 …
×5 and five slacks, and it never fails to find a member. c_ov runs
from 0 to 6 over the grid; at a periodic α the ratios |θ_(k+1)/θ_k|
repeat with the period, so the 40 depths it checks decide them all.

## Floor division walls at every slack
Tier: theorem.
Verifier: proof; flush.py::section_floors.

At every slack and every irrational α, ⌊n/m⌋ (m ≥ 2) commits no output
tile of depth t* or more, t* the first depth with |T_t*| < 1/m, from
any input tile at any lookahead. Every point is a wall, and no slack
changes that: the price is the map's.

Proof. The strings sharing a depth-t prefix have stars in one
translate of T_t, which is an arc of length |T_t| on the circle. Take
any input tile, a non-cut x inside it, and a residue r mod m. By
OSTROWSKI.md#floor-division-is-never-middle-here, for the integers n ≡
r in every input tile about x, the points ⌊n/m⌋α mod 1 come
arbitrarily close to each of the m points (x − rα + P)/m, P = 0 … m −
1, which lie 1/m apart. An arc shorter than 1/m cannot come within ε
of two of them once ε is small, so no depth-t* output tile holds the
images of any input tile.

Over 9,063 tests at six α, m = 2, 3 and s = s₀ = 0 … 3, one per input
tile of depth t* + c, c = 0 … 3, holding at least 12 of the inputs
n < 60000, the script finds the images' circular hull longer than
|T_t*| in every one, by at least 0.196.

## The lift game
Tier: theorem.
Verifier: proof; flush.py::section_grid; flush.py::section_universal.

At a periodic α, the integer reader of n ↦ mn + ω (0 ≤ ω ≤ m) at
lookahead c exists iff the reader wins a finite game, and so does the
reader with the flush dropped. Over a finite alphabet of quotients the
same holds for one reader serving every α with quotients in it, which
sees the quotients through a_(t+c+1) and nothing else of α. The game at
each c is finite, pruned to a box the proof below derives without the
lookahead, so it is decided exactly, and the two least lookaheads, where
finite, are found by searching c upward: c_int, the integer reader's,
which must also flush, and c_saf, the least lookahead of the safety
game, the reader with the flush dropped.

Proof. Write the residual H_t = m Σ_(k≤t) d_k q_k + ω − Σ_(k<t) e_k q_k,
keeping the pre-read d_(t+1) … d_(t+c) apart, as g q_t + h q_(t−1), and
set σ = g θ_t + h θ_(t−1). The pair (g, h) is a lattice point of
integers, and a step sends it to (h + m d_(t+1), g − e_t − a_(t+1) h),
labelled by the local quotient alone. The seed (m d₀ + ω, −M) carries
the lift M, and each lift still possible carries its own pair, its
branch. Every branch has the same H, since two differ by a multiple of
(q_(t−1), −q_t), so the state is the set of lifts still alive together
with the pending quotients, the position in α's period, the pending
digits and three flags: whether the last input digit is 0, which bounds
the next one; whether the step is at position 0, whose output cap is
a₁ − 1 + s₀; and, when the game is run on the legal output (s = s₀ = 0
with the dropped condition restored, the table's legal-output column),
whether the last output digit is 0. A correct reader's own lift has
σ_t = (output tail star) − m (input tail star from t + 1), so
|σ_t| < (1 + s)|θ_(t−1)| + m|θ_t|, and |H_t| ≤ μ q_(t+1) with
μ = max(m, 1 + s): a greedy input prefix is below q_(t+1), so
H_t ≤ m(q_(t+1) − 1) + ω ≤ m q_(t+1) as ω ≤ m, and the output prefix,
every digit at most a_(k+1) + s, is at most (1 + s)(q_(t+1) − 1), by
Σ_(k<t) a_(k+1) q_k = q_t + q_(t−1) − 1 ≤ q_(t+1) − 1 and Σ_(k<t)
q_k < q_(t+1). The frame is unimodular, and q_t |θ_(t−1)|, q_(t+1) |θ_t|
and q_(t−1)|θ_(t−1)| are at most 1, with equality only at q₀|θ₋₁|, where
the bound on σ_t is strict, while q_(t+1) |θ_(t−1)| < a_(t+1) + 1, so
that branch obeys

    |g| < B_g = μ(A + 1) + 1 + s + m,    |h| < B_h = 1 + s + m + μ,

A the largest quotient. Pruning branches outside this box never removes
it, so a win of the pruned game is a reader and a loss is a loss. The
integer game asks, besides safety, that under zero input the reader can
force the branch (0, 0) with nothing pending, which is H = 0: the flush.
The safety game omits that. Both are a greatest fixed point over
finitely many states. The safety game's fixed point keeps the states
with a move whose every reply stays in the set; the integer game's
alternates that cut with keeping only the states from which, under zero
input, the reader can force the flush without leaving the set, until
neither cut removes a state.

The script's c_int agrees at all 144 cells of its grid (six periodic α,
×2 … ×5, six slacks) with a second, independent computation over the
quadratic field of α with a larger box, whose table flush.py carries,
and every winning strategy writes the right value under the output
caps and ends, for every n < 1000. Solved at twice the box, the
flushing branches of the reader of ×2 at s = s₀ = 1 over the quotient
alphabet {1, 2} (the universal reader below) never leave the box
itself, over the alphabet's two constant members and four random ones
and every n < 250: at most (4, 2) against (10, 6).

## The completion reader is the safety game
Tier: theorem.
Verifier: proof; flush.py::section_completion; flush.py::section_grid;
flush.py::section_band.

At every periodic α and over every finite quotient alphabet, with
s₀ ≤ s + 1, the completion reader's least lookahead c_comp equals c_saf
at ω = 0.
So tracking the lifts costs no lookahead, and c_int − c_comp is the
flush's price alone. The lifts are these integer differences: the fibre
of R over R/Z, which the circle carries, and not n mod m, which
OSTROWSKI.md proves no tile carries and which stays floor division's.

Proof. In a safe play the set of branches is never empty, each branch
has one parent, and the box holds finitely many. By König's lemma one
lineage runs forever. Its σ_t obeys |σ_t| ≤ B_g|θ_t| + B_h|θ_(t−1)|,
which tends to 0, so the output codes mx + M for that lineage's lift: a
safe reader is a completion reader. A completion reader's own lift is a
true branch, inside the box by the lift game's bound, so the reader
plays safe. It may use its whole history, but the states it visits are
closed under its moves and so lie in the greatest fixed point: the
positional game is won too. The width of the box above that bound is
irrelevant.

The script tracks the overlap reader's own lift in the game's frame over
its 36,000 runs, with A the largest of a₁ … a₄₁, the quotients its
tracked times 0 … 40 use (at the fractional part of Euler's number the
box is not defined over the whole expansion): it uses at most 0.92 of
B_g and 0.42 of B_h. It finds c_saf ≤ c_ov at every cell, and c_saf
unchanged at twice the box at four cells.

## The flush floor
Tier: theorem.
Verifier: proof; flush.py::section_digitwise; flush.py::section_grid.

Let m ≥ 2. If s ≥ (m − 1) a_(k+1) at every k ≥ 1, the integer reader
reads at lookahead 0, whatever s₀. If (m − 1) a_(k+1) > s and m
a_(k+1) < q_(k−1) at infinitely many k, it reads at no lookahead below
2. So at a purely periodic α with largest quotient A, c_int is 0 when
s ≥ (m − 1)A and at least 2 otherwise, and never 1.

Proof. For the first half the reader writes e₀ = m d₀ mod a₁, e₁ = m
d₁ + ⌊m d₀/a₁⌋ and e_k = m d_k beyond, a function of the digits seen at
lookahead 0 with value mn, since q₁ = a₁. The output caps hold: d₀ ≥ 1
forces d₁ ≤ a₂ − 1, so e₁ ≤ m a₂ − 1. For the second, take a reader at
lookahead c ≤ 1, an integer n, and k with n's digits all below
position k − 1 and past the position where the reader has written the
whole of mn. On
n′ = n + a_(k+1) q_k it writes the same prefix, having seen the same
digits, and it owes exactly m a_(k+1) q_k, from level k − c ≥ k − 1.
Write q_(k+j) = U_j q_k + V_j q_(k−1) with V_j ≥ 1. A string of value m
a_(k+1) q_k from level k − 1 has m a_(k+1) q_k = X q_k + Y q_(k−1) with
Y = e_(k−1) + Σ_(j≥1) e_(k+j) V_j, so q_k divides Y. Y ≥ q_k would force
m a_(k+1) ≥ q_(k−1), so Y = 0 and the only string is e_k = m a_(k+1),
over its output cap a_(k+1) + s. The overflow could only spill down,
q_k = a_k q_(k−1) + q_(k−2), into two levels of which a reader at
lookahead 1 has
already written the lower and one at lookahead 0 both.

Over the grid the script finds c_int = 0 exactly where s ≥ (m − 1)A
and 2 or more elsewhere, never 1. c_int − c_saf is 0 at 91 of the 120
finite cells, 1 at 28 and 2 at one ([1, 1, 1, 2] ×3 at s = s₀ = 3,
where c_saf = 0). At four cells beyond the grid, [4] and [5] ×2 at
s = s₀ = 3, and [4] and bronze ×3 at 5, c_ov = 1 and c_int = 2:
the completion reader reads at 1 and the integer reader cannot. The
first half's reader (flush.py's digitwise reader) is correct at every α
of the grid, ×2 … ×5 and n < 1000, at s = (m − 1)A with s₀ = 0, and m
a_(k+1) q_k has one
string from level k − 1 at every phase.

## The universal reader
Tier: rule (the finite game solved exhaustively at the cells below).
Verifier: flush.py::section_universal.

Over the alphabet {1, …, A} the lift game with the opponent choosing
each quotient is one finite game, and a win is a reader that sees the
quotients through a_(t+c+1) and nothing else of α, correct at every α
with quotients at most A.

×2 at s = s₀ = 1 reads at exactly 2 over {1, 2} and over {1, 2, 3}. ×3
at s = s₀ = 1 reads at exactly 3 over {1, 2}, although all 472 purely
periodic α of primitive period at most 8 in that class read it at 2: an
opponent free to switch quotients costs one digit that no periodic α of
period at most 8 charges. ×3 at s = s₀ = 2 reads at 2 over {1, 2}. Each
win is certified on every n < 500 at the class's constant members and
twelve random ones. The reader is a tool: flush.py's
Game(Source(alphabet = (1, 2, 3)), m = 2, s = 1, s0 = 1, look = 2), once
solved, reads a greedy string at any such α, given its quotients far
enough, through its read method, which reports whether it flushed.

## Open fronts

At unbounded quotients the lift game's box grows with the largest
quotient, so the construction gives no finite game, and the integer
reader's least lookahead is not read. The flush floor puts it at 2 or
more wherever (m − 1) a_(k+1) > s and m a_(k+1) < q_(k−1) at infinitely
many k; whether it is finite there at all is open.
