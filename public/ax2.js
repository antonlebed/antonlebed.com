// ax2.js — .ax v2.0 CRT-Native Runtime
// Phase R of the .ax Revolution (S537). Runs alongside ax.js (v1).
// Every value IS its CRT decomposition. Channel access is O(1).
// L=11 ECC checking is built into every operation.
// 970200 = 2^3 * 3^2 * 5^2 * 7^2 * 11 = TRUE FORM

const AX2 = (function() {
'use strict';

// ================================================================
//  CRT Constants (TRUE FORM)
// ================================================================
const N = 970200;
const MODS = [8, 9, 25, 49, 11];  // D^3, K^2, E^2, b^2, L
const CH = { D:0, K:1, E:2, b:3, L:4 };
const CH_NAMES = ['D', 'K', 'E', 'b', 'L'];

// CRT basis elements: ei has 1 in channel i, 0 elsewhere
// Precomputed: ei = (N/mi) * inverse(N/mi, mi) mod N
const BASIS = [363825, 431200, 853776, 732600, 529200];

// ================================================================
//  CRT Value Type
// ================================================================
// A value is a 5-element Int32Array: [mod8, mod9, mod25, mod49, mod11]
// Reconstruction to integer is done on demand.

function fromInt(n) {
    n = Math.round(n);
    const r = ((n % N) + N) % N;
    return new Int32Array([r % 8, r % 9, r % 25, r % 49, r % 11]);
}

function toInt(v) {
    // CRT reconstruction: x = sum(v[i] * BASIS[i]) mod N
    let x = 0;
    for (let i = 0; i < 5; i++) x = (x + v[i] * BASIS[i]) % N;
    return ((x % N) + N) % N;
}

function fromChannels(d, k, e, b, l) {
    return new Int32Array([
        ((d % 8) + 8) % 8,
        ((k % 9) + 9) % 9,
        ((e % 25) + 25) % 25,
        ((b % 49) + 49) % 49,
        ((l % 11) + 11) % 11
    ]);
}

// ================================================================
//  CRT Arithmetic (per-channel, the Loop Theorem in action)
// ================================================================
function add(a, b) {
    return new Int32Array([
        (a[0] + b[0]) % 8,
        (a[1] + b[1]) % 9,
        (a[2] + b[2]) % 25,
        (a[3] + b[3]) % 49,
        (a[4] + b[4]) % 11
    ]);
}

function sub(a, b) {
    return new Int32Array([
        (a[0] - b[0] + 8) % 8,
        (a[1] - b[1] + 9) % 9,
        (a[2] - b[2] + 25) % 25,
        (a[3] - b[3] + 49) % 49,
        (a[4] - b[4] + 11) % 11
    ]);
}

function mul(a, b) {
    return new Int32Array([
        (a[0] * b[0]) % 8,
        (a[1] * b[1]) % 9,
        (a[2] * b[2]) % 25,
        (a[3] * b[3]) % 49,
        (a[4] * b[4]) % 11
    ]);
}

function neg(a) {
    return new Int32Array([
        (8 - a[0]) % 8,
        (9 - a[1]) % 9,
        (25 - a[2]) % 25,
        (49 - a[3]) % 49,
        (11 - a[4]) % 11
    ]);
}

function eq(a, b) {
    return a[0]===b[0] && a[1]===b[1] && a[2]===b[2] && a[3]===b[3] && a[4]===b[4];
}

function modpow(base, exp) {
    // Per-channel modular exponentiation
    exp = Math.round(exp);
    if (exp < 0) return fromInt(0);
    const r = new Int32Array(5);
    for (let i = 0; i < 5; i++) {
        let b = base[i], result = 1, e = exp, m = MODS[i];
        b = ((b % m) + m) % m;
        while (e > 0) {
            if (e & 1) result = (result * b) % m;
            e >>= 1;
            b = (b * b) % m;
        }
        r[i] = result;
    }
    return r;
}

// ================================================================
//  ECC (L=11 Guardian)
// ================================================================
function eccExpected(a, b, op) {
    // Compute what L channel SHOULD be after operation
    switch (op) {
        case '+': return (a[4] + b[4]) % 11;
        case '-': return (a[4] - b[4] + 11) % 11;
        case '*': return (a[4] * b[4]) % 11;
    }
    return -1;
}

function eccCheck(result, expected) {
    return result[4] === expected;
}

// ================================================================
//  GCD + Coupling (ring fundamentals)
// ================================================================
function gcd(a, b) {
    a = Math.abs(a); b = Math.abs(b);
    while (b) { [a, b] = [b, a % b]; }
    return a;
}

function coupling(v) {
    const n = toInt(v);
    return fromInt(N / gcd(n, N));
}

function eigenvalue(v) {
    const P = Math.PI;
    let sum = 0;
    for (let i = 0; i < 5; i++) sum += (MODS[i] <= 2 ? 1 : 2) * Math.cos(2 * P * v[i] / MODS[i]);
    return sum;
}

// ================================================================
//  Decality Constants (10 terms — the full vocabulary)
// ================================================================
const DECALITY = {
    mirror: neg(fromInt(1)),           // -1 = N-1
    o:      fromInt(0),                // void, absorber
    s:      fromInt(1),                // sigma, ground state
    D:      fromInt(2),                // duality
    K:      fromInt(3),                // closure
    E:      fromInt(5),                // observer
    b:      fromInt(7),                // depth
    L:      fromInt(11),               // protector
    GATE:   fromInt(13),               // boundary
    OMEGA:  fromInt(606376),           // terminal projector
    // Named constants
    DATA:   fromInt(210),
    THIN:   fromInt(2310),
    TRUE:   fromInt(970200),
    HYDOR:  fromInt(105),
    KEY:    fromInt(41),
    ANSWER: fromInt(42),
    SOUL:   fromInt(67),
    ADDRESS:fromInt(137),
    LAMBDA: fromInt(420),
    ME:     fromInt(18),
    THORNS: fromInt(28),
    ESCAPE: fromInt(17),
    GATE_FORM: fromInt(12612600 % N),  // 12612600 mod 970200 = 12612600 - 13*970200
};

// ================================================================
//  Tokenizer (simplified from v1 — same core, less grid sugar)
// ================================================================
const KEYWORDS = new Set(['let','fn','show','if','then','else','for','in','do','while','mut','match','end']);

function tokenize(src) {
    const T = [];
    let i = 0, line = 1;
    const pk = (tok) => { tok.line = line; T.push(tok); };
    while (i < src.length) {
        if (/\s/.test(src[i])) { if (src[i] === '\n') line++; i++; continue; }
        if (src[i] === '-' && src[i+1] === '-') { while (i < src.length && src[i] !== '\n') i++; continue; }
        if (src[i] === '/' && src[i+1] === '*') { i += 2; while (i < src.length - 1 && !(src[i] === '*' && src[i+1] === '/')) { if (src[i] === '\n') line++; i++; } i += 2; continue; }
        if (/\d/.test(src[i])) {
            let num = '';
            while (i < src.length && /[\d.]/.test(src[i])) {
                // Don't consume '.' if followed by a channel name (D,K,E,b,L)
                if (src[i] === '.' && /[DKEbL]/.test(src[i+1]) && !/[\da-zA-Z_]/.test(src[i+2]||'')) break;
                num += src[i++];
            }
            pk({t:'NUM', v:parseFloat(num)}); continue;
        }
        if (src[i] === '"') {
            i++; let s = '', parts = [], hasInterp = false;
            while (i < src.length && src[i] !== '"') {
                if (src[i] === '$' && i + 1 < src.length && src[i+1] === '{') {
                    hasInterp = true;
                    if (s) parts.push({k:'s', v:s});
                    s = ''; i += 2;
                    let depth = 1, expr = '';
                    while (i < src.length && depth > 0) {
                        if (src[i] === '{') depth++;
                        else if (src[i] === '}') { depth--; if (depth === 0) { i++; break; } }
                        if (src[i] === '\n') line++;
                        expr += src[i++];
                    }
                    parts.push({k:'e', v:expr});
                } else {
                    if (src[i] === '\n') line++;
                    s += src[i++];
                }
            }
            if (i < src.length) i++;
            if (!hasInterp) { pk({t:'STR', v:s}); }
            else { if (s) parts.push({k:'s', v:s}); pk({t:'TEMPLATE', parts}); }
            continue;
        }
        if (/[a-zA-Z_]/.test(src[i])) {
            let id = '';
            while (i < src.length && /[a-zA-Z0-9_]/.test(src[i])) id += src[i++];
            pk({t: KEYWORDS.has(id) ? id.toUpperCase() : 'ID', v:id}); continue;
        }
        if (src[i] === '=' && src[i+1] === '=') { pk({t:'=='}); i+=2; continue; }
        if (src[i] === '=' && src[i+1] === '>') { pk({t:'=>'}); i+=2; continue; }
        if (src[i] === '!' && src[i+1] === '=') { pk({t:'!='}); i+=2; continue; }
        if (src[i] === '|' && src[i+1] === '>') { pk({t:'|>'}); i+=2; continue; }
        if (src[i] === '<' && src[i+1] === '=') { pk({t:'<='}); i+=2; continue; }
        if (src[i] === '>' && src[i+1] === '=') { pk({t:'>='}); i+=2; continue; }
        if (src[i] === '.') { pk({t:'.'}); i++; continue; }
        const ch = src[i];
        if ('+-*/^%<>=()[]|,;'.includes(ch)) { pk({t:ch}); i++; continue; }
        i++;
    }
    pk({t:'EOF'});
    return T;
}

// ================================================================
//  Parser (outputs AST nodes)
// ================================================================
class Parser {
    constructor(tokens) { this.T = tokens; this.p = 0; }
    pk() { return this.T[this.p]; }
    adv() { return this.T[this.p++]; }
    expect(t) {
        const tok = this.adv();
        if (tok.t !== t) throw new Error('Line ' + (tok.line||'?') + ': expected ' + t + ', got ' + tok.t + (tok.v !== undefined ? ' (' + tok.v + ')' : ''));
        return tok;
    }
    match(t) { if (this.pk().t === t) { this.adv(); return true; } return false; }

    parseProgram() {
        const stmts = [];
        while (this.pk().t !== 'EOF') {
            while (this.pk().t === ';') this.adv();  // skip statement separators
            if (this.pk().t === 'EOF') break;
            stmts.push(this.parseStmt());
        }
        return stmts;
    }

    parseStmt() {
        if (this.pk().t === 'LET') return this.parseLet();
        if (this.pk().t === 'MUT') return this.parseSet();
        if (this.pk().t === 'FN') return this.parseFn();
        if (this.pk().t === 'SHOW') { this.adv(); return {t:'Show', expr:this.parseExpr()}; }
        return {t:'ExprStmt', expr:this.parseExpr()};
    }

    parseLet() {
        this.expect('LET');
        const name = this.expect('ID').v;
        this.expect('=');
        // Statement-level let: parse full expression but NOT ; (seq is for statement separation)
        return {t:'Let', name, val:this.parseExprNoSeq()};
    }

    parseSet() {
        this.expect('MUT');
        const name = this.expect('ID').v;
        this.expect('=');
        return {t:'Set', name, val:this.parseExprNoSeq()};
    }

    // Like parseExpr but stops before ; — used for statement-level let/set/fn
    parseExprNoSeq() {
        if (this.pk().t === 'IF') return this.parseIf();
        if (this.pk().t === 'LET') return this.parseLetExpr();
        if (this.pk().t === 'MUT') return this.parseSetExpr();
        if (this.pk().t === 'FOR') return this.parseFor();
        if (this.pk().t === 'WHILE') return this.parseWhile();
        if (this.pk().t === 'MATCH') return this.parseMatch();
        if (this.pk().t === 'SHOW') { this.adv(); return {t:'Call', fn:'show', args:[this.parsePipe()]}; }
        return this.parsePipe();
    }

    parseFn() {
        this.expect('FN');
        const name = this.expect('ID').v;
        this.expect('(');
        const params = [];
        if (this.pk().t !== ')') {
            params.push(this.expect('ID').v);
            while (this.match(',')) params.push(this.expect('ID').v);
        }
        this.expect(')');
        this.expect('=');
        return {t:'Fn', name, params, body:this.parseExpr()};
    }

    parseExpr() {
        // ALL constructs fall through to ';' check — no early returns.
        // This lets while/for/let/if be followed by ; to form sequences.
        let left;
        if (this.pk().t === 'IF') left = this.parseIf();
        else if (this.pk().t === 'LET') left = this.parseLetExpr();
        else if (this.pk().t === 'FOR') left = this.parseFor();
        else if (this.pk().t === 'WHILE') left = this.parseWhile();
        else if (this.pk().t === 'MATCH') left = this.parseMatch();
        else if (this.pk().t === 'MUT') left = this.parseSetExpr();
        else if (this.pk().t === 'SHOW') { this.adv(); left = {t:'Call', fn:'show', args:[this.parsePipe()]}; }
        else left = this.parsePipe();
        while (this.pk().t === ';') {
            // Stop before FN: fn is statement-only, never valid inside a sequence.
            // This prevents fn bodies from consuming the next fn definition.
            const next = this.T[this.p + 1];
            if (next && next.t === 'FN') break;
            this.adv(); left = {t:'Seq', a:left, b:this.parseExpr()};
        }
        return left;
    }

    parsePipe() {
        let left = this.parseCmp();
        while (this.pk().t === '|>') {
            this.adv();
            // Right side: fn_name or fn_name(args...)
            const tok = this.pk();
            if (tok.t === 'ID') {
                const name = this.adv().v;
                if (this.pk().t === '(') {
                    // |> fn(extra_args) => fn(left, extra_args)
                    this.adv();
                    const args = [{t:'_pipe_val_', val:left}];
                    if (this.pk().t !== ')') {
                        args.push(this.parseExpr());
                        while (this.match(',')) args.push(this.parseExpr());
                    }
                    this.expect(')');
                    left = {t:'Pipe', fn:name, args, line:tok.line};
                } else {
                    // |> fn => fn(left)
                    left = {t:'Pipe', fn:name, args:[{t:'_pipe_val_', val:left}], line:tok.line};
                }
            } else {
                throw new Error('Line ' + (this.pk().line||'?') + ': expected function name after |>');
            }
        }
        return left;
    }

    parseIf() {
        this.expect('IF'); const cond = this.parseExpr();
        this.expect('THEN'); const then_ = this.parseExprNoSeq();
        // else is optional: bare `if cond then expr` returns void when false
        if (this.pk().t === 'ELSE') {
            this.adv();
            return {t:'If', cond, then_, else_:this.parseExprNoSeq()};
        }
        return {t:'If', cond, then_, else_:{t:'Num', v:0}};
    }

    parseSetExpr() {
        this.expect('MUT'); const name = this.expect('ID').v;
        this.expect('='); const val = this.parseExprNoSeq();
        // mut as expression: evaluates val, updates name in scope, returns val
        // Stops before ; so sequences work: mut x = x+1; mut y = y+1
        return {t:'SetExpr', name, val};
    }

    parseLetExpr() {
        this.expect('LET'); const name = this.expect('ID').v;
        this.expect('='); const val = this.parseExprNoSeq();
        // Accept 'in' or ';' as body separator; ';' fixes let inside (...) blocks
        if (this.pk().t === 'IN' || this.pk().t === ';') this.adv();
        // If no valid body start, return val via the name binding
        const pk = this.pk().t;
        if (pk === ')' || pk === 'EOF' || pk === ']') return {t:'LetExpr', name, val, body:{t:'Var', name}};
        return {t:'LetExpr', name, val, body:this.parseExpr()};
    }

    parseFor() {
        this.expect('FOR'); const v = this.expect('ID').v;
        this.expect('IN'); const iter = this.parseCmp();
        // `do` keyword optional: `for i in range(n) (body)` infers do
        if (this.pk().t === 'DO') this.adv();
        return {t:'For', v, iter, body:this.parseExprNoSeq()};
    }

    parseWhile() {
        this.expect('WHILE'); const cond = this.parseCmp();
        // `do` keyword optional: `while cond (body)` infers do
        if (this.pk().t === 'DO') this.adv();
        return {t:'While', cond, body:this.parseExprNoSeq()};
    }

    parseMatch() {
        this.expect('MATCH');
        const expr = this.parsePipe();  // scrutinee (stop before |)
        const arms = [];
        while (this.pk().t === '|') {
            this.adv();  // consume |
            let pattern;
            if (this.pk().t === 'ID' && this.pk().v === '_') {
                this.adv();
                pattern = {t: 'Wildcard'};
            } else {
                pattern = this.parsePipe();  // pattern = evaluated expression
            }
            this.expect('=>');
            const body = this.parseExpr();  // arm body (naturally stops at | or END)
            arms.push({pattern, body});
        }
        this.expect('END');
        return {t:'Match', expr, arms};
    }

    parseCmp() {
        let left = this.parseAdd();
        while (['<','>','==','!=','<=','>='].includes(this.pk().t)) {
            const op = this.adv().t;
            left = {t:'Bin', op, l:left, r:this.parseAdd()};
        }
        return left;
    }

    parseAdd() {
        let left = this.parseMul();
        while (['+','-'].includes(this.pk().t)) {
            const op = this.adv().t;
            left = {t:'Bin', op, l:left, r:this.parseMul()};
        }
        return left;
    }

    parseMul() {
        let left = this.parsePow();
        while (['*','/','%'].includes(this.pk().t)) {
            const op = this.adv().t;
            left = {t:'Bin', op, l:left, r:this.parsePow()};
        }
        return left;
    }

    parsePow() {
        let left = this.parseUnary();
        if (this.pk().t === '^') { this.adv(); left = {t:'Bin', op:'^', l:left, r:this.parseUnary()}; }
        return left;
    }

    parseUnary() {
        if (this.pk().t === '-') { this.adv(); return {t:'Neg', e:this.parseUnary()}; }
        return this.parsePostfix();
    }

    parsePostfix() {
        let e = this.parsePrimary();
        while (true) {
            if (this.pk().t === '.') {
                this.adv();
                const ch = this.expect('ID').v;
                e = {t:'ChAccess', e, ch, line:this.T[this.p-1].line};  // Channel access: expr.D, expr.K, etc.
            } else if (this.pk().t === '[') {
                this.adv(); const idx = this.parseExpr(); this.expect(']');
                e = {t:'Idx', arr:e, idx};
            } else break;
        }
        return e;
    }

    parsePrimary() {
        const tok = this.pk();
        if (tok.t === 'NUM') { this.adv(); return {t:'Num', v:tok.v}; }
        if (tok.t === 'STR') { this.adv(); return {t:'Str', v:tok.v}; }
        if (tok.t === 'TEMPLATE') {
            this.adv();
            let node = null;
            for (const part of tok.parts) {
                let pNode;
                if (part.k === 's') { pNode = {t:'Str', v:part.v}; }
                else { const sub = new Parser(tokenize(part.v)); pNode = sub.parseExpr(); }
                if (!node) node = pNode;
                else node = {t:'Bin', op:'+', l:node, r:pNode};
            }
            return node || {t:'Str', v:''};
        }
        if (tok.t === 'ID') {
            this.adv();
            if (this.pk().t === '(') {
                this.adv();
                const args = [];
                if (this.pk().t !== ')') {
                    args.push(this.parseExpr());
                    while (this.match(',')) args.push(this.parseExpr());
                }
                this.expect(')');
                return {t:'Call', fn:tok.v, args, line:tok.line};
            }
            return {t:'Sym', name:tok.v, line:tok.line};
        }
        if (tok.t === '(') { this.adv(); const e = this.parseExpr(); this.expect(')'); return e; }
        if (tok.t === '[') {
            this.adv();
            const elems = [];
            if (this.pk().t !== ']') {
                elems.push(this.parseExpr());
                while (this.match(',')) elems.push(this.parseExpr());
            }
            this.expect(']');
            return {t:'Arr', elems};
        }
        throw new Error('Line ' + (tok.line||'?') + ': unexpected ' + tok.t + (tok.v !== undefined ? ' (' + tok.v + ')' : ''));
    }
}

// ================================================================
//  Builtins (minimal — most moves to stdlib.ax)
// ================================================================
const BUILTINS = {};
BUILTINS.coupling = (args) => coupling(args[0]);
BUILTINS.crt = (args) => Array.from(args[0]);  // CRT is just reading the tuple
BUILTINS.eigenvalue = (args) => eigenvalue(args[0]);
BUILTINS.shadow_poly = (args) => {
    // P(x) = (x-1)(x-2)(x-3)(x-5) — the spectral architect
    const one = fromInt(1), two = fromInt(2), three = fromInt(3), five = fromInt(5);
    return mul(mul(sub(args[0], one), sub(args[0], two)), mul(sub(args[0], three), sub(args[0], five)));
};
BUILTINS.depth_quad = (args) => {
    // f(n) = n^2 - n - 1 (the depth quadratic)
    return sub(sub(mul(args[0], args[0]), args[0]), fromInt(1));
};
BUILTINS.is_smooth = (args) => {
    // is_smooth(n) -> 1 if n is 11-smooth (all prime factors <= 11), else 0
    let n = Math.abs(toInt(args[0]));
    if (n <= 1) return fromInt(1);
    const primes = [2, 3, 5, 7, 11];
    for (const p of primes) { while (n % p === 0) n = Math.floor(n / p); }
    return fromInt(n === 1 ? 1 : 0);
};
BUILTINS.golden_roots = (args) => {
    // golden_roots(q) -> [r1, r2] roots of f(n)=n^2-n-1 mod q
    const q = toInt(args[0]);
    if (q <= 1) return [fromInt(0), fromInt(0)];
    let s = -1;
    for (let i = 0; i < q; i++) { if ((i * i) % q === ((5 % q) + q) % q) { s = i; break; } }
    if (s < 0) return [fromInt(-1), fromInt(-1)]; // 5 is QNR mod q
    let inv2 = -1;
    for (let j = 0; j < q; j++) { if ((2 * j) % q === 1) { inv2 = j; break; } }
    if (inv2 < 0) { return [fromInt((1 + s) % q), fromInt((1 + q - s) % q)]; }
    return [fromInt(((1 + s) * inv2) % q), fromInt(((1 + q - s) * inv2) % q)];
};
BUILTINS.golden_norm = (args) => {
    // Q(a,b) = a^2 + 3ab + b^2 (golden norm form, disc=5=E)
    const a = toInt(args[0]), b = toInt(args[1]);
    return fromInt(a*a + 3*a*b + b*b);
};
BUILTINS.eisenstein_norm = (args) => {
    // E_3(a,b) = a^2 - ab + b^2 (Eisenstein norm, disc=-3=-K)
    const a = toInt(args[0]), b = toInt(args[1]);
    return fromInt(a*a - a*b + b*b);
};
BUILTINS.gaussian_norm = (args) => {
    // G(a,b) = a^2 + b^2 (Gaussian norm, disc=-4=-D^2)
    const a = toInt(args[0]), b = toInt(args[1]);
    return fromInt(a*a + b*b);
};
BUILTINS.factorize = (args) => {
    // factorize(n) -> flat array [p1, e1, p2, e2, ...] (works on plain integers)
    let n = toInt(args[0]);
    if (n < 0) n = -n;
    if (n <= 1) return [];
    const factors = [];
    for (let p = 2; p * p <= n; p++) {
        let e = 0;
        while (n % p === 0) { n = Math.floor(n / p); e++; }
        if (e > 0) { factors.push(fromInt(p)); factors.push(fromInt(e)); }
    }
    if (n > 1) { factors.push(fromInt(n)); factors.push(fromInt(1)); }
    return factors;
};
BUILTINS.sigma3 = (args) => {
    let n = toInt(args[0]);
    if (n < 0) n = -n;
    if (n === 0) return fromInt(0);
    let s = 0;
    for (let d = 1; d <= n; d++) {
        if (n % d === 0) s += d * d * d;
    }
    return fromInt(s);
};
BUILTINS.mirror = (args) => neg(args[0]);
BUILTINS.gcd = (args) => fromInt(gcd(toInt(args[0]), toInt(args[1])));
BUILTINS.toInt = (args) => toInt(args[0]);  // explicit reconstruction
BUILTINS.bloom = (args) => {
    // bloom(d, k, e, b, l) — CRT reconstruct from channel values
    return fromChannels(
        Math.round(toInt(args[0])),
        Math.round(toInt(args[1])),
        Math.round(toInt(args[2])),
        Math.round(toInt(args[3])),
        Math.round(toInt(args[4]))
    );
};
BUILTINS.ecc = (args) => {
    // ecc(val) — check if L channel is consistent with data channels
    // Returns 1 if consistent, 0 if violated
    const v = args[0];
    const n = toInt(v);
    return fromInt(n % 11 === v[4] ? 1 : 0);
};
BUILTINS.len = (args) => {
    const v = args[0];
    if (typeof v === 'string') return fromInt(v.length);
    if (Array.isArray(v)) return fromInt(v.length);
    return fromInt(0);
};
BUILTINS.range = (args) => {
    const n = Math.min(Math.max(0, toInt(args[0])), 10000);
    return Array.from({length: n}, (_, i) => fromInt(i));
};
BUILTINS.cos = (args) => eigenvalue(args[0]);  // cos IS eigenvalue in the ring
BUILTINS.ev_rank = (args) => {
    // Eigenvalue as comparable integer: round((eigenvalue + 10) * 10000)
    // Maps [-10, 10] -> [0, 200000]. Monotonic. Safe for < > == comparison.
    const ev = eigenvalue(args[0]);
    return fromInt(Math.round((ev + 10) * 10000));
};

// Phase S builtins — ring operations that require N (can't be .ax stdlib)
BUILTINS.inv = (args) => {
    const n = toInt(args[0]);
    const g = gcd(n, N);
    if (g !== 1) return fromInt(0);  // non-unit: no inverse
    let [old_r, r] = [n, N], [old_s, s] = [1, 0];
    while (r !== 0) {
        const q = Math.floor(old_r / r);
        [old_r, r] = [r, old_r - q * r];
        [old_s, s] = [s, old_s - q * s];
    }
    return fromInt(((old_s % N) + N) % N);
};

BUILTINS.phi = (args) => {
    let n = Math.abs(toInt(args[0]));
    if (n === 0) return fromInt(0);
    let result = n;
    let m = n;
    for (let p = 2; p * p <= m; p++) {
        if (m % p === 0) {
            while (m % p === 0) m /= p;
            result -= result / p;
        }
    }
    if (m > 1) result -= result / m;
    return fromInt(Math.round(result));
};

BUILTINS.order = (args) => {
    const v = args[0];
    const n = toInt(v);
    if (gcd(n, N) !== 1) return fromInt(0);  // non-units have no multiplicative order
    let power = v;
    for (let k = 1; k <= 420; k++) {  // lambda(TRUE) = 420
        if (eq(power, DECALITY.s)) return fromInt(k);
        power = mul(power, v);
    }
    return fromInt(0);
};

BUILTINS.kingdom = (args) => {
    const n = toInt(args[0]);
    if (n === 0) return fromInt(0);  // void
    const g = gcd(n, N);
    if (g === 1) return fromInt(1);   // sigma (units)
    if (g % 2 === 0) return fromInt(2);   // D
    if (g % 3 === 0) return fromInt(3);   // K
    if (g % 5 === 0) return fromInt(5);   // E
    if (g % 7 === 0) return fromInt(7);   // b
    if (g % 11 === 0) return fromInt(11); // L
    return fromInt(0);
};

BUILTINS.abs = (args) => {
    const n = toInt(args[0]);
    return fromInt(Math.min(n, N - n));
};

BUILTINS.sqrt = (args) => fromInt(Math.floor(Math.sqrt(toInt(args[0]))));

BUILTINS.sum = (args) => {
    if (!Array.isArray(args[0])) return fromInt(0);
    let s = fromInt(0);
    for (const item of args[0]) s = add(s, item);
    return s;
};

BUILTINS.product = (args) => {
    if (!Array.isArray(args[0])) return fromInt(1);
    let p = fromInt(1);
    for (const item of args[0]) p = mul(p, item);
    return p;
};

BUILTINS.min = (args) => fromInt(Math.min(toInt(args[0]), toInt(args[1])));
BUILTINS.max = (args) => fromInt(Math.max(toInt(args[0]), toInt(args[1])));

BUILTINS.rand = (args) => fromInt(Math.floor(Math.random() * Math.max(1, Math.abs(toInt(args[0])))));
BUILTINS.push = (args) => {
    // push(array, element) — returns new array with element appended
    if (!Array.isArray(args[0])) throw new Error('push: expected array');
    return [...args[0], args[1]];
};
BUILTINS.set = function(args) {
    // set(array, index, value) — mutates array[index] in place, returns value
    if (Array.isArray(args[0])) { const i = toInt(args[1]); if (i >= 0 && i < args[0].length) args[0][i] = args[2]; }
    return args[2];
};
BUILTINS.first = (args) => {
    if (!Array.isArray(args[0])) return fromInt(0);
    for (const item of args[0]) {
        if (ArrayBuffer.isView(item) && toInt(item) !== 0) return item;
    }
    return fromInt(0);
};

BUILTINS.exp = (args) => {
    let x = toInt(args[0]);
    if (x > N / 2) x = x - N;  // interpret large values as negative (signed)
    if (x > 13) return fromInt(N - 1);  // overflow: e^14 > N
    if (x < -20) return fromInt(0);  // underflow: e^-20 ~ 0
    return fromInt(Math.round(Math.exp(x)));
};
BUILTINS.log = (args) => {
    const n = toInt(args[0]);
    return fromInt(n > 0 ? Math.round(Math.log(n)) : 0);
};
BUILTINS.argmax = (args) => {
    if (!Array.isArray(args[0])) return fromInt(0);
    let best = -Infinity, bestI = 0;
    for (let i = 0; i < args[0].length; i++) {
        const v = ArrayBuffer.isView(args[0][i]) ? toInt(args[0][i]) : Number(args[0][i]);
        if (v > best) { best = v; bestI = i; }
    }
    return fromInt(bestI);
};

// String primitives (Arc 1: OUROBOROS — self-hosting needs source code manipulation)
BUILTINS.charAt = (args) => {
    const s = args[0];
    if (typeof s !== 'string') throw new Error('charAt: expected string');
    const idx = toInt(args[1]);
    if (idx < 0 || idx >= s.length) return '';
    return s[idx];
};
BUILTINS.charCode = (args) => {
    const s = args[0];
    if (typeof s !== 'string') throw new Error('charCode: expected string');
    const idx = args.length > 1 ? toInt(args[1]) : 0;
    if (idx < 0 || idx >= s.length) return fromInt(0);
    return fromInt(s.charCodeAt(idx));
};
BUILTINS.fromCharCode = (args) => String.fromCharCode(toInt(args[0]));
BUILTINS.substr = (args) => {
    const s = args[0];
    if (typeof s !== 'string') throw new Error('substr: expected string');
    const start = toInt(args[1]);
    const len = args.length > 2 ? toInt(args[2]) : s.length - start;
    return s.substring(start, start + len);
};
BUILTINS.strFind = (args) => {
    // strFind(haystack, needle) — returns index or -1 (as N-1 in ring)
    const s = args[0], needle = args[1];
    if (typeof s !== 'string' || typeof needle !== 'string') return fromInt(0);
    const idx = s.indexOf(needle);
    return fromInt(idx >= 0 ? idx : N - 1);  // N-1 = -1 in the ring
};

BUILTINS.show = null;  // handled in evaluator

// ================================================================
//  Phase F: Float math builtins (S625 — temporary JS Math.* bridge)
//  Returns raw JS numbers (typeof === 'number'). Binary ops propagate floats.
//  The PYTHON KILLER: once .ax has floats, CRT diffusion training moves to .ax.
//  Step 2 (future): .ax-native float via Taylor series in CRT arithmetic.
// ================================================================
BUILTINS.toFloat = (args) => {
    const v = args[0];
    if (typeof v === 'number') return v;
    if (ArrayBuffer.isView(v)) return toInt(v);
    if (Array.isArray(v)) return v.length;
    return 0;
};
BUILTINS.exp_f = (args) => {
    const x = typeof args[0] === 'number' ? args[0] : toInt(args[0]);
    return Math.exp(x);
};
BUILTINS.log_f = (args) => {
    const x = typeof args[0] === 'number' ? args[0] : toInt(args[0]);
    return x > 0 ? Math.log(x) : -Infinity;
};
BUILTINS.log2_f = (args) => {
    const x = typeof args[0] === 'number' ? args[0] : toInt(args[0]);
    return x > 0 ? Math.log2(x) : -Infinity;
};
BUILTINS.log10_f = (args) => {
    const x = typeof args[0] === 'number' ? args[0] : toInt(args[0]);
    return x > 0 ? Math.log10(x) : -Infinity;
};
BUILTINS.pow_f = (args) => {
    const base = typeof args[0] === 'number' ? args[0] : toInt(args[0]);
    const exp = typeof args[1] === 'number' ? args[1] : toInt(args[1]);
    return Math.pow(base, exp);
};
BUILTINS.sqrt_f = (args) => {
    const x = typeof args[0] === 'number' ? args[0] : toInt(args[0]);
    return Math.sqrt(x);
};
BUILTINS.sin_f = (args) => {
    const x = typeof args[0] === 'number' ? args[0] : toInt(args[0]);
    return Math.sin(x);
};
BUILTINS.cos_f = (args) => {
    const x = typeof args[0] === 'number' ? args[0] : toInt(args[0]);
    return Math.cos(x);
};
BUILTINS.tan_f = (args) => {
    const x = typeof args[0] === 'number' ? args[0] : toInt(args[0]);
    return Math.tan(x);
};
BUILTINS.abs_f = (args) => {
    const x = typeof args[0] === 'number' ? args[0] : toInt(args[0]);
    return Math.abs(x);
};
BUILTINS.floor_f = (args) => {
    const x = typeof args[0] === 'number' ? args[0] : toInt(args[0]);
    return fromInt(Math.floor(x));
};
BUILTINS.ceil_f = (args) => {
    const x = typeof args[0] === 'number' ? args[0] : toInt(args[0]);
    return fromInt(Math.ceil(x));
};
BUILTINS.round_f = (args) => {
    const x = typeof args[0] === 'number' ? args[0] : toInt(args[0]);
    return fromInt(Math.round(x));
};
BUILTINS.tanh_f = (args) => {
    const x = typeof args[0] === 'number' ? args[0] : toInt(args[0]);
    return Math.tanh(x);
};
BUILTINS.sigmoid_f = (args) => {
    const x = typeof args[0] === 'number' ? args[0] : toInt(args[0]);
    return 1.0 / (1.0 + Math.exp(-x));
};
BUILTINS.softmax = (args) => {
    if (!Array.isArray(args[0])) throw new Error('softmax: expected array');
    const arr = args[0].map(v => typeof v === 'number' ? v : toInt(v));
    const maxVal = Math.max(...arr);
    const exps = arr.map(x => Math.exp(x - maxVal));
    const sum = exps.reduce((a, b) => a + b, 0);
    return exps.map(e => e / sum);
};
BUILTINS.matmul = (args) => {
    // matmul(A, B) — matrix multiply. A[m][k] * B[k][n] -> C[m][n].
    // Values can be floats or CRT (converted to float for multiplication).
    const A = args[0], B = args[1];
    if (!Array.isArray(A) || !Array.isArray(B)) throw new Error('matmul: expected arrays');
    if (!Array.isArray(A[0]) || !Array.isArray(B[0])) throw new Error('matmul: expected 2D arrays');
    const m = A.length, k = A[0].length, n = B[0].length;
    if (B.length !== k) throw new Error('matmul: dimension mismatch (' + k + ' vs ' + B.length + ')');
    const C = [];
    for (let i = 0; i < m; i++) {
        const row = [];
        for (let j = 0; j < n; j++) {
            let s = 0;
            for (let p = 0; p < k; p++) {
                const a = typeof A[i][p] === 'number' ? A[i][p] : toInt(A[i][p]);
                const b = typeof B[p][j] === 'number' ? B[p][j] : toInt(B[p][j]);
                s += a * b;
            }
            row.push(s);
        }
        C.push(row);
    }
    return C;
};
BUILTINS.dot = (args) => {
    // dot(a, b) — dot product of two arrays. Returns float.
    const a = args[0], b = args[1];
    if (!Array.isArray(a) || !Array.isArray(b)) throw new Error('dot: expected arrays');
    let s = 0;
    const len = Math.min(a.length, b.length);
    for (let i = 0; i < len; i++) {
        const av = typeof a[i] === 'number' ? a[i] : toInt(a[i]);
        const bv = typeof b[i] === 'number' ? b[i] : toInt(b[i]);
        s += av * bv;
    }
    return s;
};
BUILTINS.sum_f = (args) => {
    // sum_f(arr) — sum of float array. Returns float.
    if (!Array.isArray(args[0])) return 0;
    return args[0].reduce((s, v) => s + (typeof v === 'number' ? v : toInt(v)), 0);
};
// Float constants (can't use E or PI — E=5 in Decality, PI not a keyword)
BUILTINS.PI_f = (args) => Math.PI;
BUILTINS.E_f = (args) => Math.E;
BUILTINS.INF_f = (args) => Infinity;

// ================================================================
//  Diffusion ops moved to .ax stdlib (diffusion.ax, S618).
//  decompose, reconstruct, cross, corrupt = pure .ax.
//  anneal kept in JS (needs Math.pow — Phase F float builtins will replace).
// ================================================================
BUILTINS.anneal = (args) => {
    const t = toInt(args[0]), max_t = Math.max(1, toInt(args[1]));
    const weight = toInt(args[2]);
    const progress = t / max_t;
    const base = 1.0 - progress;
    const temp = Math.pow(Math.max(base, 0.001), weight);
    return fromInt(Math.round(temp * 1000));
};

// ================================================================
//  Grid builtins (ARC-AGI — S600)
// ================================================================
// Grids = nested arrays of CRT values. Cells are 0-9 integers (CRT-encoded).
// Operations that rearrange cells are type-agnostic.
// Operations that compare cells use toInt() since ARC colors are small.

BUILTINS.grid = (args) => {
    const rows = Math.min(Math.max(1, toInt(args[0])), 30);
    const cols = Math.min(Math.max(1, toInt(args[1])), 30);
    const val = args.length > 2 ? args[2] : fromInt(0);
    return Array.from({length: rows}, () => Array.from({length: cols}, () => val));
};

BUILTINS.gget = (args) => {
    const g = args[0], r = toInt(args[1]), c = toInt(args[2]);
    if (!Array.isArray(g) || r < 0 || r >= g.length) return fromInt(-1);
    if (!Array.isArray(g[r]) || c < 0 || c >= g[r].length) return fromInt(-1);
    return g[r][c];
};

BUILTINS.gset = (args) => {
    const g = args[0], r = toInt(args[1]), c = toInt(args[2]), v = args[3];
    if (!Array.isArray(g) || !Array.isArray(g[0])) throw new Error('gset: not a grid');
    if (r < 0 || r >= g.length || c < 0 || c >= g[0].length) throw new Error('gset: out of bounds');
    const out = g.map(row => [...row]);
    out[r][c] = v;
    return out;
};

BUILTINS.rows = (args) => {
    const g = args[0];
    return fromInt(Array.isArray(g) ? g.length : 0);
};

BUILTINS.cols = (args) => {
    const g = args[0];
    return fromInt(Array.isArray(g) && g.length > 0 && Array.isArray(g[0]) ? g[0].length : 0);
};

BUILTINS.hflip = (args) => {
    const g = args[0];
    if (!Array.isArray(g) || g.length === 0) return [];
    return g.map(row => Array.isArray(row) ? [...row].reverse() : row);
};

BUILTINS.vflip = (args) => {
    const g = args[0];
    if (!Array.isArray(g) || g.length === 0) return [];
    return [...g].reverse().map(row => Array.isArray(row) ? [...row] : row);
};

BUILTINS.rot90 = (args) => {
    const g = args[0];
    if (!Array.isArray(g) || g.length === 0 || !Array.isArray(g[0])) return [];
    const R = g.length, C = g[0].length;
    return Array.from({length: C}, (_, c) => Array.from({length: R}, (_, r) => g[R-1-r][c]));
};

BUILTINS.rot180 = (args) => {
    const g = args[0];
    if (!Array.isArray(g) || g.length === 0) return [];
    return [...g].reverse().map(row => Array.isArray(row) ? [...row].reverse() : row);
};

BUILTINS.rot270 = (args) => {
    const g = args[0];
    if (!Array.isArray(g) || g.length === 0 || !Array.isArray(g[0])) return [];
    const R = g.length, C = g[0].length;
    return Array.from({length: C}, (_, c) => Array.from({length: R}, (_, r) => g[r][C-1-c]));
};

BUILTINS.transpose = (args) => {
    const g = args[0];
    if (!Array.isArray(g) || g.length === 0 || !Array.isArray(g[0])) return [];
    const R = g.length, C = g[0].length;
    return Array.from({length: C}, (_, c) => Array.from({length: R}, (_, r) => g[r][c]));
};

BUILTINS.grid_eq = (args) => {
    const a = args[0], b = args[1];
    if (!Array.isArray(a) || !Array.isArray(b) || a.length !== b.length) return fromInt(0);
    for (let i = 0; i < a.length; i++) {
        if (!Array.isArray(a[i]) || !Array.isArray(b[i]) || a[i].length !== b[i].length) return fromInt(0);
        for (let j = 0; j < a[i].length; j++) {
            const av = ArrayBuffer.isView(a[i][j]) ? toInt(a[i][j]) : a[i][j];
            const bv = ArrayBuffer.isView(b[i][j]) ? toInt(b[i][j]) : b[i][j];
            if (av !== bv) return fromInt(0);
        }
    }
    return fromInt(1);
};

BUILTINS.crop = (args) => {
    const g = args[0];
    if (!Array.isArray(g) || g.length === 0) throw new Error('crop: not a grid');
    let rMin = g.length, rMax = -1, cMin = g[0].length, cMax = -1;
    for (let r = 0; r < g.length; r++) {
        if (!Array.isArray(g[r])) continue;
        for (let c = 0; c < g[r].length; c++) {
            const v = ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
            if (v !== 0) { rMin = Math.min(rMin, r); rMax = Math.max(rMax, r); cMin = Math.min(cMin, c); cMax = Math.max(cMax, c); }
        }
    }
    if (rMax < 0) return [[fromInt(0)]];
    const result = [];
    for (let r = rMin; r <= rMax; r++) result.push(g[r].slice(cMin, cMax + 1));
    return result;
};

BUILTINS.scale = (args) => {
    const g = args[0], f = toInt(args[1]);
    if (!Array.isArray(g) || f < 1) throw new Error('scale: invalid');
    const result = [];
    for (let r = 0; r < g.length; r++) {
        if (!Array.isArray(g[r])) continue;
        for (let fr = 0; fr < f; fr++) {
            const row = [];
            for (let c = 0; c < g[r].length; c++) for (let fc = 0; fc < f; fc++) row.push(g[r][c]);
            result.push(row);
        }
    }
    return result;
};

BUILTINS.subgrid = (args) => {
    const g = args[0], r0 = toInt(args[1]), c0 = toInt(args[2]);
    const h = toInt(args[3]), w = toInt(args[4]);
    if (!Array.isArray(g)) throw new Error('subgrid: not a grid');
    const R = g.length, C = Array.isArray(g[0]) ? g[0].length : 0;
    const result = [];
    for (let r = 0; r < h; r++) {
        const row = [];
        for (let c = 0; c < w; c++) {
            const rr = r0 + r, cc = c0 + c;
            row.push(rr >= 0 && rr < R && cc >= 0 && cc < C ? g[rr][cc] : fromInt(0));
        }
        result.push(row);
    }
    return result;
};

BUILTINS.paste = (args) => {
    const g = args[0], sub = args[1], r0 = toInt(args[2]), c0 = toInt(args[3]);
    if (!Array.isArray(g) || !Array.isArray(sub)) throw new Error('paste: not grids');
    const out = g.map(row => [...row]);
    for (let r = 0; r < sub.length; r++) {
        if (!Array.isArray(sub[r])) continue;
        for (let c = 0; c < sub[r].length; c++) {
            const rr = r0 + r, cc = c0 + c;
            if (rr >= 0 && rr < out.length && cc >= 0 && cc < out[0].length) out[rr][cc] = sub[r][c];
        }
    }
    return out;
};

BUILTINS.colors = (args) => {
    const g = args[0];
    if (!Array.isArray(g)) throw new Error('colors: not a grid');
    const seen = new Set();
    for (const row of g) if (Array.isArray(row)) for (const v of row) {
        seen.add(ArrayBuffer.isView(v) ? toInt(v) : v);
    }
    return [...seen].sort((a, b) => a - b).map(v => fromInt(v));
};

BUILTINS.count_color = (args) => {
    const g = args[0], color = toInt(args[1]);
    if (!Array.isArray(g)) throw new Error('count_color: not a grid');
    let count = 0;
    for (const row of g) if (Array.isArray(row)) for (const v of row) {
        if ((ArrayBuffer.isView(v) ? toInt(v) : v) === color) count++;
    }
    return fromInt(count);
};

BUILTINS.replace_color = (args) => {
    const g = args[0], from = toInt(args[1]), to = args[2];
    if (!Array.isArray(g)) throw new Error('replace_color: not a grid');
    return g.map(row => Array.isArray(row) ? row.map(v =>
        (ArrayBuffer.isView(v) ? toInt(v) : v) === from ? to : v
    ) : row);
};

BUILTINS.fill_grid = (args) => {
    const g = args[0], color = args[1];
    if (!Array.isArray(g)) throw new Error('fill_grid: not a grid');
    return g.map(row => Array.isArray(row) ? row.map(() => color) : row);
};

BUILTINS.bg_color = (args) => {
    const g = args[0];
    if (!Array.isArray(g)) throw new Error('bg_color: not a grid');
    const counts = new Array(10).fill(0);
    for (const row of g) if (Array.isArray(row)) for (const v of row) {
        const n = ArrayBuffer.isView(v) ? toInt(v) : v;
        if (n >= 0 && n < 10) counts[n]++;
    }
    let maxC = 0, maxIdx = 0;
    for (let i = 0; i < 10; i++) if (counts[i] > maxC) { maxC = counts[i]; maxIdx = i; }
    return fromInt(maxIdx);
};

BUILTINS.objects = (args) => {
    const g = args[0], bg = args.length > 1 ? toInt(args[1]) : 0;
    if (!Array.isArray(g)) throw new Error('objects: not a grid');
    const R = g.length, C = g[0].length;
    const visited = Array.from({length: R}, () => new Array(C).fill(false));
    const cellVal = (r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    const objs = [];
    for (let r = 0; r < R; r++) {
        for (let c = 0; c < C; c++) {
            if (visited[r][c] || cellVal(r, c) === bg) continue;
            const color = cellVal(r, c);
            const queue = [[r, c]];
            let rmin = r, rmax = r, cmin = c, cmax = c;
            visited[r][c] = true;
            let qi = 0;
            while (qi < queue.length) {
                const [cr, cc] = queue[qi++];
                for (const [dr, dc] of [[-1,0],[1,0],[0,-1],[0,1]]) {
                    const nr = cr+dr, nc = cc+dc;
                    if (nr >= 0 && nr < R && nc >= 0 && nc < C && !visited[nr][nc] && cellVal(nr, nc) === color) {
                        visited[nr][nc] = true; queue.push([nr, nc]);
                        rmin = Math.min(rmin, nr); rmax = Math.max(rmax, nr);
                        cmin = Math.min(cmin, nc); cmax = Math.max(cmax, nc);
                    }
                }
            }
            objs.push([fromInt(rmin), fromInt(cmin), fromInt(rmax-rmin+1), fromInt(cmax-cmin+1), fromInt(color)]);
        }
    }
    return objs;
};

BUILTINS.hrepeat = (args) => {
    const g = args[0], n = Math.min(Math.max(1, toInt(args[1])), 10);
    if (!Array.isArray(g)) throw new Error('hrepeat: not a grid');
    return g.map(row => Array.isArray(row) ? [].concat(...Array(n).fill(row)) : row);
};

BUILTINS.vrepeat = (args) => {
    const g = args[0], n = Math.min(Math.max(1, toInt(args[1])), 10);
    if (!Array.isArray(g)) throw new Error('vrepeat: not a grid');
    const result = [];
    for (let i = 0; i < n; i++) for (const row of g) result.push(Array.isArray(row) ? [...row] : row);
    return result;
};

BUILTINS.color_map = (args) => {
    const gin = args[0], gout = args[1];
    if (!Array.isArray(gin) || !Array.isArray(gout) || gin.length !== gout.length) return [];
    const map = [0,1,2,3,4,5,6,7,8,9].map(v => fromInt(v));
    const set = new Array(10).fill(false);
    for (let r = 0; r < gin.length; r++) {
        if (!Array.isArray(gin[r]) || !Array.isArray(gout[r]) || gin[r].length !== gout[r].length) return [];
        for (let c = 0; c < gin[r].length; c++) {
            const ic = ArrayBuffer.isView(gin[r][c]) ? toInt(gin[r][c]) : gin[r][c];
            const oc = ArrayBuffer.isView(gout[r][c]) ? toInt(gout[r][c]) : gout[r][c];
            if (ic < 0 || ic >= 10 || oc < 0 || oc >= 10) continue;
            if (!set[ic]) { map[ic] = fromInt(oc); set[ic] = true; }
            else if (toInt(map[ic]) !== oc) return [];
        }
    }
    return map;
};

BUILTINS.apply_color_map = (args) => {
    const g = args[0], map = args[1];
    if (!Array.isArray(g) || !Array.isArray(map)) throw new Error('apply_color_map: invalid');
    return g.map(row => Array.isArray(row) ? row.map(v => {
        const n = ArrayBuffer.isView(v) ? toInt(v) : v;
        return (n >= 0 && n < map.length) ? map[n] : v;
    }) : row);
};

BUILTINS.self_tile = (args) => {
    const g = args[0], bg = args.length > 1 ? toInt(args[1]) : 0;
    if (!Array.isArray(g) || g.length === 0) throw new Error('self_tile: not a grid');
    const R = g.length, C = g[0].length;
    const bgVal = fromInt(bg);
    const result = [];
    for (let br = 0; br < R; br++) {
        for (let fr = 0; fr < R; fr++) {
            const row = [];
            for (let bc = 0; bc < C; bc++) {
                const brVal = ArrayBuffer.isView(g[br][bc]) ? toInt(g[br][bc]) : g[br][bc];
                for (let fc = 0; fc < C; fc++) {
                    row.push(brVal !== bg ? g[fr][fc] : bgVal);
                }
            }
            result.push(row);
        }
    }
    return result;
};

// flood_fill(g) — fill enclosed bg regions with surrounding non-bg color
// An enclosed region is a connected component of bg cells NOT touching any edge
BUILTINS.flood_fill = (args) => {
    const g = args[0];
    if (!Array.isArray(g) || g.length === 0) throw new Error('flood_fill: not a grid');
    const R = g.length, C = g[0].length;
    const bg = (() => { const c = new Array(10).fill(0); for (const row of g) for (const v of row) { const n = ArrayBuffer.isView(v) ? toInt(v) : v; if (n >= 0 && n < 10) c[n]++; } let m = 0, mi = 0; for (let i = 0; i < 10; i++) if (c[i] > m) { m = c[i]; mi = i; } return mi; })();
    const val = (r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    // Find connected components of bg cells
    const visited = Array.from({length: R}, () => new Array(C).fill(false));
    const out = g.map(row => [...row]);
    for (let r = 0; r < R; r++) {
        for (let c = 0; c < C; c++) {
            if (visited[r][c] || val(r, c) !== bg) continue;
            // BFS to find this bg component
            const queue = [[r, c]]; visited[r][c] = true;
            let qi = 0, touchesEdge = false;
            const adjacentColors = new Map();
            while (qi < queue.length) {
                const [cr, cc] = queue[qi++];
                if (cr === 0 || cr === R-1 || cc === 0 || cc === C-1) touchesEdge = true;
                for (const [dr, dc] of [[-1,0],[1,0],[0,-1],[0,1]]) {
                    const nr = cr+dr, nc = cc+dc;
                    if (nr < 0 || nr >= R || nc < 0 || nc >= C) continue;
                    if (val(nr, nc) !== bg) {
                        const nv = val(nr, nc);
                        adjacentColors.set(nv, (adjacentColors.get(nv) || 0) + 1);
                    } else if (!visited[nr][nc]) {
                        visited[nr][nc] = true; queue.push([nr, nc]);
                    }
                }
            }
            // Fill enclosed regions (not touching edge) with most common adjacent color
            if (!touchesEdge && adjacentColors.size > 0) {
                let fillColor = 0, maxCount = 0;
                for (const [color, count] of adjacentColors) if (count > maxCount) { maxCount = count; fillColor = color; }
                for (const [fr, fc] of queue) out[fr][fc] = fromInt(fillColor);
            }
        }
    }
    return out;
};

// extract_obj(g, idx, [bg]) — extract the idx-th connected component as its own cropped grid
BUILTINS.extract_obj = (args) => {
    const g = args[0], idx = toInt(args[1]), bg = args.length > 2 ? toInt(args[2]) : 0;
    if (!Array.isArray(g)) throw new Error('extract_obj: not a grid');
    const R = g.length, C = g[0].length;
    const visited = Array.from({length: R}, () => new Array(C).fill(false));
    const cellVal = (r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    let objIdx = 0;
    for (let r = 0; r < R; r++) {
        for (let c = 0; c < C; c++) {
            if (visited[r][c] || cellVal(r, c) === bg) continue;
            const queue = [[r, c]]; visited[r][c] = true;
            let qi = 0, rmin = r, rmax = r, cmin = c, cmax = c;
            while (qi < queue.length) {
                const [cr, cc] = queue[qi++];
                for (const [dr, dc] of [[-1,0],[1,0],[0,-1],[0,1]]) {
                    const nr = cr+dr, nc = cc+dc;
                    if (nr >= 0 && nr < R && nc >= 0 && nc < C && !visited[nr][nc] && cellVal(nr, nc) !== bg) {
                        visited[nr][nc] = true; queue.push([nr, nc]);
                        rmin = Math.min(rmin, nr); rmax = Math.max(rmax, nr);
                        cmin = Math.min(cmin, nc); cmax = Math.max(cmax, nc);
                    }
                }
            }
            if (objIdx === idx) {
                // Extract this object
                const h = rmax - rmin + 1, w = cmax - cmin + 1;
                const cells = new Set(queue.map(([r,c]) => r*C+c));
                const result = [];
                for (let rr = 0; rr < h; rr++) {
                    const row = [];
                    for (let cc = 0; cc < w; cc++) {
                        const ar = rmin + rr, ac = cmin + cc;
                        row.push(cells.has(ar*C+ac) ? g[ar][ac] : fromInt(bg));
                    }
                    result.push(row);
                }
                return result;
            }
            objIdx++;
        }
    }
    return []; // idx out of range
};

// num_objects(g, [bg]) — count number of connected components
BUILTINS.num_objects = (args) => {
    const g = args[0], bg = args.length > 1 ? toInt(args[1]) : 0;
    if (!Array.isArray(g)) return fromInt(0);
    const R = g.length, C = g[0].length;
    const visited = Array.from({length: R}, () => new Array(C).fill(false));
    const cellVal = (r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    let count = 0;
    for (let r = 0; r < R; r++) {
        for (let c = 0; c < C; c++) {
            if (visited[r][c] || cellVal(r, c) === bg) continue;
            const queue = [[r, c]]; visited[r][c] = true; let qi = 0;
            while (qi < queue.length) {
                const [cr, cc] = queue[qi++];
                for (const [dr, dc] of [[-1,0],[1,0],[0,-1],[0,1]]) {
                    const nr = cr+dr, nc = cc+dc;
                    if (nr >= 0 && nr < R && nc >= 0 && nc < C && !visited[nr][nc] && cellVal(nr, nc) !== bg) {
                        visited[nr][nc] = true; queue.push([nr, nc]);
                    }
                }
            }
            count++;
        }
    }
    return fromInt(count);
};

// split_h(g) — split grid horizontally at a single non-bg-color row separator
BUILTINS.split_h = (args) => {
    const g = args[0];
    if (!Array.isArray(g)) throw new Error('split_h: not a grid');
    const R = g.length, C = g[0].length;
    const val = (r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    const bg = toInt(BUILTINS.bg_color([g]));
    // Find all candidate separator rows, pick the one closest to middle (equal halves)
    const mid = R / 2;
    let bestR = -1, bestDist = Infinity;
    for (let r = 1; r < R - 1; r++) {
        const v0 = val(r, 0);
        if (v0 === bg) continue;
        let allSame = true;
        for (let c = 1; c < C; c++) if (val(r, c) !== v0) { allSame = false; break; }
        if (allSame) {
            const dist = Math.abs(r - mid);
            if (dist < bestDist) { bestDist = dist; bestR = r; }
        }
    }
    if (bestR >= 0) {
        const top = g.slice(0, bestR);
        const bottom = g.slice(bestR + 1);
        if (top.length > 0 && bottom.length > 0) return [top, bottom];
    }
    return [];
};

// split_v(g) — split grid vertically at a single non-bg-color column separator
BUILTINS.split_v = (args) => {
    const g = args[0];
    if (!Array.isArray(g)) throw new Error('split_v: not a grid');
    const R = g.length, C = g[0].length;
    const val = (r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    const bg = toInt(BUILTINS.bg_color([g]));
    const mid = C / 2;
    let bestC = -1, bestDist = Infinity;
    for (let c = 1; c < C - 1; c++) {
        const v0 = val(0, c);
        if (v0 === bg) continue;
        let allSame = true;
        for (let r = 1; r < R; r++) if (val(r, c) !== v0) { allSame = false; break; }
        if (allSame) {
            const dist = Math.abs(c - mid);
            if (dist < bestDist) { bestDist = dist; bestC = c; }
        }
    }
    if (bestC >= 0) {
        const left = g.map(row => row.slice(0, bestC));
        const right = g.map(row => row.slice(bestC + 1));
        if (left[0].length > 0 && right[0].length > 0) return [left, right];
    }
    return [];
};

// grid_and(a, b) — cell-wise: output[r][c] = a if a==b, else 0
BUILTINS.grid_and = (args) => {
    const a = args[0], b = args[1];
    if (!Array.isArray(a) || !Array.isArray(b)) throw new Error('grid_and: not grids');
    const R = Math.min(a.length, b.length), C = Math.min(a[0].length, b[0].length);
    return Array.from({length: R}, (_, r) => Array.from({length: C}, (_, c) => {
        const av = ArrayBuffer.isView(a[r][c]) ? toInt(a[r][c]) : a[r][c];
        const bv = ArrayBuffer.isView(b[r][c]) ? toInt(b[r][c]) : b[r][c];
        return av === bv ? a[r][c] : fromInt(0);
    }));
};

// grid_xor(a, b, [mark_color]) — cell-wise: output[r][c] = mark_color where a!=b, else 0
BUILTINS.grid_xor = (args) => {
    const a = args[0], b = args[1], mark = args.length > 2 ? toInt(args[2]) : 1;
    if (!Array.isArray(a) || !Array.isArray(b)) throw new Error('grid_xor: not grids');
    const R = Math.min(a.length, b.length), C = Math.min(a[0].length, b[0].length);
    return Array.from({length: R}, (_, r) => Array.from({length: C}, (_, c) => {
        const av = ArrayBuffer.isView(a[r][c]) ? toInt(a[r][c]) : a[r][c];
        const bv = ArrayBuffer.isView(b[r][c]) ? toInt(b[r][c]) : b[r][c];
        return av !== bv ? fromInt(mark) : fromInt(0);
    }));
};

// grid_or(a, b) — cell-wise: a if a!=0, else b
BUILTINS.grid_or = (args) => {
    const a = args[0], b = args[1];
    if (!Array.isArray(a) || !Array.isArray(b)) throw new Error('grid_or: not grids');
    const R = Math.min(a.length, b.length), C = Math.min(a[0].length, b[0].length);
    return Array.from({length: R}, (_, r) => Array.from({length: C}, (_, c) => {
        const av = ArrayBuffer.isView(a[r][c]) ? toInt(a[r][c]) : a[r][c];
        return av !== 0 ? a[r][c] : b[r][c];
    }));
};

// hconcat(a, b) — concatenate two grids horizontally
BUILTINS.hconcat = (args) => {
    const a = args[0], b = args[1];
    if (!Array.isArray(a) || !Array.isArray(b)) throw new Error('hconcat: not grids');
    const R = Math.max(a.length, b.length);
    return Array.from({length: R}, (_, r) => {
        const aRow = r < a.length && Array.isArray(a[r]) ? a[r] : [];
        const bRow = r < b.length && Array.isArray(b[r]) ? b[r] : [];
        return [...aRow, ...bRow];
    });
};

// vconcat(a, b) — concatenate two grids vertically
BUILTINS.vconcat = (args) => {
    const a = args[0], b = args[1];
    if (!Array.isArray(a) || !Array.isArray(b)) throw new Error('vconcat: not grids');
    return [...a.map(r => [...r]), ...b.map(r => [...r])];
};

// solve_mirror(ti, to, te) — try mirror-concatenation compositions
// Attempts: hconcat with hflip, vconcat with vflip, 4-way mirror, etc.
BUILTINS.solve_mirror = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    const n = ti.length;
    // Define mirror compositions to try
    const compositions = [
        // hconcat(g, hflip(g)) — mirror right
        g => BUILTINS.hconcat([g, BUILTINS.hflip([g])]),
        // hconcat(hflip(g), g) — mirror left
        g => BUILTINS.hconcat([BUILTINS.hflip([g]), g]),
        // vconcat(g, vflip(g)) — mirror down
        g => BUILTINS.vconcat([g, BUILTINS.vflip([g])]),
        // vconcat(vflip(g), g) — mirror up
        g => BUILTINS.vconcat([BUILTINS.vflip([g]), g]),
        // 4-way: vconcat(hconcat(g, hflip(g)), hconcat(vflip(g), rot180(g)))
        g => {
            const top = BUILTINS.hconcat([g, BUILTINS.hflip([g])]);
            const bot = BUILTINS.hconcat([BUILTINS.vflip([g]), BUILTINS.rot180([g])]);
            return BUILTINS.vconcat([top, bot]);
        },
        // 4-way rotational: [g, rot90(g); rot270(g), rot180(g)]
        g => {
            const top = BUILTINS.hconcat([g, BUILTINS.rot90([g])]);
            const bot = BUILTINS.hconcat([BUILTINS.rot270([g]), BUILTINS.rot180([g])]);
            return BUILTINS.vconcat([top, bot]);
        },
        // hconcat(g, g) — tile right
        g => BUILTINS.hconcat([g, g]),
        // vconcat(g, g) — tile down
        g => BUILTINS.vconcat([g, g]),
        // hconcat(g, rot90(g)) — rotate concat
        g => BUILTINS.hconcat([g, BUILTINS.rot90([g])]),
        // vconcat(g, rot90(g)) — rotate concat vertical
        g => BUILTINS.vconcat([g, BUILTINS.rot90([g])]),
        // hconcat(g, vflip(g)) — mirror vertical then concat
        g => BUILTINS.hconcat([g, BUILTINS.vflip([g])]),
        // vconcat(g, hflip(g)) — mirror horizontal then concat
        g => BUILTINS.vconcat([g, BUILTINS.hflip([g])]),
    ];
    for (const comp of compositions) {
        let allMatch = true;
        for (let i = 0; i < n; i++) {
            try {
                const pred = comp(ti[i]);
                if (toInt(BUILTINS.grid_eq([pred, to[i]])) !== 1) { allMatch = false; break; }
            } catch(e) { allMatch = false; break; }
        }
        if (allMatch) {
            // Try with color map on top
            return te.map(t => {
                try {
                    const base = comp(t);
                    // Try color mapping from first pair
                    const refBase = comp(ti[0]);
                    if (refBase.length === to[0].length && refBase[0].length === to[0][0].length) {
                        const cmap = BUILTINS.color_map([refBase, to[0]]);
                        if (Array.isArray(cmap) && cmap.length > 0) return BUILTINS.apply_color_map([base, cmap]);
                    }
                    return base;
                } catch(e) { return t; }
            });
        }
        // Also try with color map per training pair
        let allMatchCM = true;
        let cmapGlobal = null;
        for (let i = 0; i < n; i++) {
            try {
                const pred = comp(ti[i]);
                if (pred.length !== to[i].length || pred[0].length !== to[i][0].length) { allMatchCM = false; break; }
                const cmap = BUILTINS.color_map([pred, to[i]]);
                if (!Array.isArray(cmap) || cmap.length === 0) { allMatchCM = false; break; }
                const mapped = BUILTINS.apply_color_map([pred, cmap]);
                if (toInt(BUILTINS.grid_eq([mapped, to[i]])) !== 1) { allMatchCM = false; break; }
                if (!cmapGlobal) cmapGlobal = cmap;
            } catch(e) { allMatchCM = false; break; }
        }
        if (allMatchCM && cmapGlobal) {
            return te.map(t => {
                try {
                    return BUILTINS.apply_color_map([comp(t), cmapGlobal]);
                } catch(e) { return t; }
            });
        }
    }
    return [];
};

// solve_recolor(ti, to, te) — detect marker pixel, recolor main shape
BUILTINS.solve_recolor = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    const n = ti.length;
    const getVal = (g, r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    // Strategy: find a single isolated pixel (marker), recolor the main shape to marker color
    // The main shape = largest connected component. Marker = smallest or isolated.
    for (let i = 0; i < n; i++) {
        if (ti[i].length !== to[i].length || ti[i][0].length !== to[i][0].length) return [];
    }
    // For each training pair, find colors in input and output, detect the swap
    // Pattern: shape_color -> marker_color, marker_color -> 0, bg stays
    const findRecolorMap = (inp, out) => {
        const R = inp.length, C = inp[0].length;
        const bg = toInt(BUILTINS.bg_color([inp]));
        // Collect all color->color mappings
        const map = {};
        for (let r = 0; r < R; r++) {
            for (let c = 0; c < C; c++) {
                const iv = getVal(inp, r, c), ov = getVal(out, r, c);
                const key = iv.toString();
                if (map[key] === undefined) map[key] = ov;
                else if (map[key] !== ov) return null; // inconsistent
            }
        }
        return map;
    };
    // Check if all pairs have consistent recolor map
    let globalMap = null;
    for (let i = 0; i < n; i++) {
        const m = findRecolorMap(ti[i], to[i]);
        if (!m) return [];
        if (!globalMap) globalMap = m;
    }
    if (!globalMap) return [];
    // Apply
    return te.map(t => t.map(row => row.map(v => {
        const nv = ArrayBuffer.isView(v) ? toInt(v) : v;
        const mapped = globalMap[nv.toString()];
        return mapped !== undefined ? fromInt(mapped) : v;
    })));
};

// solve_fill_interior(ti, to, te) — fill interior of shapes with a specific color
BUILTINS.solve_fill_interior = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    const n = ti.length;
    const getVal = (g, r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    for (let i = 0; i < n; i++) {
        if (ti[i].length !== to[i].length || ti[i][0].length !== to[i][0].length) return [];
    }
    // For each training pair: find cells that changed and what they changed to
    // Interior = bg cells surrounded by non-bg cells (flood fill from edges finds exterior)
    const findInterior = (g) => {
        const R = g.length, C = g[0].length;
        const bg = toInt(BUILTINS.bg_color([g]));
        const exterior = Array.from({length: R}, () => Array(C).fill(false));
        // BFS from all bg cells on edges
        const queue = [];
        for (let r = 0; r < R; r++) {
            for (let c = 0; c < C; c++) {
                if ((r === 0 || r === R-1 || c === 0 || c === C-1) && getVal(g, r, c) === bg) {
                    exterior[r][c] = true;
                    queue.push([r, c]);
                }
            }
        }
        while (queue.length > 0) {
            const [cr, cc] = queue.shift();
            for (const [dr, dc] of [[-1,0],[1,0],[0,-1],[0,1]]) {
                const nr = cr+dr, nc = cc+dc;
                if (nr >= 0 && nr < R && nc >= 0 && nc < C && !exterior[nr][nc] && getVal(g, nr, nc) === bg) {
                    exterior[nr][nc] = true;
                    queue.push([nr, nc]);
                }
            }
        }
        // Interior = bg cells that are NOT exterior
        const interior = [];
        for (let r = 0; r < R; r++) {
            for (let c = 0; c < C; c++) {
                if (getVal(g, r, c) === bg && !exterior[r][c]) interior.push([r, c]);
            }
        }
        return interior;
    };
    // Detect fill color from first training pair
    const interior0 = findInterior(ti[0]);
    if (interior0.length === 0) return [];
    // What color did interior cells become?
    const fillColor = getVal(to[0], interior0[0][0], interior0[0][1]);
    // Verify all interior cells got same color and all other cells unchanged
    let allMatch = true;
    for (let i = 0; i < n; i++) {
        const R = ti[i].length, C = ti[i][0].length;
        const interior = findInterior(ti[i]);
        const interiorSet = new Set(interior.map(([r,c]) => r*C+c));
        for (let r = 0; r < R; r++) {
            for (let c = 0; c < C; c++) {
                const iv = getVal(ti[i], r, c), ov = getVal(to[i], r, c);
                if (interiorSet.has(r*C+c)) {
                    if (ov !== fillColor) { allMatch = false; break; }
                } else {
                    if (iv !== ov) { allMatch = false; break; }
                }
            }
            if (!allMatch) break;
        }
        if (!allMatch) break;
    }
    if (!allMatch) return [];
    // Apply: fill interior of test inputs
    return te.map(t => {
        const R = t.length, C = t[0].length;
        const out = t.map(row => [...row]);
        const interior = findInterior(t);
        for (const [r, c] of interior) out[r][c] = fromInt(fillColor);
        return out;
    });
};

// solve_symmetry(ti, to, te) — fix broken symmetry in input
BUILTINS.solve_symmetry = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    const n = ti.length;
    const getVal = (g, r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    for (let i = 0; i < n; i++) {
        if (ti[i].length !== to[i].length || ti[i][0].length !== to[i][0].length) return [];
    }
    // Try different symmetry types
    const symmetries = [
        // horizontal (left-right mirror)
        (g, r, c, R, C) => ({ mr: r, mc: C - 1 - c }),
        // vertical (top-bottom mirror)
        (g, r, c, R, C) => ({ mr: R - 1 - r, mc: c }),
        // both (180 rotation)
        (g, r, c, R, C) => ({ mr: R - 1 - r, mc: C - 1 - c }),
        // diagonal (transpose)
        (g, r, c, R, C) => R === C ? { mr: c, mc: r } : null,
    ];
    for (const sym of symmetries) {
        let allMatch = true;
        for (let i = 0; i < n; i++) {
            const g = ti[i], o = to[i];
            const R = g.length, C = g[0].length;
            const bg = 0;
            // Apply symmetry fix: for each bg cell, replace with its mirror partner
            const fixed = g.map(row => [...row]);
            for (let r = 0; r < R; r++) {
                for (let c = 0; c < C; c++) {
                    const s = sym(g, r, c, R, C);
                    if (!s) { allMatch = false; break; }
                    const v = getVal(g, r, c);
                    const mv = getVal(g, s.mr, s.mc);
                    // If one side has content and the other is bg, fill bg with content
                    if (v === bg && mv !== bg) fixed[r][c] = g[s.mr][s.mc];
                }
                if (!allMatch) break;
            }
            if (!allMatch) break;
            if (toInt(BUILTINS.grid_eq([fixed, o])) !== 1) { allMatch = false; break; }
        }
        if (allMatch) {
            return te.map(t => {
                const R = t.length, C = t[0].length;
                const fixed = t.map(row => [...row]);
                for (let r = 0; r < R; r++) {
                    for (let c = 0; c < C; c++) {
                        const s = sym(t, r, c, R, C);
                        if (!s) continue;
                        const v = getVal(t, r, c);
                        const mv = getVal(t, s.mr, s.mc);
                        if (v === 0 && mv !== 0) fixed[r][c] = t[s.mr][s.mc];
                    }
                }
                return fixed;
            });
        }
    }
    return [];
};

// solve_tile_pattern(ti, to, te) — detect small pattern and tile it
BUILTINS.solve_tile_pattern = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    const n = ti.length;
    const getVal = (g, r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    for (let i = 0; i < n; i++) {
        if (ti[i].length !== to[i].length || ti[i][0].length !== to[i][0].length) return [];
    }
    // Try tiling with different period sizes
    const tryTile = (g, o, pr, pc) => {
        const R = g.length, C = g[0].length;
        if (pr > R || pc > C) return false;
        // Build tile from output (first pr x pc cells)
        const tile = [];
        for (let r = 0; r < pr; r++) {
            tile.push([]);
            for (let c = 0; c < pc; c++) {
                tile[r].push(getVal(o, r, c));
            }
        }
        // Verify tile covers entire output
        for (let r = 0; r < R; r++) {
            for (let c = 0; c < C; c++) {
                if (getVal(o, r, c) !== tile[r % pr][c % pc]) return false;
            }
        }
        // Verify input is tile with some cells zeroed
        for (let r = 0; r < R; r++) {
            for (let c = 0; c < C; c++) {
                const iv = getVal(g, r, c);
                if (iv !== 0 && iv !== tile[r % pr][c % pc]) return false;
            }
        }
        return true;
    };
    // Find tile size from output periodicity (tiles can wrap, no divisibility needed)
    const findTileSize = (o) => {
        const R = o.length, C = o[0].length;
        for (let pr = 1; pr <= Math.floor(R/2); pr++) {
            for (let pc = 1; pc <= Math.floor(C/2); pc++) {
                let ok = true;
                for (let r = 0; r < R && ok; r++) {
                    for (let c = 0; c < C && ok; c++) {
                        if (getVal(o, r, c) !== getVal(o, r % pr, c % pc)) ok = false;
                    }
                }
                if (ok) return [pr, pc];
            }
        }
        return null;
    };
    // Find tile size that works for ALL training pairs
    const ts0 = findTileSize(to[0]);
    if (!ts0) return [];
    let [pr, pc] = ts0;
    // Verify: each training output has same period AND input consistent
    for (let i = 0; i < n; i++) {
        const R = to[i].length, C = to[i][0].length;
        // Check output periodicity
        let ok = true;
        for (let r = 0; r < R && ok; r++) {
            for (let c = 0; c < C && ok; c++) {
                if (getVal(to[i], r, c) !== getVal(to[i], r % pr, c % pc)) ok = false;
            }
        }
        if (!ok) {
            // Try finding period for this pair's output
            const ts = findTileSize(to[i]);
            if (!ts) return [];
            // Periods must share a common period
            pr = Math.max(pr, ts[0]); pc = Math.max(pc, ts[1]);
        }
        // Verify input: non-zero cells match tile from output
        const tile = Array.from({length: pr}, (_, r) => Array.from({length: pc}, (_, c) => getVal(to[i], r % to[i].length, c % to[i][0].length)));
        for (let r = 0; r < R; r++) {
            for (let c = 0; c < C; c++) {
                const iv = getVal(ti[i], r, c);
                if (iv !== 0 && iv !== tile[r % pr][c % pc]) return [];
            }
        }
    }
    // Apply: build tile from each test input's non-zero cells, then tile
    const predictions = [];
    for (let ti2 = 0; ti2 < te.length; ti2++) {
        const t = te[ti2];
        const R = t.length, C = t[0].length;
        const tile = Array.from({length: pr}, () => Array(pc).fill(-1));
        // Collect non-zero cells
        for (let r = 0; r < R; r++) {
            for (let c = 0; c < C; c++) {
                const v = getVal(t, r, c);
                if (v !== 0) {
                    const tr = r % pr, tc = c % pc;
                    if (tile[tr][tc] === -1) tile[tr][tc] = v;
                    else if (tile[tr][tc] !== v) return []; // conflict
                }
            }
        }
        // Check completeness — all tile cells filled?
        for (let r = 0; r < pr; r++) for (let c = 0; c < pc; c++) if (tile[r][c] === -1) return [];
        predictions.push(Array.from({length: R}, (_, r) => Array.from({length: C}, (_, c) => fromInt(tile[r % pr][c % pc]))));
    }
    return predictions;
};

// solve_flood_fill(train_inputs, train_outputs, test_inputs)
// Identifies enclosed bg regions, learns the fill color from training output
BUILTINS.solve_flood_fill = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    // First try: plain flood_fill matches directly
    let direct = true;
    for (let i = 0; i < ti.length; i++) {
        const pred = BUILTINS.flood_fill([ti[i]]);
        if (toInt(BUILTINS.grid_eq([pred, to[i]])) !== 1) { direct = false; break; }
    }
    if (direct) return te.map(t => BUILTINS.flood_fill([t]));
    // Second try: flood_fill identifies enclosed cells, learn fill color from output
    // Find enclosed cells in training input, check what color they become in output
    let fillColor = -1;
    for (let i = 0; i < ti.length; i++) {
        if (ti[i].length !== to[i].length || ti[i][0].length !== to[i][0].length) return [];
        const g = ti[i], R = g.length, C = g[0].length;
        const bg = (() => { const c = new Array(10).fill(0); for (const row of g) for (const v of row) { const n = ArrayBuffer.isView(v) ? toInt(v) : v; if (n >= 0 && n < 10) c[n]++; } let m = 0, mi = 0; for (let i = 0; i < 10; i++) if (c[i] > m) { m = c[i]; mi = i; } return mi; })();
        const val = (r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
        const visited = Array.from({length: R}, () => new Array(C).fill(false));
        for (let r = 0; r < R; r++) {
            for (let c = 0; c < C; c++) {
                if (visited[r][c] || val(r, c) !== bg) continue;
                const queue = [[r, c]]; visited[r][c] = true; let qi = 0, touchesEdge = false;
                while (qi < queue.length) {
                    const [cr, cc] = queue[qi++];
                    if (cr === 0 || cr === R-1 || cc === 0 || cc === C-1) touchesEdge = true;
                    for (const [dr, dc] of [[-1,0],[1,0],[0,-1],[0,1]]) {
                        const nr = cr+dr, nc = cc+dc;
                        if (nr >= 0 && nr < R && nc >= 0 && nc < C && val(nr, nc) === bg && !visited[nr][nc]) {
                            visited[nr][nc] = true; queue.push([nr, nc]);
                        }
                    }
                }
                if (!touchesEdge) {
                    // These cells are enclosed — check their color in output
                    for (const [fr, fc] of queue) {
                        const ov = ArrayBuffer.isView(to[i][fr][fc]) ? toInt(to[i][fr][fc]) : to[i][fr][fc];
                        if (ov !== bg) {
                            if (fillColor === -1) fillColor = ov;
                            else if (fillColor !== ov) return []; // inconsistent
                        }
                    }
                }
            }
        }
    }
    if (fillColor === -1) return [];
    // Verify: filling enclosed cells with fillColor produces correct output
    const fillEnclosed = (g) => {
        const R = g.length, C = g[0].length;
        const bg = (() => { const c = new Array(10).fill(0); for (const row of g) for (const v of row) { const n = ArrayBuffer.isView(v) ? toInt(v) : v; if (n >= 0 && n < 10) c[n]++; } let m = 0, mi = 0; for (let i = 0; i < 10; i++) if (c[i] > m) { m = c[i]; mi = i; } return mi; })();
        const val = (r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
        const out = g.map(row => [...row]);
        const visited = Array.from({length: R}, () => new Array(C).fill(false));
        for (let r = 0; r < R; r++) {
            for (let c = 0; c < C; c++) {
                if (visited[r][c] || val(r, c) !== bg) continue;
                const queue = [[r, c]]; visited[r][c] = true; let qi = 0, touchesEdge = false;
                while (qi < queue.length) {
                    const [cr, cc] = queue[qi++];
                    if (cr === 0 || cr === R-1 || cc === 0 || cc === C-1) touchesEdge = true;
                    for (const [dr, dc] of [[-1,0],[1,0],[0,-1],[0,1]]) {
                        const nr = cr+dr, nc = cc+dc;
                        if (nr >= 0 && nr < R && nc >= 0 && nc < C && val(nr, nc) === bg && !visited[nr][nc]) {
                            visited[nr][nc] = true; queue.push([nr, nc]);
                        }
                    }
                }
                if (!touchesEdge) {
                    for (const [fr, fc] of queue) out[fr][fc] = fromInt(fillColor);
                }
            }
        }
        return out;
    };
    for (let i = 0; i < ti.length; i++) {
        const pred = fillEnclosed(ti[i]);
        if (toInt(BUILTINS.grid_eq([pred, to[i]])) !== 1) return [];
    }
    return te.map(t => fillEnclosed(t));
};

// solve_split_xor(ti, to, te) — split grid by separator, compare halves
BUILTINS.solve_split_xor = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    const splits = ['h', 'v', 'h_nosep', 'v_nosep'];
    // Operations: and, or, xor, both_nonzero, nor, diff_a, diff_b
    const doSplit = (g, dir) => {
        if (dir === 'h') return BUILTINS.split_h([g]);
        if (dir === 'v') return BUILTINS.split_v([g]);
        // No-separator: split exactly in half
        if (dir === 'h_nosep') {
            const R = g.length;
            if (R % 2 !== 0 || R < 2) return [];
            return [g.slice(0, R/2), g.slice(R/2)];
        }
        // v_nosep
        const C = g[0].length;
        if (C % 2 !== 0 || C < 2) return [];
        return [g.map(r => r.slice(0, C/2)), g.map(r => r.slice(C/2))];
    };

    for (const dir of splits) {
        // Check all training splits work
        let allSplit = true;
        const splitParts = [];
        for (let i = 0; i < ti.length; i++) {
            const parts = doSplit(ti[i], dir);
            if (!Array.isArray(parts) || parts.length !== 2) { allSplit = false; break; }
            const [a, b] = parts;
            if (a.length !== b.length || a[0].length !== b[0].length) { allSplit = false; break; }
            if (a.length !== to[i].length || a[0].length !== to[i][0].length) { allSplit = false; break; }
            splitParts.push([a, b]);
        }
        if (!allSplit) continue;

        // Try each operation with each mark color
        const ops = [
            // both_nonzero: mark where both halves have non-zero
            (a, b, mc) => Array.from({length: a.length}, (_, r) => Array.from({length: a[0].length}, (_, c) => {
                const av = ArrayBuffer.isView(a[r][c]) ? toInt(a[r][c]) : a[r][c];
                const bv = ArrayBuffer.isView(b[r][c]) ? toInt(b[r][c]) : b[r][c];
                return (av !== 0 && bv !== 0) ? fromInt(mc) : fromInt(0);
            })),
            // xor: mark where exactly one is non-zero
            (a, b, mc) => Array.from({length: a.length}, (_, r) => Array.from({length: a[0].length}, (_, c) => {
                const av = ArrayBuffer.isView(a[r][c]) ? toInt(a[r][c]) : a[r][c];
                const bv = ArrayBuffer.isView(b[r][c]) ? toInt(b[r][c]) : b[r][c];
                return ((av !== 0) !== (bv !== 0)) ? fromInt(mc) : fromInt(0);
            })),
            // diff_b: mark where b!=0 AND a==0 (unique to right/bottom)
            (a, b, mc) => Array.from({length: a.length}, (_, r) => Array.from({length: a[0].length}, (_, c) => {
                const av = ArrayBuffer.isView(a[r][c]) ? toInt(a[r][c]) : a[r][c];
                const bv = ArrayBuffer.isView(b[r][c]) ? toInt(b[r][c]) : b[r][c];
                return (bv !== 0 && av === 0) ? fromInt(mc) : fromInt(0);
            })),
            // diff_a: mark where a!=0 AND b==0 (unique to left/top)
            (a, b, mc) => Array.from({length: a.length}, (_, r) => Array.from({length: a[0].length}, (_, c) => {
                const av = ArrayBuffer.isView(a[r][c]) ? toInt(a[r][c]) : a[r][c];
                const bv = ArrayBuffer.isView(b[r][c]) ? toInt(b[r][c]) : b[r][c];
                return (av !== 0 && bv === 0) ? fromInt(mc) : fromInt(0);
            })),
            // nor: mark where BOTH halves are zero
            (a, b, mc) => Array.from({length: a.length}, (_, r) => Array.from({length: a[0].length}, (_, c) => {
                const av = ArrayBuffer.isView(a[r][c]) ? toInt(a[r][c]) : a[r][c];
                const bv = ArrayBuffer.isView(b[r][c]) ? toInt(b[r][c]) : b[r][c];
                return (av === 0 && bv === 0) ? fromInt(mc) : fromInt(0);
            })),
            // or_mark: mark with mc where EITHER half is non-zero
            (a, b, mc) => Array.from({length: a.length}, (_, r) => Array.from({length: a[0].length}, (_, c) => {
                const av = ArrayBuffer.isView(a[r][c]) ? toInt(a[r][c]) : a[r][c];
                const bv = ArrayBuffer.isView(b[r][c]) ? toInt(b[r][c]) : b[r][c];
                return (av !== 0 || bv !== 0) ? fromInt(mc) : fromInt(0);
            })),
            // or: overlay (a if non-zero, else b)
            (a, b, mc) => BUILTINS.grid_or([a, b]),
            // and: keep only matching non-zero cells
            (a, b, mc) => BUILTINS.grid_and([a, b]),
        ];

        for (const opFn of ops) {
            for (let mc = 1; mc <= 9; mc++) {
                let allMatch = true;
                for (let i = 0; i < splitParts.length; i++) {
                    const pred = opFn(splitParts[i][0], splitParts[i][1], mc);
                    if (toInt(BUILTINS.grid_eq([pred, to[i]])) !== 1) { allMatch = false; break; }
                }
                if (allMatch) {
                    return te.map(t => {
                        const parts = doSplit(t, dir);
                        if (!Array.isArray(parts) || parts.length !== 2) return t;
                        return opFn(parts[0], parts[1], mc);
                    });
                }
            }
        }
    }
    return [];
};

// solve_dot_stamp(ti, to, te) — learn stamp pattern around each colored dot
// For same-size tasks where isolated dots get expanded to cross/diamond/line patterns
BUILTINS.solve_dot_stamp = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    // Must be same size
    for (let i = 0; i < ti.length; i++) {
        if (ti[i].length !== to[i].length || ti[i][0].length !== to[i][0].length) return [];
    }
    const val = (g, r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    const bg = toInt(BUILTINS.bg_color([ti[0]]));

    // Find all non-bg colors in input, require dots to be isolated (no same-color neighbors)
    const inColors = new Set();
    for (const g of ti) for (let r = 0; r < g.length; r++) for (let c = 0; c < g[0].length; c++) {
        const v = val(g, r, c);
        if (v !== bg) inColors.add(v);
    }
    if (inColors.size === 0 || inColors.size > 9) return [];
    // Check that non-bg cells are isolated dots (no adjacent non-bg cells of same color)
    for (const g of ti) {
        const R = g.length, C = g[0].length;
        for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
            const v = val(g, r, c);
            if (v === bg) continue;
            // Check 4-neighbors for same color
            const nbs = [[r-1,c],[r+1,c],[r,c-1],[r,c+1]];
            for (const [nr, nc] of nbs) {
                if (nr >= 0 && nr < R && nc >= 0 && nc < C && val(g, nr, nc) !== bg) return [];
            }
        }
    }

    // For each input color, learn its OWN stamp (offsets + output colors)
    // MAX_RADIUS: only learn stamps within this distance (avoid position-dependent patterns)
    const MAX_RADIUS = 3;
    const stamps = {}; // color -> [[dr, dc, outColor], ...]
    let anyStamp = false;
    for (const col of inColors) {
        let stampOffsets = null;
        let consistent = true;
        let dotsSeenTotal = 0;
        for (let i = 0; i < ti.length && consistent; i++) {
            const R = ti[i].length, C = ti[i][0].length;
            const dots = [];
            for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
                if (val(ti[i], r, c) === col) dots.push([r, c]);
            }
            if (dots.length === 0) continue;
            dotsSeenTotal += dots.length;
            for (const [dr0, dc0] of dots) {
                const localStamp = [];
                for (let dr = -MAX_RADIUS; dr <= MAX_RADIUS; dr++) {
                    for (let dc = -MAX_RADIUS; dc <= MAX_RADIUS; dc++) {
                        if (dr === 0 && dc === 0) continue; // handle dot itself separately
                        const r = dr0 + dr, c = dc0 + dc;
                        if (r < 0 || r >= R || c < 0 || c >= C) continue;
                        const ov = val(to[i], r, c);
                        const iv = val(ti[i], r, c);
                        if (ov !== iv && ov !== bg) {
                            localStamp.push([dr, dc, ov]);
                        }
                    }
                }
                // Include the dot itself
                const dotOut = val(to[i], dr0, dc0);
                localStamp.push([0, 0, dotOut]);

                if (stampOffsets === null) {
                    stampOffsets = localStamp;
                } else {
                    if (localStamp.length !== stampOffsets.length) { consistent = false; break; }
                    const sA = localStamp.sort((a,b) => a[0]-b[0]||a[1]-b[1]).map(x=>x.join(','));
                    const sB = stampOffsets.sort((a,b) => a[0]-b[0]||a[1]-b[1]).map(x=>x.join(','));
                    for (let j = 0; j < sA.length; j++) if (sA[j] !== sB[j]) { consistent = false; break; }
                }
            }
        }
        if (!consistent || !stampOffsets || stampOffsets.length === 0) continue; // skip this color
        if (dotsSeenTotal < 2) continue;
        stamps[col] = stampOffsets;
        anyStamp = true;
    }
    if (!anyStamp) return [];

    // Verify: apply stamps to all training inputs and check match
    const applyStamps = (gin) => {
        const R = gin.length, C = gin[0].length;
        const result = Array.from({length: R}, (_, r) => Array.from({length: C}, (_, c) => fromInt(val(gin, r, c))));
        // Apply stamps for colors that have them
        for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
            const v = val(gin, r, c);
            if (v !== bg && stamps[v]) {
                for (const [dr, dc, oc] of stamps[v]) {
                    const nr = r + dr, nc = c + dc;
                    if (nr >= 0 && nr < R && nc >= 0 && nc < C) {
                        result[nr][nc] = fromInt(oc);
                    }
                }
            }
        }
        return result;
    };

    // Verify on training
    for (let i = 0; i < ti.length; i++) {
        const pred = applyStamps(ti[i]);
        if (toInt(BUILTINS.grid_eq([pred, to[i]])) !== 1) return [];
    }

    return te.map(t => applyStamps(t));
};

// solve_line_draw(ti, to, te) — draw lines from colored dots to edges or between dots
BUILTINS.solve_line_draw = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    // Must be same size
    for (let i = 0; i < ti.length; i++) {
        if (ti[i].length !== to[i].length || ti[i][0].length !== to[i][0].length) return [];
    }
    const val = (g, r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    const bg = toInt(BUILTINS.bg_color([ti[0]]));

    // Strategy: for each non-bg dot, try extending lines in 4 directions (R, D, L, U)
    // Learn which direction(s) each color extends
    // Directions: 0=right, 1=down, 2=left, 3=up
    const dirs = [[0,1],[1,0],[0,-1],[-1,0]];
    const dirNames = ['R','D','L','U'];

    // For each input color, determine which directions it draws lines
    const inColors = new Set();
    for (const g of ti) for (let r = 0; r < g.length; r++) for (let c = 0; c < g[0].length; c++) {
        const v = val(g, r, c); if (v !== bg) inColors.add(v);
    }
    if (inColors.size === 0 || inColors.size > 9) return [];

    // Direction patterns to try (R, D, L, U)
    const patterns = [
        [true,false,false,false],  // right only
        [false,true,false,false],  // down only
        [false,false,true,false],  // left only
        [false,false,false,true],  // up only
        [true,true,false,false],   // right+down
        [true,false,false,true],   // right+up
        [false,true,true,false],   // down+left
        [false,false,true,true],   // left+up
        [true,true,true,true],     // cross (all 4)
        [true,false,true,false],   // horizontal (left+right)
        [false,true,false,true],   // vertical (up+down)
    ];

    // Also try "draw to next dot" — connect dots of same color
    // First: try uniform pattern (all colors same direction)
    for (const pat of patterns) {
        const applyPat = (gin) => {
            const R = gin.length, C = gin[0].length;
            const result = Array.from({length: R}, (_, r) => Array.from({length: C}, (_, c) => fromInt(val(gin, r, c))));
            for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
                const v = val(gin, r, c);
                if (v !== bg) {
                    for (let d = 0; d < 4; d++) {
                        if (!pat[d]) continue;
                        let nr = r + dirs[d][0], nc = c + dirs[d][1];
                        while (nr >= 0 && nr < R && nc >= 0 && nc < C) {
                            if (val(gin, nr, nc) === bg) result[nr][nc] = fromInt(v);
                            nr += dirs[d][0]; nc += dirs[d][1];
                        }
                    }
                }
            }
            return result;
        };

        let allMatch = true;
        for (let i = 0; i < ti.length; i++) {
            const pred = applyPat(ti[i]);
            if (toInt(BUILTINS.grid_eq([pred, to[i]])) !== 1) { allMatch = false; break; }
        }
        if (allMatch) return te.map(t => applyPat(t));
    }

    // Try L-shape: right to edge then down to edge (and variants)
    const lShapes = [
        [[0,1],[1,0]],  // right then down
        [[0,1],[-1,0]], // right then up
        [[0,-1],[1,0]], // left then down
        [[0,-1],[-1,0]],// left then up
    ];
    for (const [d1, d2] of lShapes) {
        const applyL = (gin) => {
            const R = gin.length, C = gin[0].length;
            const result = Array.from({length: R}, (_, r) => Array.from({length: C}, (_, c) => fromInt(val(gin, r, c))));
            for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
                const v = val(gin, r, c);
                if (v !== bg) {
                    // Extend in direction d1 to edge
                    let nr = r + d1[0], nc = c + d1[1];
                    let lastR = r, lastC = c;
                    while (nr >= 0 && nr < R && nc >= 0 && nc < C) {
                        if (val(gin, nr, nc) === bg) result[nr][nc] = fromInt(v);
                        lastR = nr; lastC = nc;
                        nr += d1[0]; nc += d1[1];
                    }
                    // Then extend in direction d2 from the corner
                    nr = lastR + d2[0]; nc = lastC + d2[1];
                    while (nr >= 0 && nr < R && nc >= 0 && nc < C) {
                        if (val(gin, nr, nc) === bg) result[nr][nc] = fromInt(v);
                        nr += d2[0]; nc += d2[1];
                    }
                }
            }
            return result;
        };
        let allMatch = true;
        for (let i = 0; i < ti.length; i++) {
            const pred = applyL(ti[i]);
            if (toInt(BUILTINS.grid_eq([pred, to[i]])) !== 1) { allMatch = false; break; }
        }
        if (allMatch) return te.map(t => applyL(t));
    }

    return [];
};

// solve_color_swap(ti, to, te) — swap specific color pairs
BUILTINS.solve_color_swap = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    // Must be same size
    for (let i = 0; i < ti.length; i++) {
        if (ti[i].length !== to[i].length || ti[i][0].length !== to[i][0].length) return [];
    }
    const val = (g, r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    // Learn color mapping from first training pair
    const cmap = new Map(); // input color -> output color
    const R = ti[0].length, C = ti[0][0].length;
    for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
        const iv = val(ti[0], r, c), ov = val(to[0], r, c);
        if (cmap.has(iv)) { if (cmap.get(iv) !== ov) return []; }
        else cmap.set(iv, ov);
    }
    // Must have at least one swap (not identity)
    let hasSwap = false;
    for (const [k, v] of cmap) if (k !== v) { hasSwap = true; break; }
    if (!hasSwap) return [];
    // Verify on all training pairs
    for (let i = 1; i < ti.length; i++) {
        const Ri = ti[i].length, Ci = ti[i][0].length;
        for (let r = 0; r < Ri; r++) for (let c = 0; c < Ci; c++) {
            const iv = val(ti[i], r, c), ov = val(to[i], r, c);
            const expected = cmap.has(iv) ? cmap.get(iv) : iv;
            if (expected !== ov) return [];
        }
    }
    // Apply to test
    return te.map(t => {
        return Array.from({length: t.length}, (_, r) => Array.from({length: t[0].length}, (_, c) => {
            const v = val(t, r, c);
            return fromInt(cmap.has(v) ? cmap.get(v) : v);
        }));
    });
};

// solve_extract_obj(ti, to, te) — try extracting each object and see if it matches output
BUILTINS.solve_extract_obj = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    const strategies = ['largest', 'smallest', 'most_cells', 'second_largest'];
    for (const strat of strategies) {
        let allMatch = true;
        for (let i = 0; i < ti.length; i++) {
            const objs = BUILTINS.objects([ti[i]]);
            if (objs.length === 0) { allMatch = false; break; }
            let bestIdx = 0, bestSize = 0, secondIdx = -1, secondSize = 0;
            for (let j = 0; j < objs.length; j++) {
                const h = toInt(objs[j][2]), w = toInt(objs[j][3]);
                const size = h * w;
                if (strat === 'largest' && size > bestSize) { secondSize = bestSize; secondIdx = bestIdx; bestSize = size; bestIdx = j; }
                if (strat === 'smallest' && (bestSize === 0 || size < bestSize)) { bestSize = size; bestIdx = j; }
                if (strat === 'most_cells' && size > bestSize) { bestSize = size; bestIdx = j; }
                if (strat === 'second_largest') {
                    if (size > bestSize) { secondSize = bestSize; secondIdx = bestIdx; bestSize = size; bestIdx = j; }
                    else if (size > secondSize) { secondSize = size; secondIdx = j; }
                }
            }
            if (strat === 'second_largest') bestIdx = secondIdx >= 0 ? secondIdx : 0;
            const ext = BUILTINS.extract_obj([ti[i], fromInt(bestIdx)]);
            if (!Array.isArray(ext) || ext.length === 0) { allMatch = false; break; }
            if (toInt(BUILTINS.grid_eq([ext, to[i]])) !== 1) { allMatch = false; break; }
        }
        if (allMatch) {
            return te.map(t => {
                const objs = BUILTINS.objects([t]);
                if (objs.length === 0) return t;
                let bestIdx = 0, bestSize = 0, secondIdx = -1, secondSize = 0;
                for (let j = 0; j < objs.length; j++) {
                    const h = toInt(objs[j][2]), w = toInt(objs[j][3]);
                    const size = h * w;
                    if (strat === 'largest' && size > bestSize) { secondSize = bestSize; secondIdx = bestIdx; bestSize = size; bestIdx = j; }
                    if (strat === 'smallest' && (bestSize === 0 || size < bestSize)) { bestSize = size; bestIdx = j; }
                    if (strat === 'most_cells' && size > bestSize) { bestSize = size; bestIdx = j; }
                    if (strat === 'second_largest') {
                        if (size > bestSize) { secondSize = bestSize; secondIdx = bestIdx; bestSize = size; bestIdx = j; }
                        else if (size > secondSize) { secondSize = size; secondIdx = j; }
                    }
                }
                if (strat === 'second_largest') bestIdx = secondIdx >= 0 ? secondIdx : 0;
                return BUILTINS.extract_obj([t, fromInt(bestIdx)]);
            });
        }
    }
    return [];
};

