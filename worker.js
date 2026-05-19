/* [DEAD] SCAFFOLDING -- Cloudflare Worker: sensor API + SSG.
   142 pages pre-rendered as static HTML. Zero WASM imports.
   Dies when WASI provides native server-side DOM. */
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

    /* ===== SSG: serve pre-rendered HTML ===== */
    var parts = url.pathname.split('/').filter(Boolean);
    var route = parts.length >= 2 ? parts[parts.length - 1] : (parts[0] || 'home');
    try {
      var res = await env.ASSETS.fetch(new URL('/ssr/' + route + '.html', url.origin));
      if (res.ok) return new Response(res.body, { headers: { 'Content-Type': 'text/html;charset=utf-8' } });
    } catch(e) {}
    return env.ASSETS.fetch(new URL('/_app.html', url.origin));
  }
};
