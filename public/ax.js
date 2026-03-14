// ax.js — The .ax Language Interpreter
// ONE FILE. Every page, CLI, and tool that speaks .ax includes this.
// 970200 = 2^3 * 3^2 * 5^2 * 7^2 * 11 = TRUE FORM
// S465: extracted from repl.html. Single source of truth.

const AX = (function() {
'use strict';

let N = 970200;
let CRT_MODS = [8, 9, 25, 49, 11];
let _rawMode = false; // raw_mode(1): regular arithmetic. raw_mode(0): ring arithmetic (default).
let _wasm = null; // Phase W v0.2: WASM module for native-speed ring ops (S739)
const TRUE_N = 970200; // WASM only works for TRUE FORM

function factorPrimePowers(n) {
    n = Math.abs(Math.round(n));
    const factors = [];
    for (let p = 2; p * p <= n; p++) {
        if (n % p === 0) {
            let pk = 1;
            while (n % p === 0) { pk *= p; n /= p; }
            factors.push(pk);
        }
    }
    if (n > 1) factors.push(n);
    return factors;
}

function setRing(newN) {
    newN = Math.abs(Math.round(newN));
    if (newN < 2) newN = 2;
    N = newN;
    CRT_MODS = factorPrimePowers(N);
}

// ================================================================
//  Ring Arithmetic
// ================================================================
function ringMod(x) { x = Math.round(x); return ((x % N) + N) % N; }

function modPow(base, exp) {
    if (_wasm && N === TRUE_N) return _wasm._wasm_modpow(Math.round(base), Math.round(exp));
    base = ((Math.round(base) % N) + N) % N;
    exp = Math.round(exp);
    if (exp < 0) return 0;
    let r = 1;
    while (exp > 0) {
        if (exp & 1) r = (r * base) % N;
        exp >>= 1;
        base = (base * base) % N;
    }
    return r;
}

function gcd(a, b) {
    if (_wasm && N === TRUE_N) return _wasm._wasm_gcd(Math.abs(Math.round(a)), Math.abs(Math.round(b)));
    a = Math.abs(Math.round(a)); b = Math.abs(Math.round(b));
    while (b) { [a, b] = [b, a % b]; }
    return a;
}

function coupling(n) {
    if (_wasm && N === TRUE_N) return _wasm._wasm_coupling(ringMod(n));
    return N / gcd(ringMod(n), N);
}

function crt(n) {
    if (_wasm && N === TRUE_N) {
        const ptr = _wasm._wasm_decompose(ringMod(n));
        const r = [];
        for (let i = 0; i < 5; i++) r.push(_wasm.getValue(ptr + i*4, 'i32'));
        return r;
    }
    const r = ringMod(n);
    return CRT_MODS.map(m => r % m);
}

function eigenvalue(n) {
    if (_wasm && N === TRUE_N) return _wasm._wasm_eigenvalue(ringMod(n));
    const c = crt(n), P = Math.PI;
    return c.reduce((sum, ci, i) => sum + 2*Math.cos(2*P*ci/CRT_MODS[i]), 0);
}

function mirror(n) {
    if (_wasm && N === TRUE_N) return _wasm._wasm_mirror(ringMod(n));
    return ringMod(N - ringMod(n));
}

function eulerPhi(n) {
    n = Math.abs(Math.round(n));
    if (n < 1) return 0;
    let result = n;
    for (let p = 2; p * p <= n; p++) {
        if (n % p === 0) {
            while (n % p === 0) n /= p;
            result -= result / p;
        }
    }
    if (n > 1) result -= result / n;
    return Math.round(result);
}

function multOrder(n) {
    if (_wasm && N === TRUE_N) return _wasm._wasm_order(ringMod(n));
    const m = ringMod(n);
    if (gcd(m, N) !== 1) return 0;
    let x = m, k = 1;
    while (x !== 1 && k <= 420) { x = (x * m) % N; k++; }
    return x === 1 ? k : 0;
}

function multInverse(n) {
    let m = ringMod(n);
    if (gcd(m, N) !== 1) return -1;
    let [old_r, r] = [m, N], [old_s, s] = [1, 0];
    while (r !== 0) {
        const q = Math.floor(old_r / r);
        [old_r, r] = [r, old_r - q * r];
        [old_s, s] = [s, old_s - q * s];
    }
    return ((old_s % N) + N) % N;
}

// ================================================================
//  Constants
// ================================================================
const CONSTANTS = {
    s:1, D:2, K:3, E:5, b:7, L:11,
    sigma:1, OMEGA:606376, DATA:210, THIN:2310,
    HYDOR:105, KEY:41, ANSWER:42, SOUL:67,
    G:97, ADDRESS:137, DUAL:173, ME:18, LAMBDA:420,
    GATE:13, ESCAPE:17, THORNS:28, TRUE:970200,
    GATE_FORM:12612600,
    pi:Math.PI
};

const VALUE_NAMES = {
    0:'void', 1:'s', 2:'D', 3:'K', 5:'E', 7:'b', 11:'L',
    18:'ME', 41:'KEY', 42:'ANSWER', 67:'SOUL', 97:'G',
    105:'HYDOR', 137:'ADDRESS', 173:'DUAL', 210:'DATA',
    420:'LAMBDA', 2310:'THIN', 606376:'OMEGA',
    970200:'TRUE', 12612600:'GATE_FORM'
};

// ================================================================
//  Formatting
// ================================================================
function esc(s) { return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function fmtText(s) { return '<span class="out-text">' + esc(s) + '</span>'; }
function fmtNum(v) { return Number.isInteger(v) ? String(v) : v.toFixed(4); }

function fmtValue(v) {
    if (typeof v === 'string') return fmtText(v);
    if (Array.isArray(v)) {
        // Detect grid (nested array of same-length arrays with small integers)
        if (v.length > 0 && Array.isArray(v[0]) && v.every(r => Array.isArray(r) && r.length === v[0].length)) {
            return fmtGrid(v);
        }
        const inner = v.map(x => typeof x === 'number' ? fmtNum(x) : esc(String(x))).join(', ');
        return '<span class="out-val">[' + inner + ']</span>';
    }
    if (typeof v === 'number') {
        const display = Number.isInteger(v) ? String(v) : v.toFixed(6);
        const ann = Number.isInteger(v) && VALUE_NAMES[v] ? '  <span class="out-ann">(' + VALUE_NAMES[v] + ')</span>' : '';
        return '<span class="out-val">' + esc(display) + '</span>' + ann;
    }
    return '<span class="out-val">' + esc(String(v)) + '</span>';
}

const GRID_COLORS = ['#111','#0074D9','#FF4136','#2ECC40','#FFDC00','#AAAAAA','#F012BE','#FF851B','#7FDBFF','#870C25'];

function fmtGrid(g) {
    if (!Array.isArray(g) || g.length === 0) return fmtValue(g);
    const R = g.length, C = Array.isArray(g[0]) ? g[0].length : 0;
    if (C === 0) return '<span class="out-val">[]</span>';
    let html = '<div class="grid-display" style="grid-template-columns:repeat(' + C + ',20px)">';
    for (let r = 0; r < R; r++) {
        const row = g[r];
        if (!Array.isArray(row)) continue;
        for (let c = 0; c < row.length; c++) {
            const v = typeof row[c] === 'number' ? Math.round(row[c]) : 0;
            const color = (v >= 0 && v < 10) ? GRID_COLORS[v] : '#333';
            const txt = v !== 0 ? v : '';
            html += '<div class="grid-cell" style="background:' + color + '">' + txt + '</div>';
        }
    }
    return html + '</div>';
}

// ================================================================
//  Tokenizer
// ================================================================
const KEYWORDS = new Set(['let','fn','print','if','then','else','while','do','for','in']);

function tokenize(src) {
    const T = [];
    let i = 0, len = src.length, line = 1;
    const pk = (tok) => { tok.line = line; T.push(tok); };
    while (i < len) {
        if (/\s/.test(src[i])) { if (src[i] === '\n') line++; i++; continue; }
        if (src[i] === '-' && src[i+1] === '-') { while (i < len && src[i] !== '\n') i++; continue; }
        if (/\d/.test(src[i]) || (src[i] === '.' && i+1 < len && /\d/.test(src[i+1]))) {
            let num = '';
            while (i < len && /[\d.]/.test(src[i])) {
                // Don't consume '.' if followed by a channel name (D,K,E,b,L)
                if (src[i] === '.' && /[DKEbL]/.test(src[i+1]) && !/[\da-zA-Z_]/.test(src[i+2]||'')) break;
                num += src[i++];
            }
            pk({t:'NUM', v:parseFloat(num)}); continue;
        }
        if (src[i] === '"') {
            i++; let s = '', parts = [], hasInterp = false;
            while (i < len && src[i] !== '"') {
                if (src[i] === '$' && i + 1 < len && src[i+1] === '{') {
                    hasInterp = true;
                    if (s) parts.push({k:'s', v:s});
                    s = ''; i += 2;
                    let depth = 1, expr = '';
                    while (i < len && depth > 0) {
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
            if (i < len) i++;
            if (!hasInterp) { pk({t:'STR', v:s}); }
            else { if (s) parts.push({k:'s', v:s}); pk({t:'TEMPLATE', parts}); }
            continue;
        }
        if (/[a-zA-Z_]/.test(src[i])) {
            let id = '';
            while (i < len && /[a-zA-Z0-9_]/.test(src[i])) id += src[i++];
            pk({t: KEYWORDS.has(id) ? id.toUpperCase() : 'ID', v:id}); continue;
        }
        if (src[i] === '=' && i+1 < len && src[i+1] === '=') { pk({t:'==', v:'=='}); i+=2; continue; }
        if (src[i] === '!' && i+1 < len && src[i+1] === '=') { pk({t:'!=', v:'!='}); i+=2; continue; }
        if (src[i] === '<' && i+1 < len && src[i+1] === '=') { pk({t:'<=', v:'<='}); i+=2; continue; }
        if (src[i] === '>' && i+1 < len && src[i+1] === '=') { pk({t:'>=', v:'>='}); i+=2; continue; }
        if (src[i] === '/' && src[i+1] === '*') { i += 2; while (i < len - 1 && !(src[i] === '*' && src[i+1] === '/')) { if (src[i] === '\n') line++; i++; } i += 2; continue; }
        const ch = src[i];
        if ('+-*/^~@<>=()[]|,;%'.includes(ch)) { pk({t:ch, v:ch}); i++; continue; }
        i++;
    }
    pk({t:'EOF', v:null});
    return T;
}

// ================================================================
//  Parser
// ================================================================
class Parser {
    constructor(tokens) { this.T = tokens; this.p = 0; }
    pk() { return this.T[this.p]; }
    adv() { return this.T[this.p++]; }
    expect(t) {
        const tok = this.adv();
        if (tok.t !== t) throw new Error('Expected ' + t + ', got ' + tok.t + ' "' + tok.v + '"');
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
        switch (this.pk().t) {
            case 'LET': return this.parseLet();
            case 'FN': return this.parseFn();
            case 'PRINT': return this.parsePrint();
            default: return {t:'ExprStmt', expr:this.parseExpr()};
        }
    }

    parseLet() {
        this.expect('LET');
        const name = this.expect('ID').v;
        this.expect('=');
        return {t:'Let', name, val:this.parseExpr()};
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

    parsePrint() {
        this.expect('PRINT');
        if (this.pk().t === 'STR') return {t:'Print', expr:{t:'Str', v:this.adv().v}};
        return {t:'Print', expr:this.parseExpr()};
    }

    parseExpr() {
        let left = this.parseIfOrCmp();
        while (this.pk().t === ';') {
            // Stop before FN: fn is statement-only, never valid inside a sequence.
            const next = this.T[this.p + 1];
            if (next && next.t === 'FN') break;
            this.adv(); left = {t:'Seq', a:left, b:this.parseIfOrCmp()};
        }
        return left;
    }

    parseIfOrCmp() {
        if (this.pk().t === 'IF') return this.parseIf();
        if (this.pk().t === 'LET') return this.parseLetExpr();
        if (this.pk().t === 'FOR') return this.parseFor();
        return this.parseCmp();
    }

    parseFor() {
        this.expect('FOR');
        const varName = this.expect('ID').v;
        this.expect('IN');
        const iter = this.parseCmp();
        this.expect('DO');
        return {t:'For', varName, iter, body:this.parseExpr()};
    }

    parseLetExpr() {
        this.expect('LET');
        const name = this.expect('ID').v;
        this.expect('=');
        const val = this.parseIfOrCmp();  // Not parseExpr: stops before ; so let scope works inside (...)
        // Accept 'in' or ';' as body separator; ';' fixes let inside (...) blocks
        if (this.pk().t === 'IN' || this.pk().t === ';') { this.adv(); }
        const pk = this.pk().t;
        if (pk === ')' || pk === 'EOF' || pk === ']') return {t:'LetExpr', name, val, body:{t:'Var', name}};
        return {t:'LetExpr', name, val, body:this.parseExpr()};
    }

    parseIf() {
        this.expect('IF');
        const cond = this.parseExpr();
        this.expect('THEN');
        const then_ = this.parseExpr();
        this.expect('ELSE');
        return {t:'If', cond, then_, else_:this.parseExpr()};
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
        if (this.pk().t === '~') { this.adv(); return {t:'Unary', op:'~', e:this.parseUnary()}; }
        if (this.pk().t === '-') { this.adv(); return {t:'Bin', op:'-', l:{t:'Num',v:0}, r:this.parseUnary()}; }
        return this.parseThresh();
    }

    parseThresh() {
        let e = this.parsePostfix();
        if (this.pk().t === '@') { this.adv(); e = {t:'Thresh', val:e, th:this.parsePostfix()}; }
        return e;
    }

    parsePostfix() {
        let e = this.parsePrimary();
        while (this.pk().t === '[') { this.adv(); const idx = this.parseExpr(); this.expect(']'); e = {t:'Idx', arr:e, idx}; }
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
        if (tok.t === '(') {
            this.adv();
            const first = this.parseExpr();
            if (this.pk().t === '|') {
                this.adv(); const second = this.parseExpr();
                this.expect('|'); const third = this.parseExpr();
                this.expect(')');
                return {t:'DFloat', s:first, b:second, a:third};
            }
            this.expect(')');
            return first;
        }
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
        throw new Error('Unexpected: ' + tok.t + ' "' + tok.v + '"');
    }
}

function parse(src) {
    return new Parser(tokenize(src)).parseProgram();
}

// ================================================================
//  Builtins Registry
// ================================================================
const BUILTINS = {};

// --- Ring builtins (with trace) ---
BUILTINS.coupling = function(args, ctx) {
    const n = args[0], r = ringMod(n), g = gcd(r, N), result = N / g;
    ctx.trace('<span class="tr-fn">coupling</span>(' + n + '): <span class="tr-step">' + n + ' mod ' + N + ' = ' + r + ', gcd(' + r + ', ' + N + ') = ' + g + ', ' + N + ' / ' + g + '</span> = <span class="tr-result">' + result + '</span>');
    return result;
};

BUILTINS.crt = function(args, ctx) {
    const result = crt(args[0]), r = ringMod(args[0]);
    const parts = result.map((v, i) => r + ' mod ' + CRT_MODS[i] + ' = ' + v).join(', ');
    ctx.trace('<span class="tr-fn">crt</span>(' + args[0] + '): <span class="tr-step">' + parts + '</span> = <span class="tr-result">[' + result.join(', ') + ']</span>');
    return result;
};

BUILTINS.eigenvalue = function(args, ctx) {
    const c = crt(args[0]), P = Math.PI;
    const result = c.reduce((sum, ci, i) => sum + 2*Math.cos(2*P*ci/CRT_MODS[i]), 0);
    ctx.trace('<span class="tr-fn">eigenvalue</span>(' + args[0] + '): <span class="tr-step">crt=[' + c.join(',') + ']</span> = <span class="tr-result">' + result.toFixed(6) + '</span>');
    return result;
};

BUILTINS.shadow_poly = function(args, ctx) {
    const n = args[0];
    const result = (n - 1) * (n - 2) * (n - 3) * (n - 5);
    ctx.trace('<span class="tr-fn">shadow_poly</span>(' + n + '): <span class="tr-step">(' + n + '-1)(' + n + '-2)(' + n + '-3)(' + n + '-5)</span> = <span class="tr-result">' + result + '</span>');
    return result;
};

BUILTINS.depth_quad = function(args, ctx) {
    // f(n) = n^2 - n - 1 (the depth quadratic)
    const n = args[0];
    const result = n * n - n - 1;
    ctx.trace('<span class="tr-fn">depth_quad</span>(' + n + '): <span class="tr-step">' + n + '^2-' + n + '-1</span> = <span class="tr-result">' + result + '</span>');
    return result;
};

BUILTINS.is_smooth = function(args, ctx) {
    // is_smooth(n) -> 1 if n is 11-smooth (all prime factors <= 11), else 0
    var n = Math.abs(Math.round(args[0]));
    if (n <= 1) { ctx.trace('<span class="tr-fn">is_smooth</span>(' + args[0] + ') = <span class="tr-result">1</span>'); return 1; }
    var primes = [2, 3, 5, 7, 11];
    for (var i = 0; i < primes.length; i++) { while (n % primes[i] === 0) n /= primes[i]; }
    var result = (n === 1) ? 1 : 0;
    ctx.trace('<span class="tr-fn">is_smooth</span>(' + args[0] + ') = <span class="tr-result">' + result + '</span>');
    return result;
};

BUILTINS.golden_roots = function(args, ctx) {
    // golden_roots(q) -> [r1, r2] roots of f(n)=n^2-n-1 mod q (if disc=5 is QR)
    var q = Math.round(args[0]);
    if (q <= 1) return [0, 0];
    // find sqrt(5) mod q by brute force (small q)
    var s = -1;
    for (var i = 0; i < q; i++) { if ((i * i) % q === 5 % q) { s = i; break; } }
    if (s < 0) { ctx.trace('<span class="tr-fn">golden_roots</span>(' + q + '): <span class="tr-step">5 is QNR</span>'); return [-1, -1]; }
    // roots = (1 +/- sqrt(5)) / 2 mod q
    var inv2 = -1;
    for (var j = 0; j < q; j++) { if ((2 * j) % q === 1) { inv2 = j; break; } }
    if (inv2 < 0) { // q even
        var r1 = (1 + s) % q; var r2 = (1 + q - s) % q;
        ctx.trace('<span class="tr-fn">golden_roots</span>(' + q + ') = <span class="tr-result">[' + r1 + ',' + r2 + ']</span>');
        return [r1, r2];
    }
    var r1 = ((1 + s) * inv2) % q;
    var r2 = ((1 + q - s) * inv2) % q;
    ctx.trace('<span class="tr-fn">golden_roots</span>(' + q + ') = <span class="tr-result">[' + r1 + ',' + r2 + ']</span>');
    return [r1, r2];
};

BUILTINS.factorize = function(args, ctx) {
    // factorize(n) -> flat array [p1, e1, p2, e2, ...]
    var n = args[0];
    if (n < 0) n = -n;
    if (n <= 1) { ctx.trace('<span class="tr-fn">factorize</span>(' + args[0] + ') = <span class="tr-result">[]</span>'); return []; }
    var factors = [];
    for (var p = 2; p * p <= n; p++) {
        var e = 0;
        while (n % p === 0) { n /= p; e++; }
        if (e > 0) { factors.push(p); factors.push(e); }
    }
    if (n > 1) { factors.push(n); factors.push(1); }
    var display = [];
    for (var i = 0; i < factors.length; i += 2) {
        display.push(factors[i] + (factors[i+1] > 1 ? '^' + factors[i+1] : ''));
    }
    ctx.trace('<span class="tr-fn">factorize</span>(' + args[0] + ') = <span class="tr-result">' + display.join(' * ') + '</span>');
    return factors;
};

BUILTINS.sigma3 = function(args, ctx) {
    // sigma3(n) = sum of cubes of divisors of n
    var n = args[0];
    if (n < 0) n = -n;
    if (n === 0) { ctx.trace('<span class="tr-fn">sigma3</span>(0) = <span class="tr-result">0</span>'); return 0; }
    var s = 0;
    for (var d = 1; d <= n; d++) {
        if (n % d === 0) s += d * d * d;
    }
    ctx.trace('<span class="tr-fn">sigma3</span>(' + args[0] + ') = <span class="tr-result">' + s + '</span>');
    return s;
};

BUILTINS.mirror = function(args, ctx) {
    const result = mirror(args[0]);
    ctx.trace('<span class="tr-fn">mirror</span>(' + args[0] + '): <span class="tr-step">' + N + ' - ' + ringMod(args[0]) + '</span> = <span class="tr-result">' + result + '</span>');
    return result;
};

BUILTINS.phi = function(args, ctx) {
    const input = args.length > 0 ? args[0] : N;
    const result = eulerPhi(input);
    ctx.trace('<span class="tr-fn">phi</span>(' + input + ') = <span class="tr-result">' + result + '</span>');
    return result;
};

BUILTINS.order = function(args, ctx) {
    const result = multOrder(args[0]);
    ctx.trace('<span class="tr-fn">order</span>(' + args[0] + '): <span class="tr-step">gcd(' + ringMod(args[0]) + ', ' + N + ')=' + gcd(ringMod(args[0]), N) + (gcd(ringMod(args[0]), N) !== 1 ? ' (not a unit!)' : ', ' + ringMod(args[0]) + '^k mod ' + N + ' = 1 at k=' + result) + '</span> = <span class="tr-result">' + result + '</span>');
    return result;
};

// --- Lattice dynamics builtins (S494) ---
BUILTINS.omega_of = function(args, ctx) {
    // omega_of(m) = D^420 mod m. OMEGA for any ring size m.
    const m = Math.abs(Math.round(args[0]));
    if (m < 2) return 0;
    let result = 1, base = 2 % m, exp = 420;
    while (exp > 0) { if (exp & 1) result = (result * base) % m; base = (base * base) % m; exp >>= 1; }
    ctx.trace('<span class="tr-fn">omega_of</span>(' + m + '): <span class="tr-step">D^420 mod ' + m + '</span> = <span class="tr-result">' + result + '</span>');
    return result;
};

BUILTINS.delta_of = function(args, ctx) {
    // delta_of(m) = (1 - omega) mod m. The D-ghost for ring m.
    const m = Math.abs(Math.round(args[0]));
    if (m < 2) return 0;
    let omega = 1, base = 2 % m, exp = 420;
    while (exp > 0) { if (exp & 1) omega = (omega * base) % m; base = (base * base) % m; exp >>= 1; }
    const result = ((1 - omega) % m + m) % m;
    ctx.trace('<span class="tr-fn">delta_of</span>(' + m + '): <span class="tr-step">sigma - omega = 1 - ' + omega + ' mod ' + m + '</span> = <span class="tr-result">' + result + '</span>');
    return result;
};

BUILTINS.d_orbit = function(args, ctx) {
    // d_orbit(x) = array of D-multiplication orbit: x, 2x, 4x, ... until cycle.
    const x = ringMod(args[0]);
    const orbit = [x];
    let cur = (2 * x) % N;
    let maxSteps = 500;
    while (cur !== x && maxSteps-- > 0) { orbit.push(cur); cur = (2 * cur) % N; }
    ctx.trace('<span class="tr-fn">d_orbit</span>(' + args[0] + '): <span class="tr-step">length=' + orbit.length + '</span> = <span class="tr-result">[' + (orbit.length <= 10 ? orbit.join(',') : orbit.slice(0,5).join(',') + ',...,' + orbit.slice(-2).join(',')) + ']</span>');
    return orbit;
};

BUILTINS.water_cycle = function(args, ctx) {
    // water_cycle(m) = checks all 4 laws for ring Z/mZ. Returns [o_idem, d_idem, orth, sum_s].
    const m = Math.abs(Math.round(args.length > 0 ? args[0] : N));
    if (m < 2) return [0, 0, 0, 0];
    let omega = 1, base = 2 % m, exp = 420;
    while (exp > 0) { if (exp & 1) omega = (omega * base) % m; base = (base * base) % m; exp >>= 1; }
    const delta = ((1 - omega) % m + m) % m;
    const oi = (omega * omega % m === omega) ? 1 : 0;
    const di = (delta * delta % m === delta) ? 1 : 0;
    const or_ = (omega * delta % m === 0) ? 1 : 0;
    const ss = ((omega + delta) % m === 1) ? 1 : 0;
    const result = [oi, di, or_, ss];
    ctx.trace('<span class="tr-fn">water_cycle</span>(' + m + '): <span class="tr-step">O=' + omega + ', d=' + delta + '</span> = <span class="tr-result">[' + result.join(',') + '] (' + (oi+di+or_+ss) + '/4 laws)</span>');
    return result;
};

// --- Gate configuration builtins (S501) ---
BUILTINS.idempotent = function(args, ctx) {
    // idempotent(mask) = the CRT idempotent for channel bitmask.
    // mask bits: 0=first channel, 1=second, etc.
    // In TRUE FORM (5 channels): mask 0..31. In GATE FORM (6 channels): mask 0..63.
    const mask = Math.abs(Math.round(args[0]));
    const mods = factorPrimePowers(N);
    const k = mods.length;
    if (mask >= (1 << k)) return 0;
    let result = 0;
    for (let i = 0; i < k; i++) {
        if (!((mask >> i) & 1)) continue;
        // CRT basis element: 1 in channel i, 0 in others
        const Mi = N / mods[i];
        // Find inverse of Mi mod mods[i]
        let inv = 0;
        for (let t = 0; t < mods[i]; t++) {
            if ((Mi % mods[i]) * t % mods[i] === 1) { inv = t; break; }
        }
        result = (result + (Mi % N) * inv) % N;
    }
    const ch = [];
    for (let i = 0; i < k; i++) if ((mask >> i) & 1) ch.push(mods[i]);
    ctx.trace('<span class="tr-fn">idempotent</span>(' + mask + '): <span class="tr-step">channels [' + ch.join(',') + ']</span> = <span class="tr-result">' + result + '</span>');
    return result;
};

BUILTINS.body_proj = function(args, ctx) {
    // body_proj(n) = project n onto body channels (all except last = skin).
    // In GATE FORM: projects onto D^3*K^2*E^2*b^2*L (= TRUE FORM subring).
    const n = Math.round(args[0]);
    const mods = factorPrimePowers(N);
    const k = mods.length;
    const bodyMask = (1 << (k - 1)) - 1; // all channels except last
    const bodyN = mods.slice(0, k - 1).reduce((a, b) => a * b, 1);
    const result = ((n % bodyN) + bodyN) % bodyN;
    ctx.trace('<span class="tr-fn">body_proj</span>(' + n + '): <span class="tr-step">project to body (N=' + bodyN + ')</span> = <span class="tr-result">' + result + '</span>');
    return result;
};

// --- Multi-ring builtins (S497) ---
BUILTINS.ring_crt = function(args, ctx) {
    const n = Math.round(args[0]);
    const m = Math.abs(Math.round(args[1]));
    if (m < 2) return [0];
    const mods = factorPrimePowers(m);
    const r = ((n % m) + m) % m;
    const result = mods.map(mod => r % mod);
    ctx.trace('<span class="tr-fn">ring_crt</span>(' + n + ', ' + m + '): <span class="tr-step">mods=[' + mods.join(',') + ']</span> = <span class="tr-result">[' + result.join(', ') + ']</span>');
    return result;
};

BUILTINS.ring_coupling = function(args, ctx) {
    const n = Math.round(args[0]);
    const m = Math.abs(Math.round(args[1]));
    if (m < 1) return 0;
    const r = ((n % m) + m) % m;
    const g = gcd(r, m);
    const result = m / g;
    ctx.trace('<span class="tr-fn">ring_coupling</span>(' + n + ', ' + m + '): <span class="tr-step">gcd(' + r + ', ' + m + ')=' + g + '</span> = <span class="tr-result">' + result + '</span>');
    return result;
};

BUILTINS.project = function(args, ctx) {
    const n = Math.round(args[0]);
    const n1 = Math.abs(Math.round(args[1]));
    const n2 = Math.abs(Math.round(args[2]));
    if (n1 < 1 || n2 < 1) return 0;
    const r = ((n % n1) + n1) % n1;
    const result = r % n2;
    ctx.trace('<span class="tr-fn">project</span>(' + n + ', ' + n1 + ' -> ' + n2 + '): <span class="tr-step">' + r + ' mod ' + n2 + '</span> = <span class="tr-result">' + result + '</span>');
    return result;
};

BUILTINS.ring_size = function(args, ctx) {
    ctx.trace('<span class="tr-fn">ring_size</span>(): <span class="tr-result">' + N + '</span>');
    return N;
};

BUILTINS.set_ring = function(args, ctx) {
    const newN = Math.abs(Math.round(args[0]));
    setRing(newN);
    ctx.trace('<span class="tr-fn">set_ring</span>(' + newN + '): <span class="tr-step">Z/' + N + 'Z, CRT mods=[' + CRT_MODS.join(',') + ']</span>');
    return N;
};

BUILTINS.ring_eigenvalue = function(args, ctx) {
    const n = Math.round(args[0]);
    const m = Math.abs(Math.round(args[1]));
    if (m < 2) return 0;
    const mods = factorPrimePowers(m);
    const r = ((n % m) + m) % m;
    const P = Math.PI;
    const result = mods.reduce((sum, mod) => sum + 2*Math.cos(2*P*(r % mod)/mod), 0);
    ctx.trace('<span class="tr-fn">ring_eigenvalue</span>(' + n + ', ' + m + ') = <span class="tr-result">' + result.toFixed(6) + '</span>');
    return result;
};

// --- Math builtins (no trace) ---
BUILTINS.gcd = (args) => gcd(args[0], args[1]);
BUILTINS.lcm = (args) => { const a = Math.abs(Math.round(args[0])), b = Math.abs(Math.round(args[1])); return a === 0 || b === 0 ? 0 : (a / gcd(a, b)) * b; };
BUILTINS.mod = (args) => args[1] !== 0 ? ringMod(Math.round(args[0]) % Math.round(args[1])) : 0;
BUILTINS.inv = (args) => { const r = multInverse(args[0]); if (r < 0) throw new Error('No inverse: gcd(' + args[0] + ', ' + N + ') != 1'); return r; };
BUILTINS.is_unit = (args) => { if (_wasm && N === TRUE_N) return _wasm._wasm_is_unit(ringMod(args[0])); return gcd(ringMod(args[0]), N) === 1 ? 1 : 0; };
BUILTINS.ecc_detect = function(args, ctx) {
    const c = crt(args[0]);
    if (_wasm && N === TRUE_N) {
        const d = _wasm._wasm_ecc_detect(c[0], c[1], c[2], c[3], c[4]);
        ctx.trace('<span class="tr-fn">ecc_detect</span>(' + args[0] + '): CRT=[' + c.join(',') + '] <span class="tr-result">' + (d ? 'CORRUPTED' : 'CLEAN') + '</span>');
        return d;
    }
    // JS fallback: reconstruct data ring value from 4 data channels, check mod 11
    const dw = [11025, 78400, 59976, 27000]; // CRT weights for Z/88200Z
    let data = 0;
    for (let i = 0; i < 4; i++) data += dw[i] * c[i];
    data = ((data % 88200) + 88200) % 88200;
    const expected = data % 11;
    const d = c[4] !== expected ? 1 : 0;
    ctx.trace('<span class="tr-fn">ecc_detect</span>(' + args[0] + '): L-check ' + c[4] + ' vs ' + expected + ' <span class="tr-result">' + (d ? 'CORRUPTED' : 'CLEAN') + '</span>');
    return d;
};
BUILTINS.ecc_correct = function(args, ctx) {
    const c = crt(args[0]);
    if (_wasm && N === TRUE_N) {
        const corrected = _wasm._wasm_ecc_correct(c[0], c[1], c[2], c[3], c[4]);
        ctx.trace('<span class="tr-fn">ecc_correct</span>(' + args[0] + '): <span class="tr-result">' + corrected + '</span>');
        return corrected;
    }
    // JS fallback: L-fix (recompute L channel from data channels)
    const dw = [11025, 78400, 59976, 27000];
    let data = 0;
    for (let i = 0; i < 4; i++) data += dw[i] * c[i];
    data = ((data % 88200) + 88200) % 88200;
    c[4] = data % 11;
    // Reconstruct from corrected CRT (weights from crt.h)
    const w = [363825, 431200, 853776, 732600, 529200];
    let n = 0;
    for (let i = 0; i < 5; i++) n += w[i] * c[i];
    const result = ((n % N) + N) % N;
    ctx.trace('<span class="tr-fn">ecc_correct</span>(' + args[0] + '): L-fix <span class="tr-result">' + result + '</span>');
    return result;
};
BUILTINS.abs = (args) => Math.abs(args[0]);
BUILTINS.min = (args) => Math.min(args[0], args[1]);
BUILTINS.max = (args) => Math.max(args[0], args[1]);
BUILTINS.sqrt = (args) => Math.floor(Math.sqrt(Math.abs(args[0])));
BUILTINS.cos = (args) => Math.cos(args[0]);
BUILTINS.sin = (args) => Math.sin(args[0]);
BUILTINS.acos = (args) => Math.acos(Math.max(-1, Math.min(1, args[0])));
BUILTINS.asin = (args) => Math.asin(Math.max(-1, Math.min(1, args[0])));
BUILTINS.log = (args) => Math.log(Math.abs(args[0]));
BUILTINS.exp = (args) => Math.exp(args[0]);
BUILTINS.floor = (args) => Math.floor(args[0]);
BUILTINS.ceil = (args) => Math.ceil(args[0]);
BUILTINS.pow = (args) => Math.pow(args[0], args[1]);
BUILTINS.len = (args) => Array.isArray(args[0]) ? args[0].length : 0;
BUILTINS.rand = (args) => Math.floor(Math.random() * (args.length > 0 && args[0] > 0 ? args[0] : 2));

// --- Phase F: Float math builtins (S626 — parity with ax2.js) ---
// Returns raw JS floats. Binary ops propagate: non-integer + anything = float arithmetic.
BUILTINS.toFloat = (args) => {
    const v = args[0];
    if (typeof v === 'number') return v + 0.0; // ensure float semantics
    if (Array.isArray(v)) return v.length;
    return 0;
};
BUILTINS.exp_f = (args) => Math.exp(typeof args[0] === 'number' ? args[0] : 0);
BUILTINS.log_f = (args) => { const x = typeof args[0] === 'number' ? args[0] : 0; return x > 0 ? Math.log(x) : -Infinity; };
BUILTINS.log2_f = (args) => { const x = typeof args[0] === 'number' ? args[0] : 0; return x > 0 ? Math.log2(x) : -Infinity; };
BUILTINS.log10_f = (args) => { const x = typeof args[0] === 'number' ? args[0] : 0; return x > 0 ? Math.log10(x) : -Infinity; };
BUILTINS.pow_f = (args) => Math.pow(typeof args[0] === 'number' ? args[0] : 0, typeof args[1] === 'number' ? args[1] : 0);
BUILTINS.sqrt_f = (args) => Math.sqrt(typeof args[0] === 'number' ? args[0] : 0);
BUILTINS.sin_f = (args) => Math.sin(typeof args[0] === 'number' ? args[0] : 0);
BUILTINS.cos_f = (args) => Math.cos(typeof args[0] === 'number' ? args[0] : 0);
BUILTINS.tan_f = (args) => Math.tan(typeof args[0] === 'number' ? args[0] : 0);
BUILTINS.abs_f = (args) => Math.abs(typeof args[0] === 'number' ? args[0] : 0);
BUILTINS.floor_f = (args) => Math.floor(typeof args[0] === 'number' ? args[0] : 0);
BUILTINS.ceil_f = (args) => Math.ceil(typeof args[0] === 'number' ? args[0] : 0);
BUILTINS.round_f = (args) => Math.round(typeof args[0] === 'number' ? args[0] : 0);
BUILTINS.tanh_f = (args) => Math.tanh(typeof args[0] === 'number' ? args[0] : 0);
BUILTINS.sigmoid_f = (args) => { const x = typeof args[0] === 'number' ? args[0] : 0; return 1.0 / (1.0 + Math.exp(-x)); };
BUILTINS.softmax = (args) => {
    if (!Array.isArray(args[0])) throw new Error('softmax: expected array');
    const arr = args[0].map(v => typeof v === 'number' ? v : 0);
    const mx = Math.max(...arr);
    const exps = arr.map(x => Math.exp(x - mx));
    const s = exps.reduce((a, b) => a + b, 0);
    return exps.map(e => e / s);
};
BUILTINS.matmul = (args) => {
    const A = args[0], B = args[1];
    if (!Array.isArray(A) || !Array.isArray(B)) throw new Error('matmul: expected arrays');
    if (!Array.isArray(A[0]) || !Array.isArray(B[0])) throw new Error('matmul: expected 2D arrays');
    const m = A.length, k = A[0].length, n = B[0].length;
    if (B.length !== k) throw new Error('matmul: dimension mismatch');
    const C = [];
    for (let i = 0; i < m; i++) {
        const row = [];
        for (let j = 0; j < n; j++) {
            let s = 0;
            for (let p = 0; p < k; p++) s += (typeof A[i][p] === 'number' ? A[i][p] : 0) * (typeof B[p][j] === 'number' ? B[p][j] : 0);
            row.push(s);
        }
        C.push(row);
    }
    return C;
};
BUILTINS.dot = (args) => {
    const a = args[0], b = args[1];
    if (!Array.isArray(a) || !Array.isArray(b)) throw new Error('dot: expected arrays');
    let s = 0;
    for (let i = 0; i < Math.min(a.length, b.length); i++) s += (typeof a[i] === 'number' ? a[i] : 0) * (typeof b[i] === 'number' ? b[i] : 0);
    return s;
};
BUILTINS.sum_f = (args) => {
    if (!Array.isArray(args[0])) return 0;
    return args[0].reduce((s, v) => s + (typeof v === 'number' ? v : 0), 0);
};
BUILTINS.PI_f = () => Math.PI;
BUILTINS.E_f = () => Math.E;
BUILTINS.INF_f = () => Infinity;

// --- Array builtins ---
BUILTINS.range = function(args) {
    if (args.length === 1) { const n = Math.min(Math.max(0, Math.round(args[0])), 10000); return Array.from({length:n}, (_,i) => i); }
    const a = Math.round(args[0]), b = Math.min(Math.round(args[1]), a + 10000);
    return Array.from({length: Math.max(0, b - a)}, (_, i) => a + i);
};

BUILTINS.kingdom = function(args) {
    const n = ringMod(args[0]); if (n === 0) return 0;
    const g = gcd(n, N);
    if (g % 2 === 0) return 2; if (g % 3 === 0) return 3;
    if (g % 5 === 0) return 5; if (g % 7 === 0) return 7;
    if (g % 11 === 0) return 11; return 1;
};

BUILTINS.sum = function(args) {
    if (!Array.isArray(args[0])) throw new Error('sum expects array');
    let s = 0; for (const x of args[0]) s = ringMod(s + (typeof x === 'number' ? x : 0)); return s;
};

BUILTINS.product = function(args) {
    if (!Array.isArray(args[0])) throw new Error('product expects array');
    let p = 1; for (const x of args[0]) p = ringMod(p * (typeof x === 'number' ? x : 0)); return p;
};

// --- Output builtins ---
BUILTINS.show = function(args, ctx) {
    ctx.output(fmtValue(args[0]), args[0]);
    return args[0];
};

BUILTINS.show_grid = function(args, ctx) {
    const g = args[0];
    if (!Array.isArray(g)) throw new Error('show_grid: not a grid');
    ctx.output(fmtGrid(g), g);
    return g;
};

// --- Grid builtins (S465) ---
BUILTINS.grid = function(args) {
    const rows = Math.min(Math.max(1, Math.round(args[0])), 30);
    const cols = Math.min(Math.max(1, Math.round(args[1])), 30);
    const val = args.length > 2 ? args[2] : 0;
    return Array.from({length: rows}, () => Array.from({length: cols}, () => val));
};

BUILTINS.gset = function(args) {
    const g = args[0], r = Math.floor(args[1]), c = Math.floor(args[2]), v = args[3];
    if (!Array.isArray(g) || !Array.isArray(g[0])) throw new Error('gset: not a grid');
    if (r < 0 || r >= g.length || c < 0 || c >= g[0].length) throw new Error('gset: out of bounds (' + r + ',' + c + ')');
    g[r][c] = v;
    return g;
};

BUILTINS.rows = (args) => Array.isArray(args[0]) ? args[0].length : 0;
BUILTINS.cols = (args) => (Array.isArray(args[0]) && args[0].length > 0 && Array.isArray(args[0][0])) ? args[0][0].length : 0;

BUILTINS.hflip = function(args) {
    const g = args[0];
    if (!Array.isArray(g)) throw new Error('hflip: not a grid');
    return g.map(row => Array.isArray(row) ? [...row].reverse() : row);
};

BUILTINS.vflip = function(args) {
    const g = args[0];
    if (!Array.isArray(g)) throw new Error('vflip: not a grid');
    return [...g].reverse().map(row => Array.isArray(row) ? [...row] : row);
};

BUILTINS.rot90 = function(args) {
    const g = args[0];
    if (!Array.isArray(g) || g.length === 0 || !Array.isArray(g[0])) throw new Error('rot90: not a grid');
    const R = g.length, C = g[0].length;
    return Array.from({length: C}, (_, c) => Array.from({length: R}, (_, r) => g[R-1-r][c]));
};

BUILTINS.transpose = function(args) {
    const g = args[0];
    if (!Array.isArray(g) || g.length === 0 || !Array.isArray(g[0])) throw new Error('transpose: not a grid');
    const R = g.length, C = g[0].length;
    return Array.from({length: C}, (_, c) => Array.from({length: R}, (_, r) => g[r][c]));
};

BUILTINS.grid_eq = function(args) {
    const a = args[0], b = args[1];
    if (!Array.isArray(a) || !Array.isArray(b) || a.length !== b.length) return 0;
    for (let i = 0; i < a.length; i++) {
        if (!Array.isArray(a[i]) || !Array.isArray(b[i]) || a[i].length !== b[i].length) return 0;
        for (let j = 0; j < a[i].length; j++) if (a[i][j] !== b[i][j]) return 0;
    }
    return 1;
};

// --- Grid builtins Phase 2 (S467) ---
BUILTINS.gget = function(args) {
    const g = args[0], r = Math.floor(args[1]), c = Math.floor(args[2]);
    if (!Array.isArray(g) || r < 0 || r >= g.length) return -1;
    if (!Array.isArray(g[r]) || c < 0 || c >= g[r].length) return -1;
    return g[r][c];
};

BUILTINS.subgrid = function(args) {
    const g = args[0], r0 = Math.floor(args[1]), c0 = Math.floor(args[2]);
    const h = Math.floor(args[3]), w = Math.floor(args[4]);
    if (!Array.isArray(g)) throw new Error('subgrid: not a grid');
    const R = g.length, C = Array.isArray(g[0]) ? g[0].length : 0;
    const result = [];
    for (let r = 0; r < h; r++) {
        const row = [];
        for (let c = 0; c < w; c++) {
            const rr = r0 + r, cc = c0 + c;
            row.push(rr >= 0 && rr < R && cc >= 0 && cc < C ? g[rr][cc] : 0);
        }
        result.push(row);
    }
    return result;
};

BUILTINS.paste = function(args) {
    const g = args[0], sub = args[1], r0 = Math.floor(args[2]), c0 = Math.floor(args[3]);
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

BUILTINS.scale = function(args) {
    const g = args[0], f = Math.floor(args[1]);
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

BUILTINS.colors = function(args) {
    const g = args[0];
    if (!Array.isArray(g)) throw new Error('colors: not a grid');
    const seen = new Set();
    for (const row of g) if (Array.isArray(row)) for (const v of row) seen.add(v);
    return [...seen].sort((a, b) => a - b);
};

BUILTINS.crop = function(args) {
    const g = args[0];
    if (!Array.isArray(g) || g.length === 0) throw new Error('crop: not a grid');
    let rMin = g.length, rMax = -1, cMin = g[0].length, cMax = -1;
    for (let r = 0; r < g.length; r++) {
        if (!Array.isArray(g[r])) continue;
        for (let c = 0; c < g[r].length; c++) {
            if (g[r][c] !== 0) { rMin = Math.min(rMin, r); rMax = Math.max(rMax, r); cMin = Math.min(cMin, c); cMax = Math.max(cMax, c); }
        }
    }
    if (rMax < 0) return [[0]];
    const result = [];
    for (let r = rMin; r <= rMax; r++) result.push(g[r].slice(cMin, cMax + 1));
    return result;
};

BUILTINS.count_color = function(args) {
    const g = args[0], color = args[1];
    if (!Array.isArray(g)) throw new Error('count_color: not a grid');
    let count = 0;
    for (const row of g) if (Array.isArray(row)) for (const v of row) if (v === color) count++;
    return count;
};

BUILTINS.replace_color = function(args) {
    const g = args[0], from = args[1], to = args[2];
    if (!Array.isArray(g)) throw new Error('replace_color: not a grid');
    return g.map(row => Array.isArray(row) ? row.map(v => v === from ? to : v) : row);
};

BUILTINS.fill_grid = function(args) {
    const g = args[0], color = args[1];
    if (!Array.isArray(g)) throw new Error('fill_grid: not a grid');
    return g.map(row => Array.isArray(row) ? row.map(() => color) : row);
};

BUILTINS.rot180 = function(args) {
    const g = args[0];
    if (!Array.isArray(g)) throw new Error('rot180: not a grid');
    return [...g].reverse().map(row => Array.isArray(row) ? [...row].reverse() : row);
};

BUILTINS.rot270 = function(args) {
    const g = args[0];
    if (!Array.isArray(g) || g.length === 0 || !Array.isArray(g[0])) throw new Error('rot270: not a grid');
    const R = g.length, C = g[0].length;
    return Array.from({length: C}, (_, c) => Array.from({length: R}, (_, r) => g[r][C-1-c]));
};

BUILTINS.hrepeat = function(args) {
    const g = args[0], n = Math.min(Math.max(1, Math.floor(args[1])), 10);
    if (!Array.isArray(g)) throw new Error('hrepeat: not a grid');
    return g.map(row => Array.isArray(row) ? [].concat(...Array(n).fill(row)) : row);
};

BUILTINS.vrepeat = function(args) {
    const g = args[0], n = Math.min(Math.max(1, Math.floor(args[1])), 10);
    if (!Array.isArray(g)) throw new Error('vrepeat: not a grid');
    const result = [];
    for (let i = 0; i < n; i++) for (const row of g) result.push(Array.isArray(row) ? [...row] : row);
    return result;
};

BUILTINS.color_map = function(args) {
    const gin = args[0], gout = args[1];
    if (!Array.isArray(gin) || !Array.isArray(gout)) return [];
    if (gin.length !== gout.length) return [];
    const map = [0,1,2,3,4,5,6,7,8,9];
    const set = [false,false,false,false,false,false,false,false,false,false];
    for (let r = 0; r < gin.length; r++) {
        if (!Array.isArray(gin[r]) || !Array.isArray(gout[r]) || gin[r].length !== gout[r].length) return [];
        for (let c = 0; c < gin[r].length; c++) {
            const ic = gin[r][c], oc = gout[r][c];
            if (ic < 0 || ic >= 10 || oc < 0 || oc >= 10) continue;
            if (!set[ic]) { map[ic] = oc; set[ic] = true; }
            else if (map[ic] !== oc) return [];
        }
    }
    return map;
};

BUILTINS.apply_color_map = function(args) {
    const g = args[0], map = args[1];
    if (!Array.isArray(g) || !Array.isArray(map)) throw new Error('apply_color_map: invalid');
    return g.map(row => Array.isArray(row) ? row.map(v => (v >= 0 && v < map.length && map[v] !== undefined) ? map[v] : v) : row);
};

BUILTINS.self_tile = function(args) {
    const g = args[0], bg = args.length > 1 ? Math.floor(args[1]) : 0;
    if (!Array.isArray(g) || g.length === 0) throw new Error('self_tile: not a grid');
    const R = g.length, C = g[0].length;
    const result = [];
    for (let br = 0; br < R; br++) {
        for (let fr = 0; fr < R; fr++) {
            const row = [];
            for (let bc = 0; bc < C; bc++) {
                for (let fc = 0; fc < C; fc++) {
                    row.push(g[br][bc] !== bg ? g[fr][fc] : bg);
                }
            }
            result.push(row);
        }
    }
    return result;
};

BUILTINS.bg_color = function(args) {
    const g = args[0];
    if (!Array.isArray(g)) throw new Error('bg_color: not a grid');
    const counts = new Array(10).fill(0);
    for (const row of g) if (Array.isArray(row)) for (const v of row) if (v >= 0 && v < 10) counts[v]++;
    let maxC = 0, maxIdx = 0;
    for (let i = 0; i < 10; i++) if (counts[i] > maxC) { maxC = counts[i]; maxIdx = i; }
    return maxIdx;
};

BUILTINS.objects = function(args) {
    const g = args[0], bg = args.length > 1 ? Math.floor(args[1]) : 0;
    if (!Array.isArray(g)) throw new Error('objects: not a grid');
    const R = g.length, C = g[0].length;
    const visited = Array.from({length: R}, () => new Array(C).fill(false));
    const objs = [];
    for (let r = 0; r < R; r++) {
        for (let c = 0; c < C; c++) {
            if (visited[r][c] || g[r][c] === bg) continue;
            const color = g[r][c];
            const queue = [[r, c]];
            let rmin = r, rmax = r, cmin = c, cmax = c;
            visited[r][c] = true;
            let qi = 0;
            while (qi < queue.length) {
                const [cr, cc] = queue[qi++];
                for (const [dr, dc] of [[-1,0],[1,0],[0,-1],[0,1]]) {
                    const nr = cr+dr, nc = cc+dc;
                    if (nr >= 0 && nr < R && nc >= 0 && nc < C && !visited[nr][nc] && g[nr][nc] === color) {
                        visited[nr][nc] = true; queue.push([nr, nc]);
                        rmin = Math.min(rmin, nr); rmax = Math.max(rmax, nr);
                        cmin = Math.min(cmin, nc); cmax = Math.max(cmax, nc);
                    }
                }
            }
            objs.push([rmin, cmin, rmax-rmin+1, cmax-cmin+1, color]);
        }
    }
    return objs;
};

// ================================================================
//  Canvas builtins (Phase D1 — S701)
//  Hosting page sets window._ax_canvas_ctx = canvas.getContext('2d')
// ================================================================
function getCanvasCtx() {
    if (typeof window !== 'undefined' && window._ax_canvas_ctx) return window._ax_canvas_ctx;
    return null;
}

function resolveColor(c) {
    if (typeof c === 'string') return c;
    if (typeof c === 'number' && c >= 0 && c < 10) return GRID_COLORS[c];
    if (typeof c === 'number') return '#' + (Math.abs(Math.round(c)) % 0xFFFFFF).toString(16).padStart(6, '0');
    return '#e8e6e3';
}

BUILTINS.canvas_clear = function(args) {
    const ctx = getCanvasCtx(); if (!ctx) return 0;
    ctx.fillStyle = resolveColor(args.length > 0 ? args[0] : 0);
    // Use CSS size if available (high-DPI), fall back to canvas size
    const w = parseInt(ctx.canvas.style.width) || ctx.canvas.width;
    const h = parseInt(ctx.canvas.style.height) || ctx.canvas.height;
    ctx.fillRect(0, 0, w, h);
    return 0;
};

BUILTINS.canvas_line = function(args) {
    const ctx = getCanvasCtx(); if (!ctx) return 0;
    ctx.strokeStyle = resolveColor(args.length > 4 ? args[4] : 8);
    ctx.lineWidth = args.length > 5 ? Math.max(1, args[5]) : 1;
    ctx.beginPath();
    ctx.moveTo(args[0], args[1]);
    ctx.lineTo(args[2], args[3]);
    ctx.stroke();
    return 0;
};

BUILTINS.canvas_rect = function(args) {
    const ctx = getCanvasCtx(); if (!ctx) return 0;
    ctx.fillStyle = resolveColor(args.length > 4 ? args[4] : 8);
    ctx.fillRect(args[0], args[1], args[2], args[3]);
    return 0;
};

BUILTINS.canvas_circle = function(args) {
    const ctx = getCanvasCtx(); if (!ctx) return 0;
    ctx.fillStyle = resolveColor(args.length > 3 ? args[3] : 8);
    ctx.beginPath();
    ctx.arc(args[0], args[1], Math.abs(args[2]), 0, 2 * Math.PI);
    ctx.fill();
    return 0;
};

BUILTINS.canvas_text = function(args) {
    const ctx = getCanvasCtx(); if (!ctx) return 0;
    const size = args.length > 3 ? Math.max(8, args[3]) : 14;
    ctx.fillStyle = resolveColor(args.length > 4 ? args[4] : 8);
    ctx.font = size + 'px monospace';
    ctx.fillText(String(args[2]), args[0], args[1]);
    return 0;
};

BUILTINS.canvas_pixel = function(args) {
    const ctx = getCanvasCtx(); if (!ctx) return 0;
    ctx.fillStyle = resolveColor(args.length > 2 ? args[2] : 8);
    ctx.fillRect(args[0], args[1], 1, 1);
    return 0;
};

BUILTINS.canvas_size = function() {
    const ctx = getCanvasCtx();
    if (!ctx) return [0, 0];
    const w = parseInt(ctx.canvas.style.width) || ctx.canvas.width;
    const h = parseInt(ctx.canvas.style.height) || ctx.canvas.height;
    return [w, h];
};

// ================================================================
//  Audio builtins (Phase D2 — S701)
//  Uses Web Audio API. Creates AudioContext on first use.
// ================================================================
function getAudioCtx() {
    if (typeof window === 'undefined') return null;
    if (!window._ax_audio_ctx) {
        try { window._ax_audio_ctx = new (window.AudioContext || window.webkitAudioContext)(); }
        catch(e) { return null; }
    }
    return window._ax_audio_ctx;
}

BUILTINS.beep = function(args) {
    const actx = getAudioCtx(); if (!actx) return 0;
    const freq = args.length > 0 ? Math.max(20, Math.min(20000, args[0])) : 440;
    const dur = args.length > 1 ? Math.max(10, Math.min(5000, args[1])) / 1000 : 0.2;
    const vol = args.length > 2 ? Math.max(0, Math.min(1, args[2])) : 0.3;
    const osc = actx.createOscillator();
    const gain = actx.createGain();
    osc.frequency.value = freq;
    osc.type = 'sine';
    gain.gain.value = vol;
    osc.connect(gain);
    gain.connect(actx.destination);
    osc.start(actx.currentTime);
    osc.stop(actx.currentTime + dur);
    return 0;
};

BUILTINS.playNote = function(args) {
    const actx = getAudioCtx(); if (!actx) return 0;
    const freq = args.length > 0 ? args[0] : 440;
    const vol = args.length > 1 ? Math.max(0, Math.min(1, args[1])) : 0.3;
    // Stop previous sustained note if any
    if (window._ax_sustained_osc) {
        try { window._ax_sustained_osc.stop(); } catch(e) {}
        window._ax_sustained_osc = null;
    }
    if (freq <= 0 || vol <= 0) return 0;
    const osc = actx.createOscillator();
    const gain = actx.createGain();
    osc.frequency.value = Math.max(20, Math.min(20000, freq));
    osc.type = 'sine';
    gain.gain.value = vol;
    osc.connect(gain);
    gain.connect(actx.destination);
    osc.start();
    window._ax_sustained_osc = osc;
    return 0;
};

BUILTINS.stopSound = function() {
    if (typeof window !== 'undefined' && window._ax_sustained_osc) {
        try { window._ax_sustained_osc.stop(); } catch(e) {}
        window._ax_sustained_osc = null;
    }
    return 0;
};

// ================================================================
//  Timer builtin (Phase D3 — S701)
// ================================================================
BUILTINS.now_ms = function() {
    if (typeof performance !== 'undefined') return Math.floor(performance.now());
    return Date.now();
};

// ================================================================
//  Persistent game state (Phase D4 — S701)
//  gvar("name") reads, svar("name", value) writes.
//  State persists across AX.run calls until clearState().
// ================================================================
const _gameState = {};
BUILTINS.raw_mode = function(args) {
    _rawMode = !!args[0];
    return args[0];
};

BUILTINS.gvar = function(args) {
    const name = String(args[0]);
    return (name in _gameState) ? _gameState[name] : 0;
};
BUILTINS.svar = function(args) {
    const name = String(args[0]);
    _gameState[name] = args[1];
    return args[1];
};

// ================================================================
//  Evaluator
// ================================================================
const MAX_DEPTH = 49; // b^2

function run(src) {
    const outputLines = [];
    const values = [];
    const traces = [];
    const TRACE_LIMIT = 50;
    const _now = typeof performance !== 'undefined' ? function() { return performance.now(); } : Date.now;

    const ctx = {
        trace: function(html) {
            if (traces.length < TRACE_LIMIT) traces.push(html);
            else if (traces.length === TRACE_LIMIT) traces.push('<span class="tr-step">... (trace limit reached)</span>');
        },
        output: function(html, val) {
            outputLines.push(html);
            values.push(val);
        }
    };

    const t0 = _now();
    const tokens = tokenize(src);
    const t1 = _now();
    const stmts = new Parser(tokens).parseProgram();
    const t2 = _now();
    const env = {...CONSTANTS};
    const fns = {};

    function ev(node, localEnv, depth) {
        if (depth > MAX_DEPTH) throw new Error('Max recursion depth (' + MAX_DEPTH + ') exceeded');
        switch (node.t) {
            case 'Num': return (_rawMode || !Number.isInteger(node.v)) ? node.v : ringMod(node.v);
            case 'Str': return node.v;
            case 'Sym': {
                if (node.name in localEnv) return localEnv[node.name];
                if (node.name in fns) return fns[node.name];
                throw new Error('Line ' + (node.line||'?') + ': Unknown: ' + node.name);
            }
            case 'Bin': {
                const l = ev(node.l, localEnv, depth), r = ev(node.r, localEnv, depth);
                // String concatenation: "str" + anything = string
                if (node.op === '+' && (typeof l === 'string' || typeof r === 'string')) {
                    const ls = typeof l === 'string' ? l : (Number.isInteger(l) ? String(l) : (typeof l === 'number' ? l.toFixed(6) : String(l)));
                    const rs = typeof r === 'string' ? r : (Number.isInteger(r) ? String(r) : (typeof r === 'number' ? r.toFixed(6) : String(r)));
                    return ls + rs;
                }
                // Raw mode OR float propagation: regular JS arithmetic
                if (_rawMode || (typeof l === 'number' && !Number.isInteger(l)) || (typeof r === 'number' && !Number.isInteger(r))) {
                    const lv = typeof l === 'number' ? l : 0, rv = typeof r === 'number' ? r : 0;
                    switch (node.op) {
                        case '+': return lv + rv;
                        case '-': return lv - rv;
                        case '*': return lv * rv;
                        case '/': if (rv === 0) throw new Error('Division by zero'); return lv / rv;
                        case '%': return rv !== 0 ? lv % rv : 0;
                        case '^': return Math.pow(lv, rv);
                        case '<': return lv < rv ? 1 : 0;
                        case '>': return lv > rv ? 1 : 0;
                        case '==': return Math.abs(lv - rv) < 1e-10 ? 1 : 0;
                        case '!=': return Math.abs(lv - rv) >= 1e-10 ? 1 : 0;
                        case '<=': return lv <= rv ? 1 : 0;
                        case '>=': return lv >= rv ? 1 : 0;
                    }
                }
                switch (node.op) {
                    case '+': return ringMod(l + r);
                    case '-': return ringMod(l - r);
                    case '*': return ringMod(l * r);
                    case '/': {
                        const inv = multInverse(r);
                        if (inv >= 0) return ringMod(l * inv);
                        if (r === 0) throw new Error('Division by zero');
                        return l / r;
                    }
                    case '%': return r !== 0 ? ringMod(l % r) : 0;
                    case '^': return modPow(l, r);
                    case '<': return l < r ? 1 : 0;
                    case '>': return l > r ? 1 : 0;
                    case '==': return l === r ? 1 : 0;
                    case '!=': return l !== r ? 1 : 0;
                    case '<=': return l <= r ? 1 : 0;
                    case '>=': return l >= r ? 1 : 0;
                }
                break;
            }
            case 'Unary':
                if (node.op === '~') {
                    const uv = ev(node.e, localEnv, depth);
                    return _rawMode ? -uv : ringMod(N - uv);
                }
                break;
            case 'Thresh': {
                const v = ev(node.val, localEnv, depth);
                const th = ev(node.th, localEnv, depth);
                return v > th ? v : ringMod(N - v);
            }
            case 'If': {
                const c = ev(node.cond, localEnv, depth);
                return c !== 0 ? ev(node.then_, localEnv, depth) : ev(node.else_, localEnv, depth);
            }
            case 'Seq':
                ev(node.a, localEnv, depth);
                return ev(node.b, localEnv, depth);
            case 'LetExpr': {
                const val = ev(node.val, localEnv, depth);
                return ev(node.body, {...localEnv, [node.name]: val}, depth);
            }
            case 'Call': return evalCall(node.fn, node.args, localEnv, depth, node.line);
            case 'Idx': {
                const arr = ev(node.arr, localEnv, depth);
                const idx = Math.floor(ev(node.idx, localEnv, depth));
                if (!Array.isArray(arr)) throw new Error('Cannot index non-array');
                if (idx < 0 || idx >= arr.length) throw new Error('Index out of bounds: ' + idx);
                return arr[idx];
            }
            case 'Arr': return node.elems.map(e => ev(e, localEnv, depth));
            case 'For': {
                const arr = ev(node.iter, localEnv, depth);
                if (!Array.isArray(arr)) throw new Error('for..in requires an array');
                if (arr.length > 10000) throw new Error('Iteration limit (max 10000)');
                return arr.map(item => ev(node.body, {...localEnv, [node.varName]: item}, depth));
            }
            case 'DFloat': {
                const s = ev(node.s, localEnv, depth);
                const b = ev(node.b, localEnv, depth);
                return ringMod(Math.floor(s * b));
            }
        }
        throw new Error('Cannot evaluate: ' + JSON.stringify(node));
    }

    function evalCall(fnName, argNodes, localEnv, depth, line) {
        const args = argNodes.map(a => ev(a, localEnv, depth));
        // Check builtins
        if (BUILTINS[fnName]) return BUILTINS[fnName](args, ctx);
        // User-defined function
        if (fnName in fns) {
            const fn = fns[fnName];
            if (args.length !== fn.params.length) throw new Error('Line ' + (line||'?') + ': ' + fnName + ' expects ' + fn.params.length + ' args, got ' + args.length);
            const callEnv = {...fn.closureEnv};
            for (let i = 0; i < fn.params.length; i++) callEnv[fn.params[i]] = args[i];
            return ev(fn.body, callEnv, depth + 1);
        }
        throw new Error('Line ' + (line||'?') + ': Unknown function: ' + fnName);
    }

    // Execute statements
    let error = null;
    try {
        for (const stmt of stmts) {
            switch (stmt.t) {
                case 'Let':
                    env[stmt.name] = ev(stmt.val, env, 0);
                    break;
                case 'Fn':
                    fns[stmt.name] = {params:stmt.params, body:stmt.body, closureEnv:{...env}};
                    for (const name in fns) fns[name].closureEnv = {...env, ...Object.fromEntries(Object.entries(fns).map(([k,v])=>[k,v]))};
                    break;
                case 'Print': {
                    const outBefore = outputLines.length;
                    const val = ev(stmt.expr, env, 0);
                    if (outputLines.length === outBefore) {
                        outputLines.push(typeof val === 'string' ? fmtText(val) : fmtValue(val));
                    }
                    values.push(val);
                    break;
                }
                case 'ExprStmt': {
                    const outBefore = outputLines.length;
                    const val = ev(stmt.expr, env, 0);
                    if (outputLines.length === outBefore) {
                        outputLines.push(fmtValue(val));
                    }
                    values.push(val);
                    break;
                }
            }
        }
    } catch(e) {
        error = e.message;
    }

    const t3 = _now();
    const profile = {
        tokenize_ms: +(t1 - t0).toFixed(2),
        parse_ms: +(t2 - t1).toFixed(2),
        eval_ms: +(t3 - t2).toFixed(2),
        total_ms: +(t3 - t0).toFixed(2),
        wasm: _wasm !== null && N === TRUE_N
    };
    return { lines: outputLines, values, traces, error, profile };
}

// ================================================================
//  Persistent Session (Phase D — S701, for game loops)
//  Parse once, call tick(N) without re-parsing the whole source.
// ================================================================
function createSession() {
    const env = {...CONSTANTS};
    const fns = {};

    const ctx = {
        trace: function() {},
        output: function() {}
    };

    function ev(node, localEnv, depth) {
        if (depth > MAX_DEPTH) throw new Error('Max depth');
        switch (node.t) {
            case 'Num': return (_rawMode || !Number.isInteger(node.v)) ? node.v : ringMod(node.v);
            case 'Str': return node.v;
            case 'Sym': {
                if (node.name in localEnv) return localEnv[node.name];
                if (node.name in fns) return fns[node.name];
                if (node.name in env) return env[node.name];
                throw new Error('Unknown: ' + node.name);
            }
            case 'Bin': {
                const l = ev(node.l, localEnv, depth), r = ev(node.r, localEnv, depth);
                if (node.op === '+' && (typeof l === 'string' || typeof r === 'string')) {
                    const ls = typeof l === 'string' ? l : (Number.isInteger(l) ? String(l) : (typeof l === 'number' ? l.toFixed(6) : String(l)));
                    const rs = typeof r === 'string' ? r : (Number.isInteger(r) ? String(r) : (typeof r === 'number' ? r.toFixed(6) : String(r)));
                    return ls + rs;
                }
                if (_rawMode || (typeof l === 'number' && !Number.isInteger(l)) || (typeof r === 'number' && !Number.isInteger(r))) {
                    const lv = typeof l === 'number' ? l : 0, rv = typeof r === 'number' ? r : 0;
                    switch (node.op) {
                        case '+': return lv + rv; case '-': return lv - rv;
                        case '*': return lv * rv; case '%': return rv !== 0 ? lv % rv : 0;
                        case '/': if (rv === 0) throw new Error('Division by zero'); return lv / rv;
                        case '^': return Math.pow(lv, rv);
                        case '<': return lv < rv ? 1 : 0; case '>': return lv > rv ? 1 : 0;
                        case '==': return Math.abs(lv - rv) < 1e-10 ? 1 : 0;
                        case '!=': return Math.abs(lv - rv) >= 1e-10 ? 1 : 0;
                        case '<=': return lv <= rv ? 1 : 0; case '>=': return lv >= rv ? 1 : 0;
                    }
                }
                switch (node.op) {
                    case '+': return ringMod(l + r); case '-': return ringMod(l - r);
                    case '*': return ringMod(l * r); case '%': return r !== 0 ? ringMod(l % r) : 0;
                    case '/': { const inv = multInverse(r); if (inv >= 0) return ringMod(l * inv); if (r === 0) throw new Error('Division by zero'); return l / r; }
                    case '^': return modPow(l, r);
                    case '<': return l < r ? 1 : 0; case '>': return l > r ? 1 : 0;
                    case '==': return l === r ? 1 : 0; case '!=': return l !== r ? 1 : 0;
                    case '<=': return l <= r ? 1 : 0; case '>=': return l >= r ? 1 : 0;
                }
                break;
            }
            case 'Unary': if (node.op === '~') { const uv = ev(node.e, localEnv, depth); return _rawMode ? -uv : ringMod(N - uv); } break;
            case 'Thresh': { const v = ev(node.val, localEnv, depth), th = ev(node.th, localEnv, depth); return v > th ? v : ringMod(N - v); }
            case 'If': return ev(node.cond, localEnv, depth) !== 0 ? ev(node.then_, localEnv, depth) : ev(node.else_, localEnv, depth);
            case 'Seq': ev(node.a, localEnv, depth); return ev(node.b, localEnv, depth);
            case 'LetExpr': return ev(node.body, {...localEnv, [node.name]: ev(node.val, localEnv, depth)}, depth);
            case 'Call': {
                const args = node.args.map(a => ev(a, localEnv, depth));
                if (BUILTINS[node.fn]) return BUILTINS[node.fn](args, ctx);
                if (node.fn in fns) {
                    const fn = fns[node.fn];
                    const callEnv = {...fn.closureEnv};
                    for (let i = 0; i < fn.params.length; i++) callEnv[fn.params[i]] = args[i];
                    return ev(fn.body, callEnv, depth + 1);
                }
                throw new Error('Unknown function: ' + node.fn);
            }
            case 'Idx': { const arr = ev(node.arr, localEnv, depth), idx = Math.floor(ev(node.idx, localEnv, depth)); if (!Array.isArray(arr)) throw new Error('Not array'); return arr[idx]; }
            case 'Arr': return node.elems.map(e => ev(e, localEnv, depth));
            case 'For': { const arr = ev(node.iter, localEnv, depth); if (!Array.isArray(arr)) throw new Error('for needs array'); return arr.map(item => ev(node.body, {...localEnv, [node.varName]: item}, depth)); }
            case 'DFloat': return ringMod(Math.floor(ev(node.s, localEnv, depth) * ev(node.b, localEnv, depth)));
        }
        throw new Error('Cannot eval: ' + node.t);
    }

    return {
        exec: function(src) {
            try {
                const stmts = new Parser(tokenize(src)).parseProgram();
                let lastVal = 0;
                for (const stmt of stmts) {
                    switch (stmt.t) {
                        case 'Let': env[stmt.name] = ev(stmt.val, env, 0); break;
                        case 'Fn':
                            fns[stmt.name] = {params:stmt.params, body:stmt.body, closureEnv:{...env}};
                            for (const name in fns) fns[name].closureEnv = {...env, ...Object.fromEntries(Object.entries(fns).map(([k,v])=>[k,v]))};
                            break;
                        case 'Print': lastVal = ev(stmt.expr, env, 0); break;
                        case 'ExprStmt': lastVal = ev(stmt.expr, env, 0); break;
                    }
                }
                return { error: null, value: lastVal };
            } catch(e) {
                return { error: e.message, value: 0 };
            }
        }
    };
}

// ================================================================
//  Public API
// ================================================================
return {
    get N() { return N; },
    get CRT_MODS() { return CRT_MODS.slice(); },
    CONSTANTS, VALUE_NAMES, KEYWORDS, BUILTINS, GRID_COLORS,
    BUILTIN_NAMES: new Set(Object.keys(BUILTINS)),

    // WASM acceleration (Phase W v0.2 — S739)
    setWasm: function(mod) { _wasm = mod; },
    get wasmActive() { return _wasm !== null && N === TRUE_N; },

    // Ring configuration (S497)
    setRing, factorPrimePowers,

    // Ring math (exposed for pages that need direct access)
    ringMod, gcd, crt, coupling, eigenvalue, mirror,
    eulerPhi, multOrder, multInverse, modPow,

    // Language
    tokenize, parse, Parser, run, createSession,

    // Game state
    clearState: function() { for (const k in _gameState) delete _gameState[k]; _rawMode = false; },

    // Formatting
    esc, fmtValue, fmtGrid, fmtNum, fmtText
};

})();
