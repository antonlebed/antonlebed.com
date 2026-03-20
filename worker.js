/* ☠️ SCAFFOLDING — Cloudflare Worker for SPA routing.
   Routes /new/* to webax bootstrap. Old site untouched.
   Dies when old site is swapped out (becomes simple not_found_handling). */
export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    /* Static assets (files with extensions): serve directly */
    if (url.pathname.match(/\.[a-z0-9]+$/i)) {
      return env.ASSETS.fetch(request);
    }

    /* /new/* routes: serve webax bootstrap (SPA routing) */
    if (url.pathname.startsWith('/new')) {
      return env.ASSETS.fetch(new Request(new URL('/new/index.html', url.origin), request));
    }

    /* Everything else: old site (static files, index.html, etc.) */
    return env.ASSETS.fetch(request);
  }
};
