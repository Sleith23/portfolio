# Portfolio — v2 (Astro rewrite)

Static portfolio for **Scot Leith**, rebuilt from the Django version into a
light, editorial Astro site. Design: paper + ink + one volt accent,
Bricolage Grotesque display type, JetBrains Mono metadata labels, hand-rolled
SVG art tiles (no image assets required).

## Stack

- [Astro 5](https://astro.build) — static output, ~0 client JS (one scroll-reveal observer)
- [Tailwind CSS v4](https://tailwindcss.com) via `@tailwindcss/vite`
- Content collections (`src/content/`) for projects + experience
- Google Fonts: Bricolage Grotesque · Inter · JetBrains Mono

## Local dev

```bash
npm install
npm run dev       # http://localhost:4321
npm run build     # outputs static site to dist/
npm run preview   # serve the build locally
```

## Editing content

- **Personal facts** (name, role, email, links, tagline) — `src/data/site.ts`
- **Projects** — one Markdown file per project in `src/content/projects/`
  (frontmatter: title, year, role, summary, stack[], repo?, live?,
  featured, draft, art)
- **Experience** — one Markdown file per role in `src/content/experience/`
  (company, role, period, points[], draft)
- **Design tokens / fonts / utilities** — `src/styles/global.css` (`@theme`)
- **Page layout** — `src/pages/index.astro` + `src/components/`

`draft: true` entries render with a visible "Draft" chip and a how-to note in
the file body — flip it off when real content is in.

### Placeholders to replace before public launch

- [ ] `src/data/site.ts` — confirm name/tagline/email/location; add LinkedIn
- [ ] `src/content/projects/lead-manager.md`, `space-studio.md` — real summaries
- [ ] `src/content/experience/*.md` — real roles (both files are drafts)
- [ ] `index.astro` About section — replace seeded paragraphs with your story
- [ ] Delete `src/content/projects/draft-template.md`
- [ ] Deploy: repo builds as static `dist/` (GitHub Pages / Netlify / Vercel / Render all fine)

## Design notes

Ruled-paper grid, ghost index numerals, marker-highlight accent, dotted-link
hover language, and a skill marquee keep it editorial rather than
template-dark. Art tile per project via the `art` frontmatter field
(`grid | signal | field | orbit`) — swap in real screenshots later if you
prefer photos over the SVG abstracts.