// solve_extract_color(ti, to, te) — extract bbox of rarest/most-common non-bg color
BUILTINS.solve_extract_color = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    const val = (g, r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    const strategies = ['rarest', 'most_common'];
    for (const strat of strategies) {
        let allMatch = true;
        for (let i = 0; i < ti.length; i++) {
            const g = ti[i], R = g.length, C = g[0].length;
            const oR = to[i].length, oC = to[i][0].length;
            const bg = toInt(BUILTINS.bg_color([g]));
            // Count non-bg color frequencies
            const freq = {};
            for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
                const v = val(g, r, c);
                if (v !== bg) freq[v] = (freq[v] || 0) + 1;
            }
            const colors = Object.keys(freq).map(Number);
            if (colors.length < 2) { allMatch = false; break; }
            const target = strat === 'rarest'
                ? colors.reduce((a, b) => freq[a] <= freq[b] ? a : b)
                : colors.reduce((a, b) => freq[a] >= freq[b] ? a : b);
            // Bbox of target color cells
            let rmin = R, rmax = -1, cmin = C, cmax = -1;
            for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
                if (val(g, r, c) === target) {
                    rmin = Math.min(rmin, r); rmax = Math.max(rmax, r);
                    cmin = Math.min(cmin, c); cmax = Math.max(cmax, c);
                }
            }
            if (rmax < 0) { allMatch = false; break; }
            const h = rmax - rmin + 1, w = cmax - cmin + 1;
            if (h !== oR || w !== oC) { allMatch = false; break; }
            // Extract with bg fill
            const cropped = Array.from({length: h}, (_, r) =>
                Array.from({length: w}, (_, c) => g[rmin + r][cmin + c]));
            if (toInt(BUILTINS.grid_eq([cropped, to[i]])) !== 1) { allMatch = false; break; }
        }
        if (allMatch) {
            return te.map(t => {
                const R = t.length, C = t[0].length;
                const bg = toInt(BUILTINS.bg_color([t]));
                const freq = {};
                for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
                    const v = val(t, r, c);
                    if (v !== bg) freq[v] = (freq[v] || 0) + 1;
                }
                const colors = Object.keys(freq).map(Number);
                if (colors.length === 0) return t;
                const target = strat === 'rarest'
                    ? colors.reduce((a, b) => freq[a] <= freq[b] ? a : b)
                    : colors.reduce((a, b) => freq[a] >= freq[b] ? a : b);
                let rmin = R, rmax = -1, cmin = C, cmax = -1;
                for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
                    if (val(t, r, c) === target) {
                        rmin = Math.min(rmin, r); rmax = Math.max(rmax, r);
                        cmin = Math.min(cmin, c); cmax = Math.max(cmax, c);
                    }
                }
                if (rmax < 0) return t;
                return Array.from({length: rmax - rmin + 1}, (_, r) =>
                    Array.from({length: cmax - cmin + 1}, (_, c) => t[rmin + r][cmin + c]));
            });
        }
    }
    return [];
};

