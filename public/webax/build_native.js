/* build_native.js — ☠️ SCAFFOLDING. Compiles site.ax using native WASM compiler.
   No ring limit. deep_ouroboros.wasm uses i32 arithmetic (up to 2^31).
   Usage: node webax/build_native.js
   Dies when .ax has its own file I/O and build_entry.ax can self-host. */
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const COMPILER = path.join(ROOT, 'anton/code/deep_ouroboros.wasm');
const OUT = path.join(__dirname, 'site.wasm');

/* Source files (6 rings × 2 + core + router) */
const SRC_DIR = path.join(__dirname, 'pages');
const FILES = [
  'core.ax', 'pages_narrative.ax', 'pages_core.ax',
  'pages_deep.ax', 'pages_kingdom.ax',
  'pages_deep_struct.ax', 'pages_deep_phys.ax',
  'pages_data.ax', 'pages_teach.ax',
  'pages_observe.ax', 'pages_living.ax',
  'router.ax'
];

/* WASM memory helpers */
function writeString(mem32, ptr, str) {
  mem32[ptr / 4] = str.length;
  for (let i = 0; i < str.length; i++) mem32[ptr / 4 + 1 + i] = str.charCodeAt(i);
  return ptr;
}
function readArr(mem32, ptr) {
  const len = mem32[ptr / 4];
  return Array.from({ length: len }, (_, i) => mem32[ptr / 4 + 1 + i]);
}

async function main() {
  /* Load native compiler */
  const compilerBytes = fs.readFileSync(COMPILER);
  const imports = {
    env: {
      show_int: v => v,
      show_str: ptr => ptr
    }
  };
  const { instance } = await WebAssembly.instantiate(compilerBytes, imports);
  const cm = instance.exports;

  /* Grow memory: 4096 pages = 256MB (compiler needs space for AST + code buffers) */
  cm.memory.grow(4080);

  /* Concatenate source files */
  const src = FILES.map(f => fs.readFileSync(path.join(SRC_DIR, f), 'utf8')).join('\n');
  console.log(`Source: ${src.length} chars (${FILES.length} files)`);

  /* Write source into WASM memory at high offset (avoid heap collision) */
  const srcOffset = 200 * 1024 * 1024; /* 200MB — far above any heap allocation */
  let mem32 = new Int32Array(cm.memory.buffer);
  writeString(mem32, srcOffset, src);

  /* Compile */
  const t0 = Date.now();
  const resultPtr = cm.wasm_from_src(srcOffset);
  const dt = Date.now() - t0;

  /* Read WASM bytes from compiler memory */
  mem32 = new Int32Array(cm.memory.buffer); /* re-read in case memory grew */
  const wasmArr = readArr(mem32, resultPtr);
  const wasmBytes = new Uint8Array(wasmArr);

  /* Validate */
  const valid = WebAssembly.validate(wasmBytes);
  console.log(`site.wasm: ${wasmBytes.length} bytes (${dt}ms, valid=${valid})`);

  if (!valid) {
    console.error('ERROR: Compiler produced invalid WASM');
    process.exit(1);
  }

  /* Write */
  fs.writeFileSync(OUT, wasmBytes);
  console.log(`Wrote ${OUT}`);
}

main().catch(e => { console.error(e); process.exit(1); });
