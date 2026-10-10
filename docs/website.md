# Website Specification

Status: artist-focused portfolio update approved by Jacob in chat on 2026-10-10; implementation requires local review and separate release approval.

This document is the source of truth for the website. Record approved process decisions in [plan.md](plan.md). This revision simplifies the first-pass portfolio and adds a place for upcoming classes and shows.

## Purpose and audience

A personal portfolio for Beth Meyerson Sterkel, a mosaic and ceramic artist in Woodland Park, Colorado. Visitors can explore her work, learn about her materials and process, read her biography, find upcoming classes and shows, and contact her about inquiries, commissions, or collaborations. The site presents Beth as an individual artist and is not a sales platform. Artist-written prose uses I, me, and my; never a collective we or our. Descriptive titles, image alternative text, and search descriptions may name Beth.

## Approved visual direction

A warm, contemporary gallery with ivory backgrounds, charcoal text, restrained terracotta accents, large serif headings, clean sans-serif body text, and generous spacing. Photographs of Beth's actual work lead the composition. The homepage introduction features the Mexican Tile Sun Table photograph. Responsive galleries use three columns on large screens, two on medium screens, and one on narrow screens. Gallery and featured photographs preserve each complete artwork rather than cropping it. Artwork is a non-interactive display, with no hover zoom or click-through arrows. Other subtle hover effects respect reduced-motion preferences.

## Shared structure and behavior

- Public brand: “Beth’s Mosaics.”
- Header: linked brand, Portfolio, Bio, Classes & Shows, Contact, and a prominent Contact Me link. Portfolio points to `index.html`, Bio to `bio/index.html`, Classes & Shows to `classes-and-shows/index.html`, and Contact to `contact/index.html`, with paths relative to the current page. Indicate the current page.
- Mobile: an accessible Menu button opens navigation. Escape closes it and restores focus. Navigation remains usable when JavaScript is disabled.
- Include a skip link to the main content and visible keyboard focus styles.
- Footer: Contact Me, `bethemeyerson@gmail.com` linked to `mailto:bethemeyerson@gmail.com`, `707-972-3040` linked to `tel:+17079723040`, Woodland Park, Colorado, page links, and “© 2026 Beth’s Mosaics.”
- Artwork photographs and captions do not open detail pages or enlargement dialogs.
- All page content and navigation work without JavaScript; only menu enhancement needs JavaScript.
- All internal links, CSS, scripts, and images use relative URLs and work under the GitHub Pages `/bethsmosaics/` subpath.
- Publishable HTML, CSS, JavaScript, images, and fonts live only in `src/`. Pages require no build step or server-side service.
- Use optimized local WebP versions of the approved Wix photographs with responsive sizes where useful, meaningful alternative text, intrinsic dimensions, and lazy loading below the first screen. Use local fonts with system fallbacks.
- Retain artwork photographs, titles, project types in gallery captions, process content, and biography facts. Remove all public artwork whereabouts, including studio and retail locations. Beth’s contact-page city and supplied event venues remain. Omit Wix branding, project setup instructions, the placeholder `info@mysite.com` link, and the incorrect future copyright year. Do not add prices, availability claims, testimonials, or unverified content.

## Portfolio homepage

- **URL/file:** `/`, `src/index.html`.
- **Page title:** Beth’s Mosaics | Portfolio.
- **Description:** Mosaic and ceramic art by Beth Meyerson Sterkel in Woodland Park, Colorado. Explore colorful tables, wall hangings, and repurposed creations.
- **Sections, in order:**
  1. `portfolio-introduction`: artist name; heading “My Portfolio”; exact introduction “Welcome to my portfolio. Here you’ll find a selection of my work.”; non-interactive Mexican Tile Sun Table feature photograph and its existing title/type caption; an “Explore the work” link to `#portfolio` and a “Meet the artist” link to the Bio page.
  2. `portfolio`: nine non-interactive artwork images with their titles and existing project types, in the order in the table below. A visible “Mosaics” heading introduces the work.
  3. `process`: heading “My Process”; exact paragraph “Mosaics are intricate works that bring color and personality to spaces. My creations are made with found and re-purposed materials, giving new life to previously loved items. My art is inspired by the beauty of Colorado, the Southwest, and Mexico.”; the existing materials photograph; three ordered photographic steps: “Step 1:” / “Finding furniture , frames, and tiles to re-purpose.”; “Step 2:” / “Preparing a design. Cutting and gluing tiles.”; “Step 3:” / “Grouting”. Use the associated process photographs below.
  4. Shared footer.