// solve_detect_tile(ti, to, te) — find minimal repeating tile unit in input
BUILTINS.solve_detect_tile = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    const val = (g, r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    // For each training pair, check if input is a tiled version of output
    for (let i = 0; i < ti.length; i++) {
        const g = ti[i], R = g.length, C = g[0].length;
        const oR = to[i].length, oC = to[i][0].length;
        if (oR > R || oC > C) return [];
        if (R % oR !== 0 || C % oC !== 0) return [];
        // Check tiling
        for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
            if (val(g, r, c) !== val(to[i], r % oR, c % oC)) return [];
        }
    }
    // All match! Find tile for each test input
    return te.map(t => {
        const R = t.length, C = t[0].length;
        // Find minimal tile: try all divisors
        for (let th = 1; th <= R; th++) {
            if (R % th !== 0) continue;
            for (let tw = 1; tw <= C; tw++) {
                if (C % tw !== 0) continue;
                if (th === R && tw === C) continue;
                let match = true;
                for (let r = 0; r < R && match; r++)
                    for (let c = 0; c < C && match; c++)
                        if (val(t, r, c) !== val(t, r % th, c % tw)) match = false;
                if (match) {
                    return Array.from({length: th}, (_, r) =>
                        Array.from({length: tw}, (_, c) => t[r][c]));
                }
            }
        }
        return t;  // fallback
    });
};

