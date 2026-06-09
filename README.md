# antonlebed.com

The deployed site for [antonlebed.com](https://antonlebed.com) — the primorial
tower: the algebra of the Eratosthenes sieve. Plain HTML/CSS/JS, no framework,
no build step, served via Cloudflare Workers.

- `public/` — the site (9 pages, stylesheet, client-side JS)
- `worker.js` — Cloudflare Worker: static assets, bare-path routing,
  301 redirects for renamed pages

This repo is the deploy target; the source of truth lives in a private
research repo. Found a problem?
[Open an issue](https://github.com/antonlebed/antonlebed.com/issues).

Content: public domain (CC0).