## Bio

- **URL/file:** `/bio/`, `src/bio/index.html`.
- **Page title:** Meet the Artist | Beth’s Mosaics.
- **Description:** Meet Beth Meyerson Sterkel, a Colorado mosaic and ceramic artist inspired by Talavera tiles, found materials, and repurposed furniture.
- **Section:** `artist-biography`, heading “Meet the Artist”; portrait and the exact biography below; “www.themountainartists.org” links to the existing source destination `http://www.themountainartists.org`; a Contact Me link.
- **Layout:** portrait and biography side by side on desktop, stacked on mobile. Shared header and footer.

I am a mosaic and ceramic artist currently living with my husband Mark, dog Skye, and cat Jasper in Woodland Park, Colorado. I have enjoyed hand-building with clay for decades and learned how to create mosaic art with colorful Mexican Talavera ceramic tiles while living in Bucerias, Mexico. My pieces use a combination of Mexican ceramic tiles, found re-purposed tiles, and self-made clay tiles. As a devotee of recycling and re-purposing, I scour thrift stores and estate sales for the frames and bases.

I also teach mosaics and am an active member of the non-profit, Mountain Artists.

## Contact

- **URL/file:** `/contact/`, `src/contact/index.html`.
- **Page title:** Contact | Beth’s Mosaics.
- **Description:** Contact Beth Meyerson Sterkel in Woodland Park, Colorado for mosaic inquiries, commissions, or collaborations.
- **Section:** `contact-details`, heading “Get in Touch”, subheading “I’d Love to Connect”.
- **Exact inquiry copy:** “For inquiries, commissions, or collaborations, please reach out via email or phone. I look forward to discussing your mosaic ideas and visions!”
- Display linked email and phone from the shared footer, labeled Email Beth and Call Beth, plus Woodland Park, Colorado. Include a Portfolio link.
- The first pass replaces the Wix contact form with direct email and phone links. There is no form, submission service, or simulated success message.
- Shared header and footer.

## Classes & Shows

- **URL/file:** `/classes-and-shows/`, `src/classes-and-shows/index.html`.
- **Page title:** Classes & Shows | Beth’s Mosaics.
- **Description:** Upcoming mosaic classes and art shows with Beth Meyerson Sterkel.
- **Section:** `classes-and-shows`, heading “Classes & Shows”.
- Until Beth supplies event details, show only “For information about upcoming classes and shows, please contact me.” with a Contact Me link. Do not assert that no events are scheduled or invent events, dates, or venues.
- Future entries use Beth-supplied title, class/show type, date and time, venue, short description, and optional information link. Update the specification and static HTML through the existing chat workflow; there is no publishing dashboard or booking service.
- Shared header and footer. This page and the Bio and Contact pages follow the established visual direction.

## Artwork display and legacy URLs

Display artwork only on the Portfolio homepage, in this order. Captions retain titles and project types. No artwork locations, individual piece details, per-piece contact controls, or previous/next project navigation are displayed.

The nine former URLs at `/portfolio/<slug>/` remain as minimal redirect files at `src/portfolio/<slug>/index.html`. Use a relative HTML refresh to `../../index.html#portfolio`, which also works without JavaScript. Provide a clearly labeled Portfolio fallback link, a single heading, and a main landmark; do not retain artwork information on these files. Homepage artwork images and captions do not link to these URLs.

| Order | Title | Legacy slug / image name | Project type |
| --- | --- | --- | --- |
| 1 | Mexican Tile Sun Table | `mexican-tile-sun-table` | Antique Pie Table |
| 2 | Dancing Women Table | `dancing-women-table` | Table |
| 3 | Talavera Tile Night Stand | `talavera-tile-night-stand` | Night Stand |
| 4 | Deer In The Trees Wall Hanging | `deer-in-the-trees-wall-hanging` | Wall Hanging |
| 5 | Potted Plant Holder | `potted-plant-holder` | Plant Holder |
| 6 | Wooden Birds Wall Hanging | `wooden-birds-wall-hanging` | Wall Hanging |
| 7 | Mountain Scene Wall Hanging | `mountain-scene-wall-hanging` | Wall Hanging |
| 8 | Black Bear Wall Hanging | `black-bear-wall-hanging` | Wall Hanging |
| 9 | Tree of Life Table | `tree-of-life-table` | Table |

## Image references and provenance

