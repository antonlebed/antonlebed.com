export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    /* Sensor API (KV bridge for ESP32 mesh) */
    if (url.pathname === '/api/sensor') {
      if (request.method === 'OPTIONS') {
        return new Response(null, { headers: { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET,POST', 'Access-Control-Allow-Headers': 'Authorization,Content-Type' } });
      }
      if (request.method === 'POST') {
        const auth = request.headers.get('Authorization') || '';
        if (auth !== 'Bearer crt7-sensor-214414200') return new Response('Unauthorized', { status: 401 });
        const body = await request.text();
        if (env.SENSOR_DATA) await env.SENSOR_DATA.put('latest', body);
        return new Response('OK', { status: 200, headers: { 'Access-Control-Allow-Origin': '*' } });
      }
      const data = env.SENSOR_DATA ? (await env.SENSOR_DATA.get('latest', { cacheTtl: 600 }) || '{}') : '{}';
      return new Response(data, { status: 200, headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', 'Cache-Control': 'public, max-age=600' } });
    }

    /* Redirects for renamed pages (P10) — keep old bookmarks alive */
    const REDIRECTS = {
      '/primer': '/sieve', '/primer.html': '/sieve',
      '/ring': '/tower', '/ring.html': '/tower',
      '/seedflower': '/prediction', '/seedflower.html': '/prediction',
    };
    const redir = REDIRECTS[url.pathname];
    if (redir) return Response.redirect(new URL(redir, url.origin), 301);

    /* Static assets — everything with an extension */
    if (url.pathname.includes('.')) {
      return env.ASSETS.fetch(request);
    }

    /* Bare paths: / → index.html, /sieve → sieve.html */
    const path = url.pathname.replace(/\/$/, '') || '/index';
    const page = path.split('/').pop() || 'index';
    return env.ASSETS.fetch(new URL('/' + page + '.html', url.origin));
  }
};
