/* ☠️ SCAFFOLDING — Cloudflare Worker for SPA routing.
   ALL extensionless paths → site.wasm via bootstrap.
   Static assets (.html, .js, .wasm, .png, .jpg, .css) served directly.
   Old HTML pages remain accessible at their .html URLs.
   ROLLBACK: git revert + wrangler deploy. */
export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    /* Paths without file extension → webax SPA bootstrap */
    if (!url.pathname.includes('.')) {
      return env.ASSETS.fetch(new URL('/index.html', url.origin).toString());
    }

    /* Static assets (old HTML, JS, WASM, images, CSS) */
    return env.ASSETS.fetch(request);
  }
};