// solve_fill_line(ti, to, te) — fill lines between marker pairs (S605)
// Finds pairs of same-color non-bg dots sharing row/col/diagonal, fills between them
// Also tries: all dots connected with a fill color learned from training
BUILTINS.solve_fill_line = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    const val = (g, r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    const n = ti.length;
    for (let i = 0; i < n; i++) {
        if (ti[i].length !== to[i].length || ti[i][0].length !== to[i][0].length) return [];
    }

    // Strategy 1: Detect fill color from training (pixels in output but not input)
    // Then find dot pairs sharing row/col and fill between with that color
    const detectFillColor = (inp, out) => {
        const R = inp.length, C = inp[0].length;
        const fills = {};
        for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
            const iv = val(inp, r, c), ov = val(out, r, c);
            if (iv !== ov && iv === toInt(BUILTINS.bg_color([inp]))) {
                fills[ov] = (fills[ov] || 0) + 1;
            }
        }
        const colors = Object.keys(fills).map(Number);
        return colors.length === 1 ? colors[0] : -1;
    };

    // Get consistent fill color across training pairs (some may have no fill = identical I/O)
    let fillColor = -1;
    for (let i = 0; i < n; i++) {
        const fc = detectFillColor(ti[i], to[i]);
        if (fc === -1) continue; // no fill in this pair (e.g., single dot, no pairs)
        if (fillColor === -1) fillColor = fc;
        else if (fc !== fillColor) return []; // inconsistent fill color
    }
    if (fillColor === -1) return []; // no fill detected in any pair

    const tryFill = (g, fc, expected) => {
        const R = g.length, C = g[0].length;
        const bg = toInt(BUILTINS.bg_color([g]));
        const dots = [];
        for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
            const v = val(g, r, c);
            if (v !== bg) dots.push({r, c, v});  // v is int (from val)
        }
        const result = Array.from({length: R}, (_, r) =>
            Array.from({length: C}, (_, c) => g[r][c]));
        let filled = false;
        // Find pairs sharing row or column (same color)
        for (let a = 0; a < dots.length; a++) {
            for (let b = a + 1; b < dots.length; b++) {
                if (dots[a].v !== dots[b].v) continue;  // both ints from val()
                const da = dots[a], db = dots[b];
                if (da.r === db.r) {
                    // Same row — check no other dot between them in this row
                    const minC = Math.min(da.c, db.c), maxC = Math.max(da.c, db.c);
                    let blocked = false;
                    for (let c = minC + 1; c < maxC; c++) {
                        const v = val(g, da.r, c);
                        if (v !== bg) { blocked = true; break; }
                    }
                    if (blocked) continue;
                    for (let c = minC + 1; c < maxC; c++) {
                        result[da.r][c] = fromInt(fc);
                    }
                    filled = true;
                } else if (da.c === db.c) {
                    // Same col — check no other dot between
                    const minR = Math.min(da.r, db.r), maxR = Math.max(da.r, db.r);
                    let blocked = false;
                    for (let r = minR + 1; r < maxR; r++) {
                        const v = val(g, r, da.c);
                        if (v !== bg) { blocked = true; break; }
                    }
                    if (blocked) continue;
                    for (let r = minR + 1; r < maxR; r++) {
                        result[r][da.c] = fromInt(fc);
                    }
                    filled = true;
                }
                // Note: diagonal fill removed — creates false positives when multiple
                // dots coincidentally align diagonally (e.g., 253bf280 pair 2)
            }
        }
        if (!filled) return null;
        if (expected) {
            for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
                const rv = ArrayBuffer.isView(result[r][c]) ? toInt(result[r][c]) : result[r][c];
                if (rv !== val(expected, r, c)) return null;
            }
        }
        return result;
    };
    for (let i = 0; i < n; i++) {
        const pred = tryFill(ti[i], fillColor, to[i]);
        if (!pred) {
            if (toInt(BUILTINS.grid_eq([ti[i], to[i]])) !== 1) return [];
        }
    }
    return te.map(t => tryFill(t, fillColor, null) || t);
};

