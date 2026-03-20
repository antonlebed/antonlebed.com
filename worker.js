/* ☠️ SCAFFOLDING — Cloudflare Worker for SPA routing.
   Routes /new/* to webax bootstrap. Old site untouched.
   Dies when old site is swapped out (becomes simple not_found_handling). */
export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    /* /new/* routes without file extension: serve webax bootstrap (SPA routing) */
    if (url.pathname.startsWith('/new') && !url.pathname.includes('.')) {
      const bootstrapUrl = new URL('/new/index.html', url.origin);
      return env.ASSETS.fetch(bootstrapUrl.toString());
    }

    /* Everything else: serve static assets (old site + /new/*.wasm etc.) */
    return env.ASSETS.fetch(request);
  }
};
