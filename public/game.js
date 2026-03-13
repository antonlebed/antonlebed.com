// game.js — .ax Game Loop Harness (Phase D4 — S701)
// Usage: <script src="ax.js"></script><script src="game.js"></script>
// Then: axGame.run(axSource, canvasId, fps)
//
// .ax source must define: fn tick(frame) = (... ; state)
// Optional: fn init() = (... ; state)
// Harness calls tick(frame) at fps, wires canvas/audio/input.
// frame = frame counter (0, 1, 2, ...). Increments each tick.
//
// Input: keyPressed("ArrowUp") etc. in .ax code, reads from _ax_keys.
// Mouse: mouseX(), mouseY(), mouseClick() in .ax code.
// 970200 = TRUE FORM. sigma/sigma = sigma.

const axGame = (function() {
'use strict';

let _animId = null;
let _running = false;

// Key state
const _keys = {};
let _mouseX = 0, _mouseY = 0, _mouseClicked = false;

function setupInput(canvas) {
    document.addEventListener('keydown', function(e) {
        _keys[e.code] = true;
        // Prevent arrow keys from scrolling
        if (e.code.startsWith('Arrow')) e.preventDefault();
    });
    document.addEventListener('keyup', function(e) {
        _keys[e.code] = false;
    });
    canvas.addEventListener('mousemove', function(e) {
        const r = canvas.getBoundingClientRect();
        _mouseX = Math.floor(e.clientX - r.left);
        _mouseY = Math.floor(e.clientY - r.top);
    });
    canvas.addEventListener('click', function() {
        _mouseClicked = true;
    });
    // Touch support
    canvas.addEventListener('touchstart', function(e) {
        const r = canvas.getBoundingClientRect();
        _mouseX = Math.floor(e.touches[0].clientX - r.left);
        _mouseY = Math.floor(e.touches[0].clientY - r.top);
        _mouseClicked = true;
        e.preventDefault();
    });
}

// Register input builtins into AX
function registerInputBuiltins() {
    AX.BUILTINS.keyPressed = function(args) {
        const code = String(args[0]);
        return _keys[code] ? 1 : 0;
    };
    AX.BUILTINS.mouseX = function() { return _mouseX; };
    AX.BUILTINS.mouseY = function() { return _mouseY; };
    AX.BUILTINS.mouseClick = function() {
        const c = _mouseClicked ? 1 : 0;
        _mouseClicked = false; // consumed on read
        return c;
    };
}

function stop() {
    _running = false;
    if (_animId) { cancelAnimationFrame(_animId); _animId = null; }
    // Stop any sustained audio
    if (typeof AX !== 'undefined' && AX.BUILTINS.stopSound) AX.BUILTINS.stopSound([]);
}

function run(axSource, canvasId, fps) {
    stop();

    const canvas = document.getElementById(canvasId);
    if (!canvas) throw new Error('game.js: canvas "' + canvasId + '" not found');
    const ctx2d = canvas.getContext('2d');
    window._ax_canvas_ctx = ctx2d;

    setupInput(canvas);
    registerInputBuiltins();

    // Parse and set up the .ax environment
    const tokens = AX.tokenize(axSource);
    const stmts = new AX.Parser(tokens).parseProgram();
    const env = {...AX.CONSTANTS};
    const fns = {};

    // First pass: register all functions and top-level lets
    for (const stmt of stmts) {
        if (stmt.t === 'Fn') {
            fns[stmt.name] = {params: stmt.params, body: stmt.body, closureEnv: {}};
        }
    }
    // Set closures
    for (const name in fns) fns[name].closureEnv = {...env};

    // Run top-level non-fn statements (let bindings, etc.)
    // We use AX.run for simplicity but capture init/tick fns
    const initResult = AX.run(axSource);
    if (initResult.error) {
        console.error('game.js init error:', initResult.error);
        return;
    }

    // Now run game loop. We call tick(frame) by running it as .ax
    let frame = 0;
    const interval = Math.max(16, Math.floor(1000 / (fps || 30)));
    _running = true;

    function gameLoop() {
        if (!_running) return;
        // Call tick(frame) via AX.run with a wrapper
        const tickSrc = axSource + '\ntick(' + frame + ')';
        const result = AX.run(tickSrc);
        if (result.error) {
            console.error('game.js tick error at frame ' + frame + ':', result.error);
            stop();
            return;
        }
        frame++;
        _animId = setTimeout(gameLoop, interval);
    }

    gameLoop();
}

return { run, stop };
})();