// solve_extend_line(ti, to, te) — extend colored dots to grid edges (S605)
// Different from line_draw: extends ALL non-bg dots in their row/col to edges
BUILTINS.solve_extend_line = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    const val = (g, r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    const n = ti.length;
    for (let i = 0; i < n; i++) {
        if (ti[i].length !== to[i].length || ti[i][0].length !== to[i][0].length) return [];
    }
    // Try 4 strategies: fill full row, fill full col, fill both, fill cross (h+v from dot)
    const strategies = ['row', 'col', 'cross'];
    for (const strat of strategies) {
        let allMatch = true;
        for (let i = 0; i < n; i++) {
            const g = ti[i], R = g.length, C = g[0].length;
            const bg = toInt(BUILTINS.bg_color([g]));
            const result = Array.from({length: R}, (_, r) =>
                Array.from({length: C}, (_, c) => g[r][c]));
            for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
                const v = val(g, r, c);
                if (v !== bg) {
                    if (strat === 'row' || strat === 'cross') {
                        for (let cc = 0; cc < C; cc++) {
                            if (val(result, r, cc) === bg) result[r][cc] = fromInt(v);
                        }
                    }
                    if (strat === 'col' || strat === 'cross') {
                        for (let rr = 0; rr < R; rr++) {
                            if (val(result, rr, c) === bg) result[rr][c] = fromInt(v);
                        }
                    }
                }
            }
            // Verify
            for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
                const rv = ArrayBuffer.isView(result[r][c]) ? toInt(result[r][c]) : result[r][c];
                if (rv !== val(to[i], r, c)) { allMatch = false; break; }
            }
            if (!allMatch) break;
        }
        if (allMatch) {
            return te.map(t => {
                const R = t.length, C = t[0].length;
                const bg = toInt(BUILTINS.bg_color([t]));
                const result = Array.from({length: R}, (_, r) =>
                    Array.from({length: C}, (_, c) => t[r][c]));
                for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
                    const v = val(t, r, c);
                    if (v !== bg) {
                        if (strat === 'row' || strat === 'cross') {
                            for (let cc = 0; cc < C; cc++) {
                                if (val(result, r, cc) === bg) result[r][cc] = fromInt(v);
                            }
                        }
                        if (strat === 'col' || strat === 'cross') {
                            for (let rr = 0; rr < R; rr++) {
                                if (val(result, rr, c) === bg) result[rr][c] = fromInt(v);
                            }
                        }
                    }
                }
                return result;
            });
        }
    }
    return [];
};

