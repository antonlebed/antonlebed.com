export default {
  async fetch(request, env) {
    const url = new URL(request.url);

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
