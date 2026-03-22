/* build_native.js — ☠️ SCAFFOLDING. Compiles site.ax using native WASM compiler.
   No ring limit. deep_ouroboros.wasm uses i32 arithmetic (up to 2^31).
   Usage: node webax/build_native.js
   Dies when .ax has its own file I/O and build_entry.ax can self-host. */
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const COMPILER = path.join(ROOT, 'anton/code/deep_ouroboros.wasm');
const OUT = path.join(__dirname, 'site.wasm');

/* Source files — core + individual pages + router */
const SRC_DIR = path.join(__dirname, 'pages');
const FILES = [
  'core.ax', 'pages_narrative.ax', 'pages_core.ax',
  'pages_deep.ax', 'pages_kingdom.ax', 'pages_kingdom_2.ax',
  /* was pages_deep_struct.ax (2674L → 14 files, S955) */
  'page_ground.ax', 'page_duality.ax', 'page_depth.ax', 'page_transcend.ax',
  'page_genesis.ax', 'page_algebra.ax', 'page_spectrum.ax', 'page_closure.ax',
  'page_geometry.ax', 'page_lambda.ax', 'page_symbiosis.ax', 'page_music.ax',
  'page_fields.ax', 'page_constants.ax',
  'pages_deep_phys.ax', 'pages_deep_phys_2.ax',
  'pages_data.ax', 'pages_data_2.ax',
  /* was pages_teach.ax (2274L → 19 files, S955) */
  'page_cunningham.ax', 'page_heegner.ax', 'page_bernoulli.ax',
  'page_k_squared_stop.ax', 'page_pell_twins.ax', 'page_universal_boundary.ax',
  'page_depth_return.ax', 'page_depth_quad.ax', 'page_mirror_cost.ax',
  'page_lambda_chain.ax', 'page_golden_ratio.ax', 'page_smooth_census.ax',
  'page_stormer_pairs.ax', 'page_shadow_eval.ax', 'page_d_power_gaussian.ax',
  'page_cyclotomic_fibonacci.ax', 'page_fano_e8.ax', 'page_arcsine_cumulant.ax',
  'page_figurate_bridge.ax',
  'page_sandpile.ax', 'pages_observe.ax', 'pages_living.ax',
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
  let cmRef = null;
  let topLevelCount = 0;
  let errorCount = 0;
  const imports = {
    env: {
      show_int: v => v,
      show_str: ptr => {
        if (!cmRef) return ptr;
        const m = new Int32Array(cmRef.memory.buffer);
        const slen = m[ptr / 4];
        let s = '';
        for (let i = 0; i < slen; i++) s += String.fromCharCode(m[ptr / 4 + 1 + i]);
        if (s.startsWith('warning:') || s.startsWith('  top-level') || s.startsWith('error:')) {
          /* Decode i32 string pointers in error messages (compiler emits ptrs for fn names) */
          const decoded = s.replace(/'(\d{7,})'/g, (_, p) => {
            try { const a = parseInt(p), l = m[a/4]; if (l > 0 && l < 200) { let n = ''; for (let j = 0; j < l; j++) n += String.fromCharCode(m[a/4+1+j]); return `'${n}'`; } } catch(e) {}
            return `'${p}'`;
          });
          console.log(decoded);
          const tlMatch = s.match(/^warning: (\d+) top-level/);
          if (tlMatch) topLevelCount = parseInt(tlMatch[1]);
          if (s.startsWith('error:')) errorCount++;
        }
        return ptr;
      }
    }
  };
  const { instance } = await WebAssembly.instantiate(compilerBytes, imports);
  const cm = instance.exports;
  cmRef = cm;

  /* Concatenate source files */
  const src = FILES.map(f => fs.readFileSync(path.join(SRC_DIR, f), 'utf8')).join('\n');
  console.log(`Source: ${src.length} chars (${FILES.length} files)`);

  /* Scale memory to source size: parser uses ~360 bytes/char, build adds ~50MB overhead.
     Formula: need ~(src.length * 400 + 100MB) for heap, plus source string at safe offset.
     WASM max = 4GB (65536 pages). Grow to 2x estimated need for safety. */
  const heapEstimate = Math.ceil(src.length * 400 / 65536) + 2048; /* pages for heap */
  const totalPages = Math.min(heapEstimate, 65520); /* cap at ~4GB */
  cm.memory.grow(totalPages - 16); /* subtract initial 16 pages */
  const totalMB = (totalPages * 65536 / 1048576) | 0;
  const srcOffset = (totalMB - 32) * 1024 * 1024; /* source 32MB below memory ceiling */
  console.log(`Memory: ${totalMB}MB, source at ${(srcOffset/1048576)|0}MB`);
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

  /* BUILD GUARD: S976 lesson — content bleed deployed because warnings were printed
     but not checked. Router entry = 1 legitimate top-level statement. Anything beyond
     that means content is leaking as top-level code. Hard error. */
  if (errorCount > 0) {
    console.error(`BUILD GUARD: ${errorCount} error(s). Fix before deploying.`);
    process.exit(1);
  }
  if (topLevelCount > 1) {
    console.error(`BUILD GUARD: ${topLevelCount} top-level statement(s) (expected 1 for router entry). Content bleed?`);
    process.exit(1);
  }

  /* Write */
  fs.writeFileSync(OUT, wasmBytes);
  console.log(`Wrote ${OUT}`);
}

main().catch(e => { console.error(e); process.exit(1); });