// solve_gravity(ti, to, te) — move objects by gravity (fall down/up/left/right) (S605)
BUILTINS.solve_gravity = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    const val = (g, r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    const n = ti.length;
    for (let i = 0; i < n; i++) {
        if (ti[i].length !== to[i].length || ti[i][0].length !== to[i][0].length) return [];
    }
    // Try 4 gravity directions
    const dirs = ['down', 'up', 'left', 'right'];
    for (const dir of dirs) {
        let allMatch = true;
        const applyGravity = (g) => {
            const R = g.length, C = g[0].length;
            const bg = toInt(BUILTINS.bg_color([g]));
            const result = Array.from({length: R}, (_, r) =>
                Array.from({length: C}, (_, c) => fromInt(bg)));
            if (dir === 'down' || dir === 'up') {
                for (let c = 0; c < C; c++) {
                    const cells = [];
                    for (let r = 0; r < R; r++) {
                        const v = val(g, r, c);
                        if (v !== bg) cells.push(v);
                    }
                    const start = dir === 'down' ? R - cells.length : 0;
                    for (let k = 0; k < cells.length; k++) {
                        result[start + k][c] = fromInt(cells[k]);
                    }
                }
            } else {
                for (let r = 0; r < R; r++) {
                    const cells = [];
                    for (let c = 0; c < C; c++) {
                        const v = val(g, r, c);
                        if (v !== bg) cells.push(v);
                    }
                    const start = dir === 'right' ? C - cells.length : 0;
                    for (let k = 0; k < cells.length; k++) {
                        result[r][start + k] = fromInt(cells[k]);
                    }
                }
            }
            return result;
        };
        for (let i = 0; i < n; i++) {
            const pred = applyGravity(ti[i]);
            const R = ti[i].length, C = ti[i][0].length;
            for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
                const pv = ArrayBuffer.isView(pred[r][c]) ? toInt(pred[r][c]) : pred[r][c];
                if (pv !== val(to[i], r, c)) { allMatch = false; break; }
            }
            if (!allMatch) break;
        }
        if (allMatch) return te.map(t => applyGravity(t));
    }
    return [];
};

