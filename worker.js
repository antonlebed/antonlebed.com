/* [DEAD] SCAFFOLDING -- Cloudflare Worker: SPA routing + pre-rendered SSR.
   Browser -> _app.html (WASM + DOM imports).
   Crawler -> pre-rendered HTML from /_ssr/ static assets.
   Dies when WASI provides native server-side DOM. */

var _routeMap = {
  '':'home','home':'home',
  'basics':'home',
  'patterns':'patterns',
  'theory':'theory',
  'connections':'connections',
  'ideas':'ideas',
  'lab':'lab',
  'demos':'demos',
  'eigenvalue_swim':'patterns','repl':'lab',
  'numbers_clocks':'home',
  'crt':'home',
  'rings_channels':'home',
  'waves_shadows':'home',
  'implications':'home',
  'story':'home',
  'derive':'home',
  'death':'home',
  'algebra':'patterns',
  'spectrum':'patterns',
  'closure':'patterns',
  'geometry':'patterns',
  'lambda':'patterns',
  'symbiosis':'patterns',
  'fields':'patterns',
  'music':'patterns',
  'constants':'patterns',
  'sandpile':'patterns',
  'swim':'patterns',
  'ring_stacking':'patterns',
  'torus':'patterns',
  'sphere':'patterns',
  'eca':'patterns',
  'carousel':'patterns',
  'cunningham':'theory',
  'heegner':'theory',
  'k_squared_stop':'theory',
  'depth_return':'theory',
  'depth_quad':'theory',
  'mirror_cost':'theory',
  'bernoulli':'theory',
  'pell_twins':'theory',
  'golden_ratio':'theory',
  'smooth_census':'theory',
  'stormer_pairs':'theory',
  'universal_boundary':'theory',
  'lambda_chain':'theory',
  'gap_pairs':'theory',
  'goldbach':'theory',
  'equator':'theory',
  'shadow_eval':'theory',
  'd_power_gaussian':'theory',
  'cyclotomic_fibonacci':'theory',
  'fano_e8':'theory',
  'arcsine_cumulant':'theory',
  'figurate_bridge':'theory',
  'freewill':'theory',
  'infinity':'theory',
  'turbulence':'connections',
  'sleep':'connections',
  'kingdoms':'connections',
  'ecc':'connections',
  'crt_stats':'connections',
  'dimension':'connections',
  'dark_energy':'connections',
  'chemistry':'connections',
  'dna':'connections',
  'braid':'connections',
  'ouroboros':'connections',
  'modular_forms':'connections',
  'lie_algebra':'connections',
  'eta_bridge':'connections',
  'monster_moonshine':'connections',
  'lambda_rlm':'connections',
  'bootstrap':'ideas',
  'septum':'ideas',
  'mirror':'ideas',
  'sacrifice':'ideas',
  'terms':'ideas',
  'lattice':'ideas',
  'duality':'ideas',
  'observer':'ideas',
  'depth':'ideas',
  'transcend':'ideas',
  'cc0':'ideas',
  'revolution':'ideas',
  'ouroboros_compiler':'lab',
  'tutorial':'lab',
  'ecc_live':'lab',
  'crt_train':'lab',
  'coupling':'lab',
  'crt_anatomy':'lab',
  'emergence':'lab',
  'omega_emergence':'lab',
  'omega_journey':'lab',
  'ax_games':'lab',
  'sensor':'lab',
  'chain':'lab',
  'ai':'lab',
  'curriculum':'lab',
  'scaling':'lab',
  'hdc':'lab',
  'evolve':'lab',
  'nca':'lab',
  'chain_ai':'lab',
  'bridge_het':'lab',
  'ring_substrate':'lab',
  'ring_sweep':'lab',
  'anti_ring':'lab',
  'proof_core':'lab',
  'proof_structure':'lab',
  'proof_ai':'lab',
  'proof_frontier':'lab',
  'compiler':'lab',
  'hash':'demos',
  'consensus':'demos',
  'rng':'demos',
  'compression':'demos',
  'pid':'demos',
  'stego':'demos',
  'key_exchange':'demos',
  'timetabling':'demos',
  'cdma':'demos',
  'fountain':'demos',
  'ofdm':'demos',
  'gpu_compute':'demos',
  'scheduling':'demos',
  'db_index':'demos',
  'audio':'demos',
  'sort':'demos',
  'cluster':'demos',
  'verify':'demos',
  'signature':'demos',
  'recommend':'demos',
  'federated':'demos',
  'protein':'demos',
  'quantum_ecc':'demos',
  'anomaly':'demos',
  'genomic':'demos',
  'finance':'demos',
  'procgen':'demos',
  'fingerprint':'demos',
  'speech':'demos',
  'object':'demos',
  'medical':'demos',
  'video':'demos',
  'bci':'demos',
  'pde':'demos',
  'arc':'demos',
  'mesh':'demos',
  'image_filter':'demos',
};
var _currentModule = '';
function _routeMod(r) { return _routeMap[r] || 'home'; }

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    /* ===== Sensor API: bridge writes, page reads ===== */
    if (url.pathname === '/api/sensor') {
      if (request.method === 'OPTIONS') {
        return new Response(null, { headers: { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET,POST', 'Access-Control-Allow-Headers': 'Authorization,Content-Type' } });
      }
      if (request.method === 'POST') {
        var auth = request.headers.get('Authorization') || '';
        if (auth !== 'Bearer crt7-sensor-214414200') {
          return new Response('Unauthorized', { status: 401 });
        }
        var body = await request.text();
        if (env.SENSOR_DATA) { await env.SENSOR_DATA.put('latest', body); }
        return new Response('OK', { status: 200, headers: { 'Access-Control-Allow-Origin': '*' } });
      }
      var data = '{}';
      if (env.SENSOR_DATA) { data = await env.SENSOR_DATA.get('latest', { cacheTtl: 600 }) || '{}'; }
      return new Response(data, { status: 200, headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', 'Cache-Control': 'public, max-age=600' } });
    }

    /* Static assets (.html, .js, .wasm, .png, .jpg, .css) */
    if (url.pathname.includes('.')) {
      return env.ASSETS.fetch(request);
    }

    /* ===== SSR: serve pre-rendered HTML unless real browser navigation ===== */
    var _sfm = request.headers.get('Sec-Fetch-Mode');
    var _isNav = (_sfm === 'navigate' || _sfm === 'same-origin');
    if (!_isNav) {
      try {
        var parts = url.pathname.split('/').filter(Boolean);
        var _ssrPath = '/_ssr/' + (parts.length ? parts.join('/') : 'home') + '.html';
        var _ssrResp = await env.ASSETS.fetch(new URL(_ssrPath, url.origin).toString());
        if (_ssrResp.ok) return new Response(_ssrResp.body, {
          headers: { 'Content-Type': 'text/html;charset=utf-8' }
        });
      } catch (e) { console.log('SSR error: ' + (e.message || e)); }
    }
    /* Browser: client-side rendering via _app.html bootstrap */
    return env.ASSETS.fetch(new URL('/_app.html', url.origin).toString());
  }
};