Fetched from the public Wix site supplied by Jacob, `https://www.bethsmosaics.com/`, on 2026-10-10. Preserve the photographs as the artwork source. Files are `assets/images/<name>.webp`; artwork and process photographs also have `<name>-small.webp` for responsive loading. Do not upscale the original portrait. Use the larger local images with responsive smaller variants in the gallery.

| Image name | Alternative text | Original source |
| --- | --- | --- |
| `mexican-tile-sun-table` | Colorful Talavera sun mosaic in an ornate round wooden table. | https://static.wixstatic.com/media/0ae6c4_dc68c2da15e74185a88ac587fba7a238~mv2.jpg |
| `dancing-women-table` | Round mosaic table with dancing women beneath a sun and mountain landscape. | https://static.wixstatic.com/media/0ae6c4_4d3bedceb8404d699e709cdf414e969f~mv2.jpg |
| `talavera-tile-night-stand` | Square night stand with blue, yellow, and orange Talavera tiles. | https://static.wixstatic.com/media/0ae6c4_b215f0ee618d42a68c0d84eadf6e5d46~mv2.jpg |
| `deer-in-the-trees-wall-hanging` | Blue and white ceramic tile wall hanging depicting deer among trees. | https://static.wixstatic.com/media/0ae6c4_32396dc3f5984b9287bd8264743f4bc0~mv2.jpg |
| `potted-plant-holder` | Red ceramic tile plant holder with a decorative bird tile. | https://static.wixstatic.com/media/0ae6c4_f028e4f0b98343a0bf2ce7abd9044ccc~mv2.jpg |
| `wooden-birds-wall-hanging` | Two patterned ceramic birds on a pale blue mosaic in a wooden frame. | https://static.wixstatic.com/media/0ae6c4_0f87af6935dc479aa06cb9caf37bb93f~mv2.jpg |
| `mountain-scene-wall-hanging` | Mountain landscape tile displayed in an octagonal wooden frame. | https://static.wixstatic.com/media/0ae6c4_205e96739514437ea6950140707dff34~mv2.jpg |
| `black-bear-wall-hanging` | Black bear and forest silhouettes on an orange tile wall hanging. | https://static.wixstatic.com/media/0ae6c4_7f4a44245e994a4a8a59566237d78697~mv2.jpg |
| `tree-of-life-table` | Round wooden table with a colorful tree of life mosaic. | https://static.wixstatic.com/media/0ae6c4_34866836dae641f6b0353494b197c1b7~mv2.jpg |
| `beth-meyerson-sterkel` | Beth Meyerson Sterkel sitting outdoors with her dog. | https://static.wixstatic.com/media/0ae6c4_8973e07cee0e4b00bf5c78eef22fb039~mv2.png |
| `process-materials` | Reclaimed wooden table and tray with ceramic pieces ready to be repurposed. | https://static.wixstatic.com/media/0ae6c4_06b1ef7b92214b57962d0e337eddfe37~mv2.jpg |
| `process-find` | Found furniture and colorful ceramic tiles gathered for a mosaic. | https://static.wixstatic.com/media/0ae6c4_0368d6893c1d488c9cf8b6c806a6ba51~mv2.jpg |
| `process-design` | A tree mosaic design with cut ceramic tiles being arranged in a frame. | https://static.wixstatic.com/media/0ae6c4_3ff2dc3c849a464685213774b8afe857~mv2.jpg |
| `process-grout` | Completed tree mosaic with grout between the colorful tile pieces. | https://static.wixstatic.com/media/0ae6c4_0d857d20dc5c4a6095d525085c6779d8~mv2.jpg |

## UI labels

Routine controls use the labels specified above plus “Menu”. Legacy redirect fallback links are labeled “Portfolio”. Gallery captions use the exact artwork title. Decorative icons have no additional accessible name.

## Implementation checks

- Compare the four content pages and nine legacy redirects, section order, exact copy, gallery captions, and images with this specification.
- Validate every local destination, asset, fragment, and image alternative text.
- Exercise mobile navigation, Escape, focus restoration, Classes & Shows contact navigation, non-interactive artwork display, and all nine legacy redirects in a real browser. Verify that no artwork whereabouts remain public.
- Check desktop and mobile layouts, 320-pixel screens, image loading, reduced motion, and JavaScript-disabled browsing.
- Check nested page URLs under the `/bethsmosaics/` subpath.
- Provide a local preview and representative screenshots before requesting release approval.
- Keep documentation and tooling outside the published artifact.