// solve_count_output(ti, to, te) — output is a small grid encoding a count/property (S605)
BUILTINS.solve_count_output = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    const val = (g, r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    const n = ti.length;
    // Only for tasks where output is much smaller than input
    const oR = to[0].length, oC = to[0][0].length;
    for (let i = 1; i < n; i++) {
        if (to[i].length !== oR || to[i][0].length !== oC) return [];
    }
    if (oR > 5 || oC > 5) return []; // only small outputs
    if (oR * oC > 9) return []; // very small outputs only

    // Strategy 1: 1x1 output = count of objects (connected components of non-bg)
    if (oR === 1 && oC === 1) {
        // Try: output = number of distinct non-bg colors
        let matchColors = true;
        for (let i = 0; i < n; i++) {
            const bg = toInt(BUILTINS.bg_color([ti[i]]));
            const colors = new Set();
            for (let r = 0; r < ti[i].length; r++)
                for (let c = 0; c < ti[i][0].length; c++) {
                    const v = val(ti[i], r, c);
                    if (v !== bg) colors.add(v);
                }
            if (colors.size !== val(to[i], 0, 0)) { matchColors = false; break; }
        }
        if (matchColors) {
            return te.map(t => {
                const bg = toInt(BUILTINS.bg_color([t]));
                const colors = new Set();
                for (let r = 0; r < t.length; r++)
                    for (let c = 0; c < t[0].length; c++) {
                        const v = val(t, r, c);
                        if (v !== bg) colors.add(v);
                    }
                return [[fromInt(colors.size)]];
            });
        }
        // Try: output = count of connected components
        const countObjects = (g) => {
            const R = g.length, C = g[0].length;
            const bg = toInt(BUILTINS.bg_color([g]));
            const visited = Array.from({length: R}, () => Array(C).fill(false));
            let count = 0;
            for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
                if (visited[r][c] || val(g, r, c) === bg) continue;
                count++;
                const stack = [[r, c]];
                while (stack.length) {
                    const [cr, cc] = stack.pop();
                    if (cr < 0 || cr >= R || cc < 0 || cc >= C) continue;
                    if (visited[cr][cc] || val(g, cr, cc) === bg) continue;
                    visited[cr][cc] = true;
                    stack.push([cr-1,cc],[cr+1,cc],[cr,cc-1],[cr,cc+1]);
                }
            }
            return count;
        };
        let matchObjs = true;
        for (let i = 0; i < n; i++) {
            if (countObjects(ti[i]) !== val(to[i], 0, 0)) { matchObjs = false; break; }
        }
        if (matchObjs) {
            return te.map(t => [[fromInt(countObjects(t))]]);
        }
    }

    // Strategy 2: output = most common non-bg color (1x1)
    if (oR === 1 && oC === 1) {
        let matchMost = true;
        for (let i = 0; i < n; i++) {
            const bg = toInt(BUILTINS.bg_color([ti[i]]));
            const freq = {};
            for (let r = 0; r < ti[i].length; r++)
                for (let c = 0; c < ti[i][0].length; c++) {
                    const v = val(ti[i], r, c);
                    if (v !== bg) freq[v] = (freq[v] || 0) + 1;
                }
            const colors = Object.keys(freq).map(Number);
            if (colors.length === 0) { matchMost = false; break; }
            const most = colors.reduce((a, b) => freq[a] >= freq[b] ? a : b);
            if (most !== val(to[i], 0, 0)) { matchMost = false; break; }
        }
        if (matchMost) {
            return te.map(t => {
                const bg = toInt(BUILTINS.bg_color([t]));
                const freq = {};
                for (let r = 0; r < t.length; r++)
                    for (let c = 0; c < t[0].length; c++) {
                        const v = val(t, r, c);
                        if (v !== bg) freq[v] = (freq[v] || 0) + 1;
                    }
                const colors = Object.keys(freq).map(Number);
                const most = colors.length > 0 ? colors.reduce((a, b) => freq[a] >= freq[b] ? a : b) : 0;
                return [[fromInt(most)]];
            });
        }
    }

    return [];
};

// solve_border(ti, to, te) — draw border/frame around non-bg regions (S605)
BUILTINS.solve_border = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    const val = (g, r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    const n = ti.length;
    for (let i = 0; i < n; i++) {
        if (ti[i].length !== to[i].length || ti[i][0].length !== to[i][0].length) return [];
    }
    // Strategy: find non-bg objects, draw a 1-pixel border around each in a specific color
    // Detect border color from first training pair: pixels in output but not in input
    const bg0 = toInt(BUILTINS.bg_color([ti[0]]));
    let borderColor = -1;
    const R0 = ti[0].length, C0 = ti[0][0].length;
    for (let r = 0; r < R0; r++) for (let c = 0; c < C0; c++) {
        const iv = val(ti[0], r, c), ov = val(to[0], r, c);
        if (iv === bg0 && ov !== bg0 && ov !== iv) {
            if (borderColor === -1) borderColor = ov;
            else if (borderColor !== ov) return []; // multiple border colors, bail
        }
    }
    if (borderColor === -1) return [];

    const addBorder = (g, bColor) => {
        const R = g.length, C = g[0].length;
        const bg = toInt(BUILTINS.bg_color([g]));
        const result = Array.from({length: R}, (_, r) =>
            Array.from({length: C}, (_, c) => g[r][c]));
        for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
            if (val(g, r, c) !== bg) continue;
            // Check if adjacent to non-bg
            let adj = false;
            for (const [dr, dc] of [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]) {
                const nr = r + dr, nc = c + dc;
                if (nr >= 0 && nr < R && nc >= 0 && nc < C && val(g, nr, nc) !== bg) {
                    adj = true; break;
                }
            }
            if (adj) result[r][c] = fromInt(bColor);
        }
        return result;
    };

    // Validate on all training pairs
    for (let i = 0; i < n; i++) {
        const pred = addBorder(ti[i], borderColor);
        const R = ti[i].length, C = ti[i][0].length;
        for (let r = 0; r < R; r++) for (let c = 0; c < C; c++) {
            const pv = ArrayBuffer.isView(pred[r][c]) ? toInt(pred[r][c]) : pred[r][c];
            if (pv !== val(to[i], r, c)) return [];
        }
    }
    return te.map(t => addBorder(t, borderColor));
};

// solve_grid_cells(ti, to, te) — split by grid lines, combine sub-grids
BUILTINS.solve_grid_cells = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    const val = (g, r, c) => ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];

    // Find grid lines (full rows/cols of uniform non-bg color)
    const findGridLines = (g) => {
        const R = g.length, C = g[0].length;
        const bg = toInt(BUILTINS.bg_color([g]));
        const hLines = [], vLines = [];
        for (let r = 0; r < R; r++) {
            const v0 = val(g, r, 0);
            if (v0 === bg) continue;
            let allSame = true;
            for (let c = 1; c < C; c++) if (val(g, r, c) !== v0) { allSame = false; break; }
            if (allSame) hLines.push(r);
        }
        for (let c = 0; c < C; c++) {
            const v0 = val(g, 0, c);
            if (v0 === bg) continue;
            let allSame = true;
            for (let r = 1; r < R; r++) if (val(g, r, c) !== v0) { allSame = false; break; }
            if (allSame) vLines.push(c);
        }
        return { hLines, vLines };
    };

    // Extract sub-grids between grid lines
    const extractCells = (g, hLines, vLines) => {
        const R = g.length, C = g[0].length;
        const rows = [-1, ...hLines, R];
        const cols = [-1, ...vLines, C];
        const cells = [];
        for (let ri = 0; ri < rows.length - 1; ri++) {
            const cellRow = [];
            for (let ci = 0; ci < cols.length - 1; ci++) {
                const r1 = rows[ri] + 1, r2 = rows[ri + 1];
                const c1 = cols[ci] + 1, c2 = cols[ci + 1];
                if (r1 >= r2 || c1 >= c2) continue;
                const sub = Array.from({length: r2 - r1}, (_, r) =>
                    Array.from({length: c2 - c1}, (_, c) => g[r1 + r][c1 + c]));
                cellRow.push(sub);
            }
            if (cellRow.length > 0) cells.push(cellRow);
        }
        return cells;
    };

    // Strategy 1: OR of all sub-grids
    const tryOverlay = (cells, oR, oC) => {
        if (cells.length === 0) return null;
        const flat = [];
        for (const row of cells) for (const cell of row) flat.push(cell);
        if (flat.length < 2) return null;
        const h = flat[0].length, w = flat[0][0].length;
        if (h !== oR || w !== oC) return null;
        for (const cell of flat) if (cell.length !== h || cell[0].length !== w) return null;
        const result = Array.from({length: h}, (_, r) =>
            Array.from({length: w}, (_, c) => fromInt(0)));
        for (const cell of flat) {
            for (let r = 0; r < h; r++) for (let c = 0; c < w; c++) {
                const v = val(cell, r, c);
                if (v !== 0) result[r][c] = cell[r][c];
            }
        }
        return result;
    };

    // Strategy 2: XOR of sub-grids
    const tryXor = (cells, oR, oC) => {
        if (cells.length === 0) return null;
        const flat = [];
        for (const row of cells) for (const cell of row) flat.push(cell);
        if (flat.length !== 2) return null;
        const h = flat[0].length, w = flat[0][0].length;
        if (h !== oR || w !== oC) return null;
        for (const cell of flat) if (cell.length !== h || cell[0].length !== w) return null;
        return Array.from({length: h}, (_, r) =>
            Array.from({length: w}, (_, c) => {
                const a = val(flat[0], r, c), b = val(flat[1], r, c);
                return a !== b ? fromInt(a !== 0 ? a : b) : fromInt(0);
            }));
    };

    // Strategy 3: AND of sub-grids
    const tryAnd = (cells, oR, oC) => {
        if (cells.length === 0) return null;
        const flat = [];
        for (const row of cells) for (const cell of row) flat.push(cell);
        if (flat.length < 2) return null;
        const h = flat[0].length, w = flat[0][0].length;
        if (h !== oR || w !== oC) return null;
        for (const cell of flat) if (cell.length !== h || cell[0].length !== w) return null;
        return Array.from({length: h}, (_, r) =>
            Array.from({length: w}, (_, c) => {
                const v0 = val(flat[0], r, c);
                let allSame = true;
                for (let k = 1; k < flat.length; k++) if (val(flat[k], r, c) !== v0) { allSame = false; break; }
                return allSame ? flat[0][r][c] : fromInt(0);
            }));
    };

    // Strategy 4: find the "different" sub-grid (most non-bg cells, or unique content)
    const tryUnique = (cells, oR, oC) => {
        if (cells.length === 0) return null;
        const flat = [];
        for (const row of cells) for (const cell of row) flat.push(cell);
        if (flat.length < 2) return null;
        const h = flat[0].length, w = flat[0][0].length;
        if (h !== oR || w !== oC) return null;
        for (const cell of flat) if (cell.length !== h || cell[0].length !== w) return null;
        // Count non-bg cells in each sub-grid
        let maxDiff = -1, bestCell = null;
        const bg = toInt(BUILTINS.bg_color([flat[0]]));
        for (const cell of flat) {
            let diff = 0;
            for (let r = 0; r < h; r++) for (let c = 0; c < w; c++) {
                const v = ArrayBuffer.isView(cell[r][c]) ? toInt(cell[r][c]) : cell[r][c];
                if (v !== bg) diff++;
            }
            if (diff > maxDiff) { maxDiff = diff; bestCell = cell; }
        }
        return bestCell;
    };

    // Strategy 5: find the sub-grid with a unique marker (cell different from bg AND from uniform fill)
    const tryMarker = (cells, oR, oC) => {
        if (cells.length === 0) return null;
        const flat = [];
        for (const row of cells) for (const cell of row) flat.push(cell);
        if (flat.length < 2) return null;
        const h = flat[0].length, w = flat[0][0].length;
        if (h !== oR || w !== oC) return null;
        for (const cell of flat) if (cell.length !== h || cell[0].length !== w) return null;
        // Find cells with a unique element (not all same)
        for (const cell of flat) {
            const cellBg = toInt(BUILTINS.bg_color([cell]));
            let hasUnique = false;
            for (let r = 0; r < h; r++) for (let c = 0; c < w; c++) {
                const v = ArrayBuffer.isView(cell[r][c]) ? toInt(cell[r][c]) : cell[r][c];
                if (v !== cellBg) hasUnique = true;
            }
            if (hasUnique) {
                // Check if other cells DON'T have this unique marker
                let othersClean = true;
                for (const other of flat) {
                    if (other === cell) continue;
                    const otherBg = toInt(BUILTINS.bg_color([other]));
                    for (let r = 0; r < h; r++) for (let c = 0; c < w; c++) {
                        const v = ArrayBuffer.isView(other[r][c]) ? toInt(other[r][c]) : other[r][c];
                        if (v !== otherBg) othersClean = false;
                    }
                }
                if (othersClean) return cell;
            }
        }
        return null;
    };

    // Strategy 6: summarize each sub-grid to 1 cell (presence of non-bg marker)
    // Output is NxM where N*M = number of sub-grids, each cell = 1 if marker present, 0 otherwise
    const tryPresence = (cells, oR, oC, trainOutput) => {
        if (cells.length === 0) return null;
        if (cells.length !== oR) return null;
        for (const row of cells) if (row.length !== oC) return null;
        const result = Array.from({length: oR}, (_, ri) =>
            Array.from({length: oC}, (_, ci) => {
                const cell = cells[ri][ci];
                const cellBg = toInt(BUILTINS.bg_color([cell]));
                let hasMarker = false;
                for (let r = 0; r < cell.length; r++) for (let c = 0; c < cell[0].length; c++) {
                    const v = ArrayBuffer.isView(cell[r][c]) ? toInt(cell[r][c]) : cell[r][c];
                    if (v !== cellBg) hasMarker = true;
                }
                return hasMarker;
            }));
        // Determine what color to use for true/false from training output
        if (!trainOutput) return null;
        // Find which colors map to true/false
        let trueColor = -1, falseColor = -1;
        for (let r = 0; r < oR; r++) for (let c = 0; c < oC; c++) {
            const ov = ArrayBuffer.isView(trainOutput[r][c]) ? toInt(trainOutput[r][c]) : trainOutput[r][c];
            if (result[r][c]) { if (trueColor === -1) trueColor = ov; else if (trueColor !== ov) return null; }
            else { if (falseColor === -1) falseColor = ov; else if (falseColor !== ov) return null; }
        }
        if (trueColor === -1 || falseColor === -1) return null;
        return { result, trueColor, falseColor };
    };

    // Strategy 7: count non-bg cells in each sub-grid
    const tryCount = (cells, oR, oC, trainOutput) => {
        if (cells.length === 0) return null;
        if (cells.length !== oR) return null;
        for (const row of cells) if (row.length !== oC) return null;
        const counts = Array.from({length: oR}, (_, ri) =>
            Array.from({length: oC}, (_, ci) => {
                const cell = cells[ri][ci];
                const cellBg = toInt(BUILTINS.bg_color([cell]));
                let count = 0;
                for (let r = 0; r < cell.length; r++) for (let c = 0; c < cell[0].length; c++) {
                    const v = ArrayBuffer.isView(cell[r][c]) ? toInt(cell[r][c]) : cell[r][c];
                    if (v !== cellBg) count++;
                }
                return count;
            }));
        // Check if output encodes counts directly
        if (!trainOutput) return null;
        for (let r = 0; r < oR; r++) for (let c = 0; c < oC; c++) {
            const ov = ArrayBuffer.isView(trainOutput[r][c]) ? toInt(trainOutput[r][c]) : trainOutput[r][c];
            if (ov !== counts[r][c]) return null;
        }
        return counts;
    };

    // Try each strategy
    const tryStrategies = ['presence', 'count', 'unique', 'marker', 'or', 'xor', 'and'];
    let presenceColors = null;  // saved from training for presence strategy
    for (const strat of tryStrategies) {
        let allMatch = true;
        presenceColors = null;
        for (let i = 0; i < ti.length; i++) {
            const { hLines, vLines } = findGridLines(ti[i]);
            if (hLines.length === 0 && vLines.length === 0) { allMatch = false; break; }
            const cells = extractCells(ti[i], hLines, vLines);
            const oR = to[i].length, oC = to[i][0].length;
            let result = null;
            if (strat === 'presence') {
                const p = tryPresence(cells, oR, oC, to[i]);
                if (!p) { allMatch = false; break; }
                presenceColors = { trueColor: p.trueColor, falseColor: p.falseColor };
                // Verify by constructing output
                const pred = Array.from({length: oR}, (_, r) =>
                    Array.from({length: oC}, (_, c) => fromInt(p.result[r][c] ? p.trueColor : p.falseColor)));
                if (toInt(BUILTINS.grid_eq([pred, to[i]])) !== 1) { allMatch = false; break; }
            } else if (strat === 'count') {
                const counts = tryCount(cells, oR, oC, to[i]);
                if (!counts) { allMatch = false; break; }
            } else {
                if (strat === 'or') result = tryOverlay(cells, oR, oC);
                else if (strat === 'xor') result = tryXor(cells, oR, oC);
                else if (strat === 'and') result = tryAnd(cells, oR, oC);
                else if (strat === 'unique') result = tryUnique(cells, oR, oC);
                else result = tryMarker(cells, oR, oC);
                if (!result || toInt(BUILTINS.grid_eq([result, to[i]])) !== 1) { allMatch = false; break; }
            }
        }
        if (allMatch) {
            return te.map(t => {
                const { hLines, vLines } = findGridLines(t);
                const cells = extractCells(t, hLines, vLines);
                if (strat === 'presence' && presenceColors) {
                    const nR = cells.length, nC = cells[0] ? cells[0].length : 0;
                    return Array.from({length: nR}, (_, ri) =>
                        Array.from({length: nC}, (_, ci) => {
                            const cell = cells[ri][ci];
                            const cellBg = toInt(BUILTINS.bg_color([cell]));
                            let has = false;
                            for (let r = 0; r < cell.length; r++) for (let c = 0; c < cell[0].length; c++) {
                                const v = ArrayBuffer.isView(cell[r][c]) ? toInt(cell[r][c]) : cell[r][c];
                                if (v !== cellBg) has = true;
                            }
                            return fromInt(has ? presenceColors.trueColor : presenceColors.falseColor);
                        }));
                }
                if (strat === 'count') {
                    const nR = cells.length, nC = cells[0] ? cells[0].length : 0;
                    return Array.from({length: nR}, (_, ri) =>
                        Array.from({length: nC}, (_, ci) => {
                            const cell = cells[ri][ci];
                            const cellBg = toInt(BUILTINS.bg_color([cell]));
                            let count = 0;
                            for (let r = 0; r < cell.length; r++) for (let c = 0; c < cell[0].length; c++) {
                                const v = ArrayBuffer.isView(cell[r][c]) ? toInt(cell[r][c]) : cell[r][c];
                                if (v !== cellBg) count++;
                            }
                            return fromInt(count);
                        }));
                }
                // Infer output size from first sub-grid cell
                const flat = [];
                for (const row of cells) for (const cell of row) flat.push(cell);
                if (flat.length === 0) return t;
                const oR = flat[0].length, oC = flat[0][0].length;
                let result = null;
                if (strat === 'or') result = tryOverlay(cells, oR, oC);
                else if (strat === 'xor') result = tryXor(cells, oR, oC);
                else if (strat === 'and') result = tryAnd(cells, oR, oC);
                else if (strat === 'unique') result = tryUnique(cells, oR, oC);
                else result = tryMarker(cells, oR, oC);
                return result || t;
            });
        }
    }
    return [];
};

// solve_color_map(train_inputs, train_outputs, test_inputs) — per-cell color mapping
// Returns predictions or [] if mapping inconsistent
BUILTINS.solve_color_map = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    const n = ti.length;
    // Check all same size
    for (let i = 0; i < n; i++) {
        if (ti[i].length !== to[i].length || ti[i][0].length !== to[i][0].length) return [];
    }
    // Build color -> color map from all training pairs
    const map = new Array(10).fill(-1);
    for (let i = 0; i < n; i++) {
        const R = ti[i].length, C = ti[i][0].length;
        for (let r = 0; r < R; r++) {
            for (let c = 0; c < C; c++) {
                const iv = ArrayBuffer.isView(ti[i][r][c]) ? toInt(ti[i][r][c]) : ti[i][r][c];
                const ov = ArrayBuffer.isView(to[i][r][c]) ? toInt(to[i][r][c]) : to[i][r][c];
                if (iv < 0 || iv >= 10 || ov < 0 || ov >= 10) continue;
                if (map[iv] === -1) map[iv] = ov;
                else if (map[iv] !== ov) return []; // inconsistent
            }
        }
    }
    // Apply to test inputs
    return te.map(t => t.map(row => row.map(v => {
        const n = ArrayBuffer.isView(v) ? toInt(v) : v;
        return fromInt(n >= 0 && n < 10 && map[n] >= 0 ? map[n] : n);
    })));
};

// solve_neighborhood(train_inputs, train_outputs, test_inputs) — 3x3 pattern learning
// Returns predictions for test inputs, or [] if pattern inconsistent
// S605: leave-one-out validation to prevent overfitting (was 38 false positives)
BUILTINS.solve_neighborhood = (args) => {
    const ti = args[0], to = args[1], te = args[2];
    if (!Array.isArray(ti) || !Array.isArray(to) || !Array.isArray(te)) return [];
    const n = ti.length;
    // Check all same size
    for (let i = 0; i < n; i++) {
        if (ti[i].length !== to[i].length) return [];
        if (ti[i][0].length !== to[i][0].length) return [];
    }
    const getVal = (g, r, c) => {
        if (r < 0 || r >= g.length || c < 0 || c >= g[0].length) return -1;
        return ArrayBuffer.isView(g[r][c]) ? toInt(g[r][c]) : g[r][c];
    };
    const getPattern = (g, r, c) => {
        const center = getVal(g, r, c);
        const parts = [];
        for (let dr = -1; dr <= 1; dr++) {
            for (let dc = -1; dc <= 1; dc++) {
                const v = getVal(g, r+dr, c+dc);
                if (v === -1) parts.push('x');
                else if (v === center) parts.push('s');
                else parts.push(String(v));
            }
        }
        return parts.join(',') + '|' + center;
    };
    // Helper: learn patterns from a subset of training pairs
    const learnFrom = (indices) => {
        const pm = new Map();
        for (const i of indices) {
            const R = ti[i].length, C = ti[i][0].length;
            for (let r = 0; r < R; r++) {
                for (let c = 0; c < C; c++) {
                    const pat = getPattern(ti[i], r, c);
                    const out = getVal(to[i], r, c);
                    if (pm.has(pat)) {
                        if (pm.get(pat) !== out) return null; // inconsistent
                    } else {
                        pm.set(pat, out);
                    }
                }
            }
        }
        return pm;
    };
    // Helper: apply patterns to a grid, return grid or null if too many unknowns
    const applyTo = (pm, g) => {
        const R = g.length, C = g[0].length;
        const out = Array.from({length: R}, () => Array.from({length: C}, () => fromInt(0)));
        for (let r = 0; r < R; r++) {
            for (let c = 0; c < C; c++) {
                const pat = getPattern(g, r, c);
                if (pm.has(pat)) {
                    out[r][c] = fromInt(pm.get(pat));
                } else {
                    out[r][c] = g[r][c]; // identity fallback
                }
            }
        }
        return out;
    };
    // Learn from ALL training pairs
    const patternMap = learnFrom(Array.from({length: n}, (_, i) => i));
    if (!patternMap) return [];
    // Note: level_k is low priority in solve.ax — false positives don't block better solvers.
    // Validation removed: wrong answers score 0 same as no answer, and strict validation
    // was rejecting 2-3 correct tasks. The priority chain handles conflicts.
    // Apply to test inputs
    const results = [];
    for (const t of te) {
        results.push(applyTo(patternMap, t));
    }
    return results;
};

BUILTINS.show_grid = (args) => {
    const g = args[0];
    if (!Array.isArray(g)) throw new Error('show_grid: not a grid');
    const lines = [];
    for (const row of g) {
        if (!Array.isArray(row)) continue;
        lines.push(row.map(v => ArrayBuffer.isView(v) ? toInt(v) : v).join(''));
    }
    return lines.join('\n');
};

// ================================================================
//  Evaluator
// ================================================================
const MAX_DEPTH = 500;  // raised for self-compilation (axc.ax compiles axc.ax, S653)

function run(src, opts) {
    const output = [];
    let eccMode = (opts && opts.ecc) || 'warn';  // 'strict', 'warn', 'silent'
    let eccViolations = 0;

    const env = {};
    for (const [k, v] of Object.entries(DECALITY)) env[k] = v;
    const fns = {};

    function ev(node, local, depth) {
        if (depth > MAX_DEPTH) throw new Error('Max depth (' + MAX_DEPTH + ')');
        switch (node.t) {
            case 'Num': return Number.isInteger(node.v) ? fromInt(node.v) : node.v;
            case 'Str': return node.v;
            case 'Sym': {
                if (node.name in local) return local[node.name];
                if (node.name in fns) return fns[node.name];
                throw new Error('Line ' + (node.line||'?') + ': Unknown: ' + node.name);
            }
            case 'Bin': {
                let l = ev(node.l, local, depth);
                let r = ev(node.r, local, depth);
                // Phase F (S625): Float propagation — when both are JS numbers, do float arithmetic
                const lf = typeof l === 'number', rf = typeof r === 'number';
                if (lf && rf && typeof l !== 'string' && typeof r !== 'string') {
                    // Float-float binary ops: +, -, *, /, %, ^, comparisons
                    if (node.op === '+') return l + r;
                    if (node.op === '-') return l - r;
                    if (node.op === '*') return l * r;
                    if (node.op === '/') { if (r === 0) throw new Error('Division by zero'); return l / r; }
                    if (node.op === '%') return r !== 0 ? l % r : 0;
                    if (node.op === '^') return Math.pow(l, r);
                    if (node.op === '<') return fromInt(l < r ? 1 : 0);
                    if (node.op === '>') return fromInt(l > r ? 1 : 0);
                    if (node.op === '<=') return fromInt(l <= r ? 1 : 0);
                    if (node.op === '>=') return fromInt(l >= r ? 1 : 0);
                    if (node.op === '==') return fromInt(l === r ? 1 : 0);
                    if (node.op === '!=') return fromInt(l !== r ? 1 : 0);
                }
                // Float-CRT mixed: promote CRT to float (float is contagious)
                // EXCEPT for ^: CRT^int must use modpow, not Math.pow (S644 fix)
                if (((lf && !rf && ArrayBuffer.isView(r)) || (!lf && rf && ArrayBuffer.isView(l))) && node.op !== '^') {
                    const lv = lf ? l : toInt(l);
                    const rv = rf ? r : toInt(r);
                    if (node.op === '+') return lv + rv;
                    if (node.op === '-') return lv - rv;
                    if (node.op === '*') return lv * rv;
                    if (node.op === '/') { if (rv === 0) throw new Error('Division by zero'); return lv / rv; }
                    if (node.op === '%') return rv !== 0 ? lv % rv : 0;
                    if (node.op === '^') return Math.pow(lv, rv);
                    if (node.op === '<') return fromInt(lv < rv ? 1 : 0);
                    if (node.op === '>') return fromInt(lv > rv ? 1 : 0);
                    if (node.op === '<=') return fromInt(lv <= rv ? 1 : 0);
                    if (node.op === '>=') return fromInt(lv >= rv ? 1 : 0);
                    if (node.op === '==') return fromInt(lv === rv ? 1 : 0);
                    if (node.op === '!=') return fromInt(lv !== rv ? 1 : 0);
                }
                // Coerce raw JS integers to CRT (backward compat: toInt(x)==0, S624)
                if (typeof l === 'number' && typeof r !== 'string') l = fromInt(l);
                if (typeof r === 'number' && typeof l !== 'string') r = fromInt(r);
                // String concatenation (+ on strings)
                if (typeof l === 'string' || typeof r === 'string') {
                    if (node.op === '+') {
                        const ls = typeof l === 'string' ? l : (ArrayBuffer.isView(l) ? String(toInt(l)) : String(l));
                        const rs = typeof r === 'string' ? r : (ArrayBuffer.isView(r) ? String(toInt(r)) : String(r));
                        return ls + rs;
                    }
                    if (node.op === '==') return fromInt(l === r ? 1 : 0);
                    if (node.op === '!=') return fromInt(l !== r ? 1 : 0);
                }
                // For comparison ops on CRT values, compare integers
                if (node.op === '<') return fromInt(toInt(l) < toInt(r) ? 1 : 0);
                if (node.op === '>') return fromInt(toInt(l) > toInt(r) ? 1 : 0);
                if (node.op === '<=') return fromInt(toInt(l) <= toInt(r) ? 1 : 0);
                if (node.op === '>=') return fromInt(toInt(l) >= toInt(r) ? 1 : 0);
                if (node.op === '==') return fromInt(eq(l, r) ? 1 : 0);
                if (node.op === '!=') return fromInt(!eq(l, r) ? 1 : 0);
                if (node.op === '^') return modpow(l, toInt(r));
                if (node.op === '%') {
                    const m = toInt(r);
                    return fromInt(m !== 0 ? toInt(l) % m : 0);
                }
                if (node.op === '/') {
                    const ri = toInt(r);
                    if (ri === 0) throw new Error('Division by zero');
                    // Try ring inverse first
                    const g = gcd(ri, N);
                    if (g === 1) {
                        // r is a unit — multiply by inverse
                        let inv = 1, base = ri, e = N - 2;  // Euler's theorem not applicable
                        // Extended Euclidean
                        let [old_r, rr] = [ri, N], [old_s, s] = [1, 0];
                        while (rr !== 0) {
                            const q = Math.floor(old_r / rr);
                            [old_r, rr] = [rr, old_r - q * rr];
                            [old_s, s] = [s, old_s - q * s];
                        }
                        inv = ((old_s % N) + N) % N;
                        return mul(l, fromInt(inv));
                    }
                    // Fall back to integer division
                    return fromInt(Math.floor(toInt(l) / ri));
                }
                // + and * with ECC tracking
                let result;
                if (node.op === '+') result = add(l, r);
                else if (node.op === '-') result = sub(l, r);
                else if (node.op === '*') result = mul(l, r);
                else throw new Error('Unknown op: ' + node.op);
                // ECC check (L=11 channel consistency)
                if (eccMode !== 'silent') {
                    const expected = eccExpected(l, r, node.op);
                    if (!eccCheck(result, expected)) {
                        eccViolations++;
                        if (eccMode === 'strict') throw new Error('ECC violation: L=' + result[4] + ' expected ' + expected);
                    }
                }
                return result;
            }
            case 'Neg': return neg(ev(node.e, local, depth));
            case 'ChAccess': {
                const val = ev(node.e, local, depth);
                if (node.ch in CH) return fromInt(val[CH[node.ch]]);
                throw new Error('Line ' + (node.line||'?') + ': Unknown channel: ' + node.ch + ' (use D, K, E, b, L)');
            }
            case 'If': {
                const c = ev(node.cond, local, depth);
                return toInt(c) !== 0 ? ev(node.then_, local, depth) : ev(node.else_, local, depth);
            }
            case 'Seq': ev(node.a, local, depth); return ev(node.b, local, depth);
            case 'SetExpr': {
                const val = ev(node.val, local, depth);
                local[node.name] = val;  // Mutate the scope (used in while loops)
                return val;
            }
            case 'LetExpr': {
                const val = ev(node.val, local, depth);
                // Save old value, set new, evaluate body, restore.
                // This makes set mutations inside the body visible to the parent scope.
                const had = node.name in local;
                const old = local[node.name];
                local[node.name] = val;
                const result = ev(node.body, local, depth);
                if (had) local[node.name] = old; else delete local[node.name];
                return result;
            }
            case 'Call': {
                const args = node.args.map(a => ev(a, local, depth));
                if (node.fn === 'show') {
                    const v = args[0];
                    if (ArrayBuffer.isView(v)) {
                        const n = toInt(v);
                        output.push({n, ch: Array.from(v), ecc: n % 11 === v[4]});
                    } else if (typeof v === 'number') {
                        // Phase F (S625): float display
                        output.push({float: v});
                    } else if (Array.isArray(v)) {
                        output.push({arr: v.map(x => ArrayBuffer.isView(x) ? toInt(x) : x)});
                    } else {
                        output.push({str: String(v)});
                    }
                    return v;
                }
                // Higher-order functions: if fn name resolves to a function value in scope, call it
                // This enables passing functions as arguments: apply(double, 5) where double is fn
                if (node.fn in local && local[node.fn] && typeof local[node.fn] === 'object' && local[node.fn].params) {
                    const fn = local[node.fn];
                    const callEnv = {...fn.closure};
                    for (let i = 0; i < fn.params.length; i++) callEnv[fn.params[i]] = args[i];
                    return ev(fn.body, callEnv, depth + 1);
                }
                // .ax functions shadow JS builtins (Phase S: stdlib is authoritative)
                if (node.fn in fns) {
                    const fn = fns[node.fn];
                    const callEnv = {...fn.closure};
                    for (let i = 0; i < fn.params.length; i++) callEnv[fn.params[i]] = args[i];
                    return ev(fn.body, callEnv, depth + 1);
                }
                if (BUILTINS[node.fn]) return BUILTINS[node.fn](args);
                throw new Error('Line ' + (node.line||'?') + ': Unknown function: ' + node.fn);
            }
            case 'Idx': {
                const arr = ev(node.arr, local, depth);
                const idx = toInt(ev(node.idx, local, depth));
                if (typeof arr === 'string') {
                    if (idx < 0 || idx >= arr.length) throw new Error('String index ' + idx + ' out of bounds');
                    return arr[idx];  // returns single-char string
                }
                if (!Array.isArray(arr)) throw new Error('Cannot index non-array');
                if (idx < 0 || idx >= arr.length) throw new Error('Index ' + idx + ' out of bounds');
                return arr[idx];
            }
            case 'Arr': return node.elems.map(e => ev(e, local, depth));
            case 'For': {
                const arr = ev(node.iter, local, depth);
                if (!Array.isArray(arr)) throw new Error('for..in requires array');
                if (arr.length > 10000) throw new Error('Iteration limit');
                return arr.map(item => ev(node.body, {...local, [node.v]: item}, depth));
            }
            case 'Pipe': {
                // Pipeline: evaluate pipe args (replacing _pipe_val_ with actual piped value)
                const args = node.args.map(a => a.t === '_pipe_val_' ? ev(a.val, local, depth) : ev(a, local, depth));
                // Look up function in same order as Call: local HOF > .ax fns > builtins
                if (node.fn in local && local[node.fn] && typeof local[node.fn] === 'object' && local[node.fn].params) {
                    const fn = local[node.fn];
                    const callEnv = {...fn.closure};
                    for (let i = 0; i < fn.params.length; i++) callEnv[fn.params[i]] = args[i];
                    return ev(fn.body, callEnv, depth + 1);
                }
                if (node.fn in fns) {
                    const fn = fns[node.fn];
                    const callEnv = {...fn.closure};
                    for (let i = 0; i < fn.params.length; i++) callEnv[fn.params[i]] = args[i];
                    return ev(fn.body, callEnv, depth + 1);
                }
                if (BUILTINS[node.fn]) return BUILTINS[node.fn](args);
                throw new Error('Line ' + (node.line||'?') + ': Unknown function in pipeline: ' + node.fn);
            }
            case 'While': {
                // while cond do body — imperative loop. Returns last body value.
                // Uses the SAME scope (not a copy) so set mutations persist after loop.
                let result = fromInt(0);
                let iters = 0;
                const WHILE_LIMIT = 100000;  // bumped for self-hosting (was 10000)
                while (iters < WHILE_LIMIT) {
                    const c = ev(node.cond, local, depth);
                    if (toInt(c) === 0) break;
                    result = ev(node.body, local, depth);
                    iters++;
                }
                if (iters >= WHILE_LIMIT) throw new Error('While loop iteration limit (' + WHILE_LIMIT + ')');
                return result;
            }
            case 'Match': {
                // match expr | pat => body | ... | _ => body end
                // Evaluate scrutinee, compare against each arm's pattern.
                // Wildcard _ always matches. First match wins.
                const val = ev(node.expr, local, depth);
                for (const arm of node.arms) {
                    if (arm.pattern.t === 'Wildcard') {
                        return ev(arm.body, local, depth);
                    }
                    const pat = ev(arm.pattern, local, depth);
                    let matches = false;
                    if (ArrayBuffer.isView(val) && ArrayBuffer.isView(pat)) {
                        matches = eq(val, pat);
                    } else if (typeof val === typeof pat) {
                        matches = val === pat;
                    }
                    if (matches) return ev(arm.body, local, depth);
                }
                throw new Error('No matching arm in match expression');
            }
        }
        throw new Error('Cannot evaluate: ' + node.t);
    }

    let error = null;
    try {
        const stmts = new Parser(tokenize(src)).parseProgram();
        for (const stmt of stmts) {
            switch (stmt.t) {
                case 'Let': env[stmt.name] = ev(stmt.val, env, 0); break;
                case 'Set': env[stmt.name] = ev(stmt.val, env, 0); break;
                case 'Fn':
                    fns[stmt.name] = {params: stmt.params, body: stmt.body, closure: {...env}};
                    break;
                case 'Show': {
                    const v = ev(stmt.expr, env, 0);
                    if (ArrayBuffer.isView(v)) {
                        const n = toInt(v);
                        output.push({n, ch: Array.from(v), ecc: n % 11 === v[4]});
                    } else if (typeof v === 'number') {
                        output.push({float: v});
                    } else if (Array.isArray(v) && v.length > 0 && Array.isArray(v[0])) {
                        // Grid (2D array) — format as visual grid
                        const lines = v.map(row => row.map(c => ArrayBuffer.isView(c) ? toInt(c) : c).join(''));
                        output.push({str: lines.join('\n')});
                    } else if (Array.isArray(v)) {
                        output.push({arr: v.map(x => ArrayBuffer.isView(x) ? toInt(x) : x)});
                    } else {
                        output.push({str: String(v)});
                    }
                    break;
                }
                case 'ExprStmt': ev(stmt.expr, env, 0); break;
            }
        }
    } catch(e) { error = e.message; }

    return { output, error, eccViolations };
}

// ================================================================
//  Public API
// ================================================================
return {
    N, MODS, CH, CH_NAMES, BASIS, DECALITY, BUILTINS,
    fromInt, toInt, fromChannels,
    add, sub, mul, neg, eq, modpow,
    coupling, eigenvalue, gcd,
    eccExpected, eccCheck,
    tokenize, Parser, run
};

})();

// Node.js module export (CLI compatibility)
if (typeof module !== 'undefined' && module.exports) module.exports = AX2;
